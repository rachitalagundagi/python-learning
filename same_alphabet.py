# code for checking if two word input begin with the same alphabet

def animal_crackers(texts):
    wordlist = texts.lower().split()
    if wordlist[0][0]==wordlist[1][0]:#wordlist[firstword][firstletter]==wordlist[secondword][firstletter]
        print(f"they are same {wordlist}")
    else:
        print(f"they are not same {wordlist}")

    return wordlist

animal_crackers("red rabbit")
animal_crackers("blue rabbit")