"""
Palindrome class realization.
"""

from arraystack import ArrayStack


class Palindrome:
    '''
    This class checks for palindroms using ArrayStack
    '''

    def __init__(self, input_file=None, output_file=None):
        '''
        Initialize input_file, output_file
        '''
        self.input_file = input_file
        self.output_file = output_file

    def read_file(self) -> list:
        '''
        Read words from file
        '''
        res = []

        with open(self.input_file, "r", encoding="utf-8") as inpt:
            for line in inpt:
                line = line.strip().split()[0]

                if line[:4] == "+cs=":
                    line = line[4:]

                res.append(line)

        return res

    def write_to_file(self, res):
        '''
        Write words to file
        '''
        with open(self.output_file, "w", encoding="utf-8") as otpt:
            for line in res:
                otpt.write(line + "\n")

    def find_palindromes(self, input_file, output_file):
        '''
        Find palindromes using stack
        '''
        palindroms = []

        self.input_file = input_file
        self.output_file = output_file

        words = self.read_file()

        for word in words:
            word_lst = list(word)
            word_stack = ArrayStack()

            flag = True

            for letter in range(len(word_lst)-1, -1, -1):
                word_stack.push(word[letter])

            while not word_stack.isEmpty():
                if word_stack.pop() != word_lst.pop():
                    flag = False
                    break

            if flag:
                palindroms.append("".join(word))

        self.write_to_file(palindroms)
        return palindroms


if __name__ == "__main__":
    palindrome = Palindrome()
    palindrome.find_palindromes("base.lst", "palindrome_uk.txt")
    palindrome.find_palindromes("words.txt", "palindrome_en.txt")
