import unittest
from src.helper_domain import set_custom_entities
import spacy

nlp = spacy.load("en_core_web_lg")
class TestHelperDomain(unittest.TestCase):
    def test_set_custom_entities(self):
        # Test case 1
        text = "'Cannot access Delfi Portal due to phone number...'"
        doc = nlp(text)
        # Act
        doc = set_custom_entities(doc)
        # Assert
        self.assertEqual(len(doc.ents), 1)
        self.assertEqual(doc.ents[0].label_, "PRODUCT")
        self.assertEqual(doc.ents[0].text, "Delfi Portal")
        
        # Test case 2
        text = 'Completed PETRONAS DELFI How to display core log images in WSW'
        doc = nlp(text)
        # Act
        doc = set_custom_entities(doc)
        # Assert
        self.assertEqual(len(doc.ents), 2)
        self.assertEqual(doc.ents[0].label_, "ORG")
        self.assertEqual(doc.ents[0].text, "PETRONAS")
        self.assertEqual(doc.ents[1].label_, "PRODUCT")
        self.assertEqual(doc.ents[1].text, "DELFI")
        
        # Test case 3
        text = 'Agora Agora gateway to mexico'
        doc = nlp(text)
        # Act
        doc = set_custom_entities(doc)
        # Assert
        self.assertEqual(len(doc.ents), 3)
        self.assertEqual(doc.ents[0].label_, "PRODUCT")
        self.assertEqual(doc.ents[0].text, "Agora")
        self.assertEqual(doc.ents[1].label_, "PRODUCT")
        self.assertEqual(doc.ents[1].text, "Agora")
        self.assertEqual(doc.ents[2].label_, "GPE")
        self.assertEqual(doc.ents[2].text, "mexico")
        
if __name__ == '__main__':
    unittest.main()