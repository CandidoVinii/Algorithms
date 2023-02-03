def is_anagram(first_string: str, second_string: str):
    first_string = merge_sort_string(list(first_string.lower()))
    second_string = merge_sort_string(list(second_string.lower()))

    is_anagram = first_string == second_string and (
        first_string != "" and second_string != ""
    )
    return (first_string, second_string, is_anagram)


def merge_sort_string(string, start=0, end=None):
    if end is None:
        end = len(string)

    if end - start > 1:
        mid = (start + end) // 2
        merge_sort_string(string, start, mid)
        merge_sort_string(string, mid, end)
        string = merge(string, start, mid, end)

    return "".join(string)


def merge(string, start, mid, end):
    left_side = string[start:mid]
    right_side = string[mid:end]

    left_index = 0
    right_index = 0

    for index in range(start, end):
        if left_index >= len(left_side):
            string[index] = right_side[right_index]
            right_index += 1
        elif right_index >= len(right_side):
            string[index] = left_side[left_index]
            left_index += 1
        elif left_side[left_index] < right_side[right_index]:
            string[index] = left_side[left_index]
            left_index += 1
        else:
            string[index] = right_side[right_index]
            right_index += 1

    return string
