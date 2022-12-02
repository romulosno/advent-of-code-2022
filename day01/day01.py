file1 = open('input01', 'r')
Lines = file1.readlines()
totais = []

count = 0
for line in Lines:
    if line.strip() == "":
        totais.insert(count, 0)
        count = count + 1
    else:
        totalAtual = totais[count-1]
        totais.insert(count-1, totalAtual+int(line.strip()))

totais.sort(reverse=True)
print(totais[0])
print(totais[0]+totais[1]+totais[2])
