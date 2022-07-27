from typing import List
from unittest import result


def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]

def is_prime(number: int) -> bool:
    result: List[int] = [n for n in range(1,number+1) if number % n == 0]
    return len(result) == 2

def main ():
    print(is_prime(98))

if __name__ == '__main__':
    main()