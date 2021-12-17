#!/usr/bin/python3
import hashlib
import sys

gre = "\033[0;32m"
whi = "\033[1;37m"
red = "\033[1;31m"
yel = "\033[1;33m"
cya = "\033[0;36m"
res = "\033[0;37;40m"


def print_banner():
    print(f'''
██████╗██╗  ██╗██████╗██████╗██╗  ██╗
   ██╔╝██║  ██║██║ ██║██╔═══╝██║  ██║
  ██╔╝ ███████║██████║██████╗███████║ 
 ██╔╝  ██╔══██║██║ ██║╚═══██║██╔══██║
██████╗██║  ██║██║ ██║██████║██║  ██║
╚═════╝╚═╝  ╚═╝╚═╝ ╚═╝╚═════╝╚═╝  ╚═╝

{gre}[{whi}-{gre}]Author: Anonymous Hacks
{gre}[{whi}-{gre}]GitHub: https://github.com/4anonz{res}
 
''')
    print(f'|--{yel}[{red}1{yel}]{cya} Crack hash{res}')
    print(f'|--{yel}[{red}2{yel}]{cya} Create hash{res}')
    print(f'|--{yel}[{red}0{yel}]{cya} Quit\n{res}')


def print_options():
    print(f'|>{yel}[{red}1{yel}]{cya} MD5{res}')
    print(f'|>{yel}[{red}2{yel}]{cya} SHA1{res}')
    print(f'|>{yel}[{red}3{yel}]{cya} SHA224{res}')
    print(f'|>{yel}[{red}4{yel}]{cya} SHA256{res}')
    print(f'|>{yel}[{red}5{yel}]{cya} SHA384{res}')
    print(f'|>{yel}[{red}6{yel}]{cya} SHA512{res}\n')


def crack_hash(hash_word, algorithm):
    print(f"{yel}[{red}*{yel}]{cya} Enter wordlist file or press ctrl+c to use the zhash wordlist{res}")
    wordlist = 'rockyou.txt'
    try:
        wordlist = input(f'{yel}[{red}*{yel}]{cya} Wordlist~$ ')
    except KeyboardInterrupt:
        print('\n')
        pass
    hash_digest = ''

    try:
        wordlist_file = open(wordlist, 'r')
    except:
        print(f'{yel}[{red}*{yel}]{cya} {wordlist} file not found')
        exit(0)
    
    n_pass = len(list(open(wordlist, "rb")))
    counter = 1

    for word in wordlist_file:
        encoded_word = word.encode('utf-8')

        if algorithm == '1':
            hash_digest = hashlib.md5(encoded_word.strip()).hexdigest()

        elif algorithm == '2':
            hash_digest = hashlib.sha1(encoded_word.strip()).hexdigest()

        elif algorithm == '3':
            hash_digest = hashlib.sha224(encoded_word.strip()).hexdigest()

        elif algorithm == '4':
            hash_digest = hashlib.sha256(encoded_word.strip()).hexdigest()
        elif algorithm == '5':
            hash_digest = hashlib.sha1(encoded_word.strip()).hexdigest()
        else:
            hash_digest = hashlib.sha1(encoded_word.strip()).hexdigest()

        # print(hash_digest)
        # print(hash_word)
        # print(word)
        sys.stdout.write(f'\r{counter} of {n_pass}')
        sys.stdout.flush()
        counter += 1

        if hash_digest == hash_word:
            print(f'\n{yel}[{red}*{yel}]{cya} Successfully cracked!')
            print(f'{hash_word}  {whi}==>{yel}  {word}')
            wordlist_file.close()
            exit(0)        
    print(f'\n{yel}[{red}*{yel}]{cya} Cracking complete but no password found!')
    print(f'{yel}[{red}*{yel}]{cya} Maybe try a different wordlist or retry using a different algorithm')
    wordlist_file.close()
    exit(0)


def create_hash(hash_word, algorithm):

    hash_digest = ''
    if algorithm == '1':
        hash_digest = hashlib.md5(hash_word.encode('utf-8').strip()).hexdigest()

    elif algorithm == '2':
        hash_digest = hashlib.sha1(hash_word.encode('utf-8').strip()).hexdigest()

    elif algorithm == '3':
        hash_digest = hashlib.sha224(hash_word.encode('utf-8').strip()).hexdigest()

    elif algorithm == '4':
        hash_digest = hashlib.sha256(hash_word.encode('utf-8').strip()).hexdigest()
    elif algorithm == '5':
        hash_digest = hashlib.sha1(hash_word.encode('utf-8').strip()).hexdigest()
    else:
        hash_digest = hashlib.sha1(hash_word.encode('utf-8').strip()).hexdigest()
    
    print(f'{yel}[{red}*{yel}]{cya} Request completed')
    print(f'{hash_word}  {whi}==>{yel} {hash_digest}\n')

    print(f'{yel}[{red}*{yel}]{cya} Press {red}ctrl+c{cya} to skip saving..')
    file_name = input(f'{yel}[{red}*{yel}]{cya} File name~$ ')

    try:
        f = open(file_name, 'w')
        f.write(hash_digest)
        f.flush()
        f.close()
        print(f'{yel}[{red}*{yel}]{cya} Saved to {file_name}{res}')
        exit(0)
    except FileNotFoundError:
        print(f'{yel}[{red}!{yel}]{cya} Error saving..{res}')
        exit(1)

if __name__ == '__main__':
    try:
        print_banner()
        # Crack or create
        action = input(f'{yel}[{red}*{yel}]{cya} Choice~$ ')
        if action != '1' and action != '2':
            exit(0)
        print(f"{yel}[{red}*{yel}]{cya} Choose an algorithm from list of supported ones below:\n{res}")

        print_options()
        algorithm =  input(f"{yel}[{red}*{yel}]{cya} Algorithm~$ ")
        a = int(algorithm)
        if a < 1 or a > 6:
            print(f'{yel}[{red}*{yel}]{cya} Invalid input{res}')
            exit(1)
        
        if action == '1':
            print(f'{yel}[{red}*{yel}]{cya} Enter a hash or file to crack')
        else:
            print(f'{yel}[{red}*{yel}]{cya} Enter a string to hash or file')
        
        hash_input = input(f'{yel}[{red}*{yel}]{cya} Enter~$ ')
        hash_word = ''

        if '.' in hash_input or len(hash_input) < 10:
            try:
                hash_file = open(hash_input, 'r')
                for word in hash_file:
                    hash_word += word
                hash_file.close()

            except FileNotFoundError:
                if len(hash_input) < 10:
                    print(f'{yel}[{red}!{yel}]{cya} {hash_input} not found!')
                    exit(1)
                hash_word = hash_input
        else:
            hash_word = hash_input
        
        if action == '01' or action == '1':
            crack_hash(hash_word, algorithm)
        else:
            create_hash(hash_word, algorithm)
    except KeyboardInterrupt:
        print(f"\n{yel}[{red}*{yel}]{cya} Goodbye!")
        quit()