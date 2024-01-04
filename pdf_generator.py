from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

class PDFGenerator:
    @staticmethod
    def generate_pdf(original_text, text_analysis, other_analysis):
        """
        Generate a PDF report.

        Args:
            original_text (list): List of original text paragraphs.
            text_analysis (list): List of text analysis results.
            other_analysis (list): List of other analysis results.

        Returns:
            BytesIO: Buffer containing the generated PDF.
        """
        try:
            pdf_buffer = BytesIO()

            # Configure PDF layout
            left_margin = 50
            page_size = letter

            # Create a SimpleDocTemplate object
            pdf = SimpleDocTemplate(pdf_buffer, pagesize=page_size, leftMargin=left_margin, rightMargin=left_margin)

            # Define paragraph styles
            styles = getSampleStyleSheet()
            title_color = "#f98e00"

            title_style = ParagraphStyle(
                'Title',
                parent=styles['Title'],
                textColor=title_color,
                spaceAfter=12
            )

            heading_style = ParagraphStyle(
                'Heading1',
                parent=styles['Heading1'],
                textColor=title_color,
                spaceAfter=12
            )

            normal_style = styles['BodyText']

            # List to store PDF elements
            elements = []

            # Main title
            elements.append(Paragraph("<font size=18 color={0}>TEXT ANALYSIS</font>".format(title_color), title_style))

            # Original Text Section
            elements.append(Spacer(1, 12))
            elements.append(Paragraph("<font size=16 color={0}>Original Text:</font>".format(title_color), heading_style))

            for paragraph in original_text:
                elements.append(Paragraph(paragraph, normal_style))
                elements.append(Spacer(1, 6))

            # Text Analysis Section
            elements.append(Spacer(1, 12))
            elements.append(Paragraph("<font size=16 color={0}>Text Analysis:</font>".format(title_color, text_analysis), heading_style))

            for result in text_analysis:
                elements.append(Paragraph(result, normal_style))
                elements.append(Spacer(1, 6))

            # Other Analysis Section
            elements.append(Spacer(1, 12))
            elements.append(Paragraph("<font size=16 color={0}>Other Analysis</font>".format(title_color), heading_style))

            for result in other_analysis:
                elements.append(Paragraph(result, normal_style))
                elements.append(Spacer(1, 6))

            # Charts Section
            elements.append(Spacer(1, 12))
            elements.append(Paragraph("<font size=16 color={0}>Charts:</font>".format(title_color), heading_style))

            # Add images
            word_lengths_path = 'word_lengths.png'
            frequent_words_path = 'frequent_words.png'
            boxplot_word_lengths_path = "boxplot_word_lengths.png"
            word_cloud_path = "word_cloud.png"

            elements.append(Image(word_lengths_path, width=400, height=200))
            elements.append(Spacer(1, 12))
            elements.append(Image(frequent_words_path, width=400, height=200))
            elements.append(Spacer(1, 12))
            elements.append(Image(boxplot_word_lengths_path, width=400, height=200))
            elements.append(Spacer(1, 12))
            elements.append(Image(word_cloud_path, width=400, height=200))

            # Build the PDF
            pdf.build(elements)

            pdf_buffer.seek(0)
            return pdf_buffer
        except Exception as e:
            raise Exception(f"Error generating PDF: {str(e)}")