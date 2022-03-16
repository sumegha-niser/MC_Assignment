import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson
#decay simulator: returns the no. of decays per experiment
def decay_sim(N,a,T):                
    N_0=N
    t=0
    while t<T:                               
        prob=np.random.random(N)
        sum=0
        for p in prob:
            if p>(10*a):                   
                sum+=1
        N=sum
        t=t+10
    decays=N_0-N                             
    return decays


#Runs the simulator 1000 times and returns a list containing the no.of decays per iteration, ie performs 1000 experiment and stores the no. of decayed nuclei
def runlist(N,a,T):                         
    decayed=[]
    for i in range(1000):
        decayed.append(decay_sim(N,a,T))   
    return decayed 



#a)
surv1=runlist(500,0.00004,100)
plt.hist(surv1)
avg= np.mean(surv1)
x = np.arange(0,7,1)
y = 1000*poisson.pmf(x, mu =avg)
plt.xlabel("Total decay -100s-->")
plt.ylabel("Repeats-->")
plt.title("alpha=0.00004,N=500")
plt.plot(x,y,label='expected poisson distribution')
plt.legend()
plt.show()

#b)
surv2=runlist(500,0.00002,100)
plt.hist(surv2)
avg = np.mean(surv2)
x = np.arange(0,7,1)
y = 1000*poisson.pmf(x, mu =avg)
plt.xlabel("Total decay -100s-->")
plt.ylabel("Repeats-->")
plt.title("alpha=0.00002,N=500")
plt.plot(x,y,label='expected poisson distribution')
plt.legend()
plt.show()
