import sys
from pypdf import PdfReader

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_pdf>")
        return

    file_path = sys.argv[1]
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    print(f"Number of pages: {number_of_pages}")
    print("Text on first page:", text)

if __name__ == "__main__":
    main()
