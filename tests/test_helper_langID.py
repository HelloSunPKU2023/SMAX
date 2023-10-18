import unittest
from src.helper_langID import *

class TestHelperLanguage(unittest.TestCase):
    
    def test_fasttext_installation(self):
        # Test case 1: Check if fasttext is installed
        self.assertTrue(is_fasttext_installed())
    def test_is_utf8(self):
        # Test case 1: Empty string
        self.assertTrue(is_utf8(""))
        
        # Test case 1: Empty string
        self.assertFalse(is_utf8(None))
        
        # Test case 2: ASCII string
        self.assertTrue(is_utf8("Hello World"))
        
        # Test case 3: UTF-8 string
        self.assertTrue(is_utf8("你好世界"))
        
        # Test case 4: Non-UTF-8 string
        self.assertFalse(is_utf8(b'\xff\xfe\x00\x31'))
        
    def test_detect_language_fasttext(self):
        # Test case 1: Empty string
        self.assertEqual(detect_language_fasttext(""), "unknown")
        
        # Test case 2: ASCII string
        self.assertEqual(detect_language_fasttext("Good Morning"), "en")
        
        # Test case 3: UTF-8 string
        self.assertEqual(detect_language_fasttext("你好世界"), "zh")
        
        # Test case 4: Non-UTF-8 string
        self.assertEqual(detect_language_fasttext(b'\xff\xfe\x00\x31'), "unknown")    
        
        # Test case 5: English string
        self.assertEqual(detect_language_fasttext("Mobile number change"), "en")
        self.assertEqual(detect_language_fasttext("Add the file comparison plug in in Notepad in DELFI"), "en")
        self.assertEqual(detect_language_fasttext("Mouse cursor and response time issues"), "en")
        self.assertEqual(detect_language_fasttext("BubbleSupport GOM Lithology pattern fill by value"), "en")
        self.assertEqual(detect_language_fasttext("Unable to see N drive"), "en")
        self.assertEqual(detect_language_fasttext("DrillOps Abraj ZAHRA DrillBoreHole TD FAILED"), "en")
        
        # Test case 6: English wrongly detected as other languages
        self.assertEqual(detect_language_fasttext("EBN Petrel error in Delfi"), "unknown")
        self.assertEqual(detect_language_fasttext("Lost mini toolbar"), "de")
        self.assertEqual(detect_language_fasttext("Agora Agora"), "pt")
        
        # Test case 7: Chinese string
        self.assertEqual(detect_language_fasttext("ev 文件封堵射孔关键字"), "zh")
        self.assertEqual(detect_language_fasttext("las 文件转换"), "zh")
        self.assertEqual(detect_language_fasttext("Mail 网格加密"), "zh")
        self.assertEqual(detect_language_fasttext("Petrel 2019.1.1 中的问题"), "zh")
        self.assertEqual(detect_language_fasttext("ev 文件封堵射孔关键字"), "zh")
        self.assertEqual(detect_language_fasttext("Wellflow_许可启动失败"), "zh")
        self.assertEqual(detect_language_fasttext("Phone Oct 缝洞型油气藏模拟"), "zh")
        self.assertEqual(detect_language_fasttext("ERMI处理报错"), "zh")
        self.assertEqual(detect_language_fasttext("AIS报错"), "zh")
        self.assertEqual(detect_language_fasttext("VISAGE运行报错"), "zh")
        self.assertEqual(detect_language_fasttext("ECS安装后看不到模块"), "zh")
        self.assertEqual(detect_language_fasttext("井间连通性"), "zh")
        self.assertEqual(detect_language_fasttext("Petrel2020_inquiry_KB校正"), "zh")
        self.assertEqual(detect_language_fasttext("ev 文件封堵射孔关键字"), "zh")
        self.assertEqual(detect_language_fasttext("las 文件转换"), "zh")
        self.assertEqual(detect_language_fasttext("Mail 网格加密"), "zh")
        self.assertEqual(detect_language_fasttext("Petrel 2019.1.1 中的问题"), "zh")
        self.assertEqual(detect_language_fasttext("FM 设置转注井"), "zh") 
        self.assertEqual(detect_language_fasttext("ofm 递减"), "zh")
        self.assertEqual(detect_language_fasttext("petrel 导入 welltops"), "zh")
        self.assertEqual(detect_language_fasttext("VFPI 压力拟合出错"), "zh")
        self.assertEqual(detect_language_fasttext("Petrel production 中递减参数咨询"), "zh")
        self.assertEqual(detect_language_fasttext("Chat SWCR 查看"), "zh")
        self.assertEqual(detect_language_fasttext("凝析气藏注气"), "zh")
        self.assertEqual(detect_language_fasttext("EasyFrac 插件咨询"), "zh")
        self.assertEqual(detect_language_fasttext("Petrel 2019.1.1 中的问题"), "zh")
        self.assertEqual(detect_language_fasttext("Mail 网格加密"), "zh")
        self.assertEqual(detect_language_fasttext("las 文件转换"), "zh")
        self.assertEqual(detect_language_fasttext("ev 文件封堵射孔关键字"), "zh")
        self.assertEqual(detect_language_fasttext("FM 设置转注井"), "zh") 
        self.assertEqual(detect_language_fasttext("ofm 递减"), "zh")
        self.assertEqual(detect_language_fasttext("[Ext] 質問（flatting）"), "zh")
        self.assertEqual(detect_language_fasttext("Inquire_示踪剂标注一采一注"), "zh")
        self.assertEqual(detect_language_fasttext("XMAC处理报错"), "zh")
        
        
        
        # Test case 8: Chinese wrongly detected as other languages
        self.assertEqual(detect_language_fasttext("FM 设置转注井"), "zh") 
        self.assertEqual(detect_language_fasttext("ofm 递减"), "zh")
        self.assertEqual(detect_language_fasttext("petrel 导入 welltops"), "zh")
        self.assertEqual(detect_language_fasttext("VFPI 压力拟合出错"), "zh")
        self.assertEqual(detect_language_fasttext("Petrel production 中递减参数咨询"), "zh")
        self.assertEqual(detect_language_fasttext("Chat SWCR 查看"), "zh")
        self.assertEqual(detect_language_fasttext("凝析气藏注气"), "zh")
        self.assertEqual(detect_language_fasttext("EasyFrac 插件咨询"), "zh")
        
        # Test case 9: Japanese string
        self.assertEqual(detect_language_fasttext("ホライゾンの Export 方式について"), "ja")
        self.assertEqual(detect_language_fasttext("Create fault polygons and map により生成される fault polygon"), "ja")
        self.assertEqual(detect_language_fasttext("ホライゾンの Export 方式について"), "ja")
        self.assertEqual(detect_language_fasttext("Create fault polygons and map により生成される fault polygon"), "ja")
        
        # Test case 10: Korean string
        self.assertEqual(detect_language_fasttext("horizontal unit 을 Field 단위로 변환하여 사용이 가능한지요"), "ko")
        
        # Test case 11: Arabic string
        self.assertEqual(detect_language_fasttext("إعادة توجيه Password Reset"), "ar")
        
        # Test case 12: Other languages
        self.assertEqual(detect_language_fasttext("Cеминар Корреляция скважин в Petrel"), "ru")
        self.assertEqual(detect_language_fasttext("Cеминар Попластовая интерпретация в RussianTools"), "ru")
        
    def test_detect_language_langdetect(self):
        # Test case 1: Empty string
        self.assertEqual(detect_language_langdetect(""), "unknown")
        
        # Test case 2: ASCII string
        self.assertEqual(detect_language_langdetect("you are the best"), "en")
        
        # Test case 3: UTF-8 string
        self.assertEqual(detect_language_langdetect("你好世界"), "zh")
        
        # Test case 4: Non-UTF-8 string
        self.assertEqual(detect_language_langdetect(b'\xff\xfe\x00\x31'), "unknown")    
        
        # Test case 5: English string
        self.assertEqual(detect_language_langdetect("Mobile number change"), "en")
        self.assertEqual(detect_language_langdetect("Add the file comparison plug in in Notepad in DELFI"), "en")
        self.assertEqual(detect_language_langdetect("BubbleSupport GOM Lithology pattern fill by value"), "en")
        self.assertEqual(detect_language_langdetect("Mobile number change"), "en")
        self.assertEqual(detect_language_langdetect("Add the file comparison plug in in Notepad in DELFI"), "en")
        self.assertEqual(detect_language_langdetect("BubbleSupport GOM Lithology pattern fill by value"), "en")
        
        # Test case 6: English wrongly detected as other languages
        self.assertNotEqual(detect_language_langdetect("DrillOps Abraj ZAHRA DrillBoreHole TD FAILED"), "en")
        self.assertNotEqual(detect_language_langdetect("Unable to see N drive"), "en")
        self.assertNotEqual(detect_language_langdetect("DrillOps Abraj ZAHRA DrillBoreHole TD FAILED"), "en")
        self.assertNotEqual(detect_language_langdetect("EBN Petrel error in Delfi"), "en")
        self.assertNotEqual(detect_language_langdetect("Lost mini toolbar"), "en")
        self.assertNotEqual(detect_language_langdetect("Agora Agora"), "en")
        
        # Test case 7: Chinese string
        self.assertEqual(detect_language_langdetect("ev 文件封堵射孔关键字"), "zh")
        self.assertEqual(detect_language_langdetect("Wellflow_许可启动失败"), "zh")
        self.assertEqual(detect_language_langdetect("Phone Oct 缝洞型油气藏模拟"), "zh")
        self.assertEqual(detect_language_langdetect("ERMI处理报错"), "zh")
        self.assertEqual(detect_language_langdetect("AIS报错"), "zh")
        self.assertEqual(detect_language_langdetect("VISAGE运行报错"), "zh")
        self.assertEqual(detect_language_langdetect("ECS安装后看不到模块"), "zh")
        self.assertEqual(detect_language_langdetect("井间连通性"), "zh")
        self.assertEqual(detect_language_langdetect("Petrel2020_inquiry_KB校正"), "zh")
        self.assertEqual(detect_language_langdetect("ev 文件封堵射孔关键字"), "zh")
        self.assertEqual(detect_language_langdetect("las 文件转换"), "zh")
        self.assertEqual(detect_language_langdetect("Mail 网格加密"), "zh")
        self.assertEqual(detect_language_langdetect("Petrel 2019.1.1 中的问题"), "zh")
        self.assertEqual(detect_language_langdetect("FM 设置转注井"), "zh") 
        self.assertEqual(detect_language_langdetect("ofm 递减"), "zh")
        self.assertEqual(detect_language_langdetect("petrel 导入 welltops"), "zh")
        self.assertEqual(detect_language_langdetect("VFPI 压力拟合出错"), "zh")
        self.assertEqual(detect_language_langdetect("Petrel production 中递减参数咨询"), "zh")
        self.assertEqual(detect_language_langdetect("Chat SWCR 查看"), "zh")
        self.assertEqual(detect_language_langdetect("凝析气藏注气"), "zh")
        self.assertEqual(detect_language_langdetect("EasyFrac 插件咨询"), "zh")
        self.assertEqual(detect_language_langdetect("Petrel 2019.1.1 中的问题"), "zh")
        self.assertEqual(detect_language_langdetect("Mail 网格加密"), "zh")
        self.assertEqual(detect_language_langdetect("las 文件转换"), "zh")
        self.assertEqual(detect_language_langdetect("ev 文件封堵射孔关键字"), "zh")
        self.assertEqual(detect_language_langdetect("FM 设置转注井"), "zh") 
        self.assertEqual(detect_language_langdetect("ofm 递减"), "zh")
        self.assertEqual(detect_language_langdetect("[Ext] 質問（flatting）"), "zh")
        self.assertEqual(detect_language_langdetect("Inquire_示踪剂标注一采一注"), "zh")
        self.assertEqual(detect_language_langdetect("XMAC处理报错"), "zh")
        
        
        # Test case 9: Japanese string
        self.assertEqual(detect_language_langdetect("ホライゾンの Export 方式について"), "ja")
        self.assertEqual(detect_language_langdetect("Create fault polygons and map により生成される fault polygon"), "ja")
        self.assertEqual(detect_language_langdetect("ホライゾンの Export 方式について"), "ja")
        self.assertEqual(detect_language_langdetect("Create fault polygons and map により生成される fault polygon"), "ja")
        
        # Test case 10: Korean string
        self.assertEqual(detect_language_langdetect("horizontal unit 을 Field 단위로 변환하여 사용이 가능한지요"), "ko")
    


if __name__ == '__main__':
    unittest.main()