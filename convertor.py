import dataclasses as dc


@dc.dataclass
class InterDimensionalConvertor:
    alien_based_num: int
    alien_num: list = dc.field(init=False)
    human_num: int = dc.field(init=False)

    def __post_init__(self):
        while self.alien_based_num < 2 or self.alien_based_num == 10:
            self.alien_based_num = int(input("Invalid numeric base, Enter number between 2-9 or bigger than 10: "))
        self.alien_num = []
        self.human_num = 0

    def set_alien_num(self, num: str) -> None:
        self.alien_num = []
        lesser_than_ten = True
        digit_placer_exponent = 0
        for char in reversed(num):
            if char.isnumeric() and lesser_than_ten:
                self.alien_num.append(int(char))
            elif char == ']':
                lesser_than_ten = False
                self.alien_num.append(0)
            elif char == '[':
                lesser_than_ten = True
                digit_placer_exponent = 0
            elif char.isnumeric() and not lesser_than_ten:
                self.alien_num[-1] += int(char) * (10 ** digit_placer_exponent)
                digit_placer_exponent += 1
        self.alien_to_human()
        if num[0] == '-':
            self.human_num = self.human_num * (-1)

    def set_human_num(self, num: int) -> None:
        self.human_num = num
        self.human_to_alien()

    def alien_to_human(self) -> None:
        """
        Convert a number from alien-based to 10-based
        On each cell we do a power action where the alien_based_number is the based,
        and index of cell is the exponent,
        and then multiply it by the digit contained in that cell,
        and finally - add up the result of all cells into one, decimal number
        Example: based-7, number 642 -> (6*7^2) + (4*7^1) + (2*7^0)
        """
        self.human_num = 0
        for index, a_num_digit in enumerate(self.alien_num):
            self.human_num += a_num_digit * (self.alien_based_num ** index)

    def human_to_alien(self) -> None:
        """
        Convert a number from 10-based to alien-based
        Have an empty array with no numbers yet (not even 0)
        Now take the human_number, divide it by the alien_based_number,
        and append the remainder at the most-right empty cell of the array
        do this over and over again until the quotient reached 0
        example: based-7, number 109 -> 109/7 == 15/7 (4) == 2/7 (14) == 0 (214)
        """
        self.alien_num = []
        temp_human_num = abs(self.human_num)  # Original human number needs to be preserved
        while temp_human_num > 0:
            self.alien_num.append(temp_human_num % self.alien_based_num)
            temp_human_num //= self.alien_based_num

    def alien_num_to_string(self) -> str:
        """
        take the alien number and convert it into string
        if the alien-based-number is greater than 10,
        every single digit greater than 10 would be represented in []
        in order to mark that this is a single digit
        :return: a string of number from alien-based
        """
        represented_of_alien_num: str = ""
        if self.human_num < 0:
            represented_of_alien_num += '-'
        for index in reversed(self.alien_num):
            represented_of_alien_num += (str(index) if index < 10 else ('[' + str(index) + ']'))
        return represented_of_alien_num

    def __repr__(self):
        return f"Number based: {self.alien_based_num}, Alien number: {self.alien_num_to_string()}, " \
               f"Which is {self.human_num} in human's 10-based"


def alien_to_alien_number(alien_in: InterDimensionalConvertor, num: int) -> str:
    """
        Convert a number from one alien-based to another, and return that number
        :param alien_in: The input alien-based number
        :param num: The based for the alien number output
        :return: Alien-based number output
        """
    temp = InterDimensionalConvertor(num)
    temp.set_human_num(alien_in.human_num)
    return temp.alien_num_to_string()


def alien_to_alien(alien_in: InterDimensionalConvertor, alien_out: InterDimensionalConvertor) -> None:
    """
        Convert a number from one alien-based to another via 10-based
        :param alien_in: The alien-based number we want to convert from
        :param alien_out: The alien-based number we want to convert to
        """
    alien_out.set_human_num(alien_in.human_num)
