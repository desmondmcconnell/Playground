"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def get_fixed_name_v2(name):
    previous_char = ''
    new_name = ''
    for character in name:
        if previous_char.islower():
            if character.isupper():
                new_name += '_'
        if previous_char == " " or previous_char == '_':
            character = character.upper()
        new_name += character
        previous_char = character
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_filename = os.path.join(directory_name, filename)
            fixed_filename = get_fixed_filename(new_filename)
            new_fixed_name = get_fixed_name_v2(fixed_filename)
            os.rename(new_filename, new_fixed_name)


demo_walk()
