import pdfplumber
from typing import Optional
from book import Book, Page, Content, ContentType, TableContent
from translator.exceptions import PageOutOfRangeException
from utils import LOG


class PDFParser:
    def __init__(self):
        pass

    def parse_pdf(self, pdf_file_path: str, pages: Optional[int] = None) -> Book:
        book = Book(pdf_file_path)

        with pdfplumber.open(pdf_file_path) as pdf:
            if pages is not None and pages > len(pdf.pages):
                raise PageOutOfRangeException(len(pdf.pages), pages)

            if pages is None:
                pages_to_parse = pdf.pages
            else:
                pages_to_parse = pdf.pages[:pages]

            for pdf_page in pages_to_parse:
                page = Page()

                # Store the original text content
                raw_text = pdf_page.extract_text(layout=True)#layout=True保留布局
                tables = pdf_page.extract_tables()

                # Remove each cell's content from the original text
                for table_data in tables:
                    for row in table_data:
                        for cell in row:
                            raw_text = raw_text.replace(cell, "", 1)

                # Handling text
                if raw_text:
                    # Remove empty lines and leading/trailing whitespaces
                    raw_text_lines = raw_text.splitlines()
                    cleaned_raw_text_lines = [line.strip() for line in raw_text_lines if line.strip()]
                    cleaned_raw_text = "\n".join(cleaned_raw_text_lines)

                    text_content = Content(content_type=ContentType.TEXT, original=cleaned_raw_text)
                    page.add_content(text_content)
                    LOG.debug(f"[raw_text]\n {cleaned_raw_text}")



                # Handling tables
                if tables:
                    table = TableContent(tables)
                    page.add_content(table)
                    LOG.debug(f"[table]\n{table}")

                book.add_page(page)

        return book
    # def parse_pdf(self, pdf_file_path: str, pages: Optional[int] = None) -> Book:
    #     book = Book(pdf_file_path)

    #     with pdfplumber.open(pdf_file_path) as pdf:
    #         if pages is not None and pages > len(pdf.pages):
    #             raise PageOutOfRangeException(len(pdf.pages), pages)

    #         if pages is None:
    #             pages_to_parse = pdf.pages
    #         else:
    #             pages_to_parse = pdf.pages[:pages]

    #         for pdf_page in pages_to_parse:
    #             page = Page()

    #             # Extract words with their position information
    #             words = pdf_page.extract_words()

    #             # Sort words by their vertical position, then by their horizontal position
    #             words.sort(key=lambda word: (word['top'], word['x0']))

    #             lines = []
    #             line = []
    #             for i in range(len(words)):
    #                 # If this word is on the same line as the previous word, add it to the line
    #                 if i > 0 and words[i]['top'] == words[i - 1]['top']:
    #                     line.append(words[i]['text'])
    #                 else:
    #                     # Otherwise, this word is on a new line. Add the previous line to the lines array
    #                     # and start a new line with this word.
    #                     if line:
    #                         lines.append(' '.join(line))
    #                     line = [words[i]['text']]

    #             # Add the last line to the lines array
    #             if line:
    #                 lines.append(' '.join(line))

    #             # Join the lines with newline characters to create the raw text
    #             raw_text = '\n'.join(lines)

    #             # Handling tables
    #             tables = pdf_page.extract_tables()

    #             # Remove each cell's content from the raw text
    #             for table_data in tables:
    #                 for row in table_data:
    #                     for cell in row:
    #                         raw_text = raw_text.replace(cell, "", 1)

    #             # Handling text
    #             if raw_text:
    #                 text_content = Content(content_type=ContentType.TEXT, original=raw_text)
    #                 page.add_content(text_content)
    #                 LOG.debug(f"[raw_text]\n {raw_text}")

    #             if tables:
    #                 table = TableContent(tables)
    #                 page.add_content(table)
    #                 LOG.debug(f"[table]\n{table}")

    #             book.add_page(page)

    #     return book