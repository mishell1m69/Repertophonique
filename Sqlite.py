import sqlite3


#Renvoi les personnes qui correspondent aux infos

def people_correspondant(data):

    conn = sqlite3.connect('SQL/v2.db')
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM PEOPLE WHERE ID_people LIKE %?% AND Nom LIKE ? AND Prenom LIKE ? AND Profession LIKE ? AND Date_de_naissance LIKE ?", data)
    conn.commit()

    liste2return=cur.fetchall()

    cur.close()
    conn.close()

    return liste2return
#Renvoi les numéros de téléphones correspondant à une personne


#Ajoute un numéro à une personne existante


#Ajoute une personne avec un numéro de téléphone


#Modifie les infos d'une personne


#Modifie les numéros de téléphone d'une personne


#Supprime un numéro de qq


#Supprime une personne et ses numéros


#########################################################################################################################

print("Results:", people_correspondant(("zzz", "Michel", "Clément", "Chomeur", 2007)))