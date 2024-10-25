# Define a class called FizzBuzzImplementations
class FizzBuzzImplementations:

    # These methods are all static methods, meaning they can be called directly on the class
    # without needing to create an instance of the class

    @staticmethod
    def if_else_impl(n):
        """
        This method implements FizzBuzz using if-else statements.

        Args:
            n: The upper limit of the FizzBuzz sequence.

        Returns:
            A list containing the FizzBuzz sequence from 1 to n.
        """
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

    @staticmethod
    def while_impl(n):
        """
        This method implements FizzBuzz using a while loop.

        Args:
            n: The upper limit of the FizzBuzz sequence.

        Returns:
            A list containing the FizzBuzz sequence from 1 to n.
        """
        result = []
        i = 1
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
            i += 1
        return result

    @staticmethod
    def function_impl(n):
        """
        This method implements FizzBuzz using a nested function.

        Args:
            n: The upper limit of the FizzBuzz sequence.

        Returns:
            A list containing the FizzBuzz sequence from 1 to n.
        """
        def fizzbuzz(num):
            if num % 3 == 0 and num % 5 == 0:
                return "FizzBuzz"
            elif num % 3 == 0:
                return "Fizz"
            elif num % 5 == 0:
                return "Buzz"
            return str(num)
        return [fizzbuzz(i) for i in range(1, n + 1)]

    # This is an inner class that defines a class-based implementation of FizzBuzz
    class ClassImpl:
        def __init__(self, n):
            """
            Initializes the ClassImpl object with the upper limit (n).

            Args:
                n: The upper limit of the FizzBuzz sequence.
            """
            self.n = n

        def generate(self):
            """
            Generates the FizzBuzz sequence using a single expression with nested ternaries.

            Returns:
                A list containing the FizzBuzz sequence from 1 to self.n.
            """
            return [
                "FizzBuzz" if i % 15 == 0 else
                "Fizz" if i % 3 == 0 else
                "Buzz" if i % 5 == 0 else
                str(i)
                for i in range(1, self.n + 1)
            ]