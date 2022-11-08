#1 popola
import pprint
pp=pprint.PrettyPrinter(indent=4)
diz={"AA123BB":[("Giugno",9,1293),("Luglio",7,3231),("Agosto",7,4020),("Settembre",6,3928)],
     "AB345CD":[("Giugno",8,1391),("Luglio",6,1234),("Agosto",9,4932),("Settembre",8,2872)],
     "CD456FF":[("Giugno",7,2872),("Luglio",6,3273),("Agosto",4,3211),("Settembre",8,2827)]}

#2 aggingi
diz["ZZ999RM"]=[("Giugno",10,18000), ("Luglio",10,18000), ("Agosto",10,18000), ("Settembre",10,18000)]

#3 stampa
print(diz["AA123BB"][1])
print(f"Mese: {diz['AA123BB'][1][0]}")
print(f"Noleggi: {diz['AA123BB'][1][1]}")
print(f"KM: {diz['AA123BB'][1][2]}")

#4 stampa
print(diz["AA123BB"][1])
print(f"Noleggi: {diz['AA123BB'][1][1]}")

#5 somma KM AB345CD
km=0
print("Somma km: ")
for i in range(len(diz["AB345CD"])):
  km+=diz['AB345CD'][i][2]
somma=km
print(somma)

#6 somma tutti km
km=0
for chiave in diz.keys():
  for i in range(len(diz[chiave])):
    km+=diz[chiave][i][2]
print(f"Somma di tutti i km: {km} ")

#7 mese con più km di CD456FF
km=diz["CD456FF"][0][2]
i=1
for i in range (len(diz["CD456FF"])):
  if(diz["CD456FF"][i][2]>km):
    km=diz["CD456FF"][i][2]
    imax=i
print("Mese con più km di CD456FF: "+ diz["CD456FF"][imax][0])
