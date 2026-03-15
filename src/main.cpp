#include "main_header.h"
#include "count_words.h"

/**
 * Главный скрипт на C++
 * 
 * Args:
 * encode - вводимый текст будет закодирован;
 * decode - вводимый текст будет раскодирован;
 * count_words - для подсчета повторений всех слов;
 * --total_count - если введен аргумент count_words, то будет подсчитано еще общее количество слов;
 * print_voland - для вывода в консоль "VOLAND";
 */
int main(int argc, char* argv[]) {
    if (argc == 1) {
        return 0;
    } else if (string(argv[1]) == "encode") {
        encode();
    } else if (string(argv[1]) == "decode") {
        decode();
    } else if (string(argv[1]) == "print_voland") {
        print_voland();
    } else if (string(argv[1]) == "count_words") {
        bool total_count = false;
        if (argc > 2 && string(argv[2]) == "--total_count") {
            total_count = true;
        }
        count_words(total_count);
    }
    return 0;
}
