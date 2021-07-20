import numpy as np
import random as rd 
import matplotlib.pyplot as plt
import time  
import Ratio 

class trayectoria() :
    def __init__(self,num_steps,dim):
        self.num_steps=num_steps+1
        self.Co=[]
        self.dimension=dim
    def caminar(self):
        for h in range(self.dimension):
            self.Co.append([0])
        for s in range(1,self.num_steps):
            for h in range(self.dimension):
                self.Co[h].append(self.Co[h][s-1]+(-1)**rd.randint(1, 2))
        for h in range(self.dimension):
            self.Co[h].pop(0)
        return np.array(self.Co)
  
   
"--------------emoezamos a crear las trayectorias--------------------------"
dim=3   #Dimensiones de la caminata
trayectorias_num=1000
max_steps=1000    #numero de pasos maximo
inc=100 #interval de pasos; tiene que ser un divisor de mzx_steps
tiempo=[]
radio_final=[]
for num_steps in range(inc,max_steps+1,inc): 
    inicio=time.time()
    radios=np.zeros((trayectorias_num,))  
    for i in range(trayectorias_num):
        radios[i]=(Ratio.radio(trayectoria(num_steps,dim).caminar(),dim,num_steps))
    radio_final.append(np.mean(radios))
    tiempo.append(time.time()-inicio)
    

    
"-----------------imprimimos los radios -----------------------------------"
print("\n","------Lista de los promedios obtenidos para distintos numeros de pasos. ",dim," Dimensiones-------")
print("\n")
print("Num Pasos","      Radio Promedio        Tiempo de calculo (s)")
for i in range(len(radio_final)):
    print("  ",(i+1)*inc,"    |    ",radio_final[i],"   |   ",tiempo[i])

fig, (ax1, ax2) = plt.subplots(1, 2)
u = str(trayectorias_num)+" caminatas en "+str(dim)+" dimensiones"
fig.suptitle(u,size=25)
ax1.plot(np.arange(inc,max_steps+1,inc),radio_final,linewidth=5)
ax1.set_xlabel("Numero de pasos",size=15)  
ax1.set_ylabel("Radio de giro promedio",size=15)
ax2.plot(np.linspace(inc,max_steps,int(max_steps/inc)),tiempo,color="green",linewidth=5)
ax2.set_ylabel("Tiempo de calculo",size=15)
ax2.set_xlabel("Numero de pasos",size=15)

plt.show()
     
 
    
