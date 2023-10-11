import sys
from pdf2docx import Converter


def main():
    """main.

    Convert PDF to DOCX.

    Example
    -------
    python convert_pdf_to_docx.py YOUR_FILE.pdf YOUR_FILE.docx
    """
    pdf_file = sys.argv[1]
    docx_file = sys.argv[2]

    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()


if __name__ == "__main__":
    main()
