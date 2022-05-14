from random import randrange
from black import out
import matplotlib.pyplot as plt

nexp = 100e3
outcomes = [7 * randrange(1, 7) - 2 for _ in range(1, int(nexp))]

# print(outcomes)
plt.hist(outcomes, 500)
plt.show()
