import os
import random


def start():
    try:
        task_number = int(input("Choose number of function to execute:\n" +
                                "1 - Task 1 - Random phrases generator\n" +
                                "2 - Task 2 - Text information\n" +
                                "3 - Task 3 - Sentences with same length frequency\n" +
                                "0 - Run all\n"))
        _run_task(task_number)
    except KeyError:
        print("Value you entered is out of given range")
    except ValueError:
        print("Enter only integer numbers")


def _task1():
    list1 = ['hello', 'welcome', 'good morning', 'hi']
    list2 = ['my name Bob', 'I have pineapple', 'dog is cucumber', 'sun']
    list3 = ['my shiny ass', 'star wars', 'Spain', 'whater']
    text = random.choice(list1) + ' ' + random.choice(list2) + ' ' + random.choice(list3)
    print("My random phrase: ", text)


def _task2():
    filename = input("Enter path to file: ")
    if not os.path.exists(filename):
        print("File doesn't exist")
    else:
        text_without_space = get_text_without_spaces(filename)
        text_with_space = get_text(filename)
        words = get_words(text_with_space)
        words_dict = get_words_dict(words)
        print("Amount of symbols without spaces: %d" % len(text_without_space))
        print("Amount of symbols with space: %d" % len(text_with_space))
        print("Amount of words: %d" % len(words))
        print("Amount of unique words: %d" % len(words_dict))
        print("Amount of unique words that occur once : %d" % get_count_of_unique_words_that_occur_once(words_dict))
        # If you want to print all unique words you should to uncomment next lines
        # print("All unique words:")
        # for word in words_dict:
        #      print(word.ljust(20), words_dict[word])


def _task3():
    filename = input("Enter path to file: ")
    if os.path.exists(filename):
        sentences_list = get_text(filename).split('.')
        appearance_dict = _get_dict_words_sentences(sentences_list)
        frequency_dict = _calculate_frequency(appearance_dict, len(sentences_list))
        for key in frequency_dict:
            print("Frequency of sentences with %d words: %f" % (key, frequency_dict[key]))
    else:
        print("File doesn't exist")


def get_text(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    return text


def get_text_without_spaces(filename):
    text = get_text(filename)
    text = text.replace(" ", "")
    return text


def get_words(text):
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


#  A set of unique words + their numbers
def get_words_dict(words):
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict


def get_count_of_unique_words_that_occur_once(words_dict):
    counter = 0
    for v in words_dict.values():
        if v == 1:
            counter += 1
    return counter


def _get_dict_words_sentences(sentences_list):
    working_dict = dict()  # key: amount of words in sentence, value: amount of sentences with this length
    for i in range(len(sentences_list)):
        words_amount = len(sentences_list[i].split(" "))
        if words_amount not in working_dict:
            working_dict[words_amount] = 1
        else:
            working_dict[words_amount] += 1
    return working_dict


def _calculate_frequency(appearance_dict, sentences_amount):
    frequency_dict = appearance_dict.copy()
    for key in frequency_dict:
        frequency_dict[key] /= sentences_amount
    return frequency_dict


def _run_task(number):
    tasks = {
        1: _task1,
        2: _task2,
        3: _task3,
        0: _run_all()
    }
    return tasks[number]()


def _run_all():
    _task1()
    _task2()
    _task3()


if __name__ == "__main__":
    start()
