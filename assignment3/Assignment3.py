next_token=''
data=[]
error=False
i=0

def lex():
    global i,next_token
    if i<len(data):
        next_token=data[i]
        i+=1
    return

def unconsumed_input():
    global i
    uncnsmd=""
    j=0
    while j<len(data):
        if j<i:
            j+=1
            continue
        else:
            uncnsmd+=data[j]+' '
            j+=1
    return uncnsmd

# G -> E
def G():
    global error, next_token
    lex()
    print("G -> E")
    E()
    if next_token=='$' and not error:
        print("success")
    else:
        print(f"failure: unconsumed input={unconsumed_input()}")
    return

# E -> T R
def E():
    global error
    if error:
        return
    print("E -> T R")
    T()
    R()
    return

# R-> + T R | - T R | e
def R():
    global error, next_token
    if error:
        return
    if next_token=='+':
        print("R -> + T R")
        lex()
        T()
        R()
    elif next_token=='-':
        print("R -> - T R")
        lex()
        T()
        R()
    else:
        print("R -> e")
    return

# T -> F S
def T():
    global error
    if error:
        return
    print("T -> F S")
    F()
    S()
    return

# S -> * F S | / F S | e
def S():
    global error, next_token
    if error:
        return
    if next_token=='*':
        print("S -> * F S")
        lex()
        F()
        S()
    elif next_token=='/':
        print("S -> / F S")
        lex()
        F()
        S()
    else:
        print("S -> e")
    return

# F -> ( E ) | N
def F():
    global error, next_token
    if error:
        return
    if next_token=='(':
        print("F -> ( E )")
        lex()
        E()
        if next_token==')':
            lex()
        else:
            error=True
            print(f"error: unexpected token {unconsumed_input()}")
            return
    elif '0'<=next_token<='9':
        print("F -> N")
        N()
    else:
        error=True
        print(f"error: unexpected token {next_token}")
        print(f"unconsumed_input {unconsumed_input()}")
    return

# N -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
def N():
    global error, next_token
    if error:
        return
    if '0'<=next_token<='9':
        print(f"N -> {next_token}")
        lex()
    else:
        error=True
        print(f"error: unexpected token {next_token}")
        print(f"unconsumed_input {unconsumed_input()}")
    return

# Reading the file
while True:
    f=input("Enter the filename:")
    try:
        with open(f, "r") as l:
            for line in l:
                for word in line.split():
                    data.append(word)
        print("File loaded sucessfully")
    except:
        print("Error reading file. Try again.\n")
        continue
    break

G()