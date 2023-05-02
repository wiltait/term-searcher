''' Modules '''
import sys
import re


def get_file_path():
    if len(sys.argv) != 2:
        print("Usage: python solution.py <path_to_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    return file_path


def get_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            read_file = file.readlines()
            return read_file
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)


def get_search_term(read_file):
    search_term = read_file[-1]
    return search_term


def get_source_terms(read_file):
    source_list = []
    source_terms = read_file[:-2]
    for line in source_terms:
        lines = line.strip()
        source_list.append(lines)
    return source_list


def get_matching_terms(search_term, source_list):
    matching_terms = []
    for term in source_list:
        if str(search_term) in term:
            matching_terms.append(term)
    return matching_terms


def output(matching_terms):
    for each_term in matching_terms:
        # Replace all non-alphabetic characters and underscores with a space
        solution = re.sub(r'[^a-zA-Z\s]', ' ', each_term)
        # Remove any leading or trailing spaces
        solution = solution.strip()
        # Replace multiple spaces with a single space
        solution = re.sub(r'\s+', ' ', solution)
        # Enclose the cleaned string in square brackets
        solution = f"[{solution}]"
        # Print solution
        print(solution)


# Function responsible for coordinating the program's overall logic
def main():
    file_path = get_file_path()
    file_content = get_file(file_path)
    search_term = get_search_term(file_content)
    source_list = get_source_terms(file_content)
    matching_terms = get_matching_terms(search_term, source_list)
    output(matching_terms)


if __name__ == '__main__':
    main()
