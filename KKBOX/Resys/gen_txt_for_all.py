import numpy as np
import sys
import time
sys.path.append('/home/fearofchou/code/pro_bar')
from mybar import *

pbar = mybar('test:',500)

for i in range(500):
    time.sleep(0.5)
    pbar.update(i)
