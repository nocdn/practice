def check_sequance(sequence):
    """
    this function takes a list of words and highlights which letter was changed

    args:
        sequence: a list of strings representing the sequence of words
    returns:
        array: a list of strings representing the sequence of words with the changed letter highlighted
    """
    # check number of words in sequence
    if len(sequence) < 3:
        raise ValueError("The sequence must have at least 3 words")
    else:
        same_length = True
        word_length = len(sequence[0])
        # will check if any word is not same length as the first word, because they have to be equal length
        for word in sequence:
            if len(word) != word_length:
                same_length = False
        if not same_length:
            raise ValueError("All words in the sequence must be the same length")
    
    is_valid_sequence = True
    # will be the output if the sequence is valid
    new_list = [sequence[0]]
    for i in range(len(sequence)-1):
        letters_original = list(sequence[i])
        letters_new = list(sequence[i+1])
        # check if any two words repeated
        if letters_original == letters_new:
            sequence[i+1] = "*" + sequence[i+1] + "*"
            is_valid_sequence = False
            break
        letter_changed = -1
        # checks letters in words to see if they are same or not
        for x in range(word_length):
            if letters_original[x] != letters_new[x]:
                if letter_changed != -1:
                    sequence[i+1] = "*" + sequence[i+1] + "*"
                    is_valid_sequence = False
                else:
                    letter_changed = x
                    letters_new[x] = "*" + letters_new[x] + "*"
        if not is_valid_sequence:
            break
        new_list.append("".join(letters_new))
    if is_valid_sequence:
        return(new_list)
    else:
        return(sequence)