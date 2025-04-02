def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def list_of_dict(dict):
    result = [{"char": key, "num": value} for key, value in dict.items()]
    result.sort(reverse=True, key=sort_on)
    return result