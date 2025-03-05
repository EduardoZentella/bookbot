def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_stats = dict()
    lower_text = text.lower()
    for char in lower_text:
        if char in char_stats:
            char_stats[char] += 1
        else:
            char_stats[char] = 1
    return char_stats
