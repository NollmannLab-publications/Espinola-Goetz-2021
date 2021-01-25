# *Cis*-regulatory chromatin loops arise before TADs and gene activation, and are independent of cell fate during early Drosophila development


Sergio Martin Espinola[^co-authors], Markus Götz[^co-authors], Maelle Bellec, Olivier Messina, Jean-Bernard Fiche, Christophe Houbron, Matthieu Dejean, Ingolf Reim, Andrés M. Cardozo Gizzi, Mounia Lagha[^co-corresponding], Marcelo Nollmann[^co-corresponding]. 



## Data

Data from this paper is included in the /data folder.

Datasets are provided as Numpy arrays. They can be easily loaded and displayed in python as follows (example):

```python
import numpy as np
import matplotlib.pylab as plt

matrix = np.load("F1/Fig1f.npy")

fig, ax1 = plt.subplots()
fig.set_size_inches((10, 10))

plt.imshow(matrix, cmap="coolwarm",vmin=0,vmax=0.6)
plt.savefig("Fig1f.png")
```



## Code

Code used for the acquisition and analysis of HiM data are included in the /code folder.

