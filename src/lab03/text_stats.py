from sys import *
from src.lib.text import normalize, tokenize, count_freq, top_n
TABLE_MODE = 1  #константа

def main(): #читаем весь ввод из stdin (до EOF(end of file)(ctr+D))

    text = stdin.read() #прочитали все там
    if not text.strip(): #если пустота в вводе
        return "нет входных данных"

    #само задание, называется как я пон "конвейер обработки"
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    count_word = count_freq(tokens)
    top_words = top_n(count_word, 5)
    print("Всего слов:", len(tokens))
    print("Уникальных слов:", len(count_word))

    #со звездочкой
    if TABLE_MODE:
        maxword= max(len(x) for x,y in top_words) #максимальная длина слова, ширина столбца
        #заголовок таблицы
        print("| слово" + " " * (maxword - 5) + " | частота |")
        print("|" + "❀" * (maxword + 2) + "|⁺˚*•̩̩͙✩•̩̩͙*˚⁺|")
        #данные
        for word, count in top_words:
            print(f"│ {word:{maxword}} │ {count:7} │")
    else:
        print("Топ-5:")
        for word, count in top_words:
            print(f"{word}:{count}")

#точка входа для запуска скрипта
if __name__ == "__main__":
    main()