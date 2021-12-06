import os


def parse_file(file_dir: str, file_name: str) -> list[str]:
    file_path: str = f"{file_dir}\\{file_name}"

    with open(file_path) as file:
        file_lines: list = [line.strip() for line in file.readlines()]
        filtered_lines: list[str] = list(filter(None, file_lines))

        return filtered_lines


def recursive_concat_requirements(requirements_file_name: str, requirements_dir: str, result_string: str) -> str:
    requirements_list: list = parse_file(requirements_dir, requirements_file_name)

    for requirement in requirements_list:
        if requirement.startswith("-r"):
            requirements_path: str = requirement.split(" ")[1]
            result_string = recursive_concat_requirements(requirements_path, requirements_dir, result_string)

        else:
            result_string += requirement + " "

    return result_string


def concat_requirements(requirements_path: str) -> str:
    requirements_file_name: str = os.path.basename(requirements_path)
    requirements_dir: str = os.path.dirname(requirements_path)
    result_str: str = ""

    all_requirements_str: str = recursive_concat_requirements(requirements_file_name, requirements_dir, result_str)

    return all_requirements_str.strip()
