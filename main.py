from PyQt5 import QtCore, QtGui, QtWidgets
from openfile import Ui_MainWindow
from LecteurTxt import take_value_file, desired_parameter, undesirable_parameter
from GenerateurPnL_Mc4U import generateur_PnL_Mc4u, formatage
from GenerateurExcel_PnL_Mc4u import excel_pnl_mc4u
import sys
import os
import tempfile
import locale
import logging


logging.basicConfig(filename='Rapport_logg.log', level=logging.INFO, format='%(asctime)s - %(message)s')
locale.setlocale(locale.LC_TIME, '')

class Pnl_Mc4u_Refactor(QtWidgets.QMainWindow):
    def __init__(self, title="default", Parent=None):
        super(Pnl_Mc4u_Refactor, self).__init__(Parent)
        logging.debug("Début création IHM")
        self.ui = Ui_MainWindow()
        # self.ui.setWindowIcon(QtGui.QIcon("nticon.png"))
        self.ui.setupUi(self)
        self.tempfile = ""
        self.pathtxt = ""
        self.nomSociete = ""
        self.donnees_a_injecter = ""
        self.ui.openfile.setStyleSheet('background-color: #F39100;')
        # Récupère le fichier temporaire où est stocké les infos de la dernière utilisation
        for f in os.listdir(tempfile.gettempdir()):
            if f.startswith('pnl_mc4u_newton_expertise'):
                self.tempfile = tempfile.gettempdir()+'\\'+f

        if self.tempfile == "":
            x = tempfile.NamedTemporaryFile(
                prefix='pnl_mc4u_newton_expertise', suffix='.txt', delete=False)
            self.tempfile = x.name
        # Dernier path utilisé :
        with open(self.tempfile, "r") as f:
            save = f.read()
            if save != "" and os.path.isdir(save):
                self.pathtxt = save
            else:
                self.pathtxt = "c://"

        # # # # # # # # # # # # # # # # # # # # # # # # #
        # Définition des signaux de la fenêtre.         #
        # # # # # # # # # # # # # # # # # # # # # # # # #
        self.ui.openfile.clicked.connect(self.openfile)
        self.ui.bouton_valider.clicked.connect(self.valide)

        logging.debug("fin création IHM")
    #~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
    # Récupération des infos
    def openfile(self):
        self.ui.comboBox.clear()
        file_periode = []
        filetxt = QtWidgets.QFileDialog.getOpenFileName(self, "open", self.pathtxt)
        
        if filetxt[0]:
            try:
                with open(self.tempfile, "w") as f:
                    f.write(str(os.path.split(filetxt[0])[0]))
                self.donnees_a_injecter = ""
                fichiertxt = filetxt[0]
                formater = {}
                formater['type'] = (0, 1)
                formater['num_compte'] = (1, 9)
                formater['date'] = (16, 20)
                formater['d_c'] = (41, 42)
                formater['montant'] = (42, 55)
                formater['code_analytique'] = (79, 89)
                donnee_voulu = {}
                donnee_exclu = {}
                donnee_voulu['type'] = 'M'
                donnee_exclu['code_analytique'] = '          '
                logging.debug('Lecture du ')
                logging.debug("lecture du fichier")
                donnees_analytique_brutes = take_value_file(fichiertxt, formater)
                logging.debug('Fin lecture fichier')
                donnees_analytique_brutes = desired_parameter(
                    donnees_analytique_brutes, dictvalue=donnee_voulu)

                donnees_analytique_brutes = undesirable_parameter(
                    donnees_analytique_brutes, dictvalue=donnee_exclu)

                self.donnees_a_injecter = generateur_PnL_Mc4u(donnees_analytique_brutes)
                if self.donnees_a_injecter:
                    for periode in self.donnees_a_injecter.keys():
                        file_periode.append(periode)
                    file_periode.sort()
                    i=0
                    for periode in file_periode:
                        file_periode[i] = periode.strftime("%B"+' '+"%Y").capitalize()
                        i+=1

                    self.ui.comboBox.setEnabled(True)
                    self.ui.comboBox.addItems(file_periode)
                    self.ui.bouton_valider.setEnabled(True)
                    self.ui.bouton_valider.setStyleSheet('background-color: #F39100;')
                    self.ui.comboBox.setStyleSheet('background-color: white; selection-background-color:#F39100;')
                else:
                    QtWidgets.QMessageBox().warning(self, "Erreur", "Merci de sélectionner le fichier créer de l'export 'ASCII' ayant pour extention .txt.")
            except Exception as e :
                logging.error(f"Erreur de fichier : {e}")
                QtWidgets.QMessageBox().warning(self, "Erreur", "Merci de sélectionner le fichier créer de l'export 'ASCII' ayant pour extention .txt.")
        else:
            pass
    def valide(self):
        if self.ui.lineEdit.text().replace(' ','').isalnum() or self.ui.lineEdit.text()=="":
            try:
                if self.ui.comboBox.currentText() != "":
                    QtCore.QCoreApplication.instance().quit()
                    nom_societe = self.ui.lineEdit.text()
                    periodemc4u = self.ui.comboBox.currentText()
                    excel_pnl_mc4u(self.donnees_a_injecter , periodemc4u, nom_societe)

                else: 
                    QtWidgets.QMessageBox().warning(self, "Erreur", "Merci de sélectionner le fichier créer de l'export 'ASCII' ayant pour extention .txt.")
                    self.ui.openfile.setStyleSheet("border-style: outset;border-color: red; border-width: 12px;")
            except Exception as e :
                logging.error(f"Erreur Génération Excel : {e}")

        else:
            QtWidgets.QMessageBox().warning(self, "Erreur", "Merci de saisir un nom d'entreprise au format alphanumérique.")
        self.ui.bouton_valider.setStyleSheet('background-color: white;')

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    w = Pnl_Mc4u_Refactor()
    w.show()
    sys.exit(app.exec_())
