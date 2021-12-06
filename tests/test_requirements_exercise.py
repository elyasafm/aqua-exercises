import unittest
from unittest.mock import patch

from requirements_exercise.requirements_exercise import recursive_concat_requirements, concat_requirements


class TestRequirementsExercise(unittest.TestCase):
    maxDiff = None

    def test_recursive_concat_requirements(self):
        string_result: str = ""

        expected_result: str = "PyYAML==6.0 requests==2.26.0 matplotlib==3.2.1 "

        with patch("requirements_exercise.requirements_exercise.parse_file") as parse_file:
            parse_file.return_value = ["PyYAML==6.0", "requests==2.26.0", "matplotlib==3.2.1"]
            string_result = recursive_concat_requirements("requirements_file_name", "requirements_dir", string_result)

            self.assertEqual(expected_result, string_result)

    def test_concat_requirements(self):
        expected_result = "PyYAML==6.0 requests==2.26.0 matplotlib==3.2.1 numpy==1.18.5 pandas==1.0.4"

        with patch("requirements_exercise.requirements_exercise.parse_file") as parse_file:
            parse_file.side_effect = [['-r requirements1.txt', 'requests==2.26.0', '-r requirements2.txt'],
                                      ["PyYAML==6.0"],
                                      ["matplotlib==3.2.1", "numpy==1.18.5", "pandas==1.0.4"]]

            result_string = concat_requirements("requirements_path")
            self.assertEqual(parse_file.call_count, 3)
            self.assertEqual(expected_result, result_string)


if __name__ == "__main__":
    unittest.main()
