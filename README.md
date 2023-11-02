# Password Generator

This Python script generates random passwords based on specified parameters. It provides the user with control over the number of words in the password, the option to use a custom word dictionary, and the ability to replace specific characters in the password.

## Usage Instructions

### Before using the program, make sure you have Python installed. To run the program, execute the following command in the command line:

    python passwords_generator.py --help

This command will show you the available options and their descriptions.

### Command Line Options

    --password_num: Number of passwords to generate (default is 1).
    --word_num: Number of words in each password (default is 1).
    --dictionary_of_words, -d: List of words to use for generating passwords (default is a built-in dictionary).
    --separators: Separator characters to add between words in the password (default is no separator).
    --change_symbols, -r: Replace specific symbols in the generated passwords (default is no replacement).
    --print_passwords: If specified, the generated passwords will be printed to the console. If not specified, passwords will be saved to a file named password_list.txt.

## Usage Examples

### Generate 3 passwords, each consisting of 4 words, and print them:

    python passwords_generator.py --password_num 3 --word_num 4 --print_passwords True

### Generate a password using a custom word list, enter passwords in file and replace                              "a" with "b":

    python passwords_generator.py --password_num 1 --word_num 3 -d cat -d dog -d cow -r a -r b

## Personal achievements in the project
This is my first project. It was created while learning the Python programming language. With the help of this project I learned the basics of git and github, and also became familiar with the click library.