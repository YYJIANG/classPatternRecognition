
import numpy as np
from matplotlib import pyplot as plt


def myPCA(X,k):
    row, column = X.shape
    X_norm=X-np.array([np.mean(X[:,i]) for i in range(column)])
    C=np.dot(np.transpose(X_norm),X_norm)/(row-1)
    eigenvalues, eigenvector=np.linalg.eig(C)
    eig= [(eigenvalues[i], eigenvector[:,i]) for i in range(column)]
    eig.sort(reverse=True)
    W=np.array([eig[i][1] for i in range(k)])
    Data=np.dot(X_norm,np.transpose(W))
    

    plt.figure(1)
    ax1=plt.axes(projection='3d')
    ax1.scatter3D(X[:,0],X[:,1],X[:,2])
    plt.show()
    
    plt.figure(2)
    ax1=plt.axes(projection='3d')
    ax1.set_zlim(0,100)
    ax1.scatter3D(X[:,0],X[:,1],X[:,2])
    xx=W[0,1]*W[1,2]-W[0,2]*W[1,1]
    yy=W[1,0]*W[0,2]-W[0,0]*W[1,2]
    zz=W[0,0]*W[1,1]-W[0,1]*W[1,0]
    x=np.arange(-200,200,1)
    y=np.arange(-200,200,1)
    XX,YY=np.meshgrid(x,y)
    ZZ=(-xx*XX-yy*YY)/zz
    ax1.plot_surface(XX,YY,ZZ,color='blue',alpha=0.5) 
    plt.show()
    return Data

Data_raw=np.random.randn(50,3)*100
print(Data_raw)
print(myPCA(Data_raw,2))


    