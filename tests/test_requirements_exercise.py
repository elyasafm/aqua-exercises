import unittest
from requirements_exercise.requirements_exercise import recursive_packages_concat, concat_requierments_packages 


class TestRequirementsExercise(unittest.TestCase):
    
    maxDiff = None

    def setUp(self):
        self.requirements_path = ".\\tests\\requirements_files\\requirements.txt"


    def test_concat_requierments_packages(self):
        result_string = concat_requierments_packages(self.requirements_path)
        expected_result = "PyYAML==6.0 requests==2.26.0 matplotlib==3.2.1 numpy==1.18.5 pandas==1.0.4"
        self.assertEqual(result_string, expected_result)


if __name__ == "__main__":
    unittest.main()

