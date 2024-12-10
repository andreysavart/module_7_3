
import string


class WordsFinder:
    file_names = []

    def __init__(self, *names):
        for i in names:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, "r",encoding='utf-8') as file:
                text = file.read()
                words = text.split()
                table = str.maketrans("", "", string.punctuation)
                all_words1 = [w.translate(table) for w in words]
                all_words[i] = all_words1
        return all_words


    def find(self, word):
        print(f"\n Номер слова: '{word}'")
        for i, j in self.get_all_words().items():
            counter = 0
            a=True
            for k in j:
                counter += 1
                if k.lower() == word.lower():
                    print( {i: counter})
                    a=False
                    break
            if a:
                print( f"----- Слово ' {word} '  НЕ найдено в ' {i} '")
    def count(self, word):
        print(f"\n Количество слов: '{word}'")
        for i, j in self.get_all_words().items():
            counter = 0
            for k in j:
                if k.lower() == word.lower():
                    counter += 1
            print({i: counter})


finder2 = WordsFinder('Mother Goose - Monday’s Child.txt','text_1.txt','Rudyard Kipling - If.txt')
print(finder2.get_all_words())  # Все слова
finder2.find('if')  # 3 слово по счёту
finder2.count('if')  # 4 слова teXT в тексте всего
