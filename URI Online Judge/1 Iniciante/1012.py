x = input()
a,b,c = x.split(' ')
a,b,c = float(a),float(b),float(c)
tri = (a*c) / 2
cir = 3.14159 * (c**2)
tra = ((a + b) * c) / 2
qua = b*b
ret = a*b

print('TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f' %(tri, cir, tra, qua, ret))
