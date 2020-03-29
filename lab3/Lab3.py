import lab3.FilesProcessing as fp


def start():
    try:
        choice = int(input("Choose option: \n" +
                           "1 - Print all from file \n" +
                           "2 - Append record to file \n" +
                           "3 - Rewrite file \n" +
                           "4 - Search record at file and print \n" +
                           "5 - Sort records and print \n" +
                           "6 - Search for files in directory \n" +
                           "Your choice: "))
        fp.choose_option(choice)
    except KeyError:
        print("Value you entered is out of given range")
    except ValueError:
        print("Enter only integer numbers")


if __name__ == "__main__":
    start()
