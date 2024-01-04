import requests
from nltk.tokenize import word_tokenize
import pandas as pd

class TextAnalyzer:
    BACON_API_URL = "https://baconipsum.com/api/"

    @staticmethod
    def fetch_bacon_paragraphs(paragraphs):
        """
        Fetch paragraphs from the Bacon Ipsum API.

        Args:
            paragraphs (int): Number of paragraphs to fetch.

        Returns:
            list: List of paragraphs.
        """

        try:
            response = requests.get(f"{TextAnalyzer.BACON_API_URL}?type=all-meat&paras={paragraphs}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error fetching paragraphs: {str(e)}")

    @staticmethod
    def preprocess_text(text):
        """
        Preprocess the given text.

        Args:
            text (str): Input text.

        Returns:
            list: List of preprocessed tokens.
        """
        try:
            tokens = word_tokenize(text)
            tokens = [word.lower() for word in tokens if word.isalpha()]
            return tokens
        except Exception as e:
            raise Exception(f"Error in text preprocessing: {str(e)}")

    @staticmethod
    def perform_text_analysis(df):
        """
        Perform text analysis on the given DataFrame.

        Args:
            df (pd.DataFrame): DataFrame containing 'text' and 'tokens' columns.

        Returns:
            tuple: Tuple containing word_lengths, frequent_words, total_words, longest_word, shortest_word,
                   len_longest_word, len_shortest_word.
        """
        try:
            all_tokens = [word for sublist in df['tokens'] for word in sublist]

            word_lengths = pd.Series([len(word) for word in all_tokens])
            frequent_words = pd.Series(all_tokens).value_counts().head(10)

            total_words = len(all_tokens)
            longest_word = max(all_tokens, key=len)
            shortest_word = min(all_tokens, key=len)
            len_longest_word = len(longest_word)
            len_shortest_word = len(shortest_word)

            return word_lengths, frequent_words, total_words, longest_word, shortest_word, len_longest_word, len_shortest_word
        except Exception as e:
            raise Exception(f"Error performing text analysis: {str(e)}")
