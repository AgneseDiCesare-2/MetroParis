from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.fermata import Fermata


class DAO():

    @staticmethod
    def getAllFermate():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM fermata"
        cursor.execute(query)

        for row in cursor:
            result.append(Fermata(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def hasconn(u: Fermata, v: Fermata) -> bool:
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from connessione c 
                    where c.id_stazP = %s and c.id_stazA =%s"""
        cursor.execute(query, (u.id_fermata, v.id_fermata)) #NB!

        for row in cursor:
            result.append(Connessione(**row))
        cursor.close()
        conn.close()
        return len(result) > 0 #booleano

    #restituisce l'elenco delle fermate che partono da u
    @staticmethod
    def getVicini(u: Fermata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * 
                FROM connessione c
                Where c.id_stazP = %s """
        cursor.execute(query, (u.id_fermata,))

        for row in cursor:
            result.append(Connessione(**row)) #restituisce gli archi che partono dal quel nodo
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM connessione c "
        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(**row))
        cursor.close()
        conn.close()
        return result