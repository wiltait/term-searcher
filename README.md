# TermSearcher

This Python script defines a class called `TermSearcher` that searches for and processes terms in a file. It takes a file path as a command-line argument, reads the file contents, searches for all terms that contain the last term in the file, processes these terms by removing non-alphabetic characters, extra spaces, and adding brackets, and finally prints the processed terms.








# Assumptions

It assumes that the file to be processed is in .txt format.

## Usage

### Requirements

* Python 3.6+

### Installation

1. Clone the repository or download the source code.
2. Navigate to the directory containing the source code.

### Example usage

`python solution.py <path-to-file>`

* `<path-to-file>`: The path to the file containing the terms to be searched.

### Running the tests

`python -m unittest test_solution.py`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
=======
