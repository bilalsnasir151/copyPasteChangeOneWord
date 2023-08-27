def replace_word_in_code(code, old_word, new_words):
    copies = []
    for new_word in new_words:
        modified_code = code.replace(old_word, new_word)
        copies.append(modified_code)
    return copies

# Input your code snippet here
original_code = """Enter your code here"""

# Input the word to be replaced
old_word = "add the word you want to replace here"

# Input the list of new words separated by spaces
new_words_input = "Create a copy of the code with each word in this string, replacing the old_word"
new_words = new_words_input.split()

modified_codes = replace_word_in_code(original_code, old_word, new_words)

# Printing the modified code
print("\n".join(modified_codes))
