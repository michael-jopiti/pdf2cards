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
    #
    # + page + 1 is to correct for shifting due to pages before the actual content
    chapters = {text[i].lower(): int(text[i + 1]) + (int(page) + 1) for i in range(0, len(text), 2)}

    for chapter, page in chapters.items():
        print(f"Chapter: {chapter} \n\tat page: {page}")

    return chapters

def chapters_paragraphs(chapter, chapters, text):
    ''' Retrieve body of given chapter, knowing which is the next one'''

    # print(text)

    # to get next chapter, convert dictionary to list and get next element
    chapters_list = list(chapters)
    keys = list(chapters.keys())

    # Find the next key
    try:
        current_index = keys.index(chapter)
        next_key = keys[current_index + 1]
    except (ValueError, IndexError):
        print("Current key is the last one or not found.")
    
    print(f"Target: {chapter}\tNext: {next_key}")
    start_paragraph = text.index(chapter.lower())
    end_paragraph = text.index(next_key.lower())

    return text[start_paragraph:end_paragraph]
