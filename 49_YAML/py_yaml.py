"""
this script is used to exercise the yaml library.

Author: FarolDaPraia
Date: 10/12/2020
"""

import yaml


def yaml_loader(filepath):
    """Load a yaml file."""
    with open(filepath, 'r') as file_descriptor:
        data = yaml.load(file_descriptor)
    return data


def yaml_dump(filepath, data):
    """Dump data to a yaml file."""
    with open(filepath, 'w') as file_descriptor:
        yaml.dump(data, file_descriptor)
    output = yaml.dump(data)
    return data


if __name__ == "__main__":
    filepath = 'data.yaml'
    data = yaml_loader(filepath)

    metadata = data.get('person')
    for metadata_name, metadata_value in metadata.items():
        print(metadata_name, metadata_value)

    filepath2 = 'test.yaml'
    data2 = {'items': {'sword': 100, 'axe': 80, 'boots': 40}}
    teste = yaml_dump(filepath2, data2)
