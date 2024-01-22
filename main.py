
class Book:
        
    def __init__(self, path):
        self.__text = self.__read_book(path)
        self.__path = path

    def __read_book(self, path):
        with open(path) as f:
            return f.read()

    def get_word_count(self):
        return len(self.__text.split())

    def get_letter_count(self):
        chars = {}
        for char in self.__text.lower():
            if not char.isalpha():
                continue
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
        return chars

    def get_sorted_letter_count(self):
        letters = list(self.get_letter_count().items())
        letters.sort(reverse=True, key=lambda letter: letter[1])
        return letters
    
    def get_report(self):
        report = [f"--- Begin report of {self.__path} ---\n{self.get_word_count()} words found in the document\n\n"]
        for letter in self.get_sorted_letter_count():
            report.append(f"The '{letter[0]}' character was found {letter[1]} times\n")
        report.append(f"--- End report ---")
        return "".join(report)

    def __str__(self):
        return self.__text


def main():
    book = Book("books/frankenstein.txt")
    print(book.get_report())

if __name__ == "__main__":
    main()