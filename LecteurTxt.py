from datetime import datetime


def take_value_file(file, dict_formater, param_indesirable="", param_voulu=""):
    """
    Prend en argument le fichier à lire et les informations a extraire sous le format 
    d'un dictionnaire comme suit : 
    dict{'nom_var': ( int(position début arg), int(position fin arg) ) }
    """
    
    Result = {}
    compteur = 0
  
    with open(file, "r",errors='ignore') as f:
        for line in f.readlines():

            compteur += 1
            listeArgumentExtrait = []
            for cle, val in dict_formater.items():
                if cle == "date" and line[val[0]:val[1]] != "":
                    try:
                        d = datetime.strptime(line[val[0]:val[1]], '%m%y')
                        listeArgumentExtrait.append((cle, d))
                    except:
                        pass
                else:
                    listeArgumentExtrait.append((cle, line[val[0]:val[1]]))
               
            Result[compteur] = dict(listeArgumentExtrait)


    return Result


def undesirable_parameter(dictionnaire, keyexclue=None, dictvalue=None):
    """
    Permet de supprimer des éléments dans un dictionnaire.
    keyexclue = tuple de clé a supprimer
    dictvalue{'val' : 'val a supprimer'}
    """

    # Si la/les valeur/s du tuple correspond/ent à la valeur d'un clé du dictionnaire, nous supprimons cette élément du dictionnaire.
    if keyexclue:
        for key in keyexclue:
            del dictionnaire[key]
    
    # Si la/les clé/s du dictvalue correspond/ent à la clé d'une valeur du dictionnaire.
    # Nous controlons les valeurs de ces clés entre elle.
    # Si elle sont égales nous ajoutons la clé du dictionnaire à annalyser dans une liste.
    # Nous bouclons sur la liste des clés a supprimer pour les retirer du dictionnaire.
    listeKeyToDel = []
    if dictvalue:
        for keydict , valdict in dictionnaire.items():
            for keydictvalue_undesirable, valdictvalue_undesirable in dictvalue.items():
                if valdict[keydictvalue_undesirable] == valdictvalue_undesirable:

                    listeKeyToDel.append(keydict)

        for delKey in listeKeyToDel:
            del dictionnaire[delKey]
    return dictionnaire


def desired_parameter(dictionnaire, keydesired=None, dictvalue=None):
    """
    Permet de supprimer des éléments dans un dictionnaire.
    keyexclue = tuple de clé a supprimer
    dictvalue{'val' : 'val a supprimer'}
    """

    # Si la/les valeur/s du tuple correspond/ent à la valeur d'un clé du dictionnaire, nous supprimons cette élément du dictionnaire.
    listeKeyToDel = []
    if keydesired:
        for key in dictionnaire.keys():
            for keyD in keydesired:
                if key != keyD:
                    
                    listeKeyToDel.append(key)    
    # Si la/les clé/s du dictvalue correspond/ent à la clé d'une valeur du dictionnaire.
    # Nous controlons les valeurs de ces clés entre elle.
    # Si elle sont égales nous ajoutons la clé du dictionnaire à annalyser dans une liste.
    # Nous bouclons sur la liste des clés a supprimer pour les retirer du dictionnaire.

    if dictvalue:
        for keydict , valdict in dictionnaire.items():
            for keydictvalue, valdictvalue in dictvalue.items():
                if valdict[keydictvalue] != valdictvalue:
                    if keydict not in listeKeyToDel:
                        listeKeyToDel.append(keydict)

    for delKey in listeKeyToDel:
        
        del dictionnaire[delKey]

    return dictionnaire





if __name__ == "__main__":

    fichiertxt = 'V:/Mathieu/Lejri/testTjustom/testTJ.txt'
    formater = {}
    formater['type'] = (0, 1)
    formater['num_compte'] = (1, 9)
    formater['date'] = (16, 20)
    formater['d_c'] = (41, 42)
    formater['montant'] = (42, 55)
    formater['code_analytique'] = (79, 89)

    z = take_value_file(fichiertxt, formater)
    dic={}
    dic['code_analytique']='003       '
    dic['num_compte']='60110000'
    f = desired_parameter(z , dictvalue=dic)


