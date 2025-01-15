def check_sequence(words):
    """
    Checks a sequence of words to ensure they form a valid word ladder.

    agrs:
        words: a list of words.

    returns:
        array: a list of strings representing the validated word ladder, 
        or a list indicating the first invalid word.

    raises:
        ValueError: If the list has less than three words or if the words 
                    are not all the same length.
    """

    if len(words) < 3:
        raise ValueError("List must contain at least three words.")

    word_length = len(words[0])
    if not all(len(word) == word_length for word in words):
        raise ValueError("All words must have the same length.")

    result = [words[0]]
    for i in range(len(words) - 1):
        diff_count = 0
        diff_indices = []
        for j in range(word_length):
            if words[i][j] != words[i+1][j]:
                diff_count += 1
                diff_indices.append(j)

        if words[i] == words[i+1]:
            result.append(f"*{words[i+1]}*")
            if i + 2 < len(words):  # checks if there are any more words after the invalid one
                result.extend(words[i+2:])
            return result
        
        elif diff_count == 1:
            new_word = list(words[i+1])
            new_word.insert(diff_indices[0], "*")
            new_word.insert(diff_indices[0] + 2, "*")
            result.append("".join(new_word))

        elif diff_count > 1:
             result.append(f"*{words[i+1]}*")
             if i + 2 < len(words):
                result.extend(words[i+2:])
             return result

    return result

print(check_sequence(["cat", "cot", "cog", "dog", "log"]))