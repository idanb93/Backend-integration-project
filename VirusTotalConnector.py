import re
import os
import sys
import json
import requests
from time import sleep
from DataModels import ConnectorResult
from SubProcessInputOutputHandler import SubProcessInputOutputHandler


def is_valid_url(string):
    regex = r'\b[A-Za-z0-9._%+-]+.[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    try:
        url = re.match(regex, string)
        return url is not None
    except:
        #  URL Checking was not successful
        return None


def list_files_in_the_source_folder(source_folder_path, text_files_from_the_given_source_folder):
    for filename in os.listdir(source_folder_path):
        if filename.endswith(".txt"):
            text_files_from_the_given_source_folder.append(f"{source_folder_path}\\{filename}")


def read_domains_from_file(filename, iteration_entities_count):
    list_of_domains_from_file = []

    with open(filename) as f:
        lines = f.read().splitlines()
        if lines:
            [list_of_domains_from_file.append(lines[i]) for i in range(0, iteration_entities_count) if is_valid_url(lines[i])]

    return list_of_domains_from_file


def scan_domains(list_of_domains, connector_result, queued_requests):

    for domain in list_of_domains:

        try:

            params = {'apikey': "4688caacd040f4ef5e0aaf7751ccc71207a8764744fc122c61228c3374764f5d", 'resource': domain, 'scan': 1}
            response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=params)
            response_json = json.loads(response.content)

            if response_json['verbose_msg'] == 'Scan request successfully queued, come back later for the report':
                # URL does not exist in VirusTotal engines database
                queued_requests.append(response_json['resource'])

            elif response_json['positives'] == 0:
                connector_result.alerts[domain] = "NOT MALICIOUS"

            else:
                connector_result.alerts[domain] = "MALICIOUS"

            # Adjusting the script to wait 30-60 before querying VirusTotal API again.
            sleep(40)

        except:
            connector_result.alerts[domain] = "MALICIOUS"


def main():

    io_mgr = SubProcessInputOutputHandler()
    connector_params = io_mgr.connector_params
    connector_result = ConnectorResult()

    queued_requests = []  # list - Scan queued requests that were not found in the VirusTotal database.
    text_files_from_the_given_source_folder = []  # list - Contains the files we want to scan in the source folder.
    current_file = ""  # string - Holds the file name you are currently working on.

    list_files_in_the_source_folder(connector_params.source_folder_path, text_files_from_the_given_source_folder)

    if not text_files_from_the_given_source_folder:
        print("There are no txt files in the folder")
        sys.exit()

    current_file = text_files_from_the_given_source_folder.pop()
    list_of_domains = read_domains_from_file(current_file, connector_params.iteration_entities_count)
    scan_domains(list_of_domains, connector_result, queued_requests)
    scan_domains(queued_requests, connector_result, queued_requests)

    # Adding .done suffix to the current file
    if current_file.endswith(".txt"):
        os.rename(current_file, current_file.replace("txt", "done"))

    # Returns the data to the service framework
    stdo = io_mgr.end(connector_result)  # original
    print(stdo)


if __name__ == "__main__":
    main()
