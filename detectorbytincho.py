# Created by: https://www.linkedin.com/in/martinmengo/ (Martin Mengo)
from modulo2 import *
from bs4 import BeautifulSoup
import re
import sys
import os
import json
import lxml
import subprocess


val = []
unfollowers = ""


def on_files_selected(file1, file2):
    global f1
    global f2
    f1 = file1
    f2 = file2


if __name__ == '__main__':
    app = MyApp(on_files_selected)
    app.run()

f1.replace("/", "\\")
f2.replace("/", "\\")

try:
    if (os.path.splitext(f1)[1] == ".json") and (os.path.splitext(f2)[1] == ".json"):

        with open(f1, 'r') as f1:
            data1 = json.load(f1)
        with open(f2, 'r') as f2:
            data2 = json.load(f2)

        for x in range(0, len(data2["relationships_following"])):
            val.append(data2["relationships_following"][x]
                       ["string_list_data"][0]["value"])
        for obj in range(0, len(data1)):
            if data1[obj]['string_list_data'][0]['value'] in val:
                val.remove(data1[obj]['string_list_data'][0]['value'])
        for x in val:
            unfollowers += (x + "\n")
    elif (os.path.splitext(f1)[1] == ".html") and (os.path.splitext(f2)[1] == ".html"):

        with open(f1) as html_file:
            soup1 = (BeautifulSoup(html_file, 'lxml')).prettify()
            f1 = re.findall(r'\b.com/\w+\.?\w*', soup1, re.I)
        with open(f2) as html_file:
            soup2 = (BeautifulSoup(html_file, 'lxml')).prettify()
            f2 = re.findall(r'\b.com/\w+\.?\w*', soup2, re.I)

        for x in f2:
            val.append(x[5:])
        for i in f1:
            if i[5:] in val:
                val.remove(i[5:])
        for x in val:
            unfollowers += (x + "\n")
    else:

        unfollowers = "Error: You entered the files in the wrong format :("
except:
    unfollowers = "Error :("

working_directory = os.path.dirname(os.path.abspath(__file__))
subprocess.run(["python", "lista.py", unfollowers], cwd=working_directory)
