import os
import argparse


def global_cpp_init():
    """ Функция для компилляции всех C++ файлов """

    if not os.path.exists("./exe/count_words"):
        try:
            print("- идет компиляция файла ./src/count_words.cpp")
            os.system("clang++ --std=c++20 -o ./exe/count_words ./src/count_words.cpp")
        except Exception as e:
            raise e("❌ Произошла ошибка компиляции программы.")

    ...

    print("✅ Компиляция всех C++ файлов прошла успешно.")


def main():
    """ Main function """

    parser = argparse.ArgumentParser(
        description='counts the number of words in text-file'
    )
    parser.add_argument("file_name", type=str, help="name of file", default="txt/Master_and_Margarita.txt", nargs="?")
    parser.add_argument("-o", default="result.json", type=str, help="result file name")
    parser.add_argument("--total_count", action="store_true", default=False,
                        help="if you need to see total count of words")

    args = parser.parse_args()
    print(f"==================== {__name__} ====================")
    os.system("./exe/print_voland")

    if not os.path.exists(args.file_name):
        raise FileNotFoundError(f"There is no file {args.file_name} in current directory   ¯\_(ツ)_/¯")
    else:
        file_name = args.file_name

    if not args.o.endswith(".json"):
        o = args.o + ".json"
    else:
        o = args.o

    global_cpp_init()

    try:
        if args.total_count:
            os.system(f'./exe/count_words "true" < {file_name} > {o}')
        else:
            os.system(f"./exe/count_words < {file_name} > {o}")
    except Exception as e:
        raise e("❌ Произошла ошибка в программе. Программа завершила работу с ненулевым кодом возврата.")
    else:
        print(f"✅ Программа завершила работу с кодом возврата 0. Результат записан в файл {o}")


if __name__ == "__main__":
    main()