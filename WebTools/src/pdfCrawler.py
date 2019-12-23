# MIT License
#
# Copyright (c) 2019 Johannes Bonk
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from PyPDF2 import PdfFileMerger
from urllib.parse import urlparse
from urllib.request import urlopen
import random
import string
import re
import os

# global variable declarations
start_font = """
            _  __  ____                    _
  _ __   __| |/ _|/ ___|_ __ __ ___      _| | ___ _ __
 | '_ \ / _` | |_| |   | '__/ _` \ \ /\ / | |/ _ | '__|
 | |_) | (_| |  _| |___| | | (_| |\ V  V /| |  __| |
 | .__/ \__,_|_|  \____|_|  \__,_| \_/\_/ |_|\___|_|
 |_|

[1] Save file in the current working directory
[2] Enter user specific directory to save the file

			"""

def getURLs():
	url = input("Input url: ")
	domain = urlparse(url)
	domain = '{uri.scheme}://{uri.netloc}/'.format(uri=domain) # format: protocol + domain
	html_src = urlopen(url) # get web html
	web_bin = html_src.read() # gets html binary
	web_src = web_bin.decode("utf-8") # decode src code binary to string
	potential_paths = re.findall('"([^"]*)"', web_src) # get all strings in between quotation marks
	url_list = []  # list containing all chapter urls
	for path in potential_paths:
		if (".pdf" in path):
			url_list.append(domain + path)
	return url_list

def getRndFileNames(url_list, save_dir):
	rnd_names = []
	for k in range(len(url_list)):
		rnd_names.append(save_dir + "\\" + ''.join(random.choice(string.ascii_letters) for i in range(20)) + ".pdf") # creates 20 char long random file names with .pdf tag
	return rnd_names

def generatePDFs(url_list, files):
	for i in range(len(url_list)):
		response = urlopen(url_list[i]) # open connection to pdf link
		file = open(files[i], 'wb') # generate file with name from files
		file.write(response.read()) # write content from connection to generated file
		file.close() # close file input stream
	return

def mergePDFs(res_file_name, files):
	merger = PdfFileMerger(False) # create pdf-merger object (strict = False to correct zero object error)
	for file in files:
		merger.append(file) # append all generated files
	merger.write(res_file_name) # write merged files as pdf with user specific file name
	merger.close() # close pdf-merger object
	return

def deletePDFs(files):
	for file in files:
		os.remove(file) # remove all  downloaded single files (merged one remains)
	return



# skript entry
print(start_font)
usr_acc = "n" # did the user accept the inputs ? (default no)
usr_option = "3" # == loop till valid user input
res_file_name = "" # name of result file without file extension
save_dir = "" # directory to save the files in
while usr_acc != "y" :
	usr_option = "3" # == loop till valid user input
	while (usr_option != "1") and (usr_option != "2"):
		usr_option = input("Enter the number of the option you want to use:")
		if (usr_option == "1"):
			save_dir = os.getcwd() # save at current working directory
		elif (usr_option == "2"):
			save_dir = input("Save as (absolute path): ") # save at specific path
			if (os.path.isdir(save_dir)): # does the path exist ?
				continue
			else:
				print("Path doesn´t exist or can´t write to directory")
				usr_option = "3"
		else:
		 	print("Invalid input!")
	file_exists = True;
	while file_exists == True:
		res_file_name = save_dir + "\\" + input("Please insert file name(without tag): ")  + ".pdf" # user input name for result file with path
		if os.path.exists(res_file_name) == True:
			print("File does already exist, please enter a new name")
		else:
			file_exists = False
	print("The file will be saved as: " + res_file_name)
	usr_acc = input("Continue? [y/n]: ")

url_list = getURLs() # get all urls linked to pdf files at page
rnd_file_names = getRndFileNames(url_list, save_dir) # generate a unique name for every pdf with preceding path
generatePDFs(url_list, rnd_file_names) # download all pdfs from url and save (temporary) with generated names
mergePDFs(res_file_name, rnd_file_names) # merge all downloaded pdfs
deletePDFs(rnd_file_names) # delete all temporary pdfs
print("Created " + res_file_name + ".pdf successfully!")
