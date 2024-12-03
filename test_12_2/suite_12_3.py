import unittest
from tests_12_3 import RunnerTest, TournamentTest


runnerTS = unittest.TestSuite()
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerTS)


