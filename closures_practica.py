from __future__ import division
from timeit import repeat
from regex import P
from tomlkit import string


def make_repeater_of(n:int):
    
    def repeater(string:str) -> str: 
        assert type(string) == str, 'Solo puedes ingresar cadenas de caracteres'
        return string * n

    return repeater


def make_division_by(n:int): 
    """This closure returns a function that returns the division of an x number by n"""

    def division(x:int) -> float:
        return round(x / n,2)

    return division

def main():
    division_by_18 = make_division_by(18)
    print(division_by_18(54))

if __name__ == '__main__':
    main()