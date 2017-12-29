# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "jsonUtility libpackage"
"""

import json


def dump_json(dictionary, store_location):   # pylint: disable=C0103
    """
    dump json
    :param dictionary: A dictionary
    :param store_location: A location Path
    :return:
    """
    file_name = "user_config.json"
    dumps = json.dumps(dictionary, indent=4)
    with open(store_location+file_name, "w") as f:
        f.write(dumps)


def add_to_json(dictionary, json_file):   # pylint: disable=C0103
    """
    add things to existing json
    :param dictionary: the new dictionary
    :param json_file: the old json file
    :return:
    """
    pass


def get_json_file(path):  # pylint: disable=C0103
    """
    get the Json file
    :param path: A location Path
    :return:
    """
    file_name = "user_config.json"
    with open(path+file_name, "r") as f:
        s = f.read()
        data = json.loads(s)
    return data


def get_key_value(search_dict, field):  # pylint: disable=C0103
    """
    get key from json dict
    :param search_dict:
    :param field:
    :return:
    """
    fields_found = []

    for key, value in search_dict.items():

        if key == field:
            fields_found.append(value)

        elif isinstance(value, dict):
            results = get_key_value(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = get_key_value(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result)

    return fields_found


def dumpKeyValue(dump_dict, field, val): # pylint: disable=C0103
    """
    Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    for key, value in dump_dict.items():

        if key == field:
            dump_dict[key] = val

        elif isinstance(value, dict):
            dumpKeyValue(value, field, val)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    dumpKeyValue(item, field, val)

    # dumpJson(dump_dict)
