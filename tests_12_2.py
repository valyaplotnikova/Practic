import unittest
from unittest import TestCase

from runner import Runner, Tournament


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrew = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(test_key)
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_start_usain_nik(self):
        tour = Tournament(90, self.usain, self.nik)
        result = tour.start()
        self.all_results['test_start_usain_nik'] = result
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')

    def test_start_andrew_nik(self):
        tour = Tournament(90, self.andrew, self.nik)
        result = tour.start()
        self.all_results['test_start_andrew_nik'] = result
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')

    def test_start_all(self):
        tour = Tournament(90, self.usain, self.andrew, self.nik)
        result = tour.start()
        self.all_results['test_start_all'] = result
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')


if __name__ == '__main__':
    unittest.main()
