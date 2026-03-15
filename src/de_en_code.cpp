#include "main_header.h"
#include <string>
#include <iostream>
#include <cctype>
using namespace std;

/// Скрипт для раскодирования файла
void decode() {
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
}

/// Скрипт для кодирования файла
void encode() {
    string line;
    while (getline(cin, line)) {
        for (char c : line) {
            if (isspace(c)) {
                cout << c;
            } else {
                c += 50;
                cout << c;
            }
        }
        cout << "\n";
    }
}
