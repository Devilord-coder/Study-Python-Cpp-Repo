#include "count_words.h"

int main(int argc, char* argv[]) {
    bool total_count = false;
    if (argc >= 2) {
        total_count = true;
    }
    count_words(total_count);
    return 0;
}
