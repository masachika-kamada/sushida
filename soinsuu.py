from time import time

num = 283598282799012588354313727318318100165490374946550831678436461954855068456871761675152071482710347887068874127489
# num = 2*3*5*5*7*11
elements = []
i = 1
start = time()
zeros = 10

while num % 2 == 0:
    elements.append(2)
    print(2)
    num /= 2

i = 3

for i in range(3, int((num ** 0.5) // 1 + 1), 2):
    if num % i == 0:
        elements.append(i)
        print(i)
        num //= i
    else:
        i += 2

    if i > zeros:
        print(zeros)
        zeros *= 10
        print(time() - start)
        start = time()

if num != 1:
    elements.append(num)

print(elements)
