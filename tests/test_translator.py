import Translator
import unittest
from unittest.mock import patch

class InitTest(unittest.TestCase):

    def test_response(self):
        """Проверка отклика"""
        self.item1 = Translator.translater('https://translate.yandex.net/api/v1.5/tr.json/translate',
                                      'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0', 'Hi, world', 'en', 'ru')
        self.assertTrue(self.item1)
        # 200
        self.item2 = Translator.translater('https://translate.yandex.net/api/v1.5/tr.json/translate',
                                      'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0', 'Hi, world', 'en', 'ru')
        self.assertEqual(str(self.item2), '<Response [200]>')
        # 403
        self.item3 = Translator.translater('https://translate.yandex.net/api/v1.5/tr.json/translate',
                                           'trnsl.1.1.2019071325332',
                                           'Hi, world', 'en', 'ru')
        self.assertEqual(str(self.item3), '<Response [403]>')
        # 404
        self.item4 = Translator.translater('https://translate.yandex.net/api/v1.5/tr.json/tran211233213',
                                      'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0', 'Hi, world', 'en', 'ru')
        self.assertEqual(str(self.item4), '<Response [404]>')
        # 400
        self.item5 = Translator.translater('https://translate.yandex.net/api/v1.5/tr.json/translate',
                                           'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0',
                                           'Hi, world', 'en', 'Russia')
        self.assertEqual(str(self.item5), '<Response [400]>')


    def test_translator(self):
        """Провепка перевода"""

        information = Translator.translater('https://translate.yandex.net/api/v1.5/tr.json/translate',
                                      'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0', 'Hi, world', 'en', 'ru')
        translate_information = information.json()


        self.assertTrue(translate_information['text'])
        self.assertEqual(*translate_information['text'], 'Привет, мир')

    def test_risers(self):
        with self.assertRaises(TypeError):
            Translator.translater('https://translate.yandex.net/api/v1.5/tr.json/translate',
                                  'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0',
                                  'Hi, world', 'en', 'ru', 'rid')






