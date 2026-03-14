#include <map>
#include <iostream>
#include <string>
using namespace std;

/**
 * Сркипт для подсчета повторений всех слов из стандартного ввода
 * 
 * Примечание: стандартный ввод и вывод лучше осуществлять из файла и в файл
 * 
 * Args:
 * Если кроме названия файла переданы другие аргументы, то в конце будет выведено общее количество слов
 */
int main(int argc, char* argv[]) {
    map<string, int> words;
    string word;
    
    // Читаем все слова по пробелам пока не закончаться
    long long total = 0;
    while (cin >> word) {
        ++words[word];
        ++total;
    }

    // Выводим результат
    cout << "{\n";
    for (const auto& [word, count] : words) {
        cout << "\t\"" << word << "\": " << count << ",\n";
    }
    if (argc >= 2) {
        cout << "\t\"TOTAL_COUNT_OF_WORDS\": " << total << "\n";
    }
    cout << "}";
    return 0;
}