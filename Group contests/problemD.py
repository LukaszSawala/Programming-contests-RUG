n = int(input())
nbin = bin(n)
coeff = 0
for i in nbin[2:]:
    if int(i) == 1:
        coeff +=1
print(2**coeff)