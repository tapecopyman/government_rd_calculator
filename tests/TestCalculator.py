import unittest
import sys
import os

# 프로젝트 루트 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))))

from src.calculator import calculate_total_research_cost

class CustomTestResult(unittest.TestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"{test._testMethodName}: PASS")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"{test._testMethodName}: FAIL")
        print(f"Failed function: {err[1]}")

class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n테스트 시작\n")

    @classmethod
    def tearDownClass(cls):
        print("\n테스트 종료")

    def test_calculate_total_research_cost_standard(self):
        government_funding = 75
        expected_total = 100
        expected_institution = 25
        expected_gov_ratio = 75
        expected_inst_ratio = 25

        result = calculate_total_research_cost(government_funding)
        
        self.assertAlmostEqual(result[0], expected_total, places=2)
        self.assertAlmostEqual(result[1], expected_institution, places=2)
        self.assertAlmostEqual(result[2], expected_gov_ratio, places=2)
        self.assertAlmostEqual(result[3], expected_inst_ratio, places=2)

    def test_calculate_total_research_cost_zero(self):
        government_funding = 0
        result = calculate_total_research_cost(government_funding)
        
        self.assertAlmostEqual(result[0], 0, places=2)
        self.assertAlmostEqual(result[1], 0, places=2)
        self.assertAlmostEqual(result[2], 0, places=2)
        self.assertAlmostEqual(result[3], 0, places=2)

    def test_calculate_total_research_cost_large_number(self):
        government_funding = 1000000
        expected_total = 1333333.33
        expected_institution = 333333.33
        expected_gov_ratio = 75
        expected_inst_ratio = 25

        result = calculate_total_research_cost(government_funding)
        
        self.assertAlmostEqual(result[0], expected_total, places=2)
        self.assertAlmostEqual(result[1], expected_institution, places=2)
        self.assertAlmostEqual(result[2], expected_gov_ratio, places=2)
        self.assertAlmostEqual(result[3], expected_inst_ratio, places=2)

    def test_calculate_total_research_cost_decimal(self):
        government_funding = 75.5
        expected_total = 100.67
        expected_institution = 25.17
        expected_gov_ratio = 75
        expected_inst_ratio = 25

        result = calculate_total_research_cost(government_funding)
        
        self.assertAlmostEqual(result[0], expected_total, places=2)
        self.assertAlmostEqual(result[1], expected_institution, places=2)
        self.assertAlmostEqual(result[2], expected_gov_ratio, places=2)
        self.assertAlmostEqual(result[3], expected_inst_ratio, places=2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    runner = unittest.TextTestRunner(resultclass=CustomTestResult)
    runner.run(suite)