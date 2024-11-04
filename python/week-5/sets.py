dictionary = {"un":1, "deux":2, "trois":3}

def display_dico(dico):
    for key, value in dico.items():
        print(f"{key} --> {value}")

print(dictionary.items())

display_dico(dictionary)
