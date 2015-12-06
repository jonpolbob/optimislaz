import numpy as np

presents=[]
#nom,heure arrivee,attente initiale duree,heure pssage reel
#aglae est arrivee a t=100, pour un job de 80 minutes. il lui  ete attribue une heure  130
presents.append(["aglae",80,100,130])
#beta est arrive a 150 pour un job de 90, il demarrera apres aglae a 130+80
presents.append(["beta",90,150,210])
#chose est arrive a 125 pour un job de 20, il demarrera apres chose a 210+90=300
presents.append(["chut",20,125,300])

print presents

#ajoute une nouvelle personne 
def addnewpersonne(nom,duree,heurecourante):
    global presents
    #quand une nouvelle personne arrive : on calcule     
    nboutputs=len(presents)+1
    arraypermut = np.ndarray(shape=(nboutputs,nboutputs), dtype=int)

    listepersonnes = []
    #creation d'une liste des presents
    for iindex,personne in enumerate(presents) :
        listepassage = [iindex]
        listepassage.extend(personne[1:3])
        listepersonnes.append(listepassage)        
        print listepassage
        
        
    print listepersonnes
    
    #fabrication d'un tableau avec le nouveau ajoute a toutes les position possibles parmi les gens en attente
    tabcroise=[]   
    for iindex,personne in enumerate(listepersonnes) :
        colonne = listepersonnes[0:iindex]
        colonne.append([nboutputs,duree,heurecourante])
        colonne.extend(listepersonnes[iindex:])
        tabindex.append(colonne)
        tabduree.append(colonne)
        tabarriv.append(colonne)
        
        
    print tabcroise
      
addnewpersonne("danae",50,127)
