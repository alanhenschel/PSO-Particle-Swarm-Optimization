
# coding: utf-8

# In[1]:


import numpy as np
import random
import math

# In[2]:


def inicializa_particula(n):
    enxame = np.zeros((n,2))
    return enxame


# In[3]:


class melhor_enxame:
    valor = [0.0,0.0]


# In[4]:


def p_posicao(dimensao):
    p = []
    for i in range(dimensao):
        p.insert(i,np.random.uniform(-10,10))
    
    return p


# In[5]:


def p_velocidade(n):
    
    v = []
    
    for i in range(n):
        v.insert(i,random.uniform(-20,20))
    return v


# In[6]:


def memoria_local(tamanho):
    
    p = np.zeros((tamanho,2))
    p = list(p)
    del p[:]
    return p
    


# In[7]:


def fitness(particula):
    x1 = particula[0]
    x2 = particula[1]
    term1 = (math.sin(3*math.pi*x1))**2
    term2 = (x1-1)**2 * (1+(math.sin(3*math.pi*x2))**2)
    term3 = (x2-1)**2 * (1+(math.sin(2*math.pi*x2))**2)
    y = term1 + term2 + term3
    return y


# In[8]:


def pso(dimensao,tamanho):
    populacao = list(inicializa_particula(tamanho))
    p = memoria_local(tamanho)
    v = [None] * tamanho
    for i in range(tamanho):
        populacao[i] = list(np.copy(p_posicao(dimensao)))
        p.append(populacao[i])
        
        if (fitness(populacao[i]) < fitness(melhor_enxame.valor)):
            melhor_enxame.valor= list(np.copy(populacao[i]))
        
        v[i] = list(np.copy(p_velocidade(dimensao)))
        
    iteracoes = 0
    w = 0.729
    fi = 1.0
    fi2= 1.0
    r1 = random.uniform(0,1)
    r2 = random.uniform(0,1)
    

    while iteracoes <=100:
        for i in range(tamanho):
            v[i][0] = w*v[i][0]+fi*r1*(p[i][0]-populacao[i][0])+fi2*r2*(melhor_enxame.valor[0]-populacao[i][0])
            v[i][1] = w*v[i][0]+fi*r1*(p[i][1]-populacao[i][1])+fi2*r2*(melhor_enxame.valor[1]-populacao[i][1])
            populacao[i][0] = populacao[i][0] + v[i][0]
            populacao[i][1] = populacao[i][1] + v[i][1]
            
            if(fitness(populacao[i]) < fitness(p[i])):
                p[i] = list(np.copy(populacao[i]))
            if(fitness(populacao[i]) < fitness(melhor_enxame.valor)):
                melhor_enxame.valor = list(np.copy(populacao[i]))
        print("\nenxame:{}\n".format(populacao))
        print("\n Melhor do enxame local:{}\n".format(p))
        print("\n melhor global:{}\n".format(melhor_enxame.valor))
        print("\n melhor global na funcao:{}\n".format(fitness(melhor_enxame.valor)))
        iteracoes+=1
            


# In[9]:


pso(2,100)

