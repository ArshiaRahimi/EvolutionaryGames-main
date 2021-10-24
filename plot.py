import matplotlib.pyplot as plt


with open('.\plot\data.txt') as f:
    lines = f.readlines()
    maximum = [int(line.split()[0]) for line in lines]
    minimum = [int(line.split()[1]) for line in lines]
    average = [int(float(line.split()[2])) for line in lines]


plt.plot(range(len(maximum)), maximum, label="maximum")
plt.plot(range(len(minimum)), minimum, label="minimum")
plt.plot(range(len(average)), average, label="average")
plt.legend()
plt.show()