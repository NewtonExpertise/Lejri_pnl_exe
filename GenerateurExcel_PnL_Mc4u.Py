import xlsxwriter
import os
import locale
import datetime
import tempfile
import sys
import os

locale.setlocale(locale.LC_TIME, '')
try:
    ressources = sys._MEIPASS
except:
    ressources = "."

def excel_pnl_mc4u(donneePnl_Mc4u, periode_selected, nomsociete = ''):
    """
    Etabli un P&L et un Mc4U a partir des données reçu.
    """
    periodeMc4u = datetime.datetime.strptime(periode_selected , "%B %Y")
    periode_selected=periode_selected.replace(' ', '_')
    wb_pnl = xlsxwriter.Workbook(os.path.join(tempfile.gettempdir(), nomsociete.replace(' ', '_')+"_PandL.xlsx"))# `
    wb_mc4u = xlsxwriter.Workbook(os.path.join(tempfile.gettempdir(), nomsociete.replace(' ', '_')+"_Mc4u_"+periode_selected+".xlsx"))
    Firstline = 3
    Firstline_Mc4u=0

    #~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~
    # P&l  Gestion des formatages cellules 
    # # # # # # # # # # # # # # # # # # # # 
    # # En-tête :
    en_tete = wb_pnl.add_format({'bold': True, 'font_size': 18, 'align': 'center', 'valign': 'vcenter', 'shrink':True, 'text_wrap':True})
    # # Titre - sous titre :
    titre_colonnes_debut = wb_pnl.add_format({'bold': True, 'font_color': '#FFffff', 'align': 'center', 'valign': 'vcenter', 'bg_color': '#FF8100', 'top': 2 , 'bottom': 2 , 'left':2})
    titre_colonnes_fin = wb_pnl.add_format({'bold': True, 'font_color': '#FFffff', 'align': 'center', 'valign': 'vcenter', 'bg_color': '#FF8100', 'top': 2 , 'bottom': 2, 'right':2})
    sous_titres_C1 = wb_pnl.add_format({'bold': True, 'bg_color': '#E7E6E6', 'left':2})
    sous_titres_OtherC = wb_pnl.add_format({'bold': True, 'bg_color': '#E7E6E6','right':2})
    # # Totaux :
    totaux = wb_pnl.add_format({'bold': True, 'bg_color': '#FF8100', 'num_format': '#,##0.00_ ;-#,##0.00\ ', 'right':2})
    pourcentage_totaux = wb_pnl.add_format({'bold': True, 'num_format': '0.00%', 'bg_color': '#FF8100', 'right':2})
    totaux_code = wb_pnl.add_format({'bold': True, 'align': 'center', 'bg_color': '#FF8100', 'left': 2})
    # # Totaux fin tableau
    totaux_ft = wb_pnl.add_format({'bold': True, 'bg_color': '#FF8100', 'num_format': '#,##0.00_ ;-#,##0.00\ ', 'right':2, 'bottom':2})
    pourcentage_totaux_ft = wb_pnl.add_format({'bold': True, 'num_format': '0.00%', 'bg_color': '#FF8100', 'right':2, 'bottom':2})
    totaux_code_ft = wb_pnl.add_format({'bold': True, 'align': 'center', 'bg_color': '#FF8100', 'left': 2, 'bottom':2})
    # # Sous Totaux
    sous_totaux = wb_pnl.add_format({'bold': True, 'bg_color': '#FFAC00', 'num_format': '#,##0.00_ ;-#,##0.00\ ', 'right':2})
    pourcentage_sous_totaux = wb_pnl.add_format({'bold': True, 'num_format': '0.00%', 'bg_color': '#FFAC00', 'right':2})
    sous_totaux_code = wb_pnl.add_format({'bold': True, 'align': 'center', 'bg_color': '#FFAC00', 'left': 2})
    # Poste ppx
    poste_principaux = wb_pnl.add_format({'num_format': '#,##0.00_ ;-#,##0.00\ ', 'right':2})
    pourcentage_poste_principaux = wb_pnl.add_format({'num_format': '0.00%', 'right':2})
    poste_principaux_code = wb_pnl.add_format({'align': 'center', 'left': 2})
    # set  dict format P&L
    formatPnl = {}
    formatPnl['pnl_pp'] ={'f_normal': poste_principaux, 'f_code': poste_principaux_code, 'f_pourcent': pourcentage_poste_principaux}
    formatPnl['pnl_st'] = {'f_normal': sous_totaux, 'f_code': sous_totaux_code, 'f_pourcent': pourcentage_sous_totaux}
    formatPnl['pnl_t'] ={'f_normal': totaux, 'f_code': totaux_code, 'f_pourcent': pourcentage_totaux}
    formatPnl['pnl_t_fin']={'f_normal': totaux_ft, 'f_code': totaux_code_ft, 'f_pourcent': pourcentage_totaux_ft}
    #
    #~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~

    #~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~
    # Mc4u Gestion des formatages cellules 
    # # # # # # # # # # # # # # # # # # # # 
    # # Titre des colonnes : 
    titre_colonne_mc4u = wb_mc4u.add_format({'bold': True, 'align': 'center', 'border':2})
    # Poste principaux :
    poste_principaux_mc4u = wb_mc4u.add_format({'num_format': '#,##0.00_ ;-#,##0.00\ ','border':2})
    poste_principaux_mc4u_code = wb_mc4u.add_format({'num_format': '@','border':2})
    # Sous totaux :
    sous_totaux_mc4u = wb_mc4u.add_format({'num_format': '#,##0.00_ ;-#,##0.00\ ','border':2, 'bg_color': '#c0c0c0'})
    sous_totaux_mc4u_code = wb_mc4u.add_format({'num_format': '@','border':2, 'bg_color': '#c0c0c0'})
    # Totaux :
    totaux_mc4u = wb_mc4u.add_format({'num_format': '#,##0.00_ ;-#,##0.00\ ','border':2,'bg_color': '#FF8100'})
    totaux_mc4u_code = wb_mc4u.add_format({'num_format': '@','border':2,'bg_color': '#FF8100'})
    #set dict format Mc4u
    formatMc4u={}
    formatMc4u['mc4u_Titre']= {'f_normal':titre_colonne_mc4u }
    formatMc4u['mc4u_pp']= {'f_normal': poste_principaux_mc4u, 'f_code': poste_principaux_mc4u_code}
    formatMc4u['mc4u_st']= {'f_normal':sous_totaux_mc4u, 'f_code': sous_totaux_mc4u_code}
    formatMc4u['mc4u_t']= {'f_normal':totaux_mc4u, 'f_code': totaux_mc4u_code}
    #
    #~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~

    # Dictionnaire pour créer les feuilles excel : clé = ligne , valeurs = (format des cellules , codes analytique, montants calculés)
    line_tableau = {
        1: {"mc4u": 0, "pnl": 0, 'formatpnl': formatPnl['pnl_st'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :'=C6+C47' , 'montantpnl_cumul':'=E6+E47' ,'montantmc4u' : "=C3+C40", 'montantmc4u_cumul' : "=D3+D40" },
        2: {"mc4u": 1, "pnl": 1, 'formatpnl': formatPnl['pnl_st'] , 'formatmc4u': formatMc4u['mc4u_t'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        3: {"mc4u": 10, "pnl": 10, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        4: {"mc4u": 11, "pnl": 11, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        5: {"mc4u": 12, "pnl": 12, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        6: {"mc4u": 13, "pnl": 14, 'formatpnl': formatPnl['pnl_st'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"=SUM(C7:C9)" , 'montantpnl_cumul':"=SUM(E7:E9)" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        7: {"mc4u": 14, "pnl": 13, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_st'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : "=C4+C5+C6", 'montantmc4u_cumul' : "=D4+D5+D6" },
        8: {"mc4u": 19, "pnl": 19, 'formatpnl': formatPnl['pnl_st'] , 'formatmc4u': formatMc4u['mc4u_st'] , 'montantpnl' :"=SUM(C10:C11)" , 'montantpnl_cumul':"=SUM(E10:E11)" ,'montantmc4u' : "=C8+C7", 'montantmc4u_cumul' : "=D8+D7" },
        9: {"mc4u": 20, "pnl": 20, 'formatpnl': formatPnl['pnl_t'] , 'formatmc4u': formatMc4u['mc4u_t'] , 'montantpnl' :"=C6-C12" , 'montantpnl_cumul':"=E6-E12" ,'montantmc4u' : "=C3-C9", 'montantmc4u_cumul' : "=D3-D9" },
        10: {"mc4u": 23, "pnl": '', 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        11: {"mc4u": 24, "pnl": 23, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        12: {"mc4u": 26, "pnl": 24, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        13: {"mc4u": 28, "pnl": 26, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_st'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : "=sum(C11:C13)", 'montantmc4u_cumul' : "=sum(D11:D13)" },
        14: {"mc4u": 30, "pnl": 30, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        15: {"mc4u": 32, "pnl": 32, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        16: {"mc4u": 34, "pnl": 34, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        17: {"mc4u": 36, "pnl": 36, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        18: {"mc4u": 38, "pnl": 38, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        19: {"mc4u": 40, "pnl": 40, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        20: {"mc4u": 42, "pnl": 42, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        21: {"mc4u": 44, "pnl": 44, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        22: {"mc4u": 46, "pnl": 46, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        23: {"mc4u": 48, "pnl": 48, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        24: {"mc4u": 50, "pnl": 50, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        25: {"mc4u": 55, "pnl": 55, 'formatpnl': formatPnl['pnl_st'] , 'formatmc4u': formatMc4u['mc4u_st'] , 'montantpnl' :"=SUM(C15:C28)" , 'montantpnl_cumul':"=SUM(E15:E28)" ,'montantmc4u' : "=sum(C14:C25)", 'montantmc4u_cumul' : "=sum(D14:D25)" },
        26: {"mc4u": 60, "pnl": '', 'formatpnl': formatPnl['pnl_st'] , 'formatmc4u': formatMc4u['mc4u_t'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : "=C10-C26", 'montantmc4u_cumul' : "=D10-D26" },
        27: {"mc4u": 62, "pnl": 60, 'formatpnl': formatPnl['pnl_t'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"=C13-C29" , 'montantpnl_cumul':"=E13-E29" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        28: {"mc4u": 64, "pnl": '', 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        29: {"mc4u": 65, "pnl": 62, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        30: {"mc4u": 68, "pnl": 65, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        31: {"mc4u": 71, "pnl": 68, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        32: {"mc4u": 74, "pnl": 71, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        33: {"mc4u": 76, "pnl": 74, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        34: {"mc4u": 77, "pnl": 76, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        35: {"mc4u": 78, "pnl": 77, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        36: {"mc4u": 80, "pnl": 78, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        37: {"mc4u": 82, "pnl": 80, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        38: {"mc4u": 84, "pnl": 82, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_st'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : "=sum(C28:C38)", 'montantmc4u_cumul' : "=sum(D28:D38)" },
        39: {"mc4u": 85, "pnl": 84, 'formatpnl': formatPnl['pnl_st'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"=SUM(C33:C42)" , 'montantpnl_cumul':"=SUM(E33:E42)" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        40: {"mc4u": 87, "pnl": '', 'formatpnl': formatPnl['pnl_st'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        41: {"mc4u": 90, "pnl": '', 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_st'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : "=C40+C41", 'montantmc4u_cumul' : "=D40+D41" },
        42: {"mc4u": 93, "pnl": '', 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_t'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : "=C27-C39+C42", 'montantmc4u_cumul' : "=D27-D39+D42" },
        43: {"mc4u": 101, "pnl": 85, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        44: {"mc4u": 102, "pnl": 87, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        45: {"mc4u": 103, "pnl": '', 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        46: {"mc4u": 104, "pnl": 90, 'formatpnl': formatPnl['pnl_st'] , 'formatmc4u': formatMc4u['mc4u_st'] , 'montantpnl' :"=SUM(C47:C48)" , 'montantpnl_cumul':"=SUM(E47:E48)" ,'montantmc4u' : "=sum(C44:C46)", 'montantmc4u_cumul' : "=sum(D44:D46)" },
        47: {"mc4u": 106, "pnl": '', 'formatpnl': formatPnl['pnl_st'] , 'formatmc4u': formatMc4u['mc4u_t'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : "=C43-C47", 'montantmc4u_cumul' : "=D43-D47" },
        48: {"mc4u": 107, "pnl": 93, 'formatpnl': formatPnl['pnl_t'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"=SUM(C31-C43+C50)" , 'montantpnl_cumul':"=SUM(E31-E43+E50)" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        49: {"mc4u": 108, "pnl": '', 'formatpnl': formatPnl['pnl_t'] , 'formatmc4u': formatMc4u['mc4u_t'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : "=C48-C49", 'montantmc4u_cumul' : "=D48-D49" },
        50: {"mc4u": 109, "pnl": 101, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        51: {"mc4u": 110, "pnl": 102, 'formatpnl': formatPnl['pnl_pp'] , 'formatmc4u': formatMc4u['mc4u_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        52: {"mc4u": "", "pnl": 103, 'formatpnl': formatPnl['pnl_pp'] ,  'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        53: {"mc4u": "", "pnl": 104, 'formatpnl': formatPnl['pnl_st'] ,  'montantpnl' :"=SUM(C54:C56)" , 'montantpnl_cumul':"=SUM(E54:E56)" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        54: {"mc4u": '', "pnl": '', 'formatpnl': formatPnl['pnl_st'] ,  'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        55: {"mc4u": "", "pnl": 106, 'formatpnl': formatPnl['pnl_t'] ,  'montantpnl' :"=C52-C57" , 'montantpnl_cumul':"=E52-E57" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        56: {"mc4u": "", "pnl": 107, 'formatpnl': formatPnl['pnl_pp'] , 'montantpnl' :"" , 'montantpnl_cumul':"" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
        57: {"mc4u": "", "pnl": '','formatpnl': formatPnl['pnl_t_fin'],  'montantpnl' :"=C59-C60" , 'montantpnl_cumul':"E59-E60" ,'montantmc4u' : 0, 'montantmc4u_cumul' : 0 },
    }

    # Réduction de la barre déroulante inférieur droite (Permet un appercu plus important des onglets)
    wb_pnl.set_tab_ratio(95)

    # About : 
    wb_pnl.set_properties({
        'title':    'P&L LEJRI',
        'author':   'Mathieu Leroy',
        'manager':  'Nicolas Rollet',
        'company':  'NEWTON EXPERTISE',
        'comments': 'Created with Python and XlsxWriter'})
    wb_mc4u.set_properties({
        'title':    'Mc4u LEJRI',
        'author':   'Mathieu Leroy',
        'manager':  'Nicolas Rollet',
        'company':  'NEWTON EXPERTISE',
        'comments': 'Created with Python and XlsxWriter'})

    for periode, dictval in donneePnl_Mc4u.items():
        ###########################################################
        ## Création du classeur Excel P&L
        ##
        # Création d'une feuille de classeur excel
        ws_pnl = wb_pnl.add_worksheet(periode.strftime("%b"+' '+"%Y").capitalize())
        # Fige un volet
        ws_pnl.freeze_panes(Firstline+1, 0)
        # setzoom à 85%
        ws_pnl.set_zoom(85)
        # masquer les valeurs zéro dans les cellules
        ws_pnl.hide_zero()
        # Définition de la zone d'impression : 
        ws_pnl.fit_to_pages(1, 1)
        # center l'impression
        ws_pnl.center_horizontally()
        # Set largeur colonne :
        ws_pnl.set_column("A:A", 16)
        ws_pnl.set_column("B:B", 40)
        ws_pnl.set_column("C:C", 15)
        ws_pnl.set_column("D:D", 9)
        ws_pnl.set_column("E:E", 15)
        ws_pnl.set_column("F:F", 9)
        # set hauteur de ligne :
        ws_pnl.set_default_row(15)
        ws_pnl.set_row(Firstline-3, 46.5)
        ws_pnl.set_row(Firstline, 27)
        # Création de l'en-tête de la feuille excel
        ws_pnl.insert_image(Firstline-3, 0, os.path.join(ressources,'logonewton.png'), {'x_scale': 0.25, 'y_scale': 0.25})
        ws_pnl.insert_image(Firstline-3, 4, os.path.join(ressources,'ma.png'),{'x_scale': 0.39, 'y_scale': 0.39, 'x_offset': 85.5, 'y_offset': 0})
        # ws_pnl.write(Firstline-2, 0, , en_tete)
        # ws_pnl.write(Firstline-3, 1, "Nom de l'entreprise", en_tete_top)
        ws_pnl.merge_range('B1:D1', nomsociete, en_tete)
        # set la période
        ws_pnl.merge_range('B2:D2', "P&L : "+periode.strftime("%B" +' '+"%Y").capitalize(), en_tete)
        # Titre des colone
        ws_pnl.write(Firstline, 0, "CODE", titre_colonnes_debut)
        ws_pnl.write(Firstline, 1, "LIBELLE", titre_colonnes_fin)
        ws_pnl.write(Firstline, 2, "Mensuel", titre_colonnes_fin)
        ws_pnl.write(Firstline, 3, "%", titre_colonnes_fin)
        ws_pnl.write(Firstline, 4, "Cumul Annuel", titre_colonnes_fin)
        ws_pnl.write(Firstline, 5, "%", titre_colonnes_fin)
        # set les lignes P&L qui ne sont pas comprises dans le mc4u
        # ligne 45 (cette ligne a des montant calculé)
        ws_pnl.write(Firstline+41,0, '041', totaux_code)
        ws_pnl.write(Firstline+41,1, 'TOTAL DES DEPENSES', totaux)
        ws_pnl.write(Firstline+41,2, '=C43+C29+C12', totaux)
        ws_pnl.write(Firstline+41,4, '=E43+E29+E12', totaux)
        ws_pnl.write(Firstline+41, 3, '=IF(AND(C45<>0,T(C45)="",$C$6<>0),C45/$C$6,"")', pourcentage_totaux)
        ws_pnl.write(Firstline+41, 5, '=IF(AND(E45<>0,T(E45)="",$E$6<>0),E45/$E$6,"")', pourcentage_totaux)
        # # ligne 61 (cette ligne a des montant calculé)
        ws_pnl.write(Firstline+57,0, '', totaux_code_ft)
        ws_pnl.write(Firstline+57,1, 'REVENU NET APRES IMPOTS', totaux_ft)
        ws_pnl.write(Firstline+57,2, '=C59-C60', totaux_ft)
        ws_pnl.write(Firstline+57,4, '=E59-E60', totaux_ft)
        ws_pnl.write(Firstline+57, 3, '=IF(AND(C61<>0,T(C61)="",$C$6<>0),C61/$C$6,"")', pourcentage_totaux_ft)
        ws_pnl.write(Firstline+57, 5, '=IF(AND(E61<>0,T(E61)="",$E$6<>0),E61/$E$6,"")', pourcentage_totaux_ft)
        # set les lignes de sous titre et ligne vide
        ws_pnl.write(Firstline+10,0, 'DEPENSES CONTROLABLES', sous_titres_C1)
        ws_pnl.write(Firstline+10,1, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+10,2, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+10,3, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+10,4, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+10,5, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+28,0, 'DEPENSES NON CONTROLABLES', sous_titres_C1)
        ws_pnl.write(Firstline+28,1, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+28,2, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+28,3, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+28,4, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+28,5, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+49,0, "FRAIS D'ADMINISTRATION", sous_titres_C1)
        ws_pnl.write(Firstline+49,1, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+49,2, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+49,3, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+49,4, '', sous_titres_OtherC)
        ws_pnl.write(Firstline+49,5, '', sous_titres_OtherC)
        # ligne vide
        ws_pnl.write(Firstline+26,0, '', sous_totaux_code)
        ws_pnl.write(Firstline+26,1, '', sous_totaux)
        ws_pnl.write(Firstline+26,2, '', sous_totaux)
        ws_pnl.write(Firstline+26,3, '', sous_totaux)
        ws_pnl.write(Firstline+26,4, '', sous_totaux)
        ws_pnl.write(Firstline+26,5, '', sous_totaux)

        ws_pnl.write(Firstline+40,0, '', sous_totaux_code)
        ws_pnl.write(Firstline+40,1, '', sous_totaux)
        ws_pnl.write(Firstline+40,2, '', sous_totaux)
        ws_pnl.write(Firstline+40,3, '', sous_totaux)
        ws_pnl.write(Firstline+40,4, '', sous_totaux)
        ws_pnl.write(Firstline+40,5, '', sous_totaux)

        ws_pnl.write(Firstline+47,0, '', sous_totaux_code)
        ws_pnl.write(Firstline+47,1, '', sous_totaux)
        ws_pnl.write(Firstline+47,2, '', sous_totaux)
        ws_pnl.write(Firstline+47,3, '', sous_totaux)
        ws_pnl.write(Firstline+47,4, '', sous_totaux)
        ws_pnl.write(Firstline+47,5, '', sous_totaux)

        ws_pnl.write(Firstline+54,0, '', sous_totaux_code)
        ws_pnl.write(Firstline+54,1, '', sous_totaux)
        ws_pnl.write(Firstline+54,2, '', sous_totaux)
        ws_pnl.write(Firstline+54,3, '', sous_totaux)
        ws_pnl.write(Firstline+54,4, '', sous_totaux)
        ws_pnl.write(Firstline+54,5, '', sous_totaux)

        ws_pnl.write(Firstline+42,0, '', poste_principaux_code)
        ws_pnl.write(Firstline+42,1, '', poste_principaux)
        ws_pnl.write(Firstline+42,2, '', poste_principaux)
        ws_pnl.write(Firstline+42,3, '', poste_principaux)
        ws_pnl.write(Firstline+42,4, '', poste_principaux)
        ws_pnl.write(Firstline+42,5, '', poste_principaux)

        ws_pnl.write(Firstline+45,0, '', poste_principaux_code)
        ws_pnl.write(Firstline+45,1, '', poste_principaux)
        ws_pnl.write(Firstline+45,2, '', poste_principaux)
        ws_pnl.write(Firstline+45,3, '', poste_principaux)
        ws_pnl.write(Firstline+45,4, '', poste_principaux)
        ws_pnl.write(Firstline+45,5, '', poste_principaux)

        for codemc4u, pnl_info in dictval.items():
            
            if codemc4u == 1 or codemc4u == 85 or codemc4u == 87:
                # Application des correctifs de signe
                pnl_info["montant"] = -pnl_info["montant"]
                pnl_info["montant_cumul"] = -pnl_info["montant_cumul"]

            for lignePnL, build_PnL in line_tableau.items():

                if codemc4u == build_PnL['pnl']:
                    pnl_info['PnL'] =str(pnl_info['PnL']).zfill(3)
                    
                    if pnl_info['PnL'] == "000":
                        pnl_info['PnL'] = ""
                    ws_pnl.write(Firstline+lignePnL, 0, pnl_info['PnL'], build_PnL['formatpnl']['f_code'])
                    ws_pnl.write(Firstline+lignePnL, 1, pnl_info['libelle'], build_PnL['formatpnl']['f_normal'])

                    stringlignePnL = str(4+lignePnL)
                    ws_pnl.write(Firstline+lignePnL, 3, '=IF(AND(C'+stringlignePnL+'<>0,T(C'+stringlignePnL+')="",$C$6<>0),C'+stringlignePnL+'/$C$6,"")',build_PnL['formatpnl']['f_pourcent'])
                    ws_pnl.write(Firstline+lignePnL, 5, '=IF(AND(E'+stringlignePnL+'<>0,T(E'+stringlignePnL+')="",$E$6<>0),E'+stringlignePnL+'/$E$6,"")',build_PnL['formatpnl']['f_pourcent'])
                    if pnl_info['montant']==0:

                        ws_pnl.write(Firstline+lignePnL, 2, build_PnL['montantpnl'], build_PnL['formatpnl']['f_normal'])
                    else:   
                        ws_pnl.write(Firstline+lignePnL, 2, pnl_info['montant'], build_PnL['formatpnl']['f_normal'])
                    if pnl_info['montant_cumul']==0:

                        ws_pnl.write(Firstline+lignePnL, 4, build_PnL['montantpnl_cumul'], build_PnL['formatpnl']['f_normal'])
                    else:
                        ws_pnl.write(Firstline+lignePnL, 4, pnl_info['montant_cumul'], build_PnL['formatpnl']['f_normal'])
                ws_pnl.write(Firstline+1, 3, 1, pourcentage_sous_totaux)
                ws_pnl.write(Firstline+1, 5, 1, pourcentage_sous_totaux)

        #/////fin de création P&L/////////////fin de création P&L/////////////fin de création P&L/////////////fin de création P&L/////////////fin de création P&L////////

        #/////début Mc4u//////////////début Mc4u//////////////début Mc4u//////////////début Mc4u//////////////début Mc4u//////////////début Mc4u//////////////début Mc4u/
        if periodeMc4u == periode:

            ###########################################################
            ## Création du classeur Excel Mc4u
            ##
            ws_mc4u = wb_mc4u.add_worksheet(periodeMc4u.strftime("%Y%m_1"))
            # Fige première ligne
            ws_mc4u.freeze_panes(Firstline_Mc4u+1, 0)
            # set largeur colone
            ws_mc4u.set_column("A:A", 11)
            ws_mc4u.set_column("B:B", 39)
            ws_mc4u.set_column("C:C", 11)
            ws_mc4u.set_column("D:D", 11)
            #set permière ligne
            ws_mc4u.write(Firstline_Mc4u, 0, "N° COMPTE", titre_colonne_mc4u)
            ws_mc4u.write(Firstline_Mc4u, 1, "COMPTES", titre_colonne_mc4u)
            ws_mc4u.write(Firstline_Mc4u, 2, "Mensuel", titre_colonne_mc4u)
            ws_mc4u.write(Firstline_Mc4u, 3, "CUMUL", titre_colonne_mc4u)
            # set hauteur ligne
            ws_mc4u.set_default_row(12.75)
            for codemc4u, pnl_info in dictval.items():

                for ligneMc4u, build_Mc4u in line_tableau.items():
                    if codemc4u == build_Mc4u['mc4u']:
                        codemc4u = str(codemc4u).zfill(3)
                        ws_mc4u.write(Firstline_Mc4u+ligneMc4u, 0, codemc4u,  build_Mc4u['formatmc4u']['f_code'] )
                        ws_mc4u.write(Firstline_Mc4u+ligneMc4u, 1, pnl_info['libelle'], build_Mc4u['formatmc4u']['f_normal'] )
                        if pnl_info['montant'] == 0:
                            ws_mc4u.write(Firstline_Mc4u+ligneMc4u, 2, build_Mc4u['montantmc4u'], build_Mc4u['formatmc4u']['f_normal'] )
                        else:
                            ws_mc4u.write(Firstline_Mc4u+ligneMc4u, 2, pnl_info['montant'], build_Mc4u['formatmc4u']['f_normal'] )
                        if pnl_info['montant_cumul'] == 0:
                            ws_mc4u.write(Firstline_Mc4u+ligneMc4u, 3, build_Mc4u['montantmc4u_cumul'], build_Mc4u['formatmc4u']['f_normal'])
                        else:
                            ws_mc4u.write(Firstline_Mc4u+ligneMc4u, 3, pnl_info['montant_cumul'], build_Mc4u['formatmc4u']['f_normal'])
  
    wb_pnl.close()
    wb_mc4u.close()
    os.system("start excel.exe "+os.path.join(tempfile.gettempdir(), nomsociete.replace(' ', '_')+"_PandL.xlsx"))
    os.system("start excel.exe "+os.path.join(tempfile.gettempdir(), nomsociete.replace(' ', '_')+"_Mc4u_"+periode_selected+".xlsx"))

if __name__ == "__main__":
    from LecteurTxt import take_value_file, desired_parameter,undesirable_parameter
    from GenerateurPnL_Mc4U import generateur_PnL_Mc4u
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
   
    c = generateur_PnL_Mc4u(f)
#  datetime.datetime(2019, 10, 1, 0, 0, 0, 0)
    excel_pnl_mc4u(c , 'Janvier 2019')