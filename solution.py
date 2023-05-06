""" TermSearcher """

import re
import argparse
import sys


class TermSearcher:
    """
    A class to search and process terms in a file.
    """

    def __init__(self, file):
        """
        Initializes the TermSearcher class with a file path and reads its contents.

        Args:
            file (str): The path to the file to be searched.

        Returns:
            None
        """
        self.file = file
        self.file_content = self.read_file()

    def read_file(self):
        """
        Reads the contents of the file and returns it as a list of strings.

        Args:
            None

        Returns:
            file_content (list): A list of strings containing the lines of the file.
        """
        try:
            with open(self.file, 'r', encoding='utf-8') as input_file:
                file_content = input_file.readlines()
            return file_content
        except FileNotFoundError:
            print("File not found.")
            sys.exit(1)

    def search_last_term(self):
        """
        Searches for the last term in the file.

        Args:
            None

        Returns:
            last_line (str): A string representing the last line of the file, i.e., the last term.
        """
        last_line = self.file_content[-1]
        return last_line

    def get_source_terms(self):
        """
        Returns all terms in the file except the last one.

        Args:
            None

        Returns:
            source_list (list): A list of strings with all terms in the file except the last one.
        """
        source_lines = self.file_content[:-1]
        source_list = list(source_lines)
        return source_list

    def search_terms(self):
        """
        Searches for all terms in the file that contain the last term.

        Args:
            None

        Returns:
            terms_found (list): A list of strings with all terms that contain the last term.
        """
        terms_found = []
        for source_term in self.get_source_terms():
            if str(self.search_last_term()) in source_term:
                terms_found.append(source_term)
        return terms_found

    def process_terms(self, terms):
        """
        Processes the terms by removing non-alphabetic characters, extra space, and adding brackets.

        Args:
            terms (list): A list of strings representing the terms to be processed.

        Returns:
            processed_terms (list): A list of strings representing the processed terms.
        """
        processed_terms = []
        for term in terms:
            term = re.sub(r'[^a-zA-Z\s]', ' ', term)
            term = term.strip()
            term = re.sub(r'\s+', ' ', term)
            term = f"[{term}]"
            processed_terms.append(term)
        return processed_terms


if __name__ == "__main__":
    # Check if the file path was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python solution.py <path-to-file>")
        sys.exit(1)

    # Parse the command-line arguments
    parser = argparse.ArgumentParser(description="Search and process terms")
    parser.add_argument("file", type=str, help="Path to file containing terms")
    args = parser.parse_args([sys.argv[1]])

    # Create an instance of the TermSearcher class and search for terms
    term_searcher = TermSearcher(args.file)
    found_terms = term_searcher.search_terms()

    # Process the terms and print the results
    solution = term_searcher.process_terms(found_terms)
    print("===== Solution =====")
    for processed_term in solution:
        print(processed_term)
