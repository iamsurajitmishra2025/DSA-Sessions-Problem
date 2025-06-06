"""
1.Infix to Postfix conversion
Input: A + B * C + D
Output: ABC*+D+
Input: ((A + B) - C * (D / E)) + F
Output: AB+CDE/*-F+
"""

def precedence(c):
    if c == '^': return 3
    if c in ('/', '*'): return 2
    if c in ('+', '-'): return 1
    return -1


def inf_postfix(infix):
    st = [] # initializing an empty stack
    res = "" # Result string


    for c in infix:
        # Checking if current character is text (a-z, A-Z) or numbers (0-9)
        # Then just add to the result string
        if c.isalnum(): res += c

        # If '(', just push it to the stack
        elif c == '(': st.append(c)

        # If c is ')', pop all the operators until the stack top is '('.
        # And add to the resultant string.
        elif c == ')':
            while st and st[-1] != '(':
                res += st.pop()
            st.pop()

        # If c is a symbol, push it to the stack but check if the precedence of current character
        # is lesser than or equal to the top operator. If yes, pop out all operators which have higher precedence
        # and add it to the resultant string.
        else:
            while st and precedence(c) <= precedence(st[-1]):
                res += st.pop()
            st.append(c)

    while st:
        res += st.pop()

    return res



if __name__ == '__main__':
    infix = "A+B*C+D"
    print('infix:', infix)
    postfix = inf_postfix(infix)

    print('postfix:', postfix)

    infix = "((A+B)-C*(D/E))+F"
    print('infix:', infix)
    postfix = inf_postfix(infix)

    print('postfix:', postfix)
