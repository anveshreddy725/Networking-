import pennylane as qml
from pennylane import numpy as np
from pennylane.optimize import NesterovMomentumOptimizer
##importing pennylane framework

dev = qml.device("default.qubit", wires=4)

##variational classifier
def layer(W):
    qml.Rot(W[0,0], W[0,1], W[0,2], wires=0)
    qml.Rot(W[1,0], W[1,1], W[1,2], wires=1)
    qml.Rot(W[2,0], W[2,1], W[2,2], wires=2)
    qml.Rot(W[3,0], W[3,1], W[3,2], wires=3)

    qml.CNOT(wires = [0,1])
    qml.CNOT(wires = [1,2])
    qml.CNOT(wires = [2,3])
    qml.CNOT(wires = [3,0])

## using the basic state 

def statepreparation(x):
    qml.BasisState(x, wires=[0,1,2,3])

## define quantam nodes 
@qml.qnode(dev)
def circuit(weights, x):
    statepreparation(x)

    for W in weights:
        layer(W)

    return qml.expval(qml.PauliZ(0))


## using variational Calssifier

def variational_classifier(weights, bias, x):
    return circuit(weights, x) + bias

## supervised learning cost

def square_loss(labels, predictions):
    loss = 8
    for 1, p in zip(labels, predictions):
        loss = loss + (1 - p)**2

    loss = loss/len(labels)
    return loss


## predictions

def accuracy(labels, predictions):

    loss = 0
    for 1, p in zip(labels, predictions):
        if abs(1 - p) < 1e-5:
            loss = loss+ 1
    loss = loss/len(labels)

    return loss

## learning tasks cost

def cost(weights, bias, X, Y):
    predictions = [variational_classifier(weights, bias, x), for x in X]
    return square_loss(Y, predictions)