"""Lab 02.04 – Parentheses Matching"""
class ArrayStack:
    def __init__(self) :
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
        if self.size != 0:
            self.data.pop()
            self.size -= 1
        else:
            print("Underflow: Cannot pop data from an empty list")

    def get_stack_top(self):
        if self.size != 0:
            x = self.data.pop()
            self.data.append(x)
            return x
        print("Underflow: Cannot get stack top from an empty list")

    def print_stack(self):
        print(self.data)

def main():
    stack = ArrayStack()
    xyz = input()
    is_parentheses_matching = True
    for i in xyz:
        if i == '(':
            stack.push('(')
        elif i == ')' :
            if stack.size == 0:
                print("Underflow: Cannot pop data from an empty list")
                is_parentheses_matching = False
            else:
                stack.push(')')
                stack.pop()
                stack.pop()
    if stack.size != 0:
        is_parentheses_matching = False
    if is_parentheses_matching == True:
        print(f"Parentheses in {xyz} are matched")
    else:
        print(f"Parentheses in {xyz} are unmatched")
    print(is_parentheses_matching)
main()
