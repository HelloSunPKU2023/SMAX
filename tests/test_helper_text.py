import unittest
from src.helper_text import *

class TestHelperText(unittest.TestCase):
    
    def test_add_space_between_cjk_and_non_cjk(self):
        # Test case 1: When input text is empty
        self.assertEqual(add_space_between_cjk_and_non_cjk(""), "")
        
        # Test case 2: When input text contains only CJK characters
        self.assertEqual(add_space_between_cjk_and_non_cjk("你好世界"), "你好世界")
        
        # Test case 3: When input text contains only non-CJK characters
        self.assertEqual(add_space_between_cjk_and_non_cjk("Hello World"), "Hello World")
        
        # Test case 4: When input text contains CJK and non-CJK characters without space
        self.assertEqual(add_space_between_cjk_and_non_cjk("你好HelloWorld世界"), "你好 HelloWorld 世界")
        
        # Test case 5: When input text contains CJK and non-CJK characters with space
        self.assertEqual(add_space_between_cjk_and_non_cjk("你好 Hello World 世界"), "你好 Hello World 世界")
        
        # Test case 6: When input text contains CJK and non-CJK characters with multiple spaces
        self.assertEqual(add_space_between_cjk_and_non_cjk("你好   Hello   World   世界"), "你好 Hello World 世界")
        
        # Test case 7: When input text contains CJK and non-CJK characters with special characters
        self.assertEqual(add_space_between_cjk_and_non_cjk("你好!@#$%^&*()HelloWorld世界"), "你好 !@#$%^&*()HelloWorld 世界")
        
        # Test case 8: When input text contains CJK and non-CJK characters with special characters
        self.assertEqual(add_space_between_cjk_and_non_cjk("[Ext] ofm-递减-chujie.sipc@sinopec.com"), "[Ext] ofm- 递减 -chujie.sipc@sinopec.com")
        
        # Test case 9: When input text contains CJK and non-CJK characters with special characters
        self.assertEqual(add_space_between_cjk_and_non_cjk("unit을Field단위로 변환하여 사용이 가능한지요?"), "unit 을 Field 단위로 변환하여 사용이 가능한지요 ?") 
    
    def test_remove_email(self):
        # Test case 1: When input text is empty
        self.assertEqual(remove_email(""), "")
        
        # Test case 2: When input text does not contain email
        self.assertEqual(remove_email("Hello World"), "Hello World")
        
        # Test case 3: When input text contains one email
        self.assertEqual(remove_email("Please contact me at john-abc@example.com"), "Please contact me at ")
        
        # Test case 4: When input text contains multiple emails
        self.assertEqual(remove_email("Please contact me at john@example.com or jane@example.com"), "Please contact me at  or ")
        
        # Test case 5: When input text contains email with special characters
        self.assertEqual(remove_email("Please contact me at john.doe@example.com"), "Please contact me at ")
        
        # Test case 6: When input text contains email with non-ASCII characters
        self.assertEqual(remove_email("Please contact me at 你好@example.com"), "Please contact me at ")
        
    def test_remove_uuid(self):
        # Test case 1: No UUIDs in text
        text = "This is a test string."
        self.assertEqual(remove_uuid(text), text)

        # Test case 2: Single UUID in text
        text = "This is a test string with a UUID: 123e4567-e89b-12d3-a456-426655440000."
        self.assertEqual(remove_uuid(text), "This is a test string with a UUID: .")

        # Test case 3: Multiple UUIDs in text
        text = "This is a test string with multiple UUIDs: 123e4567-e89b-12d3-a456-426655440000 and 123e4567-e89b-12d3-a456-426655440001."
        self.assertEqual(remove_uuid(text), "This is a test string with multiple UUIDs:  and .")

        # Test case 4: UUID at beginning of text
        text = "123e4567-e89b-12d3-a456-426655440000 is a UUID."
        self.assertEqual(remove_uuid(text), " is a UUID.")

        # Test case 5: UUID at end of text
        text = "This is a UUID: 123e4567-e89b-12d3-a456-426655440000"
        self.assertEqual(remove_uuid(text), "This is a UUID: ")
        
    def test_remove_date(self):
        # Test case 1: No date in text
        text = "This is a test string."
        self.assertEqual(remove_date(text), text)

        # Test case 2: Single date in text
        text = "This is a test string with a date: 1/1/2020."
        self.assertEqual(remove_date(text), "This is a test string with a date: .")

        # Test case 3: Multiple dates in text
        text = "This is a test string with multiple dates: 1/1/2020 and 1/2/2020."
        self.assertEqual(remove_date(text), "This is a test string with multiple dates:  and .")

        # Test case 4: Date at beginning of text
        text = "1/1/2020 is a date."
        self.assertEqual(remove_date(text), " is a date.")

        # Test case 5: Date at end of text
        text = "This is a date: 1/1/2020"
        self.assertEqual(remove_date(text), "This is a date: ")
    
    def test_remove_time(self):
        # Test case 1: No time in text
        text = "This is a test string."
        self.assertEqual(remove_time(text), text)

        # Test case 2: Single time in text
        text = "This is a test string with a time: 1:00 pm."
        self.assertEqual(remove_time(text), "This is a test string with a time: .")

        # Test case 3: Multiple times in text
        text = "This is a test string with multiple times: 1:00PM and 2:00 am."
        self.assertEqual(remove_time(text), "This is a test string with multiple times:  and .")

        # Test case 4: Time at beginning of text
        text = "14:00 is a time."
        self.assertEqual(remove_time(text), "is a time.")

        # Test case 5: Time at end of text
        text = "This is a time: 23:59"
        self.assertEqual(remove_time(text), "This is a time: ")        
    
    def test_remove_whitespace(self):
        # Test case 1: No whitespace in text
        text = "This is a test string."
        self.assertEqual(remove_whitespace(text), text)

        # Test case 2: Single whitespace in text
        text = "This is a test string with a whitespace:  ."
        self.assertEqual(remove_whitespace(text), "This is a test string with a whitespace: .")

        # Test case 3: Multiple whitespaces in text
        text = "This is a test string with multiple whitespaces:    ."
        self.assertEqual(remove_whitespace(text), "This is a test string with multiple whitespaces: .")

        # Test case 4: Whitespace at beginning of text
        text = " is a whitespace."
        self.assertEqual(remove_whitespace(text), "is a whitespace.")

        # Test case 5: Whitespace at end of text
        text = "This is a whitespace: "
        self.assertEqual(remove_whitespace(text), "This is a whitespace:")
        
    def test_remove_punctuation(self):
        # Test case 1: No punctuation in text
        text = "This is a test string."
        self.assertEqual(remove_punctuation(text), "This is a test string")

        # Test case 2: Single punctuation in text
        text = "This is a test string with a punctuation: ."
        self.assertEqual(remove_punctuation(text), "This is a test string with a punctuation ")

        # Test case 3: Multiple punctuations in text
        text = "This is a test string with multiple punctuations: ,."
        self.assertEqual(remove_punctuation(text), "This is a test string with multiple punctuations ")

        # Test case 4: Punctuation at beginning of text
        text = ",. is a punctuation."
        self.assertEqual(remove_punctuation(text), " is a punctuation")

        # Test case 5: Punctuation at end of text
        text = "This is a punctuation: ,."
        self.assertEqual(remove_punctuation(text), "This is a punctuation ")
        
        text = '을'
        self.assertEqual(remove_punctuation(text), '을')
        
    def test_remove_brackets_content(self):
        # Test case 1: No brackets in text
        text = "This is a test string."
        self.assertEqual(remove_brackets_content(text), text)

        # Test case 2: Single brackets in text
        text = "This is a test string with a brackets: [test test test]."
        self.assertEqual(remove_brackets_content(text), "This is a test string with a brackets: .")

        # Test case 3: Multiple brackets in text
        text = " [test test test][abc]This is a test string with multiple brackets."
        self.assertEqual(remove_brackets_content(text), " This is a test string with multiple brackets.")

        # Test case 4: Brackets at beginning of text
        text = "[] is a brackets."
        self.assertEqual(remove_brackets_content(text), " is a brackets.")

        # Test case 5: Brackets at end of text
        text = "This is a brackets: [abc]"
        self.assertEqual(remove_brackets_content(text), "This is a brackets: ")
    
    def test_remove_word_has_alpha_and_digit(self):
        # Test case 1: No word has alpha and digit in text
        text = "This is a test string."
        self.assertEqual(remove_word_has_alpha_and_digit(text), text)

        # Test case 2: Single word has alpha and digit in text
        text = "This is a test string with a word has alpha and digit: X-00IKW2 and 3D."
        self.assertEqual(remove_word_has_alpha_and_digit(text), "This is a test string with a word has alpha and digit:  and 3D.")

        # Test case 3: Multiple words has alpha and digit in text
        text = "This is a test string with multiple words has alpha and digit: CO2, test123 and test456."
        self.assertEqual(remove_word_has_alpha_and_digit(text), "This is a test string with multiple words has alpha and digit: CO2,  and .")

        # Test case 4: Word has alpha and digit at beginning of text
        text = "test123 is a word has alpha and digit."
        self.assertEqual(remove_word_has_alpha_and_digit(text), " is a word has alpha and digit.")

        # Test case 5: Word has alpha and digit at end of text
        text = "This is a word has alpha and digit: test123"
        self.assertEqual(remove_word_has_alpha_and_digit(text), "This is a word has alpha and digit: ")
        
    def test_remove_digits(self):
        # Test case 1: No digits in text
        text = "This is a test string."
        self.assertEqual(remove_digits(text), text)

        # Test case 2: Single digits in text
        text = "This is a test string with a digits: 123."
        self.assertEqual(remove_digits(text), "This is a test string with a digits: .")

        # Test case 3: Multiple digits in text
        text = "This is a test string with multiple digits: 123 and 456."
        self.assertEqual(remove_digits(text), "This is a test string with multiple digits:  and .")

        # Test case 4: Digits at beginning of text
        text = "123 is a digits."
        self.assertEqual(remove_digits(text), " is a digits.")

        # Test case 5: Digits at end of text
        text = "This is a digits: 123"
        self.assertEqual(remove_digits(text), "This is a digits: ")

    def test_remove_underline(self):
        # Test case 1: No underline in text
        text = "This is a test string."
        self.assertEqual(remove_underline(text), text)

        # Test case 2: Single underline in text
        text = "This is a test string with a underline: _."
        self.assertEqual(remove_underline(text), "This is a test string with a underline:  .")

        # Test case 3: Multiple underlines in text
        text = "This is a test string with multiple underlines: __ and a_b_c."
        self.assertEqual(remove_underline(text), "This is a test string with multiple underlines:   and a b c.")

        # Test case 4: Underline at beginning of text
        text = "_ is a underline."
        self.assertEqual(remove_underline(text), "  is a underline.")

        # Test case 5: Underline at end of text
        text = "This is a underline: _"
        self.assertEqual(remove_underline(text), "This is a underline:  ")
    
    def test_keep_text_after_last_pipe(self):
        # Test case 1: No prefix in text
        text = "This is a test string."
        self.assertEqual(keep_text_after_last_pipe(text), text)

        # Test case 2: Single prefix in text
        text = "This is a test string with a |: [Ext] ofm-递减-"
        self.assertEqual(keep_text_after_last_pipe(text), ': [Ext] ofm-递减-')
    
    def test_convert_abbr_in_text(self):
        # Test case 1: No abbreviation in text
        text = "This is a test string"
        self.assertEqual(convert_abbrev_in_text(text), text)

        # Test case 2: Single abbreviation in text
        text = "This is a test string with a abbreviation: 3D."
        self.assertEqual(convert_abbrev_in_text(text), "This is a test string with a abbreviation : three dimensional .")
        
        # Test case 3: Single abbreviation in text
        text = "U&O 模块咨询"
        self.assertEqual(convert_abbrev_in_text(text), "uncertainty and optimization 模块咨询")
        
        # Test case 4: Single abbreviation in text
        text = '*.las 文件转换 ticket'
        self.assertEqual(convert_abbrev_in_text(text), "* .las 文件转换 ticket")
        
    def test_quick_clean_up(self):
        # Test case 1: No email, UUID, date, time, brackets, word has alpha and digit, short words in text
        text = "This is a test string."
        expected = "This is a test string."
        self.assertEqual(quick_clean_up(text), expected)

        # Test case 2: 
        text = 'U&O模块咨询'
        expected = 'U&O 模块咨询'
        self.assertEqual(quick_clean_up(text), expected)
        
        # Test case 3: 
        text =  '[Ext] ofm-递减-chujie.sipc@sinopec.com'
        expected = 'Ext ofm 递减'
        self.assertEqual(quick_clean_up(text), expected)
        
        # Test case 4:
        text = '[CARMO | X-00SDAT] - Mobile number change bug crash'
        expected = 'CARMO Mobile number change bug crash'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 6:
        # text = '[Completed] PETRONAS DELFI X-00IS5X | Add the file comparison plug-in in Notepad++ in DELFI'
        # expected = 'Add the file comparison plug in in Notepad in DELFI'
        # self.assertEqual(quick_clean_up(text), expected)
        
        # test case 7:
        text = 'SWISF : Deploy new plugin in Suncor westus tenant data files'
        expected = 'SWISF : Deploy new plugin in Suncor westus tenant data files'
        self.assertEqual(quick_clean_up(text), expected)
        
        # # test case 8:
        # text = '[ENAUTA | 1-1LC0LUB] - Mouse cursor and response time issues '
        # expected = 'Mouse cursor and response time issues'
        # self.assertEqual(quick_clean_up(text), expected)
        
        # test case 9:
        text = '(WGS_1984_UTM_Zone_46N), horizontal unit을 Field 단위로 변환하여 사용이 가능한지요?'
        expected = 'WGS UTM Zone , horizontal unit 을 Field 단위로 변환하여 사용이 가능한지요 ?'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 10:
        text = 'DrillOps Abraj 105    ZAHRA-54H1  4b6842ef-e7c5-44dc-9477-56869c94998e DrillBoreHole.TD FAILED'
        expected = 'Drill Ops Abraj Drill Bore Hole .TD FAILED'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 11:
        text = '(JOGMEC)ホライゾンのExport方式について'
        expected = 'JOGMEC ホライゾンの Export 方式について'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 12:
        text = '"Create fault polygons and map" により生成されるfault polygon'
        expected = 'Create fault polygons and map により生成される fault polygon'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 13:
        text = '#Cеминар "Корреляция скважин в Petrel"'
        expected = 'Cеминар Корреляция скважин в Petrel'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 14:
        text = '#Cеминар "Попластовая интерпретация в RussianTools"'
        expected = 'Cеминар Попластовая интерпретация в Russian Tools'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 15:
        text = '#BubbleSupport_GOM_Lithology pattern fill by value'
        expected = 'Bubble Support GOM Lithology pattern fill by value'
        self.assertEqual(quick_clean_up(text), expected)
        
        # # test case 16:
        # text = '#Bubble_Support_COP_Alaska | 1-1SCJLCD | Unable to see N drive'
        # expected = 'Unable to see N drive'
        # self.assertEqual(quick_clean_up(text), expected)
        
        # test case 17:
        text = '#1037111 EBN: Petrel: error in Delfi'
        expected = 'EBN: Petrel : error in Delfi'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 18:
        text = "MXC Bushel 1EXP 01/05/2023 22:00: Well disconnection Rig/Town event"
        expected = "MXC Bushel : Well disconnection Rig Town event"
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 19:
        text = '[Ext] mis-tie correctionについて'
        expected = 'Ext mis tie correction について'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 20:
        text = '.ev文件封堵射孔关键字phone'
        expected = '.ev 文件封堵射孔关键字 phone'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 21:
        text = '*.las文件转换tikcets ticket'
        expected = '.las 文件转换 tikcets ticket'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 22:
        text = 'EasyFrac插件咨询'
        expected = 'Easy Frac 插件咨询'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 23:
        text = 'Mail_网格加密'
        expected = 'Mail 网格加密'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 24:
        text = '[Ext]凝析气藏注气'
        expected = 'Ext 凝析气藏注气'
        self.assertEqual(quick_clean_up(text), expected)
        
        # test case 25:
        text = 'إعادة توجيه- Password Reset'
        expected = 'إعادة توجيه Password Reset'
        self.assertEqual(quick_clean_up(text), expected)


        text = ''
        expected = None
        self.assertEqual(quick_clean_up(text), expected)

    def test_count_words(self):
        # Test case 1: No words in text
        text = "This is a test string."
        self.assertEqual(count_words(text), 5)

        # Test case 2: Single word in text
        text = "This is a test string with a word: test."
        self.assertEqual(count_words(text), 9)

        # Test case 3: Multiple words in text
        text = "This is a test string with multiple words: test and string."
        self.assertEqual(count_words(text), 11)

        # Test case 4: Word at beginning of text
        text = "test is a word."
        self.assertEqual(count_words(text), 4)

        # Test case 5: Word at end of text
        text = "This is a word: test"
        self.assertEqual(count_words(text), 5)        
        
    def test_extract_abbr(self):
        # # Test case 1: No abbreviation in text
        # texts = ["This is a test string."]
        # self.assertEqual(extract_abbr(texts), None)

        # Test case 2: Single abbreviation in text
        texts = ["This is a test string with a abbreviation: DEF."]
        self.assertEqual(extract_abbr(texts), [("DEF", 1)])

        # Test case 3: Multiple abbreviations in text
        texts = ["This is a test ABOUT string with multiple abbreviations: OFM and FM."]
        self.assertEqual(extract_abbr(texts), [("FM", 1), ("OFM", 1)])

        # Test case 4: Abbreviation at beginning of text
        texts = ["ABC is a abbreviation ABOUT, ABOVE."]
        self.assertEqual(extract_abbr(texts), [("ABC", 1)])

        # Test case 5: Abbreviation at end of text
        texts = ["This is a abbreviation: ABC", "This is a test string with multiple abbreviations: ABC and XYZ."]
        self.assertEqual(extract_abbr(texts), [("ABC", 2), ("XYZ", 1)])
        
        # Test case 5: Abbreviation at end of text
        texts = ["This is a abbreviation: 2XD", "This is a test string with multiple abbreviations: A// and XYZ."]
        self.assertEqual(extract_abbr(texts), [("XYZ", 1)])
        
    def test_add_space_between_capitalized_words(self):
        # Test case 1: No capitalized words in text
        text = "This is a test string."
        self.assertEqual(add_space_between_capitalized_words(text), text)

        # Test case 2: Single capitalized word in text
        text = "This is a test string with a capitalized word: OFM."
        self.assertEqual(add_space_between_capitalized_words(text), "This is a test string with a capitalized word: OFM.")

        # Test case 3: Multiple capitalized words in text
        text = "This is a MobileNumberChange."
        self.assertEqual(add_space_between_capitalized_words(text), "This is a Mobile Number Change .")

        # Test case 4: Capitalized word at beginning of text
        text = "OFM is a capitalized word."
        self.assertEqual(add_space_between_capitalized_words(text), "OFM is a capitalized word.")

        # Test case 5: Capitalized word at end of text
        text = "This is a CapitalizedWord: OFM"
        self.assertEqual(add_space_between_capitalized_words(text), "This is a Capitalized Word : OFM")

    def test_final_clean_up(self):
        self.assertEqual(final_clean_up("Ext FW Petrel does not accept any value for any new property"), "fw petrel accept value property")
        self.assertEqual(final_clean_up("Mixing Co2 and Ch4"), "mixing co2 ch4")

if __name__ == '__main__':
    unittest.main()