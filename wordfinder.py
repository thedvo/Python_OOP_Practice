"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """Reads words from a text file and generates a random word

    >>> >>> wf = WordFinder("/Users/Dan/Springboard_SE/Unit-Study-and-Exercises/18.Python_Fundamentals/18.4_PythonOOP/python-oo-practice/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """
    #

    def __init__(self, source):
        """Initialize starting number"""
        file = open(source)
        self.words = self.count_words(file)
        print(f'{len(self.words)} words read')

    def count_words(self, file):
        """Counts number of words in list"""
        return [word.strip() for word in file]

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special WordFinder, that excludes blank lines/comments"""

    def count_words(self, file):
        return [word.strip() for word in file if word.strip() and not word.startswith('#')]
