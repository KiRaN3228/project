def sdvig(symb, num):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    symb_index = abc.find(symb.lower())
    if symb in '1234567890 .,?"!\'-'' =)+*//':
        return symb
    if symb_index + num > 25:
        if symb.lower() == symb:
            return abc[symb_index + num - 26]
        else:
            return abc[symb_index + num - 26].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index + num]
        else:
            return abc[symb_index + num].upper()
def dlina_slova(st):
    st = "".join(filter(str.isalpha, st))
    return len(st)
def razbivka(name):
    a=name.split('')
    for i in range(len(a)):
        b=dlina_slova(a[i])
        return b
def zadacha(name):
    a=name.split()
    c=''
    for i in range(len(a)):
        c+=' '
        for j in a[i]:
            b=dlina_slova(a[i])
            a1=''.join(a[i][a[i].find(j)])
            b2=''.join(sdvig(j,b))
            c+=j.replace(a1,b2)
            
            
    return c[1:]



name=input()
print(zadacha(name))