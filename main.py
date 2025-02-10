
def main(book):
    with open(book) as f:
        content = f.read()

        num_words = count_words(content)
        chars = count_chars(content)

        report(book, num_words, chars)

def count_words(content):
    words = content.split()
    return len(words)

def count_chars(content: str):
    chars = {}
    for c in content.lower():
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1

    return chars

def display_sorted_chars(chars: dict[str, int]):
    sorted: list[dict[str, int]] = []
    for k,v in chars.items():
        if k.isalpha():
            sorted.append({"char": k, "count": v})

    sorted.sort(reverse=True, key=sort_on)
    for char in sorted:
        print(f"The '{char["char"]}' character was found {char["count"]} times")

def sort_on(dict: dict):
    return dict["count"]

def report(book: str, words: int, chars: dict[str, int]):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document\n")
    display_sorted_chars(chars)
    print("--- End report ---")


if __name__ == "__main__":
    frankenstein = "books/frankenstein.txt"
    main(frankenstein)
