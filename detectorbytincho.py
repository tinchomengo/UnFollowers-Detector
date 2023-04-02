from bs4 import BeautifulSoup
import re
import os
import json
import lxml

val = []
followers_file = ("followers.html")
following_file = ("following.html")
print("Instagram Unfollowers you follow:", "\n")

if os.path.splitext(followers_file)[1] and os.path.splitext(following_file)[1] == ".json":
    with open(followers_file, 'r') as f1:
        data1 = json.load(f1)
    with open(following_file, 'r') as f2:
        data2 = json.load(f2)

    for x in range(0, len(data2["relationships_following"])):
        val.append(data2["relationships_following"][x]
                   ["string_list_data"][0]["value"])

    for obj in range(0, len(data1)):
        if data1[obj]['string_list_data'][0]['value'] in val:
            val.remove(data1[obj]['string_list_data'][0]['value'])

    [print("- " + x) for x in val]

elif os.path.splitext(followers_file)[1] and os.path.splitext(following_file)[1] == ".html":
    with open(followers_file) as html_file:
        soup1 = (BeautifulSoup(html_file, 'lxml')).prettify()
        f1 = re.findall(r'\b.com/\w+\.?\w*', soup1, re.I)
    with open(following_file) as html_file:
        soup2 = (BeautifulSoup(html_file, 'lxml')).prettify()
        f2 = re.findall(r'\b.com/\w+\.?\w*', soup2, re.I)
    for x in f2:
        val.append(x[5:])
    for i in f1:
        if i[5:] in val:
            val.remove(i[5:])
    [print("- " + x) for x in val]
else:
    print("Error: You entered files in the wrong format :(", "\n")