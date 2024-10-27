import sys
from pypdf import PdfReader
import fitz 

import coretools as core 

def get_help():
    ''' Print all options available from CLI'''
    print("-p\tHow many pages to print:\n\t\t 2-5 prints from page 2 to 5\
    \n-c\tOn which page to find the chapters\
    \n-t\tDocument type (Summary -> s, Notes -> n, Paper -> p)\
    \n-n\tNumber of cards produced")

def argv_parser(argvs=sys.argv):
    """Parse command-line arguments into a dictionary of options and their values."""
    options = {}

    # Iterate through argv list starting from the first argument (index 1)
    for i in range(1, len(argvs), 2):
        key = argvs[i]
        # Ensure that there's a corresponding value
        if i + 1 < len(argvs):
            value = argvs[i + 1]
            options[key] = value  # Store in the dictionary
        else:
            print(f"Warning: No value provided for option {key}")
    
    print("Inputs parsed:")
    for flag in options:
        print(f"\t'{flag}'\t'{options[flag]}'")
    print("")
    return options

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_pdf> --options")
        print("To see all functionalities, run python main.py -h")
        return

    # Check for help option first
    if "-h" in sys.argv:
        get_help()
        return

    parameters = argv_parser()

    # TODO 
    # - from parameters extract the features the user wants
    # - create a card with relative informations
    # - graphically display the deck, question on front and on click, show the answer

    # variables to store:
    # dictionary because page number is associated
    chapters = {}

    # read the file:
    file_path = parameters["-i"]
    try:
        reader = fitz.open(file_path)
        print(f"Success: The file '{file_path}' has been read\n")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.\n")
        return

    if '-c' in parameters:
        page_number = int(parameters['-c'])
        print(f"Searching for chapters on page: {page_number}")
        chapters = core.search_chapters(page_number, reader.load_page(page_number).get_text()) 

    if '-p' in parameters:
        page = int(parameters["-p"])
        content_on_page = core.page_paragraphs(page, reader.load_page(page).get_text())

if __name__ == "__main__":
    main()
