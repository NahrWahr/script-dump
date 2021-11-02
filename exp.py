delV=0.01
delI=0.01

Vm=2.16
Vo=2.85
Im=4.69
Is=7.14
FF=(Im/Is * Vm/Vo)
print(FF)

delFF= FF* (delV/Vm + delV/Vo + delI/Im + delI/Is)
print(delFF)
