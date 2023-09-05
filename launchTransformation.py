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


# teste if the path given by users exists
while os.path.exists(INPUTFILE) == False:
    #if not, a message will be sent
    INPUTFILE = input("Chemin incorrect. Renseigner le chemin absolu du fichier csv qui contient l'extraction de la bdd : \n")

else:
    OUTPUTFOLDER = input("Renseigner le chemin absolu vers un dossier de votre choix qui contiendra les fichiers traités : \n")
    while os.path.exists(OUTPUTFOLDER) == False:
        #if not, a message will be sent
        OUTPUTFOLDER = input("Chemin incorrect. Renseigner le chemin absolu vers un dossier de votre choix qui contiendra les fichiers traités : \n")

    # if the path is correct, the treatment will be launched
    else:
        duplicatesFile = os.path.join(OUTPUTFOLDER + DUPLICATES)
        outputWeightFile = os.path.join(OUTPUTFOLDER + NETWORKFILEWITHWEIGHT)
        outputDatePlaceFile = os.path.join(OUTPUTFOLDER + NETWORKFILEWITHDATES)

        method = input("Pour générer des liens avec calcul du poids tapez 1.\nPour générer des liens avec les dates et les lieux, tapez 2.\n")
        #while the input is a string or is not 1 an 2, it will generate a message to ask the right number
        while method.isdigit()==False or (int(method) != 1 and int(method) != 2):
            method=input("Vous avez écrit: "+ str(method)+" Réponse incorrecte. Veuillez taper 1 ou 2 pour lancer le traitement")
        else:
            if int(method) == 1:
                generateLinkWithWeight(INPUTFILE, duplicatesFile, outputWeightFile)
            if int(method) == 2:
                generateLinksWithDatesAndPlaces(INPUTFILE, duplicatesFile, outputDatePlaceFile)