Fetch Research Papers from PubMed:

This project is a Python program that fetches research papers from PubMed based on a user-specified query. The program retrieves paper details including the title, publication date, and affiliations, and can save the results to a CSV file.


Code Organization:
The project consists of the following main files:

1. get_papers.py: The main script that fetches paper details from PubMed based on the search query.
2. requirements.txt: A list of dependencies for the project.
3. README.md: Documentation explaining how to use the project.

Installation

To set up the project, follow these steps:

1. Clone the repository:
git clone https://github.com/username/repository-name.git (link)

2. Install dependencies: The project uses Poetry for dependency management. 
Install Poetry if you haven't already:

Install Poetry: https://python-poetry.org/docs/#installation

Once Poetry is installed, run the following command in the project directory to install dependencies:

poetry install

3. Run the Program: After installing the dependencies, you can run the program using:


poetry run python get_papers.py "your_query_here"

Usage:

The program accepts the following command-line arguments:

1. query: (Required) The search query for PubMed papers (e.g., "AI in healthcare").
2. -f or --file: (Optional) Specify a filename to save the results as a CSV file. Example: -f output.csv.
3. -d or --debug: (Optional) Enable debug output to see more detailed logs.

Example Usage:
1. To search for papers on "AI in healthcare" and save the results to papers.csv:

poetry run python get_papers.py "AI in healthcare" -f papers.csv

3. To search for papers on "AI in healthcare" and view debug information:

poetry run python get_papers.py "AI in healthcare" -d

Tools Used:
1. Poetry: Dependency management and packaging tool.
2. Requests: Library for making HTTP requests to the PubMed API.
3. Argparse: For handling command-line arguments.
