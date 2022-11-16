def capitalize_titles(title: str) -> str:
    """Takes a string as argument and capitalises the first letter of each word.

    Args:
        title (str): The title of the essay.

    Returns:
        str: The title but with the first letter of each word capitalised.
    """
    return title.title()


def check_sentence_ending(sentence: str) -> bool:
    """Takes a string as argument and checks if it ends with a punctuation.

    Args:
        sentence (str): The sentence you want to check for puncutation.

    Returns:
        bool: True if the sentence ends with punctuation, else returns False.
    """
    return sentence.endswith((".", "?", "!"))


def clean_up_spacing(sentence: str) -> str:
    """Takes a string as argument and removes any whitespace at the start and end of the string.

    Args:
        sentence (str): The sentence you want to clean.

    Returns:
        str: The sentence without any starting or trailing whitespace.
    """
    return sentence.strip()


def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """Takes a string as argument and replaces any word(s) within it with a new word.

    Args:
        sentence (str): The sentence with the words you want to replace.
        old_word (str): The word(s) you want replaced.
        new_word (str): The word(s) you want to replace the old_word with.

    Returns:
        str: The sentence with the old_word replaced with new_word.
    """
    return sentence.replace(old_word, new_word)
