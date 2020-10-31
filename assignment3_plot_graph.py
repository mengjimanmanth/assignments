import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('dataset.csv')

x = df['State']
y = df['Positive']


#Bar chart.
plt.xlabel('state', fontsize=18)
plt.ylabel('positive', fontsize=13)
plt.bar(x, y)

#line graph.
plt.xlabel('state', fontsize=18)
plt.ylabel('positive', fontsize=13)
plt.scatter(x, y)

plt.show()
plt.show()