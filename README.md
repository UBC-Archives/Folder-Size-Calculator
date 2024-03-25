# Folder Size Calculator
Python Folder Size Calculator

> Version: 1.0

> [UBC Records Management Office](https://recordsmanagement.ubc.ca)

> [GPL-3.0 License](https://www.gnu.org/licenses/gpl-3.0.en.html)

**Folder Size Calculator** is a simple Python script designed to calculate the size of folders and subfolders listed in an input text file. It outputs the results to an output text file, providing the size of each folder in megabytes (MB).

**How to Use:**

1. Input File: The script reads folder information from an input text file named 'input.txt.' Each line in the input file should follow the format: 'folder_path\tsize_in_bytes', where '\t' represents a tab character separating the file path and its size. For folders, the size should be represented as '-'. You can generate the input file by using the [Directory Inventory Generator](https://github.com/UBC-Archives/Directory-Inventory-Generator) program. Simply run the program and copy the contents of the 'Full Path' and 'Size (Bytes)' columns of the output file into a text file.
2. Output File: After processing the input file, the script generates an output text file named 'output.txt'. This file contains each folder path followed by its size in megabytes (MB), calculated based on the information provided in the input file.

**Installation:**

- Install Python: Ensure Python 3.x is installed on your system. You can download Python from [here](https://www.python.org/downloads).
- Download the Script: Download the Folder Size Calculator script from [this link](https://github.com/UBC-Archives/Folder-Size-Calculator/blob/main/UBC-RMO_FSC.py).
- Once downloaded, double-click on the downloaded UBC-RMO_FSC.py file to run the program. Ensure that the input file is located in the same folder as the Python script. The output file will be saved in the same directory as well.

**Disclaimer:**

Folder Size Calculator is provided as-is without any warranty. The University of British Columbia or its affiliates shall not be held responsible for any loss of data or unintended consequences resulting from the use of this application. Use it at your own risk and ensure you have backups of important data before running the folder size calculation process.
