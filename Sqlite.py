import sqlite3



#Renvoi la plus grande clé primaire + 1 de la table

def unique_ID(table):

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    request=f"SELECT ID FROM {table}"

    cur.execute(request)
    conn.commit()

    liste2return=cur.fetchall()

    cur.close()
    conn.close()

    return liste2return[-1][0] + 1

#Renvoi les personnes qui correspondent aux infos

def people_correspondant(data):

    corep={0:"nom = ?", 1:"prenom = ?",2:"profession = ?" , 3:"date_de_naissance = ?"}

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()
    
    conditions=[]
    settings=[]

    for i in data:
        if i:
            conditions.append(corep[data.index(i)])
            settings.append(i)

    request=f"SELECT * FROM People WHERE {' AND '.join(conditions)}"

    cur.execute(request, settings)
    conn.commit()

    liste2return=cur.fetchall()

    cur.close()
    conn.close()

    return liste2return
#Renvoi les numéros de téléphones correspondant à une personne

def num_correspondant(ID_num):

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM Numbers WHERE ID = ?", ID_num)
    conn.commit()
    
    liste2return=cur.fetchall()

    cur.close()
    conn.close()

    return liste2return

#Modifie/supprime un numéro à une personne existante

def CHANGE_num(data, column):

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    request=f"UPDATE Numbers SET {column} = ? WHERE ID = ?"

    cur.execute(request, data)
    conn.commit()

    cur.close()
    conn.close()

#Ajoute une personne avec un numéro de téléphone

def ADD_people(data_people, data_num):

    data_people.insert(0, unique_ID("People"))
    data_people.append(unique_ID("Numbers"))

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO People(ID, Nom, Prenom, Profession, Date_de_naissance, ID_link) VALUES(?, ?, ?, ?, ?, ?)", data_people)
    conn.commit()

    data_num.insert(0, unique_ID("Numbers"))

    cur.execute("INSERT INTO NUMBERS(ID, Indicatif, Mobile, Fixe, Domicile, Travail) VALUES(?, ?, ?, ?, ?, ?)", data_num)
    conn.commit()

    cur.close()
    conn.close()

#Modifie/supprimer les infos d'une personne

def CHANGE_people(data, column):

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    request=f"UPDATE People SET {column} = ? WHERE ID = ?"

    cur.execute(request, data)
    conn.commit()

    cur.close()
    conn.close()

#Supprime un rang de la table

def delete(ID, table):

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()

    request=f"DELETE FROM {table} WHERE ID = ?"

    cur.execute(request, ID)
    conn.commit()

    cur.close()
    conn.close()


#########################################################################################################################

print('\n', "PEOPLE_CORRESPONDANT:", people_correspondant((None, None, None, 2007)), '\n')

print('\n')

print('\n', "NUM_CORRESPONDANT:", num_correspondant([0]), '\n')


#CHANGE_num
"""CHANGE_num([None, 0], "Fixe")"""

#ADD_people
ADD_people(["Almeras", "Ugo", "Extreme chomeur", 2007], [33, 755668977, None, None, None])#faire en sorte d'ajouter aussi des numéro

#CHANGE_people
"""CHANGE_people(["Vrai chomeur", 2], "Profession")"""

#supprimer un rang
delete([3], "Numbers")