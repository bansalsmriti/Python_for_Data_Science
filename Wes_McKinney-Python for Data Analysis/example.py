import pandas as pd
import numpy as np
frame=pd.DataFrame(np.arange(12).reshape((4,3)),columns=['a','b','c'],index=['w','x','y','z'])
f=lambda x: x.max()-x.min()
print(frame.apply(f))