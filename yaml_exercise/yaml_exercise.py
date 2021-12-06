from typing import Union
import yaml


def parse_yaml(yaml_path: str) -> dict:
    with open(yaml_path, "r") as stream:
        try:
            yaml_data: dict = yaml.safe_load(stream)
            return yaml_data

        except yaml.YAMLError as e:
            print(f"we had a problem while parsing the yaml, error: {e}")
            raise e


def recursive_append_with_compatible_key(orginal_data: Union[dict, list, str], additional_data: dict) -> bool:
    additional_data_key: str = list(additional_data.keys())[0]

    if isinstance(orginal_data, list):
        for item in orginal_data:
            if isinstance(item, dict):
                if recursive_append_with_compatible_key(item, additional_data):
                    orginal_data.append(additional_data)
                    return False

    elif isinstance(orginal_data, dict):
        if additional_data_key in orginal_data:
            return True

        for key, value in orginal_data.items():

            if recursive_append_with_compatible_key(value, additional_data):
                orginal_data[key] = [value, additional_data]
                return False

    else:
        return False


def append_additional_config(yaml_path: str, additional_config: dict) -> dict:
    yaml_data: dict = parse_yaml(yaml_path)

    recursive_append_with_compatible_key(yaml_data, additional_config)

    with open('result_yaml.yaml', 'w', encoding='utf8') as outfile:
        yaml.dump(yaml_data, outfile, default_flow_style=False, allow_unicode=True)

    return yaml_data
