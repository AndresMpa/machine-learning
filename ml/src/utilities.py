import numpy as np
import codecs
import yaml
import json
import os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"

'''
Creates a directory if it doesn't exist
'''


def handle_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


'''
Returns a list of params from params.yml
'''


def list_param():
    params = yaml.safe_load(open(ROOT_PATH + "params.yaml"))
    for param in params:
        print(f"{param}: {params[param]}")


'''
Get a param value
'''


def get_params(request):
    param = yaml.safe_load(open(ROOT_PATH + "params.yaml"))[request]
    return param


'''
Write a file in the given path
'''


def write_file(raw_content, path, name="file.json"):
    handle_directory(path)

    content = json.dumps(raw_content, indent=4)

    with open(f"{path}{name}", "w") as outfile:
        outfile.write(content)


'''
Read a Json like file
'''


def read_numpy_like_json(file_path):
    raw_content = codecs.open(f"{ROOT_PATH}{file_path}", 'r', encoding='utf-8').read()
    content = json.loads(raw_content)

    return content
