#1
diz={"Giuseppe Gullo" : [( "Corsa campestre",(40,21,0),"Allievi"),("Corsa 100mt",(0,12,0),"Juniores mas"),("Corsa 200mt",(0,29,19),"Juniores mas")],
"Antonia Barbera" : [( "Corsa campestre",(0,39,11),"Juniores fem"),("Corsa 100mt",(0,18,0),"Juniores fem"),("Corsa 200mt",(0,0,0),"Juniores fem")],
"Nicola Esposito" : [( "Corsa campestre",(0,43,22),"Allievi"),("Corsa 100mt",(0,14,0),"Juniores mas"),("Corsa 200mt",(0,36,19),"Juniores mas")],}

#2
diz["Matteo Ranzani"]=[( "Corsa campestre",(30,20,0),"Allievi"),("Corsa 100mt",(0,9,0),"Juniores mas"),("Corsa 200mt",(0,30,10),"Juniores mas")]

#3
diz["Giuseppe Gullo"]+=[("Corsa ad ostacoli 400mt",(0,40,34),"Allievi")]
diz["Antonia Barbera"]+=[("Corsa ad ostacoli 400mt",(0,39,10),"Allievi")]
diz["Nicola Esposito"]+=[("Corsa ad ostacoli 400mt",(0,40,10),"Allievi")]
diz["Matteo Ranzani"]+=[("Corsa ad ostacoli 400mt",(0,40,26),"Allievi")]
#9:53 Gornati

#4
print("Dati corsa campestre Giuseppe Gullo: ")
print(diz["Giuseppe Gullo"][0])
#9:53 Gornati

#5
print("-----------------------------")
print("Dati Corsa 200mt Nicola Esposito: ")
print(f"Sport: {diz['Nicola Esposito'][2][0]}")
print(f"Tempo: {diz['Nicola Esposito'][2][1]}")
print(f"Categoria: {diz['Nicola Esposito'][2][2]}")
#9:53 Gornati

#6
print("-----------------------------")
print("Il tempo di Antonia Barbera nei 100mt è di: ")
print(f"Tempo: {diz['Antonia Barbera'][1][1]}")
#9:53 Gornati

#7
print("-----------------------------")
print("Il tempo minimo riportato nella corsa 100mt della categoria Juniores mas è di: ")
min=(0,0,0)
if min<diz['Giuseppe Gullo'][1][1]:
  min=diz['Giuseppe Gullo'][1][1]
if min>diz['Nicola Esposito'][1][1]:
  min=diz['Nicola Esposito'][1][1]
if min>diz['Matteo Ranzani'][1][1]:
  min=diz['Matteo Ranzani'][1][1]
print(min)
#10:24 Gornati

#8
print("-----------------------------")
print("Il tempo massimo riportato nella corsa 200mt della categoria Juniores mas è di: ")
max=(0,0,0)
if max<diz['Giuseppe Gullo'][2][1]:
  max=diz['Giuseppe Gullo'][2][1]
if max<diz['Nicola Esposito'][2][1]:
  max=diz['Nicola Esposito'][2][1]
if max<diz['Matteo Ranzani'][2][1]:
    max=diz['Matteo Ranzani'][2][1]
print(max)
#10:34 Gornati

#9
print("-----------------------------")
print("La media dei tempi nella corsa campestre della categoria allievi è di: ")
somma=0
for atleta, dati in diz.items():
  print(diz[atleta][0][1])
