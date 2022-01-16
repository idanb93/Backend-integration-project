import json
from collections import defaultdict


class ConnectorSettings(object):

    run_interval_seconds = None  # int - iterations interval in seconds for current connector
    script_file_path = None  # string - the file path to the connector script
    connector_name = None  # string - connector name
    params = None  # ConnectorParams object - see below
    output_folder_path = None  # string - file path for connector output

    def __init__(self, name, interval, script_path, connector_name, output_path):

        self.name = name
        self.run_interval_seconds = interval
        self.script_file_path = script_path
        self.connector_name = connector_name
        self.output_folder_path = output_path

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    # def set_run_interval_seconds(self):
    #
    #     while True:
    #         try:
    #             interval = int(input("Please enter the interval: "))
    #         except ValueError:
    #             print("You did not enter an int, try again.")
    #             continue
    #         else:
    #             return interval
    #
    # def set_path(self):
    #
    #     while True:
    #
    #         if self.script_file_path is None:
    #             path1 = input("Please enter the connector script path: ")
    #         else:
    #             path1 = input("Please enter the path you want to create the output file: ")
    #
    #         if os.path.isdir(path1):
    #             return path1
    #         else:
    #             print("You did not enter a valid path, try again.")
    #             continue
    #
    # def set_connector_name(self):
    #
    #     while True:
    #
    #         connector_script_file = input("Please enter the name of the connector script: (without .py) ")
    #
    #         if os.path.exists(self.script_file_path + "\\" + connector_script_file + '.py'):
    #             return connector_script_file
    #         else:
    #             print(f"The script file '{connector_script_file}.py' is not at {self.script_file_path}, try again.")
    #             continue


class ConnectorParams(object):

    source_folder_path = None  # string - file path for entity list files
    iteration_entities_count = None  # int - how many entities to process each interval (ignore the rest)

    def __init__(self, path, iteration_entities_count):

        self.source_folder_path = path
        self.iteration_entities_count = iteration_entities_count

    # def set_path(self):
    #
    #     while True:
    #
    #         path1 = input("Please enter the path to the files containing the entities you want to scan using the VirusTotal API: ")
    #
    #         if os.path.isdir(path1):
    #             return path1
    #         else:
    #             print("You did not enter a valid path, try again.")
    #             continue

    # def set_iteration_entities_count(self):
    #
    #     while True:
    #
    #         try:
    #             entities_count = int(input("Please enter how many entities you would like to read from the file: "))
    #         except ValueError:
    #             print("You did not enter an int, try again.")
    #             continue
    #         else:
    #             return entities_count


class ConnectorResult(object):

    # alerts = defaultdict(lambda: "")

    alerts = {}  # Dictionary {string, any} - connector output with data per entity. Key = Entity, value = entity data
