"""Lab 02.01 - Stack (Create Stack)"""
class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()

    def is_empty(self):
        return self.size == 0

    def get_stack_top(self):
        if self.is_empty():
            print("Underflow: Cannot get stack top from an empty list")
            return None
        tda = self.data.pop(-1)
        self.data.append(tda)
        return tda        

    def get_size(self):
        return self.size

    def print_stack(self):
        print(self.data)

def main():
    stack = ArrayStack()
    while True:
        text_in = input()
        if text_in.lower() == "exit":
            break
        if ": " in text_in:
            condition, data = text_in.split(": ", 1)
        else:
            condition, data = text_in, None
        if condition == "Push":
            stack.push(data)
        elif condition == "Pop":
            stack.pop()
        elif condition == "Top":
            print(stack.get_stack_top())
        elif condition == "Size":
            print(stack.get_size())
        elif condition == "Empty":
            print(stack.is_empty())
        elif condition == "Print":
            stack.print_stack()
        else:
            print("Invalid Condition!")
    stack.print_stack()

main()
