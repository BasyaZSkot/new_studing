# Passwords Generator

This Python script generates random passwords based on a given dictionary of words. You can customize the number of passwords, the number of words in each password, specify a dictionary file, add separators between words, and replace certain symbols in the generated passwords.

## Prerequisites

You need to run virtualenv with this command:

    pipenv shell

## Usage

Before running the script, make sure to check the available options by using the following command:

    python password_generator.py --help

### Options

    - `--word_num`, `-wn`: Number of words in each password (default: 1)
    - `--password_num`, `-pn`: Number of passwords to generate (default: 1)
    - `--path_of_dictionary`, `-pof`: Path to the dictionary file containing words (default: 'dictionaries/basic_list_of_words.txt')
    - `--separators`, `-s`: Spaces or separators between words in the password (default: '')
    - `--change_symbols`, `-ch`: Symbols to be replaced in the generated passwords (default: ('', ''))
    - `--passwords_in_file`, `-pif`: Indicates whether passwords will be written to a file (default: True)
    - `--out_file`, `-of`: Path to the output file where generated passwords will be saved (default: 'output/password_list.txt')

### Example Usage

Generate a single password with 3 words from the default dictionary, separated by hyphens, and save it to a file:

    python password_generator.py --password_num 1 --word_num 3 --separators - --passwords_in_file 

Also generate a single password with 3 words from the default dictionary, separated by hyphens, and save it to a file:

    python password_generator.py -pn 1 -wn 3 -s _ -pif 

## Custom Dictionary

If you want to use your own dictionary, create a text file with one word per line and specify the path to this file using the `--path_of_dictionary` option.

### Note

Make sure to run the script with appropriate file permissions if you are writing passwords to a file in a directory where you need write access.

## Personal achievements in the project
This is my first project. It was created while learning the Python programming language. With the help of this project I learned the basics of git and github, and also became familiar with the click library.