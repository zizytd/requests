#!/usr/bin/env python3
import os
import requests

folder = '/home/user/scripts/dictionary' #the folder that contains the text files 
z = []
r = []
for filename in os.listdir(folder): #iterate over each file in the folder
    full_filename = os.path.join(folder,filename)
    with open(full_filename) as text: #open each file
        p = text.readlines()
        r.append(p)
print(r) #lines of the content of each files are in a list inside a list

r = [[x.replace('\n','') for x in l] for l in r] #replace the \n in each list  with nothing
print(r)
for i in r:
    d = {'title':i[0],' name':i[1], 'date':i[2], 'feedback':i[3]} #assign the dictionary keys(title,name,date, and feedback) to list i indexes as values
    z.append(d)
print(z)
for b in z: #iterate over each dictionary
    response = requests.post('http://35.223.115.210/feedback/', json=b) #post the content of the dictionaries as json format.
    response.raise_for_status()
