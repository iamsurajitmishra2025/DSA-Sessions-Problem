# Code which can help evaluate the postfix string

def postfix_evaluator(postfix):
    st = [] # Empty stack

    for c in postfix:
        if c.isdigit(): st.append(int(c))

        else:
            b = st.pop()
            a = st.pop()

            if c == '+':
                st.append(a + b)
            elif c == '-':
                st.append(a - b)
            elif c == '*':
                st.append(a * b)
            elif c == '/':
                st.append(int(a/ b))
            elif c == '^':
                st.append(a^b)

    return st[0]

if __name__ == '__main__':
    postfix = "231*+9-"
    evaluation = postfix_evaluator(postfix)
    print(evaluation)
