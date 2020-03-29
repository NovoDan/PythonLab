import re

import matplotlib.pyplot as plt
from matplotlib import pylab
from numpy import *


# Use resources/sample_text.txt to test this app
def main():
    task_1()
    task_2()
    task_3()


def task_1():
    x = linspace(0, 8, 50)
    y = 5 * sin(10 * x) * sin(3 * x) / x ** x
    plt.plot(x, y, "r--", label="Y(x)=5*sin(10*x)*sin(3*x)/(x^x)")
    plt.savefig("resources/plot_task_1.png", dpi=400)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Lab 7 task 1 graph")
    plt.legend()
    plt.show()


def task_2():
    symbols_dict = get_symbols_dict(get_symbols(get_text()))
    x_data = symbols_dict.keys()
    y_data = symbols_dict.values()
    pylab.bar(x_data, y_data)
    pylab.savefig("resources/plot_task_2.png", dpi=400)
    pylab.show()


def task_3():
    sentences_dict = amount_of_each_sentences(get_text())
    x_data = sentences_dict.keys()
    y_data = sentences_dict.values()
    pylab.bar(x_data, y_data)
    pylab.savefig("resources/plot_task_3.png", dpi=400)
    pylab.show()


def get_text():
    filename = input("Enter path to file: ")
    try:
        with open(filename, encoding="utf8") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found")


def get_symbols(text):
    text = text.replace("\n", "").replace(" ", "").replace(",", "").replace(".", "").replace("?", "")
    text = text.replace("!", "").replace("—", "").replace("-", "").replace(":", "").replace("«", "").replace("»", "")
    text = text.lower()
    text = list(text)
    text.sort()
    return text


def get_symbols_dict(symbols):
    symbols_dict = dict()
    for symbol in symbols:
        if symbol in symbols_dict:
            symbols_dict[symbol] = symbols_dict[symbol] + 1
        else:
            symbols_dict[symbol] = 1
    return symbols_dict


def amount_of_each_sentences(text):
    text = text.replace("\n", " ").replace("—", "") + " "  # add space at end of text for correct work regex (line 72)
    list_delimiters = ["!", "?", ".{3}", ".{1}"]
    types_sentence = ["Exclamatory", "Question", "Ellipsis", "Regular"]
    count_sentences = list()
    for x in list_delimiters:
        patern = "\w[\w\,\s]*\{delimiter}\s".format(delimiter=x)
        sentences = re.findall(patern, text)
        count_sentences.append(len(sentences))
    return dict(zip(types_sentence, count_sentences))


if __name__ == "__main__":
    main()
