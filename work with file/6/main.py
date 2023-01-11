import sys


def title():
    """
    Ця функція друкує один раз заголовок. Вся інструкція та вказівки до роботи
    :return: str
    """
    return "Лабораторна робота №6\n" \
           "Студентки КПІ/ФМФ\n" \
           "група ОМ-2*\n" \
           "Ім'я Прізвище\n" \
           f"{'-'*100}\n" \
           "Умова завдання:\n" \
           "Користув може або ввести самості деякий рядок самостійно або взяти його з файлу формату .txt\n" \
           "У рядку який обрав користувач програма розбиває цей рядок на слова. І по кожному слову \n" \
           "шукає в цьому рядку чи є ще в цьому рядку таке перевернуте слово.\n" \
           "\nНаприклад, якщо у файлі є 4 слова:\n" \
           "\tpython nohtyp ooo KPI\n" \
           "То результат буде наступним чином.\n" \
           "\tСлова 'python <-> nohtyp' це пара яка може бути отримана перевертанням одного з цих слів, щоб отримати інше\n" \
           "\tСлово 'ооо' входить в групу паліндромів. Тобто якщо це слово перевернути, то вийде той самий текст\n" \
           "\tІ нарешті слово 'KPI' нікуди не входить, бо немає пари\n" \
           "\n" \
           "Виберіть з чого почати:\n" \
           "\t1 - ввести самостійно деякий текст\n" \
           "\t2 - отримати цей текст з файлу 'test.txt'\n" \
           "\t3 - вихід" \


def foo(string_user, answer_dict):
    """
    Функція приймає два параметри, 1 - рядок користувача, 2 - пустий словник (dict). Функція перевіряє, чи може бути
    отримане одне слово перевертанням іншого такого слова
    :param string_user: str
    :param answer_dict: dict
    :return: dict <- повертає тип (dict), який в подальному буде використовуватися
    """
    user_list = string_user.split()  # функція split() перетворює рядок string_user типу (str) в новий тип list
    for i_word in user_list:  # цикл зі списку всіх слів, де i_word ключ для перевірки
        for i_word_reversed in user_list:  # цикл зі списку всіх слів, i_word_reversed значення для необхідної умови вподальшому
            if i_word[::-1] == i_word_reversed:  # перевірка умови, чи два слова дають однаковий результат під час перевертання іншого слова
                answer_dict[i_word] = i_word_reversed  # додавання результату в словник
    return answer_dict


def check_palindrome(answer_dict:dict):
    """
    Функція додатково перевіряє чи є слово паліндромом. Тобто AbA <-> AbA.
    :param answer_dict: словник з результатом, який ми отримали з минулої функції
    :return: список з усіх можливих паліндомів
    """
    palindrome = []
    for i_key, i_value in answer_dict.items():  # цикл який отримує два параметри це ключ та значення відповідного словника
        if i_key == i_value:  # якщо ключ та значення однакові, то це є паліндом
            palindrome.append(i_key)  # додаємо це слово в окремий список
    return palindrome  # повертаємо цей список


def save_word_in_file():
    """
    Функція запитує у користувача чи потрібно зберігати результат?
    :return: bool
    """
    print("Чи бажаєте ви зберегти отриманий результат? (Введіть '+' або '-')")
    save = input("> ")
    if save == "+":
        return True
    elif save == "-":
        return False
    return save_word_in_file()

def choice():
    """
    Функція перевіряє та пропонує наступний розвиток подій.
        1 - рядок символів користувач вводить самостійно
        2 - рядок символів користувач візьме з файлу
        3 - вихід
    :return: або рядок символів або вихід з програми
    """
    print("Натисність 1 або 2, або 3:")
    choice_num = input("> ")  # введення можливого значення
    if choice_num == "1":  # перевірка
        user_str = input("Введіть щось: ")  # користувач вводить свої значення
        return user_str  # повернення цього значення
    elif choice_num == "2":  # перевірка
        try:  # спроба виконати цей фрагмент коду, якщо буде помилка з назвою файлу, то програма попередить про це
            with open("test.txt", encoding='utf-8') as f:  # з файлу беремо значення та називаємо перемінну цього файлу f
                string_user = f.read()  # отримуємо всі значення з цього файлу
            return string_user  # повернення цього значення
        except:  # якщо винекла помилка, то програма перехвачує цю помилку та попереджає користувача, щоб виправили цю помилку з назвою файлу.
            print("Такого файлу не існує, помилка. Спробуйте ще раз. Але перед цим виправте помилку в коді!")
            sys.exit()
    elif choice_num == "3":  # перевірка значення
        print("Вихід")
        sys.exit()  # закриття програми
    else:  # якщо користувач обрав іншу букву, якої немає в меню. То почати спочатку
        print("Ви обрали щось не те. Спробуйте ще раз.")
        return choice()


def main():
    """
    Основна функція програми. Отримує всі інші функції і за допомогою них програма працює
    :return: результат программи. Тобто список з перевернутими словами
    """
    string_user = choice()  # функція, яка питає у користувача що будемо робити.
    answer_dict = dict()  # створення пустого словника
    list_reverse = foo(string_user, answer_dict)  # отримуємо готові значення з необхідної умови

    if len(list_reverse) == 0:  # перевірка, якщо таких слів не знайши. То показуємо це користувачу.
        print("Схожих слів не знайшлося")
    else:  # в іншому випадку
        for i_word in list_reverse:  # друкуємо всі значення, які підійшли по умові
            print("{} <-> {}".format(i_word, i_word[::-1]))
        if save_word_in_file():  # питаємо у користувача чи треба зберігати значення
            print("Введіть назву файлу, в який хочете зберегти значення.")
            name_file = input("> ")
            file = "{name_file}{type_file}".format(name_file=name_file, type_file=".txt")  # назва файлу
            print("*Підсказка, всі файли будуть показані в папці, після того як ми завершете програму!")
            with open(file, "w", encoding="utf-8") as new:  # відкриваємо файл у форматі запису
                for i_word in list_reverse:

                    new.write(f"{i_word} {i_word}\n")  # записуємо значення
        palindrome =  check_palindrome(answer_dict)  # перевіряємо значення, які входять в категорію паліндромів
        if len(palindrome) > 0:  # якщо такі значення є, то виводимо їх
            print("Такі слова є паліндромоми:")
            print(*palindrome)  # palindrome має тип list. Щоб не писати цикл for для виводу значень. Скористаємось додатковими можливостями. Та перед palindrome поставимо *, що є еквівалентним.


#  основна перевірка програми. Якщо файл відкрили, то програма працює, якщо ж файл імпортують, то програма не буде виконувати наступну функцію
if __name__ == "__main__":
    print(title())
    while True:
        main()