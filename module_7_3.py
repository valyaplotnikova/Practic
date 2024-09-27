class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self) -> dict:
        all_words = {}
        char_list = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='UTF-8') as file:
                data = "".join([i for i in file.read() if i not in char_list])
                word_list = data.lower().split()
                all_words[file_name] = word_list
        return all_words

    def find(self, word: str) -> dict:
        find_dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                find_dict[name] = words.index(word.lower()) + 1
        return find_dict

    def count(self, word: str) -> dict:
        count_dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                count_dict[name] = words.count(word.lower())
        return count_dict




