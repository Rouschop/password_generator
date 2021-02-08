Password generator to randomly generate a password from a list of words.
Example usage:

python3 password_gen.py

python3 password_gen.py	-w 4

python3 password_gen.py -w 4 --min 4 --max 10 

python3 password_gen.py -w 4 --min 5 --max 9 -n 5 --list my_own_wordlist.txt

 
'''usage: password_gen.py [-h] [-w] [-n] [--min] [--max] [--list]

Generate a password from a list of words

optional arguments:
  -h, --help            show this help message and exit
  -w , --words          (Optional) Number of words in your password
  -n , --number         (Optional) Number of passwords
  --min                 (Optional) Minimal number of letters per word
  --max                 (Optional) Maximum number of letters per word
  --list , --wordlist   (Optional) Define wordlist or use the provided one'''
