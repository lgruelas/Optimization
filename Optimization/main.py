from pyoptclass import utils as utl
from pyoptclass import pso

data = utl.getData(file_path="./../assets/sprint7ToroideMixto.csv")
pso = pso.PSO(data, 3)
print(pso.search())

