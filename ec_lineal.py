# ANDROIDEV 2020
import numpy as np
import pandas as pd

data = pd.read_csv("ejemplo_sistema.csv",header=None)

dataNumpy = pd.DataFrame(data).to_numpy()

ec_var = np.transpose(dataNumpy)[:, :10]
ec_ans = np.transpose(dataNumpy)[:, 10]

if( np.linalg.det(ec_var) == 0 ) :
    print("No es posible obtener el valor")
else:
    print("Es posible encontrar una solución")
    sol = np.linalg.inv(ec_var).dot(ec_ans)
    print("El resultado que satizface la ecuacion es : \n",sol)
    np.savetxt("x.csv", sol, delimiter=",")
