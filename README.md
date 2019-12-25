# pdfCrawler
## Description
This is a simple tool which allows you to download and merge all PDF files from a website of your desire e.g free eBooks only available in chapters at publisher websites ...
## Hyperlinks
  * [Source code](https://github.com/johannesbonk/pdfCrawler/blob/master/pdfCrawler/pdfCrawler.py "source code")
  * [License](https://github.com/johannesbonk/pdfCrawler/blob/master/LICENSE "license")
## Usage
### Prerequisites
You will need Python 3 installed on your system.
Additionally you will need the library PyPDF2 installed. 
### Step 1:
After downloading the tool, switch to the folder containing **pdfCrawler.py**, start the terminal and enter

`$ python3 pdfCrawler.py` to start the tool.
### Step 2:
Select by either entering `1` or `2` into the console, whether you want so save the resulting **.pdf** file into the working or into a user specific directory.  
### Step 2.5: (Only if you took option 2 beforehand)
Enter the absolute path of the folder you want to save the file in.
### Step 3:
Enter the url containing the PDF files you want to download and merge.
`Input url: www.your-dowload-link.tld/PATH`
### Step 4: 
Confirm your inputs with `y`or cancel the download with `n`
## TODO list: 
  * Cleanup code
  * Write unit-test
  * Upload compiled binary for Windows and Unix systems
