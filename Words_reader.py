class WordsReader:
    def __init__(self):
        with open("Words-hangman.txt", "r") as file:
            self.list_of_words = [word.strip() for word in file.readlines() if word.strip().isalpha()]

    def get(self):
        return self.list_of_words


if __name__ == "__main__":
    print(WordsReader().get())