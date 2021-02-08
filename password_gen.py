#!/usr/bin/python3

import secrets
import re
import argparse
import os
from os import path
import errno


# Define Argument Parser
parser = argparse.ArgumentParser(description='Generate a password from a list of words')
parser.add_argument('-w', '--words', help='(Optional) Number of words in your password', metavar='', required=False, type=int, dest='words')
parser.add_argument('-n', '--number', help='(Optional) Number of passwords', metavar='', required=False, type=int, dest='count')
parser.add_argument('--min', help='(Optional) Minimal number of letters per word', metavar='', required=False, type=int, dest='min')
parser.add_argument('--max', help='(Optional) Maximum number of letters per word', metavar='', required=False, type=int, dest='max')
parser.add_argument('--list', '--wordlist', help='(Optional) Define wordlist or use the provided one', metavar='', required=False, dest='wordlist')

# Define variables
args = parser.parse_args()
words = args.words
minimum = args.min
maximum = args.max
count = args.count
wordlist = args.wordlist


# Colors for error message
class colors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED


def contains_digit(string):  # Regex to check if word contains a numeral
    re_digit = re.compile(r'\d')
    if re.search(re_digit, string):
        return True


def contains_quotes(string):  # Regex to check if word contains apostrophe or a dash
    re_symbol = re.compile(r"'|-")
    if re.search(re_symbol, string):
        return True


def make_wordlist(read_lines=None):  # Makes a list of words to use for password generation
    global minimum
    global maximum
    if read_lines is None:
        read_lines = new_line
    if minimum or maximum is None:
        minimum, maximum = 6, 9
    for line in read_lines:
        if not contains_quotes(line) and not contains_digit(line):  # Check if no quotes, dash and digits in line
            if minimum < len(line) <= maximum:
                if line.islower():
                    cleaned_list.append(line[:-1])  # Append line to list without \n character


def choose_random():  # Choose the words for the password randomly with secrets
    global words
    if words is None:
        words = 4
    password = []
    for i in range(words):
        password.append(secrets.choice(cleaned_list))
    return password


def print_passwords(count):  # Print the password with one white space between each word
    if count is None:
        count = 1
    for i in range(count):
        print(' '.join(choose_random()))


if __name__ == '__main__':
    try:
        if wordlist is None:
            if path.exists('wordlist.txt'):  # If None wordlist is specified check if wordlist.txt exists
                wordlist = 'wordlist.txt'
            else:  # Raise FileNotFound error if no wordlist is specified and wordlist.txt doesnt exist
                print(colors.FAIL, "Wordlist not found, please specify a wordlist.")
                raise FileNotFoundError(
                    errno.ENOENT, os.strerror(errno.ENOENT), wordlist)
        if wordlist is not None:
            if path.exists(wordlist):
                with open(wordlist) as word_list:
                    new_line = word_list.readlines()
                    cleaned_list = []
                    make_wordlist()
                    print_passwords(count)
            else:
                print(colors.FAIL, "Path to wordlist is invalid, please specify a valid wordlist")
                raise FileNotFoundError(
                    errno.ENOENT, os.strerror(errno.ENOENT), wordlist)
    except Exception as e:
        print(colors.FAIL, "Unknown error, please report to ")
        print(e)
