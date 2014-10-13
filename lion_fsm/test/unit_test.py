__author__ = 'vi.gerasimov'

from unittest import TestCase
from lion_fsm.lion_fsm import Lion


class TestLion(TestCase):
    antelope = 'antelope'
    hunter = 'hunter'
    tree = 'tree'

    def test_lion_init(self):
        self.assertRaises(TypeError, Lion)
        self.assertRaises(ValueError, Lion, 'True')

    def test_lion_meet_antelope(self):
        self.assertEqual(Lion(True).get(self.antelope), 'Lion is eating. Lion is full.')
        self.assertEqual(Lion(False).get(self.antelope), 'Lion is sleeping. Lion is hungry.')

    def test_lion_meet_hunter(self):
        self.assertEqual(Lion(True).get(self.hunter), 'Lion is running. Lion is hungry.')
        self.assertEqual(Lion(False).get(self.hunter), 'Lion is running. Lion is hungry.')

    def test_lion_meet_tree(self):
        self.assertEqual(Lion(True).get(self.tree), 'Lion is sleeping. Lion is hungry.')
        self.assertEqual(Lion(False).get(self.tree), 'Lion is looking. Lion is hungry.')

    def test_lion_dont_know(self):
        self.assertEqual(Lion(True).get(123), 'Brr... Give me what I know!')
        self.assertEqual(Lion(False).get(123), 'Brr... Give me what I know!')