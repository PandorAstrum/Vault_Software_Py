from data.lib.localStorage import LocalStorage
import json

# dump json
def dumpJson(dict):
    """
    Dump the dictionary into a json
    :param dict: A dictionary value
    :return: None
    """
    ls = LocalStorage(debug=True)
    path = ls.dump_dir
    ls.make_dir(path)
    fileName = "user_config.json"
    dumps = json.dumps(dict, indent=4)
    with open(path+fileName, "w") as f:
        f.write(dumps)

def getJsonFile():
    """
    Get the json file
    """
    ls = LocalStorage(debug=True)
    path = ls.dump_dir
    fileName = "user_config.json"
    with open(path+fileName, "r") as f:
        s = f.read()
        data = json.loads(s)
    return data

def getKeyValue(search_dict, field):
    """
    Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    fields_found = []

    for key, value in search_dict.items():

        if key == field:
            fields_found.append(value)

        elif isinstance(value, dict):
            results = getKeyValue(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = getKeyValue(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result)

    return fields_found

def dumpKeyValue(dump_dict, field, val):
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

    dumpJson(dump_dict)