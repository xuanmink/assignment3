def create_acronym(phrase):
    words =phrase.split()
    acronym = ""
    for word in words:
        acronym+= word[0].upper()
    return acronym
if __name__== "__main__":
    text= input("Enter a phrase: ")
    print(f"Acronym:{create_acronym(text)}")