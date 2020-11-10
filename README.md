# requests
This script iterate the content of all  text files in a specific folder, each text file is made up four lines, 
this lines are the values four dictionary keys(title, name, date, and feedback) respectively for each text file. 
After converting the content of text files into dictionaries, using the requests.post from the request library,
it post the content of the dictionaries(as json format) to a webpage.
