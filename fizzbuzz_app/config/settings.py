# config/settings.py
import os

class Settings:
    APP_NAME = "FizzBuzz Professional"
    DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "users.json")
    DARK_THEME = True
    
# utils/fizzbuzz_implementations.py
class FizzBuzzImplementations:
    @staticmethod
    def if_else_impl(n):
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
        def fizzbuzz(num):
            if num % 3 == 0 and num % 5 == 0:
                return "FizzBuzz"
            elif num % 3 == 0:
                return "Fizz"
            elif num % 5 == 0:
                return "Buzz"
            return str(num)
        return [fizzbuzz(i) for i in range(1, n + 1)]

    class ClassImpl:
        def __init__(self, n):
            self.n = n
        
        def generate(self):
            return [
                "FizzBuzz" if i % 15 == 0 else
                "Fizz" if i % 3 == 0 else
                "Buzz" if i % 5 == 0 else
                str(i)
                for i in range(1, self.n + 1)
            ]