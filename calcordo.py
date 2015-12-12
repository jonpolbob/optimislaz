import numpy as np

bilan=[]

stop=0

def gettime():
    global stop;
    letime=1
    while stop==0:
        letime = letime+1
        yield letime

#presents / personne : 0 = om
#1 = job duree
#2 heure arrivee
#3 heure pssage initiale
#4 heure passage estimee

printtableaux=False
presents=[]
#nom,job, heure arrivee, duree attente initiale , heure passage arrivee, heure pssage reel
test = False
if test:
    #aglae est arrivee a t=100, pour un job de 80 minutes. heure passage initial, il lui  ete attribue une heure  130
    presents.append(["aglae", 80, 100, 130, 130])
    #beta est arrive a 150 pour un job de 90, heure de assage initiale  a 130+80 (heure dernier prog+ job) , il demarrera en fait : a l'heure prevue
    presents.append(["beta", 90, 150, 210, 210])
    #chut est arrive a 155 pour un job de 20, heure passage initiale : apres beta a 210+90=300 ; heure assage reelle : idem
    presents.append(["chut",20,155,300,300])

#ajoute une nouvelle personne 

jobcourantdur = 0
jobcourantdebreel = 0  #il faut 150+dureee < heure nouveau job


#action sur chaneent d'heure
def checkhour(newhour):
    global jobcourantdur, jobcourantdebreel,bilan 
    if jobcourantdur == 0:
        return
    if jobcourantdur + jobcourantdebreel < newhour :  #le job courant est fini
        if presents==[]:
            jobcourantdur=0
        else :
            personne = presents[0]
            presents.remove(personne)
            jobcourantdur = personne[1]
            jobcourantdebreel = newhour
            print "passage de",[personne[0],personne[1],personne[2],jobcourantdebreel, jobcourantdebreel]
            bilan.append([personne[0],personne[1],jobcourantdebreel,jobcourantdebreel-personne[2]])
            
#on commence par faire une lste contenant toutes les possibilites
# c a d une liste e liste, cacun de ces listes est la liste des personnes avec la nouvelle personne
# inseree a toutes les places possibles
def addnewpersonne(nom,duree,heurecourante):
    global presents
    global jobcourantdur, jobcourantdebreel 
    global bilan

    print "saisie de ",nom,"duree =",duree,"heure cour=",heurecourante

    #on checke l"'heure courante pour eventuellmen t faire avancer la pile
    checkhour(heurecourante)

    #gestion du premier job
    
    if presents==[]:
        if jobcourantdur ==0:           #pas e job en cours : on lance tt de suite le nouveau sans l'empiler 
            jobcourantdur=duree
            jobcourantdebreel =heurecourante
            print "passage de",[nom,duree,heurecourante,jobcourantdebreel]
            bilan.append([nom,duree,heurecourante,heurecourante-heurecourante])                        
            return [] #rien dans la liste car passe tt de suite
        else : #liste vide mais il y a un jo en cours : on le met dans la liste (il est tout sel -> rien a optimiser)
            #jobcourantdur = duree
            #jobcourantdebreel = heurecourante  #il faut 150+dureee < heure nouveau job
            #on conait son temps attent initial : c'est le temps qu'il reste du job en cours
            return [[nom,duree,heurecourante,jobcourantdebreel+jobcourantdur, jobcourantdebreel+jobcourantdur]] #liste de personnes avec une personne
    
        
    #quand une nouvelle personne arrive : on calcule     
    nboutputs=len(presents)+1  #taille des tableaux a bricoler

    listepersonnes = []
    #creation d'une liste des presents avec index
    for iindex,personne in enumerate(presents) :
        listepassage = [iindex]
        listepassage.extend(personne[1:])
        listepersonnes.append(listepassage)        
        #print personne[0],listepassage #liste actuelle des gens qui vont passer
  
    #ici on a une liste    
    heuredernierpassage = listepersonnes[-1][4]+listepersonnes[-1][1] #heure passage relle dernier personne+duree job
    if True:
        print "heuredernier",heuredernierpassage
    
    #fabrication d'un tableau avec le nouveau ajoute a toutes les position possibles parmi les gens en attente
    tabcroise = []
    for iindex,liste in enumerate(listepersonnes):
        tabcroise.append(listepersonnes[:]) #liste de lise faite avec copie de la lite 
        #(sinon on a x foi la meem liste, et i on modifie la 1ere on modifie les autres)
    tabcroise.append(listepersonnes[:]) #ue liste de plus pour l'insertion apres la fin
    
    for iindex,liste in enumerate(tabcroise):
        liste.insert(iindex,[nboutputs-1,duree,heurecourante,heuredernierpassage,0]) #on met 0 comme heure de passage calculee    
        #print "insert ",liste[iindex]
    if False:
        print tabcroise
    
    
    #on genere un tableau pour chacun des termes d'une personne
  
    flattened = [val[0] for sublist in tabcroise for val in sublist]
    tabindex = np.resize(np.asarray( flattened),[len(tabcroise),len(tabcroise)])
    flattened = [val[1] for sublist in tabcroise for val in sublist]
    tabjobduree = np.resize(np.asarray( flattened),[len(tabcroise),len(tabcroise)])
    flattened = [val[2] for sublist in tabcroise for val in sublist]
    tabheurearriv = np.resize(np.asarray( flattened),[len(tabcroise),len(tabcroise)])
    flattened = [val[3] for sublist in tabcroise for val in sublist]
    tabheurepassorig = np.resize(np.asarray( flattened),[len(tabcroise),len(tabcroise)])
    
    #heure de passage = somme des jobs du tableau : on balaie sur toutes les lignes
    tabheurepasscalc = np.zeros([tabjobduree.shape[0],tabjobduree.shape[1]]) 
    
    #for ligne in range(1,tabjobduree.shape[1]): #la 2eme valeur du tupl est lle n de lignes 
    #        tabheurepasscalc[ligne] =
    tabheurecumuljob  =np.cumsum(tabjobduree,axis=1)  #cumul des lignes jusqu'a la ligne
    
    #ici on a ds tableaux dont les lignes contiennent un candidat a l'ordre de passage 
    printtableaux = True    
    if False:
        print "index"
        print  tabindex
        print "duree"
        print tabjobduree
        print "arriv"
        print tabheurearriv
        print "orig"
        print tabheurepassorig
        print "cml"
        print tabheurecumuljob

    #temps restant sur le job en cours
    restejobcour = jobcourantdur + jobcourantdebreel -heurecourante
    if False :
        print "reste job cour",restejobcour
    
    #tableau du tems deja atendu par chacun
    tabdejaattendu = heurecourante-tabheurearriv
    if False:
        print 'deja attendu'
        print  tabdejaattendu
    
        #tableau des attentes de debut : on rajoue une colonne avec le temps restant dans le job en cours
    tabattstart = np.zeros([tabheurepasscalc.shape[0],tabheurepasscalc.shape[1]])  #reste a attendre
    tabattstart[:,1:]=tabheurecumuljob[:,:-1]
    tabattstart += restejobcour
    printtableaux=True   
    if False:
        print "startcalc"
        print tabattstart
        
    tabheurfinreelle = (tabattstart + heurecourante) + tabjobduree   #tableau delai reel avant fin job
    if False:
        print "heure fin reelle"
        print tabheurfinreelle
        
    tabattfinreelle = tabheurfinreelle - tabheurearriv  #tableau delai reel avant fin job
    if False:
        print "att fin reelle"
        print tabattfinreelle
    
    tabattfinini = tabheurepassorig + tabjobduree   #tableau delai initial avant fin job
    if False:
        print "att fin initiale"
        print tabatfinini
     
    tabpercentretard = tabattfinreelle/tabattfinini*100  
    if False:
        print "% retard"
        print tabpercentretard
        
    #calcul du retard total pour cette combinaison) 
    cumlretard = tabpercentretard.sum(axis=1) #cumul sur les elements 'une combinaison
    if False:
        print "cumul1",cumlretard
    
    resul = np.argmin(cumlretard)
    if False:
        print tabindex[resul,:]

    #positin du nouveau dans cette combinaison = resul aussi car l'index dans le tableau = la position de l'insertion
    position = np.argmax(tabindex[resul])
    print "combinaiso=",resul," position=",position

    newpresents = presents
    newpresents.insert(resul,[nom,duree,heurecourante,tabattfinini[resul,resul]-duree,0])               
    #print newpresents
    
    #mise a jour de l'heure de passage normale
    for index,personne in enumerate(newpresents) :
        personne[4]=tabattstart[resul,index] + heurecourante
        #print personne
    
    return newpresents    
    
#jeu essai    
def liste():
    global presents
    
    for personne in presents:
        print personne[0], personne[1],personne[2], "h pass:",personne[4],"h prevue",personne[3],"avance sur prevu ", personne[3]-personne[4], "attente relle", personne[4]-personne[2]         
    raw_input()
    
personnes=[]    
personnes.append(["aglae", 120, 100])
personnes.append(["beta", 60, 150])
personnes.append(["chut",20,205])    
personnes.append(["danae",90,206])
personnes.append(["elfe",30,220])
personnes.append(["fifi",90,280])
personnes.append(["golf",10,290])
personnes.append(["hibou",20,300])
personnes.append(["indigo",60,340])

laboucle = gettime()

for letime in laboucle:
    if len(personnes) ==0 and len(presents)==0 :
        stop=1
        
    for lapersonne in personnes:
        if lapersonne[2]>letime:
            presents = addnewpersonne(lapersonne[0],lapersonne[1],letime)
            liste()
            personnes.remove(lapersonne)
     
    checkhour(letime)
     
#for personne in presents:
#    checkhour(personne[4]) #on vide la pile en passant tout ce qui reste a son heure
    
for resu in bilan:
    print resu[0],"duree : ",resu[1]," heure passage : ",resu[2]," attente : ",resu[3]
