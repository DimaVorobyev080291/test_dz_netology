import unittest
from unittest import TestCase
from netology_dz import check_age, check_email, distance_traveled

class TestMain(TestCase):

    def test_check_age_with_params(self):
        """"Тест проверяет работу метода check_age."""
        for i, (age, expected) in enumerate([
            (18,'Доступ разрешён'),
            (17, 'Доступ запрещён'),
            (20,'Доступ разрешён'),
            (0, 'Доступ запрещён'),
            (111,'Доступ разрешён')
        ]):
            with self.subTest(i):
                result = check_age(age)
                self.assertEqual(expected, result)

    def test_check_email_with_params(self):
        """"Тест проверяет работу метода check_email."""
        for i,(email, expected) in enumerate([
            ('Helloworld@.ru', True),
            ('мояпочта@нетология.ру', True),
            ('python@email@net', False),
            (' em@il.ru', False),
            ('Hell7> .@mail.com', False),
        ]):
            with self.subTest(i):
                result = check_email(email)
                self.assertEqual(expected, result)

    def test_distance_traveled_with_params(self):
        """"Тест проверяет работу метода distance_traveled."""
        for i,(hare, turtle, expected) in enumerate([
            ([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3], 'черепаха'),
            ([8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3], 'заяц'),
            ([8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3], 'одинаково'),
            ([44, 55, 77, 100, 45],[33, 50, 70, 110, 30], 'заяц'),
            ([100, 110, 120, 70], [150,130, 80, 40], 'одинаково'),
        ]):
            with self.subTest(i):
                result = distance_traveled(hare, turtle)
                self.assertEqual(expected, result)