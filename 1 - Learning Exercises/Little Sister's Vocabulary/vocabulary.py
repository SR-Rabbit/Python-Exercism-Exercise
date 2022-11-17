def add_prefix_un(word: str) -> str:
    """Takes a string as argument and returns the word with the prefix "un" attached.

    Args:
        word (str): The word you want to attach "un" to.

    Returns:
        str: The new "un" prefixed word.
    """
    return f"un{word}"


def make_word_groups(word_group: list) -> str:
    """Takes a list as argument and returns a string,
       where the first element is prefixed to other elements.

    Args:
        word_group (list): A list of words. The first element is the prefix.

    Returns:
        str: Returns a string where the first element is prefixed to the other elements,
             with each element seperated by '::'
    """
    return f" :: {word_group[0]}".join(word_group)


def remove_suffix_ness(word: str) -> str:
    """Takes a string as argument, and returns the string with its suffix removed.

    Args:
        word (str): A word with a suffix 'ness'.

    Returns:
        str: Returns the given word with its suffix 'ness' removed.
             If the word contains 'i' before the suffix, then it is replaced with 'y'.
             Else return the word as is, after the removal of the suffix.
    """
    return word[:-4] if word[-5] != "i" else f"{word[:-5]}y"


def adjective_to_verb(sentence: str, index: int) -> str:
    """Takes 2 arguments and returns a word with the suffix 'en' added.
       The word is chosen by the second argument.

    Args:
        sentence (str): A sentence.
        index (int): Index for the word to add the suffix 'en' to.

    Returns:
        str: Returns the chosen word with the suffix 'en' attached.
    """
    return f"{(sentence.translate(str.maketrans('', '', '.')).split())[index]}en"
