# Takes a text file with ascii values as text as an argument and returns converted text
# Example command: "python ascii-convert.py -d demofile.txt"
# Variants: -d: Decode, e: Encode

import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]

# Used for debugging
# f = open('demofile.txt', 'r')


def argument_check():
    if arg1 not in ['-d', '-e']:
        print('Incorrect argument. Either "-e" or "-d" must be arg[1]')
        sys.exit()

def decode_ascii(text_file):
    ascii_numbers = []
    converted_list = []
    temp_list = []

    f = open(text_file, 'r')
    for obj in f.read():
        if obj != ' ':
            temp_list.append(obj)
        else:
            temp_list = ''.join(temp_list)
            ascii_numbers.append(temp_list)
            temp_list = []

    for num in ascii_numbers:
        num = int(num)
        converted_list.append(chr(num))

    return ''.join(converted_list)


def encode_ascii(text_file):
    temp_list = []
    ascii_list = []

    f = open(text_file)
    for obj in f.read():
        if obj != ' ':
            temp_list.append(str(ord(obj)) + ' ')
        else:
            for x in temp_list:
                ascii_list.append(x)
            
            temp_list = []

    return ''.join(ascii_list)


def main():
    argument_check()
    if arg1 == '-e':
        print(encode_ascii(arg2))
    if arg1 == '-d':
        print(decode_ascii(arg2))



if __name__ == "__main__":
    main()