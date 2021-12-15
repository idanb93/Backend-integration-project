# Synopsis

In this project I built a framework that runs connectors scripts as a subprocesses (a connector script is a script that connects to an API), and saves the stdout result of the subprocess to a json file in a folder.

## Goals

Gain experience working with APIs: Reading documentation of APIs, getting the correct data from the text files I work with in order to send it to the API, understand the different context, erros and responses the API can return, handle the returning data in response and manage it.

## Motivation

During the project I experimented with the following:

 - Learned about Python Decorators ( @Property ) - in order to understand the best way to use getters and setters in object-oriented programming in python. 
 
 - Reading API Documentation and understand which data the API request needs, and what are the different responses the API could return.
 
 - Automate moving data around - opening the text files i wish to interact with, readinging the correct lines from the data, and using the data to run the API request, handle the response context errors, handle the response data.
 
 - Wokring with subprocesses - sending the sub-process the script file i wish to run, making the subprocess capture the output as an stdout, transfer the stdout output back to the main process and save it to a diserable form (json file in a specific folder).
