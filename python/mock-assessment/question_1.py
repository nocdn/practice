def extractText(text, keys):
    """
    a function to return words from a text that only contain letters from the given keys

    args:
        text (str): input text containing only alphabet letters and spaces
        keys (str): string of allowed letters

    returns:
        str: space-separated string of valid words
    """

    if not text:
        return ""

    # changing everything to lowercase
    keys = set(keys.lower())

    words = text.split(" ")
    allowed_words = []

    for word in words:
        # loop to check if all letters in word are in keys
        word_valid = True
        for letter in word.lower():
            if letter not in keys:
                word_valid = False
                break

        if word_valid:
            allowed_words.append(word)

    final_result = " ".join(allowed_words)
    # ^ joining allowed words with spaces to create final result
    return final_result
