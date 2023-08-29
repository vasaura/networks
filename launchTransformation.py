#!/usr/bin/env python
# coding:utf-8
"""
Name : launchTransformation.py
Author : Aurelia Vasile, MSH, UCA

Created on : 23/08/2023 13:23

"""
import os
from scripts.generate_links_weight import generateLinkWithWeight
from scripts.generate_links_dates_place import generateLinksWithDatesAndPlaces
from CONSTANTES import NETWORKFILEWITHWEIGHT, NETWORKFILEWITHDATES, DUPLICATES

absolute_path = os.path.dirname(__file__)

# ask user to write the absolute path of the input file and the output folder
INPUTFILE = input("Renseigner le chemin absolu du fichier csv qui contient l'extraction depuis la bdd : \n")
OUTPUTFOLDER = input("Renseigner le chemin absolu vers le dossier qui contiendra les fichiers traités : \n")
duplicatesFile = os.path.join(OUTPUTFOLDER+ DUPLICATES)
outputWeightFile = os.path.join(OUTPUTFOLDER+ NETWORKFILEWITHWEIGHT)
outputDatePlaceFile = os.path.join(OUTPUTFOLDER+ NETWORKFILEWITHDATES)

# test if the path given by users exists
while os.path.exists(INPUTFILE) == False:
    #if not, a message will be sent
    INPUTFILE = input("Chemin incorrect. Renseigner le chemin absolu du fichier csv qui contient l'extraction de la bdd : \n")

# if the path is correct,  generateLinksWithDatesAndPlaces will be called to launch the treatment
else:
    method= input("Pour générer des liens avec calcul du poids tapez 1.\nPour générer des liens avec les dates et les lieu, tapez 2.\n")
    if int(method) == 1:
        generateLinkWithWeight(INPUTFILE, duplicatesFile,outputWeightFile)
    elif int(method)==2:
        generateLinksWithDatesAndPlaces(INPUTFILE, duplicatesFile, outputDatePlaceFile)
    else:
        input("Methode inexistante. Veuillez taper 1 ou 2 pour lancer le traitement")
