# LINEAR EQUATION SYSTEM WITH MATRIX 

BY ANDROIDEV on python 2020 

## 🧰 RESOURCES



First we have an **Excel file that contains our data**, which have to be solved by our method

![alt text](Captura de pantalla 2020-09-17 163211.jpg "HOLA")

**What we have here ?**



![Captura de pantalla 2020-09-17 163011](.\Captura de pantalla 2020-09-17 163011.jpg)

Each colum represent an equation, the blue sections are the coeficents  **(v)**

![Captura de pantalla 2020-09-17 163035](.\Captura de pantalla 2020-09-17 163035.jpg)

And in the bottom we have the result of this linear equation **(ans)**

![Captura de pantalla 2020-09-17 163100](.\Captura de pantalla 2020-09-17 163100.jpg)



## 🏆 GOAL



We have to find all the variables and each term that accomplish the equation logic.



## 📖 MATH APPROACH



The system is a operation of matrices that contains all the equations :

$$ {De la forma }
A * 𝑥 = Y
$$

Where the matrices are:

$$
A = 
\begin{pmatrix}
v_{0,0} & ... & v_{0,10} \\
... & ... & ... \\
... & ... & v_{10,10}
\end{pmatrix}
$$


$$
Y = 
\begin{pmatrix}
ans_{0}\\
...  \\
ans_{10} 
\end{pmatrix}
$$

**For our goal we find out this:**
$$
x = Y * A^{-1}
$$



