import re


file = "terms.txt"

def search_term(file):
    with open(file, "r") as f:
        last_line = f.readlines()[-1]
    return last_line


def source_terms(file):
    source_list = []
    with open(file, "r") as f:
        source_file = f.readlines()
        source_lines = source_file[:-1]
        for line in source_lines:
            source_line = line.strip()
            source_list.append(source_line)
    return source_list

print(f"source term: {search_term(file)}")
print(f"source_terms: {source_terms(file)}")
print("-----[Solution]-----")
terms_found = []
for terms in source_terms(file):
    if str(search_term(file)) in terms:
        terms_found.append(terms)


for each_term in terms_found:
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





