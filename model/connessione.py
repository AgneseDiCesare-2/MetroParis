from dataclasses import dataclass


@dataclass
class Connessione:
    id_connessione: int
    id_linea: int
    id_stazP: int
    id_stazA: int
    #tabella --> proprietà --> copia le righe e incollale

    def __hash__(self):
        return hash(self.id_connessione)
