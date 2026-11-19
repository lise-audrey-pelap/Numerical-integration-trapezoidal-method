import numpy as np
import matplotlib.pyplot as plt
import math

try:  
    a= float(input("Entrer la  borne inférieur d'intégration \n"))
    b= float(input("Entrer la borene supérieur d'intédration \n"))
    n= int(input("entrer le nombre de point de votre calcul \n"))
except ValueError:
    print('Veuiller entrer une valeur conforme')
    
# Initialisation de la fonction
pas=0.000001
z= np.arange(a,b+pas,pas)
t= 1/(1+z**2)

h= (b-a)/n

#Calcul de l'erreur
derive1 =np.gradient(t,z)
derive2 =np.gradient(derive1,z)
positive =np.abs(derive2)
maximum =np.max(positive)
erreur=((b-a)*(h**2)*maximum)/12

#calcul de l'intégrale
x=np.arange(a,b+h,h)
y= 1/(1+x**2)
som= np.sum(y[1:n])
integrale= (h/2)*(y[0]+y[n]+2*som)
integralexact= np.pi/4
erreurrelative= (integralexact-integrale)/integralexact

#Tracé des formules
plt.subplot(1,2,2)
plt.plot(z,t)
plt.plot(x,y,"o-")
plt.title('$y=1/(1+x^2)$')
plt.xlabel('x')
plt.ylabel('y')
plt.subplot(1,2,1)
plt.plot(z,derive2,"g")
plt.title('dérivé seconde')
plt.grid(True)
plt.show()

print(f"L'intégrale de cette fonction de {a} à {b} est {integrale} avec une erreur d'interpolation de -{erreur},\n  l'acart relatif est {erreurrelative}")
