import numpy as np
import math

class NeuralNetwork():

    def __init__(self, layer_sizes):
        # TODO : DONE
        # layer_sizes example: [4, 10, 2]
        self.inputLayer1Weights = self.randInitializeWeights(layer_sizes[1], layer_sizes[0])
        self.layer2OutputWeights = self.randInitializeWeights(layer_sizes[2], layer_sizes[1])
        self.bias1 = np.zeros((layer_sizes[1], 1))
        self.bias2 = np.zeros((layer_sizes[2], 1))

        #just for remembering a simple thing ;-)
        self.sizes = layer_sizes

        self.activation_v = np.vectorize(self.activation)

    def activation(self, x):
        # TODO : DONE
        return 1 / (1 + math.exp(-x))

    def forward(self, x):
        
        # TODO : DONE
        # x example: np.array([[0.1], [0.2], [0.3]])

        inputsOfFirstLayer = self.inputLayer1Weights.dot(x)
        out1 = np.add(inputsOfFirstLayer, self.bias1)
        sout1 = self.activation_v(out1)

        inputsOfThirdLayer = self.layer2OutputWeights.dot(sout1)
        out2 = np.add(inputsOfThirdLayer, self.bias2)
        sout2 = self.activation_v(out2)

        return sout2

    def randInitializeWeights(self, L_in, L_out):
        #print("normal")
        #print(np.random.normal(0, 1, (L_in, L_out)))
        #print(" ")
        #print("random")
        #print(np.random.random((L_in, L_out)) - 0.5)
        return np.random.normal(0, 1, (L_in, L_out))
        #return np.random.random((L_in, L_out))-0.5
