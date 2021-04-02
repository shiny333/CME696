import numpy as np
import matplotlib.pyplot as plt

n = 15
t = 100
rate = 0.9
a = np.random.randint(100, size=(n, n))


def distance(cities):
    distance = 0
    for i in range(n - 1):
        distance = distance + a[cities[i], cities[i + 1]]
    distance = distance + a[cities[n - 1], 0]
    return distance


city = np.arange(0, n)
ccity = city.copy()


def rando(x):
    index3 = np.random.randint(x)
    index4 = np.random.randint(x)
    while index3 == index4:
        index3 = np.random.randint(x)
        index4 = np.random.randint(x)
    return index3, index4


shodis = distance(ccity)
result = np.array([shodis])
while t > 1:
    i = 0
    while i < 500:
        index1, index2 = rando(n)
        ccity[index1], ccity[index2] = ccity[index2], ccity[index1]

        if distance(ccity) < distance(city):
            city = ccity.copy()
        elif distance(ccity) > distance(city):
            if np.random.random() < np.exp((distance(city) - distance(ccity)) / t):
                city = ccity.copy()
        shodis = distance(city)
        result = np.append(result, shodis)
        i += 1
    t = t * rate
print("distance array", a, shodis)
print("shortest distance", shodis)
print("shortest path", city)

# ###envolve of the whole distance
# plt.subplot(1, 1, 1)
# x = np.arange(0, len(result), 1)
# plt.plot(x, result)

##### draw the figure of the path
city = list(city)
city_x = city.copy()
city_y = city.copy()
city_y.append(city[0])
city_y.pop(0)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
x = np.arange(0, n, 1)
y = np.arange(0, n, 1)
x, y = np.meshgrid(x, y)
z = a[x, y]
ax.scatter(x, y, z, c=np.linalg.norm([x, y, z], axis=0))
ax.plot(city_x, city_y, a[city_x, city_y])
plt.show()
