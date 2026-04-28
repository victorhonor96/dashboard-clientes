import sys
import pandas as pd
import numpy as np

print("Python:", sys.version)
print("Pandas:", pd.__version__)
print("NumPy:", np.__version__)

# teste simples
dados = np.array([1.4, 2.4, 3.7])
print("Média:", dados.mean())