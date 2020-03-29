import csv
import os


def choose_option(choice):
    try:
        if choice == 1:
            choice = input("Choose group -> ")
            path = "resources/{group}.csv".format(group=choice)
            print_all_from_file(path)
        elif choice == 2:
            choice = input("Choose group -> ")
            path = "resources/{group}.csv".format(group=choice)
            users = input("Enter new records (Name Rating; Name Rating) -> ")
            append_records_to_file(path, users)
        elif choice == 3:
            choice = input("Choose group -> ")
            path = "resources/{group}.csv".format(group=choice)
            users = input("Enter new records (Name Rating; Name Rating) -> ")
            write_new_records_to_file(path, users)
        elif choice == 4:
            choice = input("Choose group -> ")
            path = "resources/{group}.csv".format(group=choice)
            user = input("Choose number of student -> ")
            search_and_print_by_number(path, user)
        elif choice == 5:
            choice = input("Choose group -> ")
            path = "resources/{group}.csv".format(group=choice)
            rating = input('Sort by name (1), sort by mark (2): ')
            rating = int(rating) - 1
            sort_and_print_by_rating(path, rating)
        elif choice == 6:
            choice = input("Choose directory -> ")
            search_csv_files_at_directory(choice)
        else:
            print("Wrong choice")
    except Exception as ex:
        print("Something bad was happened: ", ex)


def search_csv_files_at_directory(directory):
    try:
        files = os.listdir(directory)
        csv_files = filter(lambda x: x.endswith('.csv'), files)
        list_files = list(csv_files)
        if len(list_files) == 0:
            print("There isn't csv")
        else:
            for f in list_files:
                print(f)
    except Exception as ex:
        print("Something bad was happened: ", ex)


def sort_and_print_by_rating(FILENAME, rating):
    try:
        with open(FILENAME, "r", newline="", encoding='utf-8') as file:
            line = file.readlines()
            line.sort(key=lambda i: i[rating])
            for row in line:
                print(row)
    except Exception as ex:
        print("Something bad was happened: ", ex)


def search_and_print_by_number(FILENAME, number):
    try:
        with open(FILENAME, "r", newline="", encoding='utf-8') as file:
            line = file.readlines()[int(number)]
            print(line)
    except Exception as ex:
        print("Something bad was happened: ", ex)


def write_new_records_to_file(FILENAME, users_to_write):
    users = users_to_write.split('; ')
    n = len(users)
    new_users = []
    try:
        for i in range(n):
            row = users[i].split(' ')
            for j in range(len(row)):
                row[j] = str(row[j])
            new_users.append(row)
        with open(FILENAME, "w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(new_users)
    except Exception as ex:
        print("Something bad was happened: ", ex)


def append_records_to_file(FILENAME, users_to_write):
    users = users_to_write.split('; ')
    n = len(users)
    new_users = []
    for i in range(n):
        row = users[i].split(' ')
        for j in range(len(row)):
            row[j] = str(row[j])
        new_users.append(row)
    try:
        with open(FILENAME, "a", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(new_users)
    except Exception as ex:
        print("Something bad was happened: ", ex)


def print_all_from_file(FILENAME):
    try:
        with open(FILENAME, "r", newline="", encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0], " - ", row[1])
    except Exception as ex:
        print("Something bad was happened: ", ex)
