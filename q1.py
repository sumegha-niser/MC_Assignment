import matplotlib.pyplot as plt
import numpy as np

#decay simulator : returns the remaining nucleus
def remains_decay(N,a,T):
    rem=[]
    t=0
    while t<T:
        rem.append(N)
        interval=np.random.random(N)
        sum=0
        for i in interval:
            if i>a:
                sum+=1
        N=sum
        t=t+1
    return [range(t),rem]
      

# returns the expected amount of remaining nuclei as per the equation N=N0*e^(-at)
def expected(N,a,T):
    n=[]

    for i in range(T):
        n.append(N*np.exp(-a*i))
    return[range(T),n]
#for a=0.01, N=100,T=300
surv1=remains_decay(100,0.01,300)
ex1=expected(100,0.01,300)   
plt.plot(surv1[0],surv1[1],'.',label = 'numerical t vs N/No ')  

plt.plot(ex1[0],ex1[1],label = 'exact t vs (N/No)' ) 
plt.xlabel('time (t)')
plt.ylabel('N/No (disintegrations per second)')
plt.title("alpha=0.01,N=100 Linear")
plt.legend()
plt.show()

plt.semilogy()
plt.plot(surv1[0],surv1[1],'.',label = 'numerical t vs log(N/No) - Log scale (slope= -$\lambda$)')
plt.title("alpha=0.01,N=100, Log")
plt.semilogy()
plt.plot(ex1[0],ex1[1],label = 'exact t vs log(N/No)') 
plt.xlabel('time (t)')
plt.ylabel('log(N/No) (disintegrations per second)')
plt.legend()
plt.show()


#for a=0.03, N=5000,T=300 
surv2=remains_decay(5000,0.03,300)
ex2=expected(5000,0.03,300)



plt.plot(surv2[0],surv2[1],'.',label = 'numerical t vs N/No ')  

plt.plot(ex2[0],ex2[1],label = 'exact t vs (N/No)'  ) 
plt.xlabel('time (t)')
plt.ylabel('N/No (disintegrations per second)')
plt.title("alpha=0.03,N=5000 Linear")
plt.legend()
plt.show()

plt.semilogy()
plt.plot(surv1[0],surv1[1],'.',label = 'numerical t vs log(N/No) - Log scale (slope= -$\lambda$)')
plt.title("alpha=0.03,N=5000 Log")
plt.semilogy()
plt.plot(ex1[0],ex1[1],label = 'exact t vs log(N/No)' ) 
plt.xlabel('time (t)')
plt.ylabel('log(N/No) (disintegrations per second)')
plt.legend()
plt.show()

