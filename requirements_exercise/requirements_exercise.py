

def parse_file(file_dir: str, file_name: str)-> list:

    file_path = file_dir + file_name 

    with open(file_path) as file:
        lines = file.readlines()
        file_lines = [line.rstrip() for line in lines]
        
        return file_lines


def recursive_packages_concat(requirements_file_name: str,requirements_dir: str, result_string: str) -> str:
    
    requirements_list: list = parse_file(requirements_dir, requirements_file_name)


    for requirement in requirements_list:
        if "-r requirement" in requirement:
            result_string = recursive_packages_concat(requirement.split(" ")[1], requirements_dir,  result_string)
        
        else:
            result_string += requirement + " "
      
    return result_string


def concat_requierments_packages(requirements_path: str) -> str:
    

    requirements_dir: str = "\\".join(requirements_path.split('\\')[:-1]) + "\\"

    requirements_file_name: str = requirements_path.replace(requirements_dir , '')

    result_str: str = ""

    result_str = recursive_packages_concat(requirements_file_name, requirements_dir, result_str)
    result_str = " ".join(result_str.split())

    return result_str