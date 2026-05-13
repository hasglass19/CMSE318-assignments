relops=['<=','<','>','>=','==','!=']
i=0
data=[]
lexemesTable={
    "Lexemes":"Tokens",
    "FOR":"FOR_TOKEN",
    "WHILE":"WHILE_TOKEN",
    "IF":"IF_TOKEN"
    }

def is_int(nums):
    try:
        int(nums)
        return True
    except ValueError:
        return False

def is_float(nums):
    try:
        float(nums)
        return True
    except ValueError:
        return False

def special_char(string):
    spe_char_set=set('!@#$%^&*()+{}:"<>?[];\'\\,./`~-=')
    return bool(set(string) & spe_char_set)

def lex():
    global i,data,lexemesTable
    if i<len(data):
        if data[i]=="if":
            print(f"Token: IF_TOKEN\nLexeme: {data[i]}")
            lexemesTable.update({data[i]:"IF_TOKEN"})
        elif data[i]=="while":
            print(f"Token: WHILE_TOKEN\nLexeme: {data[i]}")
            lexemesTable.update({data[i]:"WHILE_TOKEN"})
        elif data[i]=="for":
            print(f"Token: FOR_TOKEN\nLexeme: {data[i]}")
            lexemesTable.update({data[i]:"FOR_TOKEN"})
        elif data[i] in relops:
            print(f"Token: RELOP\nLexeme: {data[i]}")
            lexemesTable.update({data[i]:"RELOP"})
        elif 'a'<=data[i][0].lower()<='z' and not special_char(data[i]):
            print(f"Token: ID\nLexeme: {data[i]}")
            lexemesTable.update({data[i]:"ID"})
        elif is_int(data[i]):
            print(f"Token: INTEGER\nLexeme: {data[i]}")
            lexemesTable.update({data[i]:"INTEGER"})
        elif is_float(data[i]):
            print(f"Token: FLOAT\nLexeme: {data[i]}")
            lexemesTable.update({data[i]:"FLOAT"})
        else:
            print(f"Token: ERROR\nLexeme: {data[i]}")
        i+=1
    else:
        print("No more lexemes.")
    return


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

while True:
    choice=input("\n\nChoose an option\n1- Call Lex()\n2- Show Symbol Table\n3- Exit\n")
    if choice=='1':
        lex()
    elif choice=='2':
        for key, value in lexemesTable.items():
            print("{:<10} {:<10}".format(key,value))
    elif choice=='3':
        print("Goodbye!")
        exit()