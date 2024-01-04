from flask import Flask, request, jsonify
import logging
from text_analyzer import TextAnalyzer
from chart_generator import ChartGenerator
from pdf_generator import PDFGenerator
import requests
import pandas as pd

app = Flask(__name__)

# Constants
DEFAULT_PARAGRAPHS = 5

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        paragraphs = int(request.form.get('paragraphs', DEFAULT_PARAGRAPHS))
        bacon_paragraphs = TextAnalyzer.fetch_bacon_paragraphs(paragraphs)

        df = pd.DataFrame({'text': bacon_paragraphs})
        df['tokens'] = df['text'].apply(TextAnalyzer.preprocess_text)

        word_lengths, frequent_words, total_words, longest_word, shortest_word, len_longest_word, len_shortest_word = TextAnalyzer.perform_text_analysis(df)
        ChartGenerator.generate_charts(word_lengths, frequent_words, bacon_paragraphs)

        average_word_length = word_lengths.mean()

        analysis_results = [
            f"Average Word Length: {average_word_length:.2f}",
            f"Top 10 Most Frequent Words:\n{frequent_words.to_string()}",
        ]

        other_analysis_results = [
            f"Total Words: {total_words}",
            f"Maximum Word Length: {word_lengths.max()}",
            f"Longest Word: {longest_word} (Length: {len_longest_word} characters)",
            f"Shortest Word: {shortest_word} (Length: {len_shortest_word} characters)"
        ]

        pdf_buffer = PDFGenerator.generate_pdf(bacon_paragraphs, analysis_results, other_analysis_results)

        return pdf_buffer.read(), 200, {'Content-Type': 'application/pdf'}

    except requests.RequestException as e:
        logger.error(f'Request to Bacon Ipsum API failed: {str(e)}')
        return jsonify({'error': f'Request to Bacon Ipsum API failed: {str(e)}'}), 500

    except Exception as e:
        logger.error(f'An unexpected error occurred: {str(e)}')
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

# Flask endpoint for generating PDF and performing text analysis
@app.route('/generate-pdf', methods=['POST'])
def generate_pdf_endpoint():
    return main()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)