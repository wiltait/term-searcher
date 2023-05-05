""" Unit tests for TermSearcher """

import unittest
import os
from solution import TermSearcher


class TestTermSearcher(unittest.TestCase):
    """
    Test cases for TermSearcher class
    """

    def setUp(self):
        """
        Set up the file path for testing
        """

        self.file_path = os.path.join(
            os.path.dirname(__file__), 'file/test_file.txt')


    def test_read_file(self):
        """
        Test read_file method
        """

        term_searcher = TermSearcher(self.file_path)
        file_content = term_searcher.read_file()
        expected = ['"Alice was beginning...\n',
                    'to_get9_!very\n',
                    '11111tired1111of1111sitting111111\n',
                    '      by her_sister..//``~~~~~~`.\n',
                    'on9the bank,\n',
                    'and""of""having\n',
                    'er'
                    ]
        self.assertEqual(file_content, expected)


    def test_search_last_term(self):
        """
        Test search_last_term method
        """

        term_searcher = TermSearcher(self.file_path)
        last_term = term_searcher.search_last_term()
        expected = 'er'
        self.assertEqual(last_term, expected)


    def test_get_source_terms(self):
        """
        Test get_source_terms
        """

        term_searcher = TermSearcher(self.file_path)
        source_terms = term_searcher.get_source_terms()
        expected = ['"Alice was beginning...\n',
                    'to_get9_!very\n',
                    '11111tired1111of1111sitting111111\n',
                    '      by her_sister..//``~~~~~~`.\n',
                    'on9the bank,\n',
                    'and""of""having\n'
                    ]
        self.assertEqual(source_terms, expected)


    def test_search_terms(self):
        """
        Test search_terms method
        """

        term_searcher = TermSearcher(self.file_path)
        found_terms = term_searcher.search_terms()
        expected = ['to_get9_!very\n',
                    '      by her_sister..//``~~~~~~`.\n'
                    ]
        self.assertEqual(found_terms, expected)


    def test_process_terms(self):
        """
        Test process_terms method
        """

        term_searcher = TermSearcher(self.file_path)
        found_terms = term_searcher.search_terms()
        processed_terms = term_searcher.process_terms(found_terms)
        expected = ['[to get very]', '[by her sister]']
        self.assertEqual(processed_terms, expected)
