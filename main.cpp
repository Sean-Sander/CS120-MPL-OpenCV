//
// Created by Sean on 4/9/2021.
//

#include <fstream>
#include <string>
#include <iostream>
using namespace std;


// Different OSs use different CLI commands to run Python
#ifdef _WIN32
const string python = "python";
#else
const string python = "python3";
#endif

/**
 * Prompts user for a directory to search images for faces in
 * @return directory
 */
string get_directory_choice();

int main() {
    string directory = get_directory_choice();
    char choice = directory.back();
    directory.pop_back(); // make to directory

    string command = python + " ../identifier.py " + "../" + directory + " " + choice;
    system(command.c_str());
    return 0;
}

string get_directory_choice() {
    cout << "Enter a directory for testing (enter nothing to pick from defaults): ";
    string directory;
    char choice;
    getline(cin, directory);
    if (directory.length() > 0) {
        cout << "Proceeding with " + directory + ".";
        cout << "Attempt detection of (a) faces or (b) stop signs in this directory: ";
        cin >> choice;
        while (tolower(choice) != 'a' && tolower(choice) != 'b') {
            cout << "Invalid input, try again: ";
            cin >> choice;
        }
    } else {
        cout << "Going from defaults, pick from (a) faces or (b) stop signs: ";
        cin >> choice;
        while (tolower(choice) != 'a' && tolower(choice) != 'b') {
            cout << "Invalid input, try again: ";
            cin >> choice;
        }
        choice = tolower(choice);
        if (choice == 'a')
            directory = "faces";
        else if (choice == 'b')
            directory = "stop_signs";
    }
    return directory + choice;
}