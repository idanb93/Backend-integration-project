import os
import sys

from DataModels import ConnectorParams


class SubProcessInputOutputHandler(object):
    @property
    def connector_params(self):

        result = ConnectorParams(f"{os.getcwd()}\source_folder", 4)

        # result.source_folder_path = input("Please enter the path to the files containing the entities you want to scan using the VirusTotal API: ")
        # result.iteration_entities_count = input("Please enter how many entities you would like to read from the file: ")

        return result

    def end(self, connector_result):

        return connector_result.alerts
        sys.exit()

