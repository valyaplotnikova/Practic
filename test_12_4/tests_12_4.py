import logging
import unittest
from unittest import TestCase

from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename='runner_tests.log',
    encoding='UTF-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)


class RunnerTest(TestCase):

    def test_walk(self):
        try:
            runner = Runner('Name', -3)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner = Runner(None)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':

    unittest.main()
