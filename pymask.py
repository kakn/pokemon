import numpy as np

data = np.loadtxt('MOCK_DATA.csv', skiprows=1, dtype=int)

mask = data[1:1]
print(mask)
