import numpy as np
import healpy as hp
import matplotlib.pyplot as plt


def criarImg(bl_test,i):
    ell = np.arange(len(bl_test))
    plt.clf()
    plt.rcParams['figure.figsize'] = (12,8)
    plt.xlabel('$\ell$')
    plt.ylabel('$B_\ell$')
    plt.plot(ell, bl_test)
    nome= 'Biparalell'+ str(i)+'.png'
    plt.savefig(nome)    

    print "plot", i
    plt.clf()
    plt.rcParams['figure.figsize'] = (12,8) 
    plt.xlabel('$\ell$')
    plt.ylabel('$B_\ell$')
    plt.plot(ell, bl_test)
    plt.xscale('log')
    nome2= 'Biparallel_log'+ str(i)+'.png'
    plt.savefig(nome2)
    print "plot - log", i


def salvarIMG(arqIn,nrLoopStart,nrLoopEnd):
        for i in range(nrLoopStart,nrLoopEnd):
            B_elltotal=np.loadtxt(arqIn+str(i)+".txt")
            criarImg(B_elltotal,i)
        
        