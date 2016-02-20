Evernote SDK Integration for Python
============================================

Overview
--------
**An integration of evernote api using python

Prerequisites
-------------
In order to use the code in this SDK, you need to obtain an API key from http://dev.evernote.com/documentation/cloud. You'll also find full API documentation on that page.

In order to run the sample code, you need a user account on the sandbox service where you will do your development. Sign up for an account at https://sandbox.evernote.com/Registration.action 

In order to run the client client sample code, you need a developer token. Get one at https://sandbox.evernote.com/api/DeveloperToken.action
1. In order to first run the app you would need to have Python version 3 or greater installed
2. Evernote Api version 1.25
3. To install evernote api you need to run the following command python setup.py install

Getting Started
---------------
 
1. Open app/client/auth.py
2. Add your developer token/ oauth token.
3. On the command line, run the following command to execute the script:

    python app/client/main.py

The following classes are present 
* Auth - This would allow your app to authenticate users to evernote using api
* Note - This is used to create note, get specific note using guid
* Notebook - This is used to create notebooks, fetch all notebooks and returns tags and notes associated with a notebook
* Tags - Allows users to get all tags and create new tags 

Note: You can perform more operations using <a href="https://dev.evernote.com/doc/reference/NoteStore.html">Evernote Api</a>
