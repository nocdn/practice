def check_sequance(words):
    """
    checks a sequence of words to ensure they form a valid word ladder.

    args:
        words: a list of words.

    returns:
        array: a list of strings representing the validated word ladder, 
        or a list indicating the first invalid word.

    raises:
        ValueError: if the list has less than three words or if the words 
                    are not all the same length.
    """

    # check if list has at least three words
    if len(words) < 3:
        raise ValueError("list must contain at least three words.")

    # check if all words are of the same length
    word_length = len(words[0])
    if not all(len(word) == word_length for word in words):
        raise ValueError("all words must have the same length.")

    result = [words[0]]  # initialize result with the first word
    for i in range(len(words) - 1):
        difference_count = 0  # count of differing characters
        diff_indices = []  # indices of differing characters
        for j in range(word_length):
            if words[i][j] != words[i+1][j]:
                difference_count += 1
                diff_indices.append(j)

        # if words are identical, mark as invalid and return
        if words[i] == words[i+1]:
            result.append(f"*{words[i+1]}*")
            if i + 2 < len(words):  # check if there are more words after the invalid one
                result.extend(words[i+2:])
            return result
        
        # if words differ by one character, mark that character
        elif difference_count == 1:
            new_word = list(words[i+1])
            new_word.insert(diff_indices[0], "*")
            new_word.insert(diff_indices[0] + 2, "*")
            result.append("".join(new_word))

        # if words differ by more than one character, mark as invalid and return
        elif difference_count > 1:
             result.append(f"*{words[i+1]}*")
             if i + 2 < len(words):
                result.extend(words[i+2:])
             return result

    return result  # return the validated word ladder