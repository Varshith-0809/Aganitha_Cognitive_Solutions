import argparse
import requests
import csv

# Function to fetch paper IDs based on query
def fetch_paper_ids(query):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10,  # Adjust this number based on how many results you want
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])
    else:
        print(f"Error: Unable to fetch paper IDs (HTTP {response.status_code})")
        return []

# Function to identify if an affiliation is non-academic (heuristics)
def is_non_academic_affiliation(affiliation):
    return any(keyword in affiliation.lower() for keyword in ['pharmaceutical', 'biotech', 'company', 'lab'])

# Function to fetch paper details with affiliations, including authors and emails
def fetch_paper_details_with_affiliations(paper_ids):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    papers_data = []
    for paper_id in paper_ids:
        params = {
            "db": "pubmed",  # PubMed database
            "id": paper_id,  # PubMed paper ID
            "retmode": "json",  # Return data in JSON format
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            docsum = data.get("result", {}).get(paper_id, {})
            title = docsum.get("title", "N/A")
            pub_date = docsum.get("pubdate", "N/A")
            authors = docsum.get("authors", [])
            email = "N/A"  # Placeholder for corresponding author email
            non_academic_authors = []
            companies_affiliated = []

            # Loop through authors and check for affiliations
            for author in authors:
                affiliation = author.get("affiliation", "")
                if is_non_academic_affiliation(affiliation):
                    non_academic_authors.append(author.get("name", "N/A"))
                if "pharmaceutical" in affiliation.lower() or "biotech" in affiliation.lower():
                    companies_affiliated.append(affiliation)

                # Placeholder: extract corresponding author email (adjust this as needed)
                if author.get("corresponding", False):
                    email = author.get("email", "N/A")

            papers_data.append({
                "PubmedID": paper_id,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": ", ".join(non_academic_authors),
                "Company Affiliation(s)": ", ".join(companies_affiliated),
                "Corresponding Author Email": email,
            })
        else:
            print(f"Error: Unable to fetch details for paper ID {paper_id} (HTTP {response.status_code})")
    
    return papers_data

# Function to save the results to a CSV file
def save_to_csv(papers, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"])
        writer.writeheader()
        writer.writerows(papers)

# Main function to handle command-line interface
def main():
    parser = argparse.ArgumentParser(description="Fetch papers from PubMed based on a query.")
    
    # Adding command-line arguments
    parser.add_argument("query", help="Search query for PubMed papers")
    parser.add_argument("-f", "--file", help="Specify the filename to save the results")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug information")
    
    args = parser.parse_args()
    
    # Debugging: Print query if debug flag is set
    if args.debug:
        print(f"Debug: Searching for query: {args.query}")

    # Fetch paper IDs using the query
    paper_ids = fetch_paper_ids(args.query)
    
    # Fetch paper details using the paper IDs
    papers = fetch_paper_details_with_affiliations(paper_ids)
    
    # Save to CSV or print to console
    if args.file:
        save_to_csv(papers, args.file)
    else:
        # Print papers to console
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
