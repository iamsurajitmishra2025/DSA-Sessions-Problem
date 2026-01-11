# Get Minimum in the Stack at O(1)

class Stack:
    """
    Implemented Min Stack using 2 Stacks
    Stack 1: Use to store the actual values
    Stack 2: Storing the minimum value corresponding to the current value.
    Push(data): Push data to Stack 1. Also add the minimum of current value and top value of Minstack.
    Pop(): Pop out values from both the stack.
    top(): Top value of Stack 1.
    get_min(): top value of stack 2.

    Complexity analysis:
    T.C: O(2*N)
    S.C: O(2*N)
    T.C (Minimum of stack): O(1)
    """
    def __init__(self):
        self.st = []
        self.min_stack = []
        self.min_val = int(1e9)

    def push(self, data):
        self.st.append(data)
        if not self.min_stack:
            self.min_stack.append(data)
        else:
            min_top = self.min_stack[-1]
            self.min_stack.append(min(min_top, data))

    def pop(self):
        if not self.st: return None
        self.min_stack.pop()
        return self.st.pop()

    def get_min(self):
        if not self.min_stack: return None
        return self.top(self.min_stack)


    def top(self, st):
        if not st: return None
        return st[-1]

class Stack_Optimized:
    """
    Optimized version of Get Minimum value of Stack.
    Approach:
    Push(data): If data is greater than minimum, just add it to the stack.
                if data is less than minimum, we will store newVal.
                newVal = 2 * data - minimum
                **Why? -> Will answer in pop()
    Pop(): If the top element to be popped, is greater than minimum value, then just pop it.
            if not, pop out the top of the stack and
            ** We want to go back the previous minimum value
            prevMin = 2 * cur_min_val - top

    T.C: O(N)
    S.C: O(N)
    getMin : O(1)
    """


    def __init__(self):
        self.st = []
        self.min_val = int(1e9)

    def push(self, val):
        if val >= self.min_val:
            self.st.append(val)
        else:
            self.st.append(2*val - self.min_val)
            self.min_val = val

    def pop(self):
        if not self.st: return None
        x = self.st[-1]
        if x < self.min_val:
            pop_val = self.min_val
            self.min_val = 2 * self.min_val - x
            self.st.pop()
            return pop_val
        return self.st.pop()

    def get_min(self):
        return self.min_val

    def top(self):
        if not self.st: return None
        x = self.st[-1]
        if x < self.min_val:
            return self.min_val
        return x


if __name__ == '__main__':
    print("Normal Stack: ")
    s = Stack()
    s.push(12)
    s.push(15)
    s.push(10)
    get_min = s.get_min()
    print("Min_Val:",get_min)

    pop_val = s.pop()
    print("Pop:", pop_val)

    get_min = s.get_min()
    print("Min_Val:", get_min)

    top = s.top(s.st)
    print("Top:", top)

    s.push(10)

    top = s.top(s.st)
    print("Top:", top)

    print("Optimized Stack")
    s = Stack_Optimized()
    s.push(12)
    s.push(15)
    s.push(10)
    get_min = s.get_min()
    print("Min_Val:", get_min)

    pop_val = s.pop()
    print("Pop:", pop_val)

    get_min = s.get_min()
    print("Min_Val:", get_min)

    top = s.top()
    print("Top:", top)

    s.push(10)

    top = s.top()
    print("Top:", top)