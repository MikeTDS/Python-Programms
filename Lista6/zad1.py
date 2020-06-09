import random
import numpy as np

def sigmoid(x):
    return 1.0/(1 + np.exp(-x))

def sigmoid_derivative(x):
    return x*(1.0-x)

def ReLU(x):
    return x * (x>0)

def ReLU_derivative(x):
    return 1.0 * (x>0)

def ReLU_derivative(x):
    return np.array([[0.0 if j<0.0 else 1 for j in i] for i in x])

class NeuralNetwork:
    def __init__(self, x, y, f1, f2, df1, df2, eta):
        self.f1 = f1
        self.f2 = f2
        self.df1 = df1
        self.df2 = df2
        self.input = x
        self.w1 = np.random.rand(4,self.input.shape[1])
        self.w2 = np.random.rand(1,4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = eta
    
    def feedforward(self):
        self.layer1 = self.f1(np.dot(self.input, self.w1.T))
        self.output = self.f2(np.dot(self.layer1, self.w2.T))
    
    def backprop(self):
        delta2 = (self.y - self.output) * self.df2(self.output)
        d_w2 = self.eta * np.dot(delta2.T, self.layer1)

        delta1 = self.df1(self.layer1) * np.dot(delta2, self.w2)
        d_w1 = self.eta * np.dot(delta1.T, self.input)

        self.w1 += d_w1
        self.w2 += d_w2

def main():
    np.set_printoptions(precision=3, suppress=True)
    X = np.array([[0,0,1],
                  [0,1,1],
                  [1,0,1],
                  [1,1,1]])
    funcs = ['XOR [0,1,1,0]', 'AND [0,0,0,1]', 'OR [0,1,1,1]'] #funkcja + oczekiwane wartości
    Ys = [np.array([[0],[1],[1],[0]]),
        np.array([[0],[0],[0],[1]]),
        np.array([[0],[1],[1],[1]])]
    for i in range(len(funcs)):
        y = Ys[i]
        print(funcs[i])
        print('2 x Sigmoid, eta = 0.5')
        nn = NeuralNetwork(X,y,sigmoid,sigmoid,sigmoid_derivative,sigmoid_derivative,0.5)
        for i in range(5000):
            nn.feedforward()
            nn.backprop()
        print(nn.output)
        print()

        print('2 x Relu, eta = 0.05')
        nn = NeuralNetwork(X,y,ReLU,ReLU,ReLU_derivative,ReLU_derivative,0.05)
        for i in range(5000):
            nn.feedforward()
            nn.backprop()
        print(nn.output)
        print()

        print('Sigmoid + Relu, eta = 0.5')
        nn = NeuralNetwork(X,y,sigmoid,ReLU,sigmoid_derivative,ReLU_derivative,0.5)
        for i in range(5000):
            nn.feedforward()
            nn.backprop()
        print(nn.output)
        print()
        
        print('Relu + Sigmoid, eta = 0.01')
        nn = NeuralNetwork(X,y,ReLU,sigmoid,ReLU_derivative,sigmoid_derivative,0.01)
        for i in range(5000):
            nn.feedforward()
            nn.backprop()
        print(nn.output)
        print('---------------')
    print('Najlepsze wyniki dla XOR daje Sigmoid + Relu oraz 2 x Sigmoid. \
        Samo Relu oraz Relu + Sigmoid nie dają zadowalających wyników. \
        Dla odpowiednio dobranego parametru eta wszyskie funkcje dają \
        sensowne wyniki dla AND. Dla OR Relu + Sigmoid daje najgorsze wyniki.')

if __name__ == "__main__":
    main()

#kolumna z jedynkami pozwala na uzyskanie lepszych wyników, ponieważ stanowi
#dodatkowy wyraz wolny, dzięki czemu wyliczone w macierzy wartości można
#modyfikować o dodatkową stałą