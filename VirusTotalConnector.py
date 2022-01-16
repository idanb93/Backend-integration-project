import json
import os
import re
import sys
from time import sleep

from Connector import Connector


class VirusTotalConnector(Connector):

    def __init__(self, api_key, url):
        Connector.__init__(self, api_key, url)
        self.queued_requests = []  # list of scan request that were queued
        self.list_of_files = []  # list of files that the user wish to read from

    def handle_response(self, response_json, domain):
        if response_json['verbose_msg'] == 'Scan request successfully queued, come back later for the report':
            self.queued_requests.append(response_json['resource'])
        elif response_json['positives'] == 0:
            self.connector_result.alerts[domain] = "NOT MALICIOUS"
        else:
            self.connector_result.alerts[domain] = "MALICIOUS"

    def is_valid_url(self, string_to_check):

        """
        This method check if a string is a valid url using regular expression.
        :param string_to_check: string to check if it is a valid url
        :return: return True if the string is a url, otherwise return None
        """
        regex = r'\b[A-Za-z0-9._%+-]+.[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        try:
            url = re.match(regex, string_to_check)
            return url is not None
        except:
            #  URL Checking was not successful
            return None

    def list_files(self, files_extension):

        """
        This method list the files that the user wants to work with.
        :param files_extension: the extension of the files the user wish to add to the list
        :return: None
        """

        for filename in os.listdir(self.connector_params.source_folder_path):
            if filename.endswith(files_extension):
                self.list_of_files.append(f"{self.connector_params.source_folder_path}\\{filename}")

    def read_lines_from_file(self, filename):

        """
        This method read specific lines from a file
        :param filename: file we wish to read from.
        :return: list with the specific lines.
        """

        lines_from_file = []

        with open(filename) as f:
            lines = f.read().splitlines()
            if lines:
                [lines_from_file.append(lines[i]) for i in range(0, self.connector_params.iteration_entities_count) if
                 self.is_valid_url(lines[i])]

        return lines_from_file


def main():

    api_key = "4688caacd040f4ef5e0aaf7751ccc71207a8764744fc122c61228c3374764f5d"
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    current_file = ""
    file_extension = ".txt"

    virus_total_connector = VirusTotalConnector(api_key, url)
    virus_total_connector.list_files(file_extension)

    if not virus_total_connector.list_of_files:
        print(f"There are no {file_extension} files in the source folder")
        sys.exit()

    current_file = virus_total_connector.list_of_files.pop()
    list_of_domains = virus_total_connector.read_lines_from_file(current_file)

    for domain in list_of_domains:
        response_json = virus_total_connector.request_data_from_api(domain)
        virus_total_connector.handle_response(response_json, domain)
        sleep(40)  # Waiting 40 seconds between each API request.

    # Adding .done suffix to the current file
    if current_file.endswith(".txt"):
        os.rename(current_file, current_file.replace("txt", "done"))

    # Returns the data to the service framework
    stdo = virus_total_connector.io_mgr.end(virus_total_connector.connector_result)
    print(json.dumps(stdo, sort_keys=True, indent=4, separators=(',', ': ')))


if __name__ == "__main__":
    main()
