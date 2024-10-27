def remove_whitelines(text):
    # Normalize whitespace: remove leading/trailing spaces and reduce multiple spaces/newlines
    return '\n'.join(line.strip() for line in text.splitlines() if line.strip())

def search_chapters(page, text):
    ''' Searches all the chapters in the provided page'''
    # Normalize whitespace: remove leading/trailing spaces and reduce multiple spaces/newlines
    text = remove_whitelines(text)

    # Split the modified text by lines
    text = text.split('\n')[1:]  # Skip the first element if needed

    # create a dictionary:
    # keys: chapters' name
    # values: page number
    chapters = {text[i]: int(text[i + 1]) for i in range(0, len(text), 2)}

    for chapter, page in chapters.items():
        print(f"Chapter: {chapter} \n\tat page: {page}")

    return chapters


def page_paragraphs(page, text):
    ''' retrieves all the paragraphs in a page '''
    # Remove first element as it's the page number
    text = remove_whitelines(text)[1:]

    # TODO
    # Retrieve the entire content of each chapter given it's successor (from dictionary)

    print(text)
