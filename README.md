# Synopsis

In this project I built a service that runs connectors scripts(scripts that fetches an API) as a subprocesses, and saves the STDOUT of the subprocess to a JSON file in a folder.

## Goals

Gain experience working with APIs - Reading documentation of APIs, getting the correct data from the text files I work with in order to send it to the API, understand the different context, erros and responses the API can return, handle the returning data in response and manage it.

## Motivation

During the project I experimented with the following:

 - Learned about Python Decorators ( @Property ) - in order to understand the best way to use getters and setters in object-oriented programming in python. 
 
 - Reading API Documentation - understand which data the API request needs, and what are the different responses the API could return.
 
 - Automate moving data around - open specific text files from a specific folder, reading the relevant lines, using the data within the API request, handle the response context errors returning from the API, handle the response data.
 
 - Wokring with subprocesses - making the sub-process run a specific script file from a specific folder, making the subprocess capture the output as an stdout, transfer the stdout output back to the main process and save it to a diserable form (json file in a specific folder).
