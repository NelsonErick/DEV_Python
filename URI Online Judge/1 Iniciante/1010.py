x = input()
y = input()

a,b,c = x.split(' ')
d,f,g = y.split(' ')

h = float(b)*float(c)
j = float(f)*float(g)

print ('VALOR A PAGAR: R$ %.2f' %(h+j))
