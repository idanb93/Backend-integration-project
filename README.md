# Synopsis

In this project I built a service that runs connector scripts (script that query API) as subprocesses, the service saves the STDOUT of each subprocess to a JSON file in a folder.

## Goals

Gain experience working with APIs in Python (requests library) - Reading documentation of APIs, getting the correct data from the text files I work with in order to send it to the API, understand the different context, erros and responses the API can return, handle the returning data in response and manage it.

## Motivation

During the project I experimented with the following:

 - Learned about Python Decorators ( @Property ) - in order to understand the best way to use getters and setters in object-oriented programming in python. 
 
 - Reading API Documentation - understand which data the API request needs, and what are the different responses the API could return.
 
 - Working with files and sending data to APIs - open specific text files from a specific folder, reading the relevant lines, using this data within an API request, handle the response, context, errors returning from the API.
 
 - Wokring with subprocesses - making the sub-process run a specific script file from a specific folder, making the subprocess capture the output as an STDOUT, transfer the STDOUT output back to the main process, and save it to a specific format (JSON file in a specific folder).
