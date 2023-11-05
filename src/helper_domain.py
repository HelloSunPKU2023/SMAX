import re

import spacy
from spacy.tokens import Doc, Span
from spacy.language import Language

Entities= {
    'ORG': ['eni', 'petronas', 'tpao', 'slb', 'cvx', 'equinor', 'Ecopetrol', 'omv', 'int', 'ongc', 
                'bp', 'bsp', 'spic', 'chevron', "mpcl", 'schlumberger', 'santos', 'woodside'],
    
    'GPE': ['USL', 'SCA', 'SLR', 'KSA', 'ING', 'EUR', 'EAG', 'APG', 'CHG'],
    
    'PRODUCT': ['Agile Reservoir Modeling', 'Avocet', 'Agora',
                'Cameron Supplier Document Management', 'Cameron Supplier Portal', 'Cameron Surface Surveillance', 'ConnectedProduction', 
                'DELFI RE', 'DNS Management', 
                'Data Delivery Services', 'Data Ingestion', 'Data Integration Framework', 'Data Integrator', 'Data Migration', 'Data Science', 'Dataiku DSS', 
                'Delfi Help', 'Delfi Opportunity Assessor', 'Delfi Portal', 'Delfi Production Chemical', 'Developer Portal', 'Delfi',
                'DrillOps', 'DrillPlan', 'Drillbench', 'Drilling Insights', 'Drilling Office', 'Drilling Interpretation',
                'ECLIPSE', 'EXP_PS', 'Edge', 'Engine Ecosystem', 
                'Enterprise Data Management Agent', 'Enterprise Data Solution', 'Enterprise Data Workspace', 'Enterprise Developer Portal', 'Enterprise Portal', 
                'ExplorePlan', 'eSearch',
                'FDPlan', 'FORGAS', 'Facility Planner', 'Flaresim', 'FluidModeler', 
                'GAIA', 'GeoX', 
                'INTERSECT', 'InnerLogix', 'Integrated Asset Modeler', 'InterACT', 
                'Kinetix'
                'LiveQuest', 
                'MEPO', 'MERAK', 'Malcom', 
                'Nasuni', 'NetApp ANF', 
                'OFM', 'OLGA', 'OLGA Online', 'OMNI3D', 'Ocean Framework', 'Ocean Plug-ins','Ocean Store','Omega', 'On Demand Reservoir Simulation', 'Osprey', 
                'PIPEFLO', 'PIPESIM', 'PIPESYS', 'PerformView', 'Petrel', 'Petrel Exploration Geology', 'PetrelRE', 'PetroMod', 
                'Petrotechnical Suite', 'ProSource', 'ProcessOps', 'ProdOps', 'Production Data Foundation', 'Provisioning & Decommissioning', 
                'RP Planner', 'RTDS', 'Rapid Screening', 'Reservoir Analytics', 'RigHour', 
                'Seabed', 'Secure Data Exchange', 'Simulation Cluster Manager', 'Studio', 'Symmetry', 'Spotfire', 
                'TGX', 'TDI', 'Techlog', 
                'VISAGE', 'VISTA', 
                'WELLFLO', 'WMS', 'Wellbarrier', 'WinGLink', 
                'ZFS', 
                ]
    }

# function to get ReGex pattern from a text which ignores the case and matches the words
def get_regex_pattern(text):
    return rf"(?i)\b{text}\b"
    
# initialize the matcher with a vocab
from spacy.matcher import PhraseMatcher
import spacy

nlp = spacy.load("en_core_web_lg")

phrase_matcher = PhraseMatcher(nlp.vocab)

# Iterate over the dictionary and add patterns for each label
for label, values in Entities.items():
    patterns = [nlp.make_doc(value.lower()) for value in values]
    for pattern in patterns:
        phrase_matcher.add(label, None, pattern)

def remove_overlapping_matches(matches):
    # Remove overlapping matches
    matches = [match for match in matches if not any(ent[1] <= match[1] <match[2] < ent[2] for ent in matches if ent != match)]
    return matches

# Custom component class for setting entities
@Language.component("custom_entity_setter")
def set_custom_entities(doc):
    doc_lower = nlp.make_doc(doc.text.lower())
    matches = phrase_matcher(doc_lower)
    # print((matches))
    matches = remove_overlapping_matches(matches)
    # print((matches))
    spans = []
    for match_id, start, end in matches:
        # print(doc[start:end], match_id)
        span = Span(doc, start, end, label=match_id)
        spans.append(span)
    doc.ents = spans
    return doc

# def export_entity_csv():
# # load Entities into a dataframe which has two columns: 'Entity' and 'Label'
#     import pandas as pd
#     array_entities = []

#     for key in Entities.keys():
#         for entity in Entities[key]:
#             # insert a row into the dataframe
#             array_entities.append([key, entity])
#     df_entities = pd.DataFrame(array_entities, columns=['Label', 'Entity'])

#     # export the dataframe to cvs file
#     # print current working directory
#     from src.config import SRC_FOLDER_PATH
    
#     df_entities.to_csv(f'{SRC_FOLDER_PATH}/entities.csv', index=False)