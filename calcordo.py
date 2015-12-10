import numpy as np

presents=[]
#nom,heure arrivee,attente initiale duree,heure pssage reel
#aglae est arrivee a t=100, pour un job de 80 minutes. il lui  ete attribue une heure  130
presents.append(["aglae",80,100,130,10])
#beta est arrive a 150 pour un job de 90, il demarrera apres aglae a 130+80
presents.append(["beta",90,150,210,90])
#chose est arrive a 125 pour un job de 20, il demarrera apres chose a 210+90=300
presents.append(["chut",20,125,300,300])

print presents

#ajoute une nouvelle personne 

#on commence par faire une lste contenant toutes les possibilites
# c a d une liste e liste, cacun de ces listes est la liste des personnes avec la nouvelle personne
# inseree a toutes les places possibles
def addnewpersonne(nom,duree,heurecourante,attentearrivee):
    global presents
    #quand une nouvelle personne arrive : on calcule     
    nboutputs=len(presents)+1
    arraypermut = np.ndarray(shape=(nboutputs,nboutputs), dtype=int)

    listepersonnes = []
    #creation d'une liste des presents
    for iindex,personne in enumerate(presents) :
        listepassage = [iindex]
        listepassage.extend(personne[1:])
        listepersonnes.append(listepassage)        
        print listepassage
        
    
    #fabrication d'un tableau avec le nouveau ajoute a toutes les position possibles parmi les gens en attente
    tabcroise = []
    for iindex,liste in enumerate(listepersonnes):
        tabcroise.append(listepersonnes[:]) #liste de lise faite avec copie de la lite 
        #(sinon on a x foi la meem liste, et i on modifie la 1ere on modifie les autres)
    tabcroise.append(listepersonnes[:]) #ue liste de plus pour l'insertion apres la fin
    
    for iindex,liste in enumerate(tabcroise):
        liste.insert(iindex,[nboutputs,duree,heurecourante])    
    print tabcroise
    
    
    #on genere un tableau pour chacun des termes d'une personne
  
    flattened = [val[0] for sublist in tabcroise for val in sublist]
    tabindex = np.resize(np.asarray( flattened),[len(tabcroise),len(tabcroise)])
    flattened = [val[1] for sublist in tabcroise for val in sublist]
    tabinduree = np.resize(np.asarray( flattened),[len(tabcroise),len(tabcroise)])
    flattened = [val[2] for sublist in tabcroise for val in sublist]
    tabheuureairv = np.resize(np.asarray( flattened),[len(tabcroise),len(tabcroise)])
    flattened = [val[2] for sublist in tabcroise for val in sublist]
    tabheurepass = np.resize(np.asarray( flattened),[len(tabcroise),len(tabcroise)])
    print tabindex
    print tabinduree
    print tabheuureairv
    print tabheurepass
                    
addnewpersonne("danae",50,127,36)
