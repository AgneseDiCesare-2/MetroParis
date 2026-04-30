import time

from model.fermata import Fermata
from model.model import Model

model=Model()
print("Numero Nodi: ", (model.get_numnodi()))
print("Numero Archi: ", (model.get_numarchi()))
model.buildGraph()
time1=time.time()
#model.addedges() #è un metodo molto lento
model.addedges2() #molto meglio
time2=time.time()

tempo_impiegato=time2-time1
print("Numero Nodi: ", (model.get_numnodi()))
print("Numero Archi: ", (model.get_numarchi()))
print(f"Tempo impiegato: {tempo_impiegato}")

source=Fermata(2, "Abbesses", 2.33855, 48.8843)

nodiBFS=model.get_BFSNodesFromEdges(source)
nodiDFS=model.get_DFSNodesFromEdges(source)

print(nodiBFS[:10])
print(nodiDFS[:10])


