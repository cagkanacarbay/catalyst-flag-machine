import PyPDF2
import re


def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        text = ''
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()

    return text


# def clean_proposal_text(proposal_text: str):
#     """
#     Cleans the proposal text by removing repeated header information on each page.
#
#     Parameters:
#     proposal_text (str): The raw proposal text.
#
#     Returns:
#     str: The cleaned proposal text.
#     """
#     # Regex pattern for the header information that is repeated on each page.
#     header_pattern = r"Page \d+ of \d+ Project Catalyst, \d{2}/\d{2}/\d{4}View IdeaCampaign: .*?Idea: .*?Submitted by: .*?Date of Submission: .*?Idea: .*?\n"
#
#     # Remove the header information from the proposal text.
#     cleaned_text = re.sub(header_pattern, '', proposal_text)
#
#     return cleaned_text


import re


def clean_proposal_text(proposal_text):
    patterns = [
        r"Page .* Project Catalyst",
        r"Idea No\. \d+",
        r"Submitted by: .+",
        r"Date of Submission: \d{2}/\d{2}/\d{4}",
        r"Idea: .+"
    ]

    lines = proposal_text.split('\n')

    cleaned_lines = []
    for line in lines:
        if not any(re.match(pattern, line) for pattern in patterns):
            cleaned_lines.append(line)

    cleaned_text = '\n'.join(cleaned_lines)

    return cleaned_text, cleaned_lines

