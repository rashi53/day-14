Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: C:\python\Python37-32\day13\dis.py ================
0.6164414002968979
>>> 
================= RESTART: C:\python\Python37-32\day13\1.py =================
>>> tr,te=load_split_data(0.6)
>>> len(tr)
81
>>> len(te)
69
>>> tr[0]
[5.1, 3.5, 1.4, 0.2, 'Iris-setosa']
>>> te[0]
[4.9, 3.0, 1.4, 0.2, 'Iris-setosa']
>>> 
================= RESTART: C:\python\Python37-32\day13\1.py =================
>>> tr,te=load_split_data(0.7)
>>> ne=getNeighbors(tr,te[0],3)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ne=getNeighbors(tr,te[0],3)
  File "C:\python\Python37-32\day13\1.py", line 8, in getNeighbors
    dist=euclideanDistance(testInstance,trainingSet[x],length)
NameError: name 'euclideanDistance' is not defined
>>> 
================= RESTART: C:\python\Python37-32\day13\1.py =================
>>> tr,te=load_split_data(0.7)
>>> ne=getNeighbors(tr,te[0],3)
>>> ne
[[5.1, 3.5, 1.4, 0.3, 'Iris-setosa'], [5.1, 3.4, 1.5, 0.2, 'Iris-setosa'], [5.2, 3.4, 1.4, 0.2, 'Iris-setosa']]
>>> ne=getNeighbors(tr,te[0],5)
>>> ne
[[5.1, 3.5, 1.4, 0.3, 'Iris-setosa'], [5.1, 3.4, 1.5, 0.2, 'Iris-setosa'], [5.2, 3.4, 1.4, 0.2, 'Iris-setosa'], [5.0, 3.5, 1.3, 0.3, 'Iris-setosa'], [5.0, 3.4, 1.5, 0.2, 'Iris-setosa']]
>>> 
