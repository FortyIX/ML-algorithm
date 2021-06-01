#implmentation of Oja’s learning rule 
# By Fu Zhang 

# 02.06.2021

import numpy as np
from prettytable import PrettyTable

#initial weight
w = np.transpose([-3,0])

#samples
xt = [[1,-2],[3,0],[4,-7],[5,1],[4,2],[3,5]]

#learning rate
n=0.01

printRes = []
res = np.transpose([0.0,0.0]);

for i in range(len(xt)):
    y = np.multiply(w,xt[i])[0]
    delta_w = n * y * (np.transpose(xt[i]) - y * w)
    res += delta_w

    printRes.append(((xt[i]), np.round(y, 4), np.round(delta_w, 4),'--'))


w = w + res

pt = PrettyTable(('Xt', 'y', 'delta_w','w'))

for row in printRes: pt.add_row(row)

pt.align['Xt'] = 'c'
pt.align['y'] = 'l'
pt.align['delta_w'] = 'l'
pt.align['w'] = 'l'

pt.add_row(('','','',''))
pt.add_row(('','','total change',''))
pt.add_row(('','','------','------'))
pt.add_row(('','',res,w))

print(pt)    
