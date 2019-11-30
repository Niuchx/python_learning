# 使用matplotlib.pyplot画图（详细的[请看](https://www.zhihu.com/collection/260736383)）
----
## 一维线图
```
import matplotlib.pyplot as plt 
import numpy as np 

## 1D
x = np.linspace(-1,1,50)
y = 2 * x
plt.plot(x, y, color = 'red',linewidth = 3.0,linestyle = '--')
plt.xlabel('the variable $x$', size = 10)
plt.ylabel('the function $y$', size = 10)
plt.title('1D line', loc = 'center')
plt.xlim((-1,2))   #更改在图表上显示x的取值范围
plt.ylim((-2,2))  #更改在图表上显示y的取值范围

# 把坐标值换成不同的单位
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1,0,1,2],[r'$really\ bad$',r'$b$',r'$c\ \alpha$',r'$d$',r'$good$']) #在对应坐标处更换名称

plt.show()

## Fugure
y1 = x ** 2 
y2 = x * 2
#这个是第一个figure对象,下面的内容都会在第一个figure中显示
plt.figure()
plt.plot(x,y1)
#这里第二个figure对象, num 可以指定窗口，figsize指定窗口大小
plt.figure(num = 3, figsize = (10,5))
plt.plot(x,y2)
# plt.show()

```
