import matplotlib.pyplot as plt

def adder(input):
    input = input + 1
    return input
empty = []
initial = 0
for i in range(10):
    plotter = adder(initial)
    empty.append(plotter)
    initial = plotter
xs = [x for x in range(len(empty))]

plt.plot(xs, empty)
plt.show()
plt.close()