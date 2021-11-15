import yaml
from typing import Union
import io


def parse_yaml(yaml_path: str) -> dict:
    with open(yaml_path, "r") as stream:
        try:
            yaml_data: dict = yaml.safe_load(stream)
            return yaml_data

        except yaml.YAMLError as e:
            print(f"we had a problem while parsing the yaml, error: {e}")
            raise e


def append_compatible_key(key: str, value: Union[str, list, object], additional_data: dict) -> bool:

    if  isinstance(value, list):
        for dict_item in value:
            for tuple_item in dict_item.items():
                if append_compatible_key(tuple_item[0], tuple_item[1], additional_data):
                    value.append(additional_data)
                    return False

    elif isinstance(value, dict):
        for item in value.items():
            if append_compatible_key(item[0], item[1], additional_data):
                # assume that in case of dictionary we want to add the additional config as new item in list
                value[item[0]] = [item[1], additional_data[item[0]]]
                return False
    

    if key == list(additional_data.keys())[0]:
        return True


def append_config(yaml_path: str, additional_config: dict):
    try:
        yaml_data: dict = parse_yaml(yaml_path)


        for key, value in yaml_data.items():
            # assume that we get the additinal config as dict 
            # that the whole dict should append as new item in the list of the compatible key
            append_compatible_key(key, value, additional_config)

        with io.open('yaml_exercise\\result-yaml.yaml', 'w', encoding='utf8') as outfile:
            yaml.dump(yaml_data, outfile, default_flow_style=False, allow_unicode=True)
    
    except Exception as e:
        print(f"we coudn't append the additional conifg to the yaml, Error: {e}")

