import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

class ChartGenerator:
    @staticmethod
    def generate_charts(word_lengths, frequent_words, original_text):
        """
        Generate charts based on word lengths and frequent words.

        Args:
            word_lengths (pd.Series): Series of word lengths.
            frequent_words (pd.Series): Series of frequent words.
            original_text (list): List of original text paragraphs.
        """
        try:
            plt.style.use('classic')
            color = "#f99a1c"

            # Histogram of word lengths distribution
            plt.figure(figsize=(10, 6))
            plt.hist(word_lengths, bins=15, edgecolor='black', color=color)
            plt.title('Distribution of Word Lengths', fontsize=18, color=color)
            plt.xlabel('Word Length')
            plt.ylabel('Frequency')
            plt.savefig('word_lengths.png')
            plt.close()

            # Bar chart of the 10 most frequent words
            plt.figure(figsize=(12, 8))
            frequent_words.plot(kind='bar', color=color)
            plt.title('Top 10 Most Frequent Words', fontsize=18, color=color)
            plt.xlabel('Word')
            plt.ylabel('Frequency')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig('frequent_words.png')
            plt.close()

            # Word Cloud
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(original_text))
            plt.figure(figsize=(12, 6))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.title('Word Cloud', fontsize=18, color=color)
            plt.savefig('word_cloud.png')
            plt.close()

            # Boxplot for word lengths
            plt.figure(figsize=(10, 6))
            sns.boxplot(word_lengths, color=color)
            plt.title('Boxplot: Word Lengths', fontsize=18, color=color)
            plt.xlabel('Word Length')
            plt.savefig('boxplot_word_lengths.png')
            plt.close()
        except Exception as e:
            raise Exception(f"Error generating charts: {str(e)}")