"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Initialize starting value for serial number"""
        self.start = self.current_num = start

    # def __repr__(self):
    #     """Shows representation"""
    #     return f"<SeriaiGenerator start = {self.start} next = {self.next}>"

    def generate(self):
        """Returns next sequential number"""
        self.current_num += 1
        return self.current_num - 1

    def reset(self):
        """Resets the number back to the original start number"""
        self.current_num = self.start
