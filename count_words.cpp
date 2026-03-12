#include <map>
#include <iostream>
#include <string>
using namespace std;

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