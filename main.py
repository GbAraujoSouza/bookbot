from stats import count_book_words, count_letters_appearences, build_letter_count_list
import sys


def build_report(raw_content: str, path: str) -> str:
    report = ""
    report += f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {count_book_words(raw_content)} total words
--------- Character Count -------
"""
    letter_count = count_letters_appearences(raw_content)
    for letter_info in build_letter_count_list(letter_count):
        if not str(letter_info["char"]).isalpha():
            continue

        report += f"{letter_info.get("char")}: {letter_info.get("count")}\n"

    report += "============= END ==============="

    return report


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    content = ""
    try:
        with open(path) as f:
            content = f.read()

    except FileNotFoundError as err:
        print(err)
        sys.exit(2)

    report = build_report(content, path)

    print(report)


if __name__ == "__main__":
    main()
