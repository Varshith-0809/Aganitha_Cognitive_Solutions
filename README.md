# Aganitha_Cognitive_Solutions Task:
This Python program fetches research papers from the PubMed database based on a user-specified search query. It filters the results to identify papers with pharmaceutical or biotech company affiliations and non-academic authors. The results are then saved as a CSV file or printed to the console.

Requirements:
Python 3.x
requests library
argparse library
csv library
Use Poetry for dependency management and packaging.

Installation
To install the dependencies, you need to have Poetry installed. After installing Poetry, run the following command to install the dependencies:


Copy: 
poetry install #To run the program from the command line, use the following format:

Copy code: 
poetry run get-papers-list "your_query_here" 
#Where your_query_here is the search query you want to use to fetch papers from PubMed. [example "biotechnology AND pharmaceutical"]

Command-Line Options
query (required): The search query you want to use to fetch research papers. This will be passed to PubMed's search API.

-f, --file (optional): Specify the filename to save the results in CSV format. If this option is not provided, the results will be printed to the console.

-d, --debug (optional): Enable debug output, which will display additional information about the execution and API responses.

Examples

Search for papers and print the results to the console:


Copy code:
poetry run get-papers-list "pharmaceutical research"
Search for papers and save the results to a CSV file:


Copy code
poetry run get-papers-list "biotech cancer treatment" -f results.csv
Search for papers with debug output enabled:

bash
Copy code
poetry run get-papers-list "drug development" -d
Output
The program will return a CSV file (or print to the console) with the following columns:

PubmedID: Unique identifier for the paper.
Title: Title of the paper.
Publication Date: Date the paper was published.
Non-academic Author(s): Authors affiliated with non-academic institutions.
Company Affiliation(s): Names of pharmaceutical or biotech companies associated with the paper.
Corresponding Author Email: Email address of the corresponding author (if available).
Sample output in CSV format:

csv
Copy code
PubmedID,Title,Publication Date,Non-academic Author(s),Company Affiliation(s),Corresponding Author Email
39782636,Drug Development.,N/A,N/A,N/A,N/A
39782617,Drug Development.,N/A,"Cleveland Clinic, Cleveland, OH, USA.", "Eicosis Inc., Davis, CA, USA.", N/A
...
Error Handling
If the program encounters any issues (e.g., invalid query, failed API request), it will display an error message and indicate what went wrong.
If no results are found for the query, the program will display a message indicating that no papers were found.
Contributing
Feel free to fork the repository and submit issues or pull requests for bug fixes or new features.
