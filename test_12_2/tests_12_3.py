import unittest
from unittest import TestCase

from runner import Runner, Tournament


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Name')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Name')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('Name1')
        runner2 = Runner('Name2')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(TestCase):
    is_frozen = True

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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_usain_nik(self):
        tour = Tournament(90, self.usain, self.nik)
        result = tour.start()
        self.all_results['test_start_usain_nik'] = result
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_andrew_nik(self):
        tour = Tournament(90, self.andrew, self.nik)
        result = tour.start()
        self.all_results['test_start_andrew_nik'] = result
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_all(self):
        tour = Tournament(90, self.usain, self.andrew, self.nik)
        result = tour.start()
        self.all_results['test_start_all'] = result
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')


if __name__ == '__main__':
    unittest.main()
