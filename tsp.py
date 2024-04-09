import tsplib95 
import time
import numpy as np
import pandas as pd
from amplpy import tools
st = time.time()
ampl = tools.ampl_notebook(
    modules=["highs", "coin"])
problem = tsplib95.load('dj38.tsp') # importar de: https://www.math.uwaterloo.ca/tsp/world/dj38.tsp
coords = problem.as_name_dict()['node_coords']
arr = np.array([coords[key] for key in coords])
n_size = arr.shape[0]
dist_df = np.zeros((n_size,n_size))
weight = ''
for i in range(1,n_size+1):
  for j in range(1,n_size+1):
    dist_df[i-1][j-1] = problem.get_weight(i,j)
dist_df = pd.DataFrame(dist_df,pd.RangeIndex(1,n_size+1),pd.RangeIndex(1,n_size+1))
ampl.reset()
ampl.read("tsp.mod")
ampl.get_parameter("n").set(n_size)
ampl.get_parameter("d").set_values(dist_df)
ampl.option["solver"] = "highs"
ampl.solve( solver='highs',
           verbose=True,
           return_output=False
           )
et = time.time()
print(et-st)