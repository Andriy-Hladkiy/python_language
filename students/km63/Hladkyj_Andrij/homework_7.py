#task1------------------------------------------------------------
"""
Iaeaeoa eiaaenu ia?aiai aoi?aaiey iaeneiaeuiiai yeaiaioa. Auaaaeoa aaa ?enea: iiia? no?iee e iiia? noieaoa, 
a eioi?uo noieo iaeaieuoee yeaiaio a aaoia?iii ianneaa. Anee oaeeo yeaiaioia ianeieuei, oi auaiaeony oio, 
o eioi?iai iaiuoa iiia? no?iee, a anee iiia?a no?ie ?aaiu oi oio, o eioi?iai iaiuoa iiia? noieaoa.
I?ia?aiia iieo?aao ia aoia ?acia?u ianneaa n e m, caoai n no?ie ii m ?enae a ea?aie. 
"""
size = input().split()
a=int(size[0])
b=int(size[1])
matrix = []
for i in range(a):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    matrix.append(row)
for i in range(a):
    for j in range(b):
        if (i==0) and (j==0):
            x=i
            y=j
            maxim = matrix[0][0] 
        elif matrix[i][j] > maxim:
            x=i
            y=j
            maxim=matrix[i][j]
print (x, y, end=' ')
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Aaii ia?aoiia ?enei n. Nicaaeoa aaoia?iue iannea ec n?n yeaiaioia, caiieiea aai neiaieaie "." 
(ea?aue yeaiaio ianneaa yaeyaony no?ieie ec iaiiai neiaiea). Caoai caiieieoa neiaieaie "*" n?aai?? no?ieo ianneaa, 
n?aaiee noieaao ianneaa, aeaaio? aeaaiiaeu e iiai?io? aeaaiiaeu. A ?acoeuoaoa aaeieou a ianneaa aie?iu ia?aciauaaou
ecia?a?aiea caacai?ee. Auaaaeoa iieo?aiiue iannea ia ye?ai, ?acaaeyy yeaiaiou ianneaa i?iaaeaie. 
"""
size=int(input())
matrix = []
matrix = ['.'] * size
for i in range(size):
    matrix[i] = ['.'] * size
for i in range(size):
    for j in range(size):
        if i==j:
            matrix[i][j] = '*' 
        elif (size-j) == (i+1):
            matrix[i][j] = '*'
        if size//2 == j:
            matrix[i][j] = '*'
        if size//2 == i:
            matrix[i][j] = '*'
for i in range(size):
    for j in range(size):
        print(matrix[i][j], end=' ')
    print() 
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Aaiu aaa ?enea n e m. Nicaaeoa aaoia?iue iannea ?acia?ii n?m e caiieieoa aai neiaieaie "." e "*" 
a oaoiaoiii ii?yaea. A eaaii aa?oiai oaeo aie?ia noiyou oi?ea.

"""
size = input().split()
a=int(size[0])
b=int(size[1])
matrix = ['.'] * a
for i in range(a):
    matrix[i] = ['.'] * b
for i in range(a):
    for j in range(b):
        if (i+j)%2 == 1:
            matrix[i][j] = '*'
for i in range(a):
    for j in range(b):
        print(matrix[i][j], end=' ')
    print()
#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Aaii ?enei n. Nicaaeoa iannea ?acia?ii n?n e caiieieoa aai ii neaao?uaio i?aaeeo. Ia aeaaiie aeaaiiaee aie?iu auou caienaiu ?enea 0. 
Ia aaoo aeaaiiaeyo, i?eeaaa?ueo e aeaaiie, ?enea 1. Ia neaao?ueo aaoo aeaaiiaeyo ?enea 2, e o.a. 
"""
size = int(input())
matrix = [0] * size
for i in range(size):
    matrix[i] = [0] * size
for k in range(1, size):
    for i in range(size-k):
        for j in range(size-k):
            if i == j:
                matrix[i][j+k] = k
                matrix[i+k][j] = k
for i in range(size):
    for j in range(size):
        print(matrix[i][j], end=' ')
    print()
print_elements(even_elements(input_elements()))
#-----------------------------------------------------------------

#task5------------------------------------------------------------------------------------------------------------------------
"""
Aaii ?enei n. Nicaaeoa iannea ?acia?ii n?n e caiieieoa aai ii neaao?uaio i?aaeeo:
?enea ia aeaaiiaee, eaouae ec i?aaiai aa?oiaai a eaaue ie?iee oaie ?aaiu 1.
?enea, noiyuea auoa yoie aeaaiiaee, ?aaiu 0.
?enea, noiyuea ie?a yoie aeaaiiaee, ?aaiu 2.
Iieo?aiiue iannea auaaaeoa ia ye?ai. ?enea a no?iea ?acaaeyeoa iaiei i?iaaeii. 
"""
size = int(input())
matrix = [0] * size
for i in range(size):
    matrix[i] = [0] * (size-i-1) + [1] + [2] * i
for i in range(size):
    for j in range(size):
        print(matrix[i][j], end=' ')
    print() 
#-----------------------------------------------------------------

#task6------------------------------------------------------------
"""
Aai aaoia?iue iannea e aaa ?enea: i e j. Iiiaiyeoa a ianneaa noieaou n iiia?aie i e j e auaaaeoa ?acoeuoao.
I?ia?aiia iieo?aao ia aoia ?acia?u ianneaa n e m, caoai yeaiaiou ianneaa, caoai ?enea i e j.
?aoaiea ioi?ieoa a aeaa ooieoee swap_columns(a, i, j). 
"""
def swap_columns(matrix, i, j):
    for z in range (a):
        buf=matrix[z][i]
        matrix[z][i]=matrix[z][j]
        matrix[z][j]=buf
    return
size = input().split()
a=int(size[0])
b=int(size[1])
matrix = []
for k in range(a):
    row = input().split()
    for k in range(len(row)):
        row[k] = int(row[k])
    matrix.append(row)
size = input().split()
i=int(size[0])
j=int(size[1])
swap_columns(matrix, i, j)
for i in range(a):
    for j in range(b):
        print(matrix[i][j], end=' ')
    print()
#----------------------------------------------------------------- 