import math
import numpy as np

def f(x):
    f = math.pow(x,3) + 2*math.pow(x,2) - 3*x - 1
    return f
  
print("-- dada la funcion  math.pow(x,3) + 2*math.pow(x,2) - 3*x - 1")
print("-- y basado en el siguiente input de ejemplo")
print("-- Input de ejemplo: regulaFalsi(1, 2, 0.0004, 100)")
  
def regulaFalsi(a,b,TOL,N):
    i = 1
    FA = f(a)
     
    print("%-20s %-20s %-20s %-20s %-20s" % ("n","x_i","x_u","x_m","f(x_m)"))
      
    while(i <= N):
        p = (a*f(b)-b*f(a))/(f(b) - f(a))
        FP = f(p)
          
        if(FP == 0 or np.abs(f(p)) < TOL):
            break
        else:
             print("%-20.8g %-20.8g %-20.8g %-20.8g %-20.8g\n" % (i, a, b, p, f(p)))
         
          
        i = i + 1
          
        if(FA*FP > 0):
            a = p
        else:
            b = p
      
    return


N = ''
TOL = ''
a = ''
b = ''


while not (a.strip("-").isnumeric()):
	print('indique el punto inferior, parametro poscisional 1')
	a = input()
a = int(a)


while not (b.strip("-").isnumeric()):
	print('indique el punto superior, parametro poscisional 2')
	b = input()
b = int(b)

print('indique la tolerancia, parametro poscisional 3')
TOL = input()
TOL = float(TOL)


while not (N.isnumeric()):
	print('indique el numero maximo de iteraciones, parametro poscisional 4')
	N = input()
N = int(N)







regulaFalsi(a,b,TOL,N)