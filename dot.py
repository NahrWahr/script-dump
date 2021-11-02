import math
import statistics

def energy(wvlen):
    h = 6.62607004e-34
    c = 3e8

    return ((h*c)/wvlen)

def radi(E,n):
    effmass=((1/me)+(1/mh))
    print(effmass)
    rsquare= ((hbar*n*pi)**2 * effmass)/(2*(E-Ebandgap))
    return(math.sqrt(rsquare))

Ebandgap=2.15e-19
pi=3.141
h = 6.62607004e-34
c = 3e8
me=7.29e-32
mh=5.47e-31
hbar=h/(2*pi)


wvlen = [528
         ,539
         ,590
         ,617]

vialen=list()
for i in wvlen:
    vialen.append(energy(i*1e-9))


dotrad=list()
for i in vialen:
    dotrad.append(radi(i,1))

print(vialen)
print(dotrad)
