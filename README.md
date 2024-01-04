# Text-analyzer
This Flask-based Text Analyzer application fetches paragraphs from the Bacon Ipsum API, performs text analysis, generates graphs, and produces a PDF report.

## Insights

Text analysis provides valuable insights into the composition of the generated paragraphs. By analyzing word lengths, frequency of words, and additional metrics, the application aims to offer a comprehensive understanding of the text structure.

### Key Insights:

1. Average Word Length:
   - Provides an indication of the average length of words in the generated text.

2. Top 10 Most Frequent Words:
   - Identifies the most frequently occurring words, offering insights into the prominent themes.

3. Total Words:
   - Presents the overall word count in the analyzed text.

4. Maximum Word Length:
   - Highlights the length of the longest word in the text.

5. Longest Word:
   - Reveals the actual longest word and its character length.

6. Shortest Word:
   - Highlights the shortest word and its character length.

## Modules

### 1. `text_analyzer.py`

Contains the `TextAnalyzer` class responsible for fetching paragraphs, preprocessing text, and performing text analysis.

### 2. `chart_generator.py`

Includes the `ChartGenerator` class that generates charts (histogram, bar chart, word cloud, boxplot) based on text analysis results.

### 3. `pdf_generator.py`

Defines the `PDFGenerator` class that creates a PDF report with original text, text analysis results, other analysis, and charts.

### 4. `app.py`

Main application file integrating the modules to create a Flask app. It provides an endpoint `/generate-pdf` to trigger the PDF generation and text analysis.

## Descriptive Data Analysis Methodology

The application follows a structured methodology for descriptive data analysis:

1. Paragraph Fetching:
Utilizes the Bacon Ipsum API to retrieve a specified number of paragraphs.

2. Text Preprocessing:
- Tokenizes the text into words and filters out non-alphabetic characters.
- Creates a DataFrame for further analysis.

3. Descriptive Text Analysis:
- Computes descriptive statistics such as mean, median, and standard deviation for word lengths.
- Visualizes the distribution of word lengths through a histogram and a boxplot.
-
4. Top 10 Most Frequent Words Analysis:
- Identifies and presents the top 10 most frequent words in the text.

5. Word Cloud Generation:
- Generates a word cloud to visually represent word frequencies.

6. PDF Report Generation:
Creates a PDF report that includes the original text, descriptive statistics, other analysis metrics, and visualizations.


## Setup Instructions

1. Clone the repository:

git clone https://github.com/yourusername/text-analyzer-app.git
cd text-analyzer-app

2. Install dependencies

## Run Instructions

1. Run the Flask application:

    python main.py

2. Open a web browser and navigate to `http://127.0.0.1:5000/generate-pdf`.

3. Use the application form to specify the number of paragraphs and submit the request.

4. The application will generate a PDF report and charts, which can be downloaded or viewed.

## Advanced Features

The application includes error handling, logging, and other enhancements for improved robustness and maintainability. Check the specific module files (`text_analyzer.py`, `chart_generator.py`, `pdf_generator.py`) for detailed error handling.





