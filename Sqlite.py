import sqlite3

conn = sqlite3.connect('SQL/v2.db')
cur = conn.cursor()

cur.execute('SELECT * FROM PEOPLE')
conn.commit()

liste = cur.fetchall()

cur.execute('SELECT * FROM NUMBERS')
conn.commit()

liste2 = cur.fetchall()

cur.close()
conn.close()

print(liste, '\n', liste2)
#Renvoi les personnes qui correspondent aux infos


#Renvoi les numéros de téléphones correspondant à une personne


#Ajoute un numéro à une personne existante


#Ajoute une personne avec un numéro de téléphone


#Modifie les infos d'une personne


#Modifie les numéros de téléphone d'une personne


#Supprime un numéro de qq


#Supprime une personne et ses numéros