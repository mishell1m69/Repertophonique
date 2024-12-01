import sqlite3


def unique_ID(table):
    """
    Renvoie la plus grande clé primaire + 1 de la table spécifiée.
    
    Args:
        table (str): Le nom de la table dans laquelle rechercher la clé primaire.
    
    Returns:
        int: La plus grande clé primaire existante + 1, ou 1 si la table est vide.
    """

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    request = f"SELECT ID FROM {table}"
    cur.execute(request)
    conn.commit()

    liste2return = cur.fetchall()

    cur.close()
    conn.close()

    return liste2return[-1][0] + 1 if len(liste2return) > 0 else 1


def people_correspondant(data):
    """
    Renvoie les personnes correspondant aux critères donnés.
    
    Args:
        data (list): Liste de valeurs (nom, prénom, profession, date de naissance) avec None pour les champs non spécifiés.
    
    Returns:
        list: Une liste de tuples contenant les informations des personnes correspondant aux critères.
    """

    corep = {0: "nom = ?", 1: "prenom = ?", 2: "profession = ?", 3: "date_de_naissance = ?"}

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    conditions = []
    settings = []

    for i in data:
        if i:
            conditions.append(corep[data.index(i)])
            settings.append(i)

    request = f"SELECT * FROM People WHERE {' AND '.join(conditions)}"
    cur.execute(request, settings)
    conn.commit()

    liste2return = cur.fetchall()

    cur.close()
    conn.close()

    return liste2return


def num_correspondant(ID_num):
    """
    Renvoie les numéros de téléphone correspondant à une personne donnée.
    
    Args:
        ID_num (list): ID des numéros de la personne dont on souhaite récupérer les numéros.
    
    Returns:
        list: Une liste de tuples contenant les numéros de téléphone.
    """

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM Numbers WHERE ID = ?", ID_num)
    conn.commit()

    liste2return = cur.fetchall()

    cur.close()
    conn.close()

    return liste2return


def CHANGE_num(data, column):
    """
    Modifie, ajoute ou supprime un numéro pour une personne existante.
    
    Args:
        data (list): Liste contenant la nouvelle valeur et l'ID de la personne.
        column (str): Le nom de la colonne à modifier.
    """

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    request = f"UPDATE Numbers SET {column} = ? WHERE ID = ?"
    cur.execute(request, data)
    conn.commit()

    cur.close()
    conn.close()


def ADD_people(data_people, data_num):
    """
    Ajoute une nouvelle personne avec un numéro de téléphone.
    
    Args:
        data_people (list): Informations personnelles (nom, prénom, profession, date de naissance).
        data_num (list): Numéros de téléphone (indicatif, mobile, fixe, domicile, travail).
    """

    data_people.insert(0, unique_ID("People"))
    data_people.append(unique_ID("Numbers"))
    data_num.insert(0, unique_ID("Numbers"))

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO People(ID, Nom, Prenom, Profession, Date_de_naissance, ID_link) VALUES(?, ?, ?, ?, ?, ?)", data_people)
    conn.commit()

    cur.execute("INSERT INTO NUMBERS(ID, Indicatif, Mobile, Fixe, Domicile, Travail) VALUES(?, ?, ?, ?, ?, ?)", data_num)
    conn.commit()

    cur.close()
    conn.close()


def CHANGE_people(data, column):
    """
    Modifie, ajoute ou supprime les informations d'une personne.
    
    Args:
        data (list): Liste contenant la nouvelle valeur et l'ID de la personne.
        column (str): Le nom de la colonne à modifier.
    """

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    request = f"UPDATE People SET {column} = ? WHERE ID = ?"
    cur.execute(request, data)
    conn.commit()

    cur.close()
    conn.close()


def delete(ID):
    """
    Supprime une personne et ses numéros associés.
    
    Args:
        ID (list): L'ID de la personne à supprimer.
    """

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    cur.execute("SELECT ID_link FROM People WHERE ID = ?", ID)
    conn.commit()

    IDlink = cur.fetchall()

    cur.execute("DELETE FROM Numbers WHERE ID = ?", IDlink[0])
    conn.commit()

    cur.execute("DELETE FROM People WHERE ID = ?", ID)
    conn.commit()

    cur.close()
    conn.close()
