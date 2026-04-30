from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._idMapFermate = {} #salvo le fermate in un dizionario cosi le trovo velocemente con l'id
        #{id_fermata: Fermata}
        self._grafo = nx.DiGraph() #grafo pesato
        self._fermate = DAO.getAllFermate() #restituisce tutte le Fermate

        for fermate in self._fermate:
            self._idMapFermate[fermate.id_fermata] = fermate #per mappare chiave primaria e oggetto

    def buildGraph(self):
        self._grafo.clear() #svuoto il grafo
        self._grafo.add_nodes_from(self._fermate) #aggiungo tutti i nodi
        self.addeges3() #uso il modo più veloce (tanti nodi)

    @property
    def fermate(self):
        return self._fermate

    def get_numnodi(self):
        return len(self._grafo.nodes)

    def get_numarchi(self):
        return len(self._grafo.edges)

    #doppio loop --> molto lento, usala solo per grafi piccoli
    def addedges(self): #giusto ma lungo --> perdi tanto tempo
        for u in self._fermate: #u  e v sono oggetti Fermata
            for v in self._fermate:
                if DAO.hasconn(u,v): #controllo ogni coppia possibile
                    self._grafo.add_edge(u, v)

    #singolo loop
    def addedges2(self): #più efficiente
        self._grafo.clear_edges()
        for u in self._fermate: #u è il nodo da cui l'arco/connessione parte (uscente)
            for conn in DAO.getVicini(u): #mi da l'elenco dei vicini (archi/connessioni)
                v=self._idMapFermate[conn.id_stazA] #v è la Fermata di arrivo della connessione (entrante)
                self._grafo.add_edge(u, v) #aggiungo l'arco tra i due

    #anche questo più efficiente
    def addeges3(self):
        self._grafo.clear_edges()
        alledges=DAO.getAllEdges()
        for conn in alledges:
            u=self._idMapFermate[conn.id_stazP]
            v=self._idMapFermate[conn.id_stazA]
            self._grafo.add_edge(u, v)

    #a questo punto ho creato i nodi e gli archi
    #posso implementare calcola raggiungibili

    def calcola_raggiungibili(self, partenza):
        lista_raggiungibili=[] #ci metto le fermate
        for vicino in self._grafo[partenza]: #modo per accedere ai vicini
            lista_raggiungibili.append(vicino)
        return lista_raggiungibili

    #4 esplorazioni equivalenti!!! cambia il tipo o l'output
    #vedremo come scegliere quello più conveniente

    #visita BFS, per livelli
    def get_BFSNodesFromEdges(self, source):
        res=[]
        archi=nx.bfs_edges(self._grafo, source) #lista di tuple
        for u,v in archi:
            res.append(v) #ne prendo uno, visto che poi l'altro lo prenderò alla prox iterazione
        return res

    def get_DFSNodesFromEdges(self, source):
        res=[]
        archi=nx.dfs_edges(self._grafo, source) #lista di tuple
        for u,v in archi:
            res.append(v) #ne prendo uno, visto che poi l'altro lo prenderò alla prox iterazione
        return res

    #oppure
    def getBFSNodesFromTree(self, source):
        tree=nx.bfs_tree(self._grafo, source)
        archi=list(tree.edges())
        nodi=list(tree.nodes())
        return nodi

    def getDFSNodesFromTree(self, source):
        tree=nx.dfs_tree(self._grafo, source)
        archi=list(tree.edges())
        nodi=list(tree.nodes())
        return nodi



