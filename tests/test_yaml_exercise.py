import unittest
from yaml_exercise.yaml_exercise import append_compatible_key, append_config, parse_yaml


class TestYamlExercise(unittest.TestCase):
    
    maxDiff = None

    def setUp(self):
        self.yaml_path = ".\\tests\example-file.yaml"
        self.result_path = "yaml_exercise\\result-yaml.yaml"
        self.result_test_path = ".\\tests\\test-result-file.yaml"
        
        

    def test_append_config(self):
        
        yaml_data = parse_yaml(self.yaml_path)

        additional_config = {
            "image": "tfidf_vectorizer:0.1", 
            "imagePullPolicy": "IfNotPresent",
            "name": "tfidfvectorizer"
            }


        append_config(self.yaml_path, additional_config)
        
        result_data = parse_yaml(self.result_path)
        result_test_data = parse_yaml(self.result_test_path)

        self.assertEqual(result_data, result_test_data)

    
    def test_append_compatible_key(self):

        dict_item = {"key": 
            {"test": "value to test"}
            }
        
        additional_data = {"test": "config to add"}

        expected_result = {"key": 
                                {"test": 
                                    ["value to test", "config to add"]
                                }
                            }
        
        key = list(dict_item)[0]
        append_compatible_key(key, dict_item[key], additional_data)
        self.assertEqual(expected_result, dict_item)
        

if __name__ == "__main__":
    unittest.main()

