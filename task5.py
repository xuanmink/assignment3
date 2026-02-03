def get_middle_chars(text):
    length = len(text)
    mid_index = length // 2
    if length % 2 == 0:
            return text[mid_index -1: mid_index + 1]
    else:
            return text[mid_index]
if __name__ =="__main__":
    user_string = input("Enter a string: ")
    result = get_middle_chars(user_string)
    print(f"Middle character(s):{result}")