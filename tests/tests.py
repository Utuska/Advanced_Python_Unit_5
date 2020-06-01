import unittest
import Unit5
from unittest.mock import patch


class InitTest(unittest.TestCase):

    def setUp(self) -> None:

        self.dirs, self.docs = Unit5.directories, Unit5.documents

    def test_initial_data_type(self):
        """Проверка начальных условий"""
        dirs, docs = Unit5.directories, Unit5.documents

        # проверка на истинность
        self.assertTrue(docs)
        self.assertTrue(dirs)

        # проверка на соответствие типам

        self.assertIsInstance(dirs, dict)
        self.assertIsInstance(docs, list)



    def test_function_people(self):
        """Проверка правильности выводимого Импени"""
        with patch('Unit5.input', return_value='p'):
            with patch('Unit5.input', return_value='11-2'):

                self.assertEqual(Unit5.people(),"Геннадий Покемонов")

    def test_function_add(self):
        """Проверка добавления элементов"""
        initial_len = len(self.docs)
        with patch('Unit5.input', return_value='a'):
            user_input = ['22', '33', '55', '2']
            with patch('Unit5.input', side_effect=user_input):
                Unit5.add()
        self.assertNotEqual(initial_len, len(self.docs))
        self.assertIn({'type': '22', 'number': '33', 'name': '55'}, self.docs)

    def test_function_add_shelf(self):
        """Проверка добавления полки"""
        with patch('Unit5.input', return_value='as'):
            """Отрицательный тест Задаем номер полки строкой"""
            with self.assertRaises(ValueError):
                with patch('Unit5.input', return_value='good'):
                    Unit5.add_shelf()






