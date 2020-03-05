import copy
from datetime import datetime

def generateur_PnL_Mc4u(donnetxt):
    """
    Retourn un dictionnaire organiser contenant les datas nécessaire pour établir un P&L
    """

    # Création d'un doctionnaire contenant les formats PnL et Mc4u.
    formatgeMc4u_PnL = formatage()
    format_Mc4u_PnL = {}
    
    for libelle, codesAnalytique in formatgeMc4u_PnL.items():
        format_Mc4u_PnL[codesAnalytique["mc4u"]]={"PnL":codesAnalytique['pnl'],"libelle":libelle,"montant":0, "montant_cumul":0}

    # Set clés du dictionnaire
    dictionnairePnL_Mc4u = {}
    for val in donnetxt.values():
        x = copy.deepcopy(format_Mc4u_PnL)
        dictionnairePnL_Mc4u.setdefault(val['date'], x)

    periode= list(dictionnairePnL_Mc4u.keys())
    # traitement des infos extaites du txt
    for val in donnetxt.values():
        try:
            codeAnalytique = int(val['code_analytique'].strip())
        except Exception as e:
            print('generateur mc4u')
            print(e)
            continue
        sensD_C = val['d_c']
        date = val['date']
        montant = float(val['montant'])/100
        compte = val['num_compte']
        if compte.startswith('6'):
            pass
        elif compte.startswith('7'):
            pass
        else:
            continue
        # Si une écriture est passé à l'envers nous devons modifié le montant en négatif
        if compte.startswith('6') and sensD_C == 'C':
            montant = montant*-1
        # Les compte produits étant négatif nous devons les passer en positif seulement lorsqu'ils sont au débit
        elif compte.startswith('7') and sensD_C == 'C':
            montant = montant*-1
        # liste des périodes

        for codeMc4u, val in dictionnairePnL_Mc4u[date].items():
            if val['PnL'] == codeAnalytique:
              
                dictionnairePnL_Mc4u[date][codeMc4u]['montant']+=montant

                for date_cumul in periode:

                    if date <= date_cumul:

                        dictionnairePnL_Mc4u[date_cumul][codeMc4u]['montant_cumul']+=montant

    return dictionnairePnL_Mc4u


def formatage():
    """
    retourn une liste contenant le formatage pour le Mc4u et le P&L
    """
    format_Mc4u_PnL = {
"Ventes nettes totales":{"mc4u":0,"pnl":1},
"Ventes produits alimentaires":{"mc4u":1,"pnl":2},
"Coût nourriture : achat nourriture":{"mc4u":10,"pnl":3},
"Coût nourriture : repas employés":{"mc4u":11,"pnl":4},
"Coût nourriture : déchets":{"mc4u":12,"pnl":5},
"Coût emballages":{"mc4u":13,"pnl":7},
"Coût total nourriture":{"mc4u":14,"pnl":6},
"Coût total produits vendus":{"mc4u":19,"pnl":8},
"Marge brute":{"mc4u":20,"pnl":9},
"Main d'oeuvre équipiers":{"mc4u":23,"pnl":10},
"Salaires managers":{"mc4u":24,"pnl":11},
"Charges sociales managers":{"mc4u":26,"pnl":12},
"Main d'oeuvre totale":{"mc4u":28,"pnl":""},
"Frais de voyage":{"mc4u":30,"pnl":13},
"Publicité GIE":{"mc4u":32,"pnl":14},
"Promotion locale":{"mc4u":34,"pnl":15},
"Services extérieurs":{"mc4u":36,"pnl":16},
"Uniformes":{"mc4u":38,"pnl":17},
"Fournitures exploitation":{"mc4u":40,"pnl":18},
"Entretien, réparations équipement":{"mc4u":42,"pnl":19},
"Electricité, eau, gaz, téléphone":{"mc4u":44,"pnl":20},
"Fournitures bureau":{"mc4u":46,"pnl":21},
"Ecarts de caisse":{"mc4u":48,"pnl":22},
"Divers *":{"mc4u":50,"pnl":23},
"Total dépenses contrôlables":{"mc4u":55,"pnl":""},
"Profit après contrôlables (PAC)":{"mc4u":60,"pnl":24},
"Redevance standard":{"mc4u":62,"pnl":30},
"Redevance équipement":{"mc4u":64,"pnl":""},
"Redevance service 5% CA net":{"mc4u":65,"pnl":31},
"Frais comptables et juridiques":{"mc4u":68,"pnl":32},
"Assurance":{"mc4u":71,"pnl":33},
"Taxes et primes":{"mc4u":74,"pnl":34},
"Perte / gain cession d'actifs":{"mc4u":76,"pnl":35},
"Dépréciations amortissements":{"mc4u":77,"pnl":36},
"Crédit bail":{"mc4u":78,"pnl":37},
"Charges / Revenus financiers":{"mc4u":80,"pnl":38},
"Dépenses / Revenus divers":{"mc4u":82,"pnl":39},
"Total dépenses non contrôlables":{"mc4u":84,"pnl":40},
"Ventes non alimentaires":{"mc4u":85,"pnl":42},
"Coût non alimentaire":{"mc4u":87,"pnl":43},
"Résultat net non alimentaire":{"mc4u":90,"pnl":44},
"Résultat net d'exploitation (SOI)":{"mc4u":93,"pnl":45},
"Salaire du locataire gérant":{"mc4u":101,"pnl":50},
"Autres dépenses":{"mc4u":102,"pnl":51},
"Dépenses de bureau":{"mc4u":103,"pnl":52},
"Total frais administratifs":{"mc4u":104,"pnl":""},
"Revenu net avant impôt":{"mc4u":106,"pnl":53},
"Provision pour impôt":{"mc4u":107,"pnl":54},
"Résultat net":{"mc4u":108,"pnl":""},
"Résultat net saisi":{"mc4u":109,"pnl":""},
"* dont participation éventuelle (pour info)":{"mc4u":110,"pnl":""},
    }
    return format_Mc4u_PnL


if __name__ == "__main__":
    from LecteurTxt import take_value_file, desired_parameter,undesirable_parameter
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    fichiertxt = 'V:/Mathieu/Lejri/JBM_ECR_2019.txt'
    formater = {}
    formater['type'] = (0, 1)
    formater['num_compte'] = (1, 9)
    formater['date'] = (16, 20)
    formater['d_c'] = (41, 42)
    formater['montant'] = (42, 55)
    formater['code_analytique'] = (79, 89)

    z = take_value_file(fichiertxt, formater)
    dicvoulu={}
    dicnonv = {}
    dicvoulu['type']='M'
    dicnonv['code_analytique'] = '          '
    
    x = desired_parameter(z , dictvalue=dicvoulu)
    f = undesirable_parameter(x, dictvalue = dicnonv)

    date=[]
    for val in f.values():
        date.append(val['date'])
        
    pp.pprint(generateur_PnL_Mc4u(f))
        