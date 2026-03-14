from pycode.const import *
from pycode.exceptions import *
import os
import argparse


def global_cpp_init():
    """ Функция для компилляции всех C++ файлов

    Raises:
        ClangCompilationError - если возникла ошибка компиляции скрипта
    """

    if not os.path.exists(COUNT_WORDS_EXE_PATH):
        try:
            print(f"- идет компиляция файла {COUNT_WORDS_PATH}")
            os.system(f"clang++ --std=c++20 -o {COUNT_WORDS_EXE_PATH} {COUNT_WORDS_PATH}")
        except Exception as e:
            raise e("❌ Произошла ошибка компиляции программы.")

        # если не появился исполняемы файл -> вызвать ошибку компиляции
        if not os.path.exists(COUNT_WORDS_EXE_PATH):
            raise ClangCompilationError(f"❌ Произошла ошибка при компиляции скрипта: {COUNT_WORDS_PATH}")

    ...

    print("✅ Компиляция всех C++ файлов прошла успешно.")


def main():
    """ Main function """

    # Парсер аргументов
    parser = argparse.ArgumentParser(
        description='counts the number of words in text-file'
    )
    parser.add_argument("file_name", type=str, help="name of file", default="txt/Master_and_Margarita.txt", nargs="?")
    parser.add_argument("-o", default="result.json", type=str, help="result file name")
    parser.add_argument("--total_count", action="store_true", default=False,
                        help="if you need to see total count of words")

    args = parser.parse_args()

    print(f"==================== {__name__} ====================")
    # Вывод большой надписи "VOLAND"
    os.system(PRINT_VOLAND_EXE_PATH)

    if not os.path.exists(args.file_name): # если указанного файла не существует
        raise FileNotFoundError(f"There is no file {args.file_name} in current directory   ¯\\_(ツ)_/¯")
    else:
        file_name = args.file_name

    if not args.o.endswith(".json"): # если не указано расширение для файла с результатом
        o = args.o + ".json"
    else:
        o = args.o

    global_cpp_init() # Компиляция всех C++ скриптов

    try:
        if args.total_count:
            os.system(f'{COUNT_WORDS_EXE_PATH} "true" < {file_name} > {o}')
        else:
            os.system(f"{COUNT_WORDS_EXE_PATH} < {file_name} > {o}")
    except Exception as e:
        raise e("❌ Произошла ошибка в программе. Программа завершила работу с ненулевым кодом возврата.")

    # Если не появился файл с результатом или он пустой -> вызвать ошибку
    with open(o, 'r') as result:
        empty = not bool(result.read())
    if not os.path.exists(o) or empty:
        raise ProgrammError("❌ Произошла ошибка при чтении файла или файл с результатом оказался пустой")

    print(f"✅ Программа завершила работу с кодом возврата 0. Результат записан в файл {o}")


if __name__ == "__main__":
    main()