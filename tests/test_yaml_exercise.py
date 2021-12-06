import unittest
from unittest.mock import patch
from yaml_exercise.yaml_exercise import append_additional_config, recursive_append_with_compatible_key


class TestYamlExercise(unittest.TestCase):
    maxDiff = None

    def test_append_config(self):
        yaml_data: dict = {'apiVersion': 'machinelearning', 'kind': 'SeldonDeployment',
                     'metadata': {'labels': {'app': 'seldon'}, 'name': 'seldon-deployment-{{workflow.name}}',
                                  'namespace': 'kubeflow'},
                     'spec': {'annotations': {'project_name': 'NLP Pipeline', 'deployment_version': 'v1'},
                              'name': 'seldon-deployment-{{workflow.name}}', 'predictors': [{'componentSpecs': [{
                             'spec': {
                                 'containers': [
                                     {
                                         'image': 'clean_text_transformer:0.1',
                                         'imagePullPolicy': 'IfNotPresent',
                                         'name': 'cleantext'}],
                                 'volumes': [
                                     {
                                         'name': 'mypvc',
                                         'persistentVolumeClaim': {
                                             'claimName': '{{workflow.name}}-my-pvc'}}]}}],
                             'graph': {'children': [{
                                 'name': 'spacytokenizer',
                                 'endpoint': {
                                     'type': 'REST'}}]},
                             'annotations': {
                                 'predictor_version': 'v1'}}]}}

        expected_result: dict = {'apiVersion': 'machinelearning', 'kind': 'SeldonDeployment',
                            'metadata': {'labels': {'app': 'seldon'}, 'name': 'seldon-deployment-{{workflow.name}}',
                                         'namespace': 'kubeflow'},
                            'spec': {'annotations': {'project_name': 'NLP Pipeline', 'deployment_version': 'v1'},
                                     'name': 'seldon-deployment-{{workflow.name}}', 'predictors': [{'componentSpecs': [{
                                    'spec': {
                                        'containers': [
                                            {
                                                'image': 'clean_text_transformer:0.1',
                                                'imagePullPolicy': 'IfNotPresent',
                                                'name': 'cleantext'},
                                            {
                                                'image': 'tfidf_vectorizer:0.1',
                                                'imagePullPolicy': 'IfNotPresent',
                                                'name': 'tfidfvectorizer'}],
                                        'volumes': [
                                            {
                                                'name': 'mypvc',
                                                'persistentVolumeClaim': {
                                                    'claimName': '{{workflow.name}}-my-pvc'}}]}}],
                                    'graph': {
                                        'children': [{
                                            'name': 'spacytokenizer',
                                            'endpoint': {
                                                'type': 'REST'}}]},
                                    'annotations': {
                                        'predictor_version': 'v1'}}]}}

        additional_config: dict = {
            "image": "tfidf_vectorizer:0.1",
            "imagePullPolicy": "IfNotPresent",
            "name": "tfidfvectorizer"
        }

        with patch("yaml_exercise.yaml_exercise.parse_yaml") as parse_yaml:
            parse_yaml.return_value = yaml_data

            yaml_data_result: dict = append_additional_config("yaml_path", additional_config)
            self.assertEqual(expected_result, yaml_data_result)

    def test_recursive_append_with_compatible_key(self):
        data: dict = {"outer_key":
                         {"inner_key": "inner_value"}
                     }

        additional_data: dict = {"inner_key": "config to add"}

        expected_result: dict = {"outer_key": [
            {"inner_key": "inner_value"},
            {"inner_key": "config to add"}
        ]
        }

        recursive_append_with_compatible_key(data, additional_data)
        self.assertEqual(expected_result, data)


if __name__ == "__main__":
    unittest.main()
