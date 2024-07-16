import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def close_window():
    window.destroy()
    os.system("python Data/difficulty.py")


def load_words():
    global hwords, hlearned_words
    learned_words = 0
    with open("Data/Difficulty/dictionary1.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            word, translation, learned = line.strip().split("|")
            words.append((word, translation, learned == "True"))
            if learned == "True":
                learned_words += 1


def save_words():
    global hwords
    with open("Data/Difficulty/dictionary1.txt", "w", encoding="utf-8") as file:
        for word, translation, learned in words:
            file.write(f"{word}|{translation}|{str(learned)}\n")


def get_next_word_index():
    global current_word_index, hwords
    next_word_index = current_word_index + 1
    while next_word_index < len(words) and words[next_word_index][2]:
        next_word_index += 1
    if next_word_index < len(words):
        return next_word_index
    else:
        return -1


current_word_index = 0
hwords = []
hlearned_words = 0


def update_label(text_word, text_translation):
    label_word.configure(text=text_word)
    label_translation.configure(text=text_translation)


def show_word():
    global current_word_index, hwords
    if current_word_index < len(words):
        word, translation, learned = words[current_word_index]
        update_label(f"Слово: {word}", "")
    else:
        update_label("Слова закончились", "")


def on_first_dictionary_click():
    global current_word_index, hwords
    current_word_index = 0
    load_words()
    next_word_index = get_next_word_index()
    if next_word_index != -1:
        current_word_index = next_word_index
    show_word()


def on_next_one_click():
    global current_word_index, hwords
    next_word_index = get_next_word_index()
    if next_word_index != -1:
        current_word_index = next_word_index
    show_word()


def on_check_click():
    global current_word_index, hwords
    if current_word_index < len(words):
        word, translation, learned = words[current_word_index]
        update_label(f"Слово: {word}", f"Перевод: {translation}")
    else:
        update_label("Слова закончились", "")


def on_done_click():
    global current_word_index, hwords, hlearned_words
    if current_word_index < len(words):
        word, translation, learned = words[current_word_index]
        if not learned:
            words[current_word_index] = (word, translation, not learned)
            learned_words += 1
            update_label("Слово выучено.", "")
            next_word_index = get_next_word_index()
            if next_word_index != -1:
                current_word_index = next_word_index
    else:
        update_label("Слова закончились", "")


def on_clear_statistics_click():
    global hwords, hlearned_words
    learned_words = 0
    for i in range(len(words)):
        word, translation, learned = words[i]
        if learned:
            words[i] = (word, translation, not learned)
    update_label("Прогресс очищен.", "")


def on_save_click():

    save_words()
    update_label("Прогресс сохранён.", "")


def on_statistics_click():
    global hlearned_words
    text = f"Выученные слова: {learned_words}"
    update_label(text, "")


window = Tk()
window.state('zoomed')
window.title("Accelingvo")
window.geometry("1920x1080")
image = Image.open("Data/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
style = ttk.Style()
style.configure("BW.TLabel", font=("Times New Roman", 32), foreground="#183b66", padding=8, background="#8fc6da")
style.configure("BW.TButton", font=("Times New Roman", 32, "bold"), foreground="#183b66", padding=12, background="#8fc6da")

labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)
load_words()
label_word = ttk.Label(window, text="", justify="left", style="BW.TLabel")
label_word.pack(pady=20)
label_translation = ttk.Label(window, text="", justify="left", style="BW.TLabel")
label_translation.pack(pady=20)
first_dictionary_button = ttk.Button(window, text="Запустить", command=on_first_dictionary_click, style="BW.TButton")
first_dictionary_button.pack(pady=10)
next_one_button = ttk.Button(window, text="Следующее слово", command=on_next_one_click, style="BW.TButton")
next_one_button.pack(pady=10)
check_button = ttk.Button(window, text="Проверить слово", command=on_check_click, style="BW.TButton")
check_button.pack(pady=10)
done_button = ttk.Button(window, text="Выполнено", command=on_done_click, style="BW.TButton")
done_button.pack(pady=10)
clear_statistics_button = ttk.Button(window, text="Очистить статистику", command=on_clear_statistics_click, style="BW.TButton")
clear_statistics_button.pack(pady=10)
save_button = ttk.Button(window, text="Сохранить словарь", command=on_save_click, style="BW.TButton")
save_button.pack(pady=10)
statistics_button = ttk.Button(window, text="Статистика", command=on_statistics_click, style="BW.TButton")
statistics_button.pack(pady=10)
back_button = ttk.Button(window, text="←", command=close_window, style="BW.TButton")
back_button.pack(pady=10)
window.mainloop()