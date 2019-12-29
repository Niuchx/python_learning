# write a .txt file:

```python
with open('result.txt', 'a') as f:
    for i in range(100):
      f.write(str(i))
      f.write("\n")
f.close()
```

Notes: 'a' appends new things at the end of result.txt. 'w' rewrites the results.txt, which means it will cover the orginal text. 

# display setting
```python
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'  #default, display all information
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  #display warning and error
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  #only display error
```

# How draw figures using matplotlib in Linux terminal without GUI
- Method 1 :adding the following codes：
```python
import matplotlib as mpl
mpl.use('Agg')
from matplotlib.pylot as plt
```
- Method 2 :adding an configuration file at ~/.config/matplotlib/matplotlibrc：
and adding the following line
```
backend : Agg
```
- Using plt.savefig() to save the figure and open it in your vscode.
