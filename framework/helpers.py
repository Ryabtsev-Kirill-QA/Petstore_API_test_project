import logging
import json
import os
from pathlib import Path

SCHEMA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')


def load_schema(file_name):
    with open(os.path.join(SCHEMA_PATH, file_name)) as file:
        schema = json.load(file)
        return schema
