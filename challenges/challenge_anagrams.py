def sort_and_merge(array):
    if len(array) <= 1:
        return "".join(array)

    mid = len(array) // 2
    left = sort_and_merge(array[:mid])
    right = sort_and_merge(array[mid:])

    return "".join(merge(left, right, array.copy()))


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] == right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[right_cursor + left_cursor] = right[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    f_word = sort_and_merge(list(first_string.lower()))
    s_word = sort_and_merge(list(second_string.lower()))

    if f_word == "" and s_word == "":
        return (first_string, second_string, False)

    return (
        f_word,
        s_word,
        f_word == s_word
    )
