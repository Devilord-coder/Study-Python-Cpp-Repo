#include <string>
#include <iostream>
#include <cctype>
using namespace std;

/// Скрипт для раскодирования файла
int main() {
    string line;
    while (getline(cin, line)) {
        for (char c : line) {
            if (isspace(c)) {
                cout << c;
            } else {
                c -= 50;
                cout << c;
            }
        }
        cout << "\n";
    }
    return 0;
}