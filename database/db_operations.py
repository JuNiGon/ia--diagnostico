import sqlite3

def conectar():
    return sqlite3.connect('diagnostico.db') 
def buscar_doencas_por_sintomas(sintomas):
    conn = conectar()
    cursor = conn.cursor()

    placeholders = ', '.join('?' for _ in sintomas)
    query = f"""
        SELECT d.nome, d.descricao, SUM(ds.peso) AS relevancia
        FROM Doencas d
        JOIN Doenca_Sintoma ds ON d.id = ds.doenca_id
        JOIN Sintomas s ON s.id = ds.sintoma_id
        WHERE s.nome IN ({placeholders})
        GROUP BY d.nome
        ORDER BY relevancia DESC;
    """
    cursor.execute(query, sintomas)
    resultados = cursor.fetchall()
    conn.close()
    return resultados
