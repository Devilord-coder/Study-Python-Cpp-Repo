import os
import argparse


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
    print(f"============ {__name__} ============")

    if not os.path.exists(args.file_name):
        raise FileNotFoundError(f"There is no file {args.file_name} in current directory   ¯\_(ツ)_/¯")
    else:
        file_name = args.file_name

    if not args.o.endswith(".json"):
        o = args.o + ".json"
    else:
        o = args.o

    try:
        print("- идет компилляция программы на C++")
        os.system("clang++ --std=c++20 -o count_words count_words.cpp")
    except Exception as e:
        raise e("❌ Произошла ошибка компилляции программы.")
    else:
        print("✅ Компилляция прошла успешно.")
    try:
        if args.total_count:
            os.system(f'./count_words "true" < {file_name} > {o}')
        else:
            os.system(f"./count_words < {file_name} > {o}")
    except Exception as e:
        raise e("❌ Произошла ошибка в программе. Программа завершила работу с ненулевым кодом возврата.")
    else:
        print(f"✅ Программа завершила работу с кодом возврата 0. Результат записан в файл {o}")


if __name__ == "__main__":
    main()