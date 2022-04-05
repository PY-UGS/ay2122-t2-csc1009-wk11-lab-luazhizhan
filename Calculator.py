class Calculator:
    """
    Calculator class that takes in two inputs.\n
    Methods available

    1. add
    2. subtract
    3. multiple
    4. divide
    """

    def __init__(self, input1, input2):
        """
        Constructor\n
        Init `input1` and `input2` attributes
        """
        self.set(input1, input2)

    def set(self, input1, input2):
        """
        Set `input1` and `input` attributes
        """
        self.input1 = input1
        self.input2 = input2

    def adder(self):
        return self.input1 + self.input2

    def subtractor(self):
        return self.input1 - self.input2

    def multiplier(self):
        return self.input1 * self.input2

    def divider(self):
        return self.input1 / self.input2

    def clear(self):
        """
        Set `input1` and `input2` attributes to 0
        """
        self.set(0, 0)


def main():
    try:
        # Get first and second input from user
        input1 = float(input("Enter first number: "))
        input2 = float(input("Enter second number: "))

        # Second input cannot be 0 due to divide operation
        if input2 == 0:
            print("Second input cannot be 0!")

        # Instantiate Calculator object
        calculator = Calculator(input1, input2)

        # Print results
        print("\nadder : " + str(calculator.adder()))
        print("subtractor : " + str(calculator.subtractor()))
        print("multiplier : " + str(calculator.multiplier()))
        print("divider : " + str(calculator.divider()))

        # Clear input1 and input2 attributes in calculator object
        calculator.clear()
    except ValueError:
        # Catch non float inputs
        print("That's not an float!")
        main()


main()
