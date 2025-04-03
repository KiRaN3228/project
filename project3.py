import random

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'


def ask_yes_no(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ('y', 'n'):
            return choice == 'y'
        print("error: enter 'y' or 'n'")


def get_password_length():
    while True:
        user_input = input("enter the desired length of your password: ")
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("error: please enter a positive integer.")


def get_chars():
    chars = ''
    if ask_yes_no('use numbers? y/n: '):
        chars += DIGITS
    if ask_yes_no('use lowercase letters? y/n: '):
        chars += LOWERCASE_LETTERS
    if ask_yes_no('use uppercase letters? y/n: '):
        chars += UPPERCASE_LETTERS
    if ask_yes_no('use special characters? y/n: '):
        chars += PUNCTUATION
    if not chars:
        print('please select at least one symbol type.')
        get_chars()

    if ask_yes_no('remove ambiguous characters (il1Lo0O)? y/n: '):
        for i in chars:
            if i in 'il1Lo0O':
                chars = chars.replace(i, "")
    return chars


def password_generate(chars, length):
    return ''.join(random.choices(chars, k=length))


def main():
    length = get_password_length()
    chars = get_chars()
    password = password_generate(chars, length)
    print(f'your password: {password}')


if __name__ == '__main__':
    main()
