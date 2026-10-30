###### **Log File Analyzer using Python**



###### **Project Description**

The Log File Analyzer is a Python-based project that reads server log files and analyzes request information. It identifies the total number of requests, error responses, frequently used IP addresses, and most requested endpoints. It also generates a summary report containing the analysis results.



###### **Objectives**

\- Read and process server log files.

\- Count total incoming requests.

\- Identify HTTP error responses.

\- Find the most frequently used IP addresses.

\- Identify the most requested endpoints.

\- Generate a summary report.



###### **Technologies Used**

\- Python

\- Regular Expressions (re)

\- Collections (Counter)

\- File Handling

\- Dictionaries

###### 

###### **Features**

\- Reads server log files.

\- Counts HTTP status codes.

\- Identifies 4xx and 5xx error responses.

\- Displays the top 5 IP addresses.

\- Finds the most requested endpoints.

\- Handles malformed log lines.

\- Saves analysis results in a separate text file.



###### **Project Structure**

Log-File-Analyzer/

│

├── log\_analyzer.py

├── access.log

├── summary\_report.txt

└── README.md



###### **How to Run the Project**



Step 1: Install Python on your system.



Step 2: Download or clone this repository.



Step 3: Make sure the `access.log` file is available in the project folder.



Step 4: Open the terminal and run: python log\_analyzer.py



Step 5: Enter the log file name when prompted: access.log



###### **Sample Output**



========== SERVER LOG ANALYSIS REPORT ==========



Total Requests: 10

Total Error Responses: 3

Malformed Log Lines: 0



HTTP STATUS CODES:

200: 7 requests

403: 1 requests

404: 1 requests

500: 1 requests



TOP IP ADDRESSES:

192.168.1.10 : 3 requests

192.168.1.11 : 3 requests

192.168.1.12 : 2 requests

192.168.1.13 : 2 requests



MOST REQUESTED ENDPOINTS:

/home : 4 requests

/about : 2 requests

/products : 2 requests



Summary report saved as summary\_report.txt



###### Learning Outcomes

Through this project, I learned how to work with text files, process strings using regular expressions, use dictionaries and Counter for data analysis, handle exceptions, and generate reports using Python.



###### **Conclusion**

This project helped me understand how server log files can be analyzed using Python. It improved my knowledge of file handling, data processing, and basic data analysis.

