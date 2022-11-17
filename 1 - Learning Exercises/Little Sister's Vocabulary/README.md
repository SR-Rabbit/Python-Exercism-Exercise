# Concepts used
- User-defined functions
- Strings
- F-strings
- String methods
- Conditional expressions (ternary operator)


## Addendum
- For task 4, there are several ways to approach the problem in 1 line.
    - You can strip the punctuation with with a second `.strip()` and set `'.'` as its optional argument : `.strip('.')`.
        - Additionally, you can use `'.?!'` as the argument to strip any these 3 punctuation marks.
        - `.strip()` is limited to removing only leading and trailing characters and nothing in the middle. But for the purposes of the task, this is a desirable trait.

    - `.replace()` can be used to replace punctuation marks `'.'` with nothing `''` : `.replace('.', '')`.
        - The *limitations* of this method is that unlike `.strip()`, you cannot specify the characters to replace in the same argument. Instead to use `.replace()` in   one line, you will have to chain them with different arguments: `word.replace('.', '').replace('?', '')`
        - So whilst you can achieve the same results, this is tedious and can easily become unreadable.
        - Another option is to use 3 lines. Set up the characters you want to remove, then loop through these characters and then with each loop use `.replace()` to replace the current character it is looping through:
        ```
        chars = ".?!"
        for c in chars:
            word = word.replace()
        ```
    - I opted to use `.translate(str.maketrans('', '', '.'))` primarily due to its performance allegedly being faster than `replace()` or `.strip()`.
        - However a *limitation* with this method is that in order to remove other punctiation marks, the use of `string.punctuation` is needed from the `string` module/library: `.translate(str.maketrans('', '', string.punctuation))`


# Instructions
You are helping your younger sister with her English vocabulary homework, which she's finding very tedious. Her class is learning to create new words by adding prefixes and suffixes. Given a set of words, the teacher is looking for correctly transformed words with correct spelling by adding the prefix to the beginning or the suffix to the ending.

There's four activities in the assignment, each with a set of text or words to work with.

## 1. Add a prefix to a word
One of the most common prefixes in English is `un`, meaning "not". In this activity, your sister needs to make negative, or "not" words by adding `un` to them.

Implement the `add_prefix_un()` function that takes `word` as a parameter and returns a new `un` prefixed word:
```
>>> add_prefix_un("happy")
'unhappy'

>>> add_prefix_un("manageable")
'unmanageable'
```

## 2. Add prefixes to word groups
There are four more common prefixes that your sister's class is studying: `en` (*meaning to 'put into' or 'cover with'*), `pre` (*meaning 'before' or 'forward'*), auto (*meaning 'self' or 'same'*), and `inter` (*meaning 'between' or 'among'*).

In this exercise, the class is creating groups of vocabulary words using these prefixes, so they can be studied together. Each prefix comes in a list with common words it's used with. The students need to apply the prefix and produce a string that shows the prefix applied to all of the words.

Implement the `make_word_groups(<vocab_words>)` function that takes a vocab_words as a parameter in the following form: `[<prefix>, <word_1>, <word_2> .... <word_n>]`, and returns a string with the prefix applied to each word that looks like: `'<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'`.
```
>>> make_word_groups(['en', 'close', 'joy', 'lighten'])
'en :: enclose :: enjoy :: enlighten'

>>> make_word_groups(['pre', 'serve', 'dispose', 'position'])
'pre :: preserve :: predispose :: preposition'

>> make_word_groups(['auto', 'didactic', 'graph', 'mate'])
'auto :: autodidactic :: autograph :: automate'

>>> make_word_groups(['inter', 'twine', 'connected', 'dependent'])
'inter :: intertwine :: interconnected :: interdependent'
```

## 3. Remove a suffix from a word
`ness` is a common suffix that means 'state of being'. In this activity, your sister needs to find the original root word by removing the `ness` suffix. But of course there are pesky spelling rules: If the root word originally ended in a consonant followed by a 'y', then the 'y' was changed to 'i'. Removing 'ness' needs to restore the 'y' in those root words. e.g. `happiness` --> `happi` --> `happy`.

Implement the `remove_suffix_ness(<word>)` function that takes in a word `str`, and returns the root word without the `ness` suffix.
```
>>> remove_suffix_ness("heaviness")
'heavy'

>>> remove_suffix_ness("sadness")
'sad'
```

## 4. Extract and transform a word
Suffixes are often used to change the part of speech a word has. A common practice in English is "verbing" or "verbifying" -- where an adjective becomes a verb by adding an `en` suffix.

In this task, your sister is going to practice "verbing" words by extracting an adjective from a sentence and turning it into a verb. Fortunately, all the words that need to be transformed here are "regular" - they don't need spelling changes to add the suffix.

Implement the `adjective_to_verb(<sentence>, <index>)` function that takes two parameters. A `sentence` using the vocabulary word, and the `index` of the word, once that sentence is split apart. The function should return the extracted adjective as a verb.
```
>>> adjective_to_verb('I need to make that bright.', -1 )
'brighten'

>>> adjective_to_verb('It got dark as the sun set.', 2)
'darken'
```