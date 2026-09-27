'''https://adventofcode.com/2015/day/1'''
# --- Day 1: Not Quite Lisp ---
# Santa was hoping for a white Christmas, but his weather machine's "snow"
# function is powered by stars, and he's fresh out! To save Christmas, he needs
# you to collect fifty stars by December 25th.

# Collect stars by helping Santa solve puzzles. Two puzzles will be made
# available on each day in the Advent calendar; the second puzzle is unlocked
# when you complete the first. Each puzzle grants one star. Good luck!

# Here's an easy puzzle to warm you up.

# Santa is trying to deliver presents in a large apartment building, but he
# can't find the right floor - the directions he got are a little confusing.
# He starts on the ground floor (floor 0) and then follows the instructions one
# character at a time.

# An opening parenthesis, (, means he should go up one floor, and a closing
# parenthesis, ), means he should go down one floor.

# The apartment building is very tall, and the basement is very deep; he will
# never find the top or bottom floors.

# For example:

#     (()) and ()() both result in floor 0.
#     ((( and (()(()( both result in floor 3.
#     ))((((( also results in floor 3.
#     ()) and ))( both result in floor -1 (the first basement level).
#     ))) and )())()) both result in floor -3.

# To what floor do the instructions take Santa?

# --- Part Two ---

# Now, given the same instructions, find the position of the first character
# that causes him to enter the basement (floor -1). The first character in the
# instructions has position 1, the second character has position 2, and so on.

# For example:

#     ) causes him to enter the basement at character position 1.
#    ()()) causes him to enter the basement at character position 5.

# What is the position of the character that causes Santa to first enter the
# basement?
from pathlib import Path

def load_parenthesis(path):
    '''Loads the instructions for Santa.'''
    file_path = Path(__file__).parent / path
    with open(file_path, 'r', encoding='utf-8') as file:
        parenthesis = file.read()
    return parenthesis


def floor(instructions):
    '''Given a set of instructions as told in the problem statement, returns
    the floor that Santa should go.'''
    return instructions.count('(') - instructions.count(')')


def first_basement(instructions):
    '''Finds the position of the first character that causes Santa to enter
    the basement.'''
    current = 0
    for i in range(len(instructions)):
        if instructions[i] == '(':
            current += 1
        else:
            current -= 1
        if current < 0:
            return i + 1


def main():
    '''Main code of module.'''
    parenthesis = load_parenthesis('resources/day01_input.txt')
    print(floor(parenthesis))  # 232
    print(first_basement(parenthesis))  # 1783
    

if __name__ == '__main__':
    main()