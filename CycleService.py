import json
import datetime
import os

from DataModels import ConnectorSettings
from time import sleep
import subprocess
from subprocess import Popen, PIPE, STDOUT


def save_to_output_folder(output_folder_path, output):

    now = datetime.datetime.now()
    current_date_and_time = now.strftime("%Y-%m-%d %H:%M:%S").replace(":", "-")

    with open(f'{output_folder_path}\\{current_date_and_time}.json', 'w') as fp:
        json.dump(output, fp)


def run_service(connectors):

    print("\nWelcome ! The Service is Up\n")
    output = ""  # output - the stdout that returns from the script of the connector.
    item = connectors.popitem()  # item - tuple of (connector_name : ConnectorSettings).

    while True:

        if output != "There are no txt files in the folder":

            print(f"Connector: {item[1].name}\n"
                  f"Script file: {os.getcwd()}\\{item[1].connector_name}.py\n"
                  f"Interval: {item[1].run_interval_seconds} seconds\n")
            print(f"The connector script is hardcoded to: \n"
                  f"iteration entities count: 4 entities from each file\n"
                  f"wait between each API request: 40 seconds\n")

            my_path = f'{os.getcwd()}\VirusTotalConnector.py'
            p1 = subprocess.Popen(["python", my_path], shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
            output = p1.stdout.read().decode('utf-8')
            print(output)
            output = output.replace("\r\n", "")

            if output != "There are no txt files in the folder":
                save_to_output_folder(item[1].output_folder_path, output)

            sleep(item[1].run_interval_seconds)

        else:
            try:
                item = connectors.popitem()
                output = ""
            except KeyError:
                print('The dictionary has no item now...')
                break


def main():

    connectors = {}  # Dictionary {string, ConnectorSettings} - connector's name with settings per connector.

    connector1 = ConnectorSettings("connector1", 30, os.getcwd(), "VirusTotalConnector", f"{os.getcwd()}\output_folder")
    connectors[connector1] = connector1
    connector2 = ConnectorSettings("connector2", 13, os.getcwd(), "VirusTotalConnector", f"{os.getcwd()}\output_folder2")
    connectors[connector2] = connector2

    if connectors:
        run_service(connectors)


if __name__ == "__main__":
    main()
