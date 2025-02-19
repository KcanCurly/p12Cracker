import colorama
from colorama import Fore, Style
import sys
from cryptography.hazmat.primitives.serialization import pkcs12
import argparse
import argcomplete

def spinner():
    sys.stdout.write(' ')
    while True:
        for cursor in '|/-\\':
            yield cursor

def spin(spinner):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    sys.stdout.write('\b')

def main():
    colorama.init(autoreset=True)
    parser = argparse.ArgumentParser(description="P12 file cracker")
    parser.add_argument("--p12-path", required=True, help="Path to the .p12 file to crack")
    parser.add_argument("--wordlist", required=True, help="Path to the wordlist of guesses")
    # Enable autocomplete
    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    p12FilePath = args.p12_path
    wordlist = args.wordlist

    iterations = 0
    spin1 = spinner()

    with open(wordlist, 'r') as fp:
        line = fp.readline()
        print('\n')
        print(Fore.CYAN + ' Brute forcing...')
        print('\n')
        while line:
            spin(spin1)
            guess = line.strip()
            try:
                p12 = pkcs12.load_pkcs12(open(p12FilePath, 'rb').read(), guess.encode('utf8'))
            except ValueError as e:
                p12 = None
            if p12:
                print(Fore.BLUE + '****************************************************************\n')
                print(' {}Success!{} Password cracked after {}{}{} attempts.'.format(Fore.GREEN, Fore.RESET, Fore.YELLOW, str(iterations), Fore.RESET))
                print('\n')

                print(" Password is: " + Style.BRIGHT + Fore.RED + guess + '\n')
                print(Fore.BLUE + ' ****************************************************************\n')
                print('\n')
                exit(0)
            else:
                iterations += 1
            line = fp.readline()

    print(Fore.RED + 'Failed to crack the password - try again with a new wordlist\n')
    exit(0)