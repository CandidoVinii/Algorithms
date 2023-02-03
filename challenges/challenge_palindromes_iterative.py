def is_palindrome_iterative(word):
    for index in range(len(word)):
        if word[index] != word[-index - 1]:
            return False

    return False if not word else True
