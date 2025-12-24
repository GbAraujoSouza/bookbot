def count_book_words(content: str) -> int:
    return len(content.split())


def count_letters_appearences(content: str) -> dict[str, int]:
    letter_count = {}

    for letter in content:
        letter = letter.lower()
        if letter in letter_count.keys():
            letter_count[letter] += 1
            continue
        letter_count[letter] = 1

    return letter_count


def build_letter_count_list(letter_count: dict[str, int]) -> list[dict[str, int]]:
    """
    Get a dictionary with the count of each letter and build a list of dicts with char: count
    """
    def sort_on_count(letter_info: dict[str, int]) -> int:
        return letter_info["count"]

    result = []
    for k, v in letter_count.items():
        result.append({"char": k, "count": v})

    result.sort(reverse=True, key=sort_on_count)
    return result




