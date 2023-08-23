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

INPUTFILE = input("Renseigner le chemin du fichier csv qui contient l'extraction depuis la bdd : \n")

# test if the path given by users exists
while os.path.exists(INPUTFILE) == False:
    #if not, a message will be sent
    INPUTFILE = input("Chemin incorrect. Renseigner le chemin du fichier csv qui contient l'extraction depuis la bdd : \n")

# if the path is correct,  generateLinksWithDatesAndPlaces will be called to launch the treatment
else:
    method= input("Pour générer des liens avec calcul du poids tapez 1.\nPour générer des liens avec les dates et les lieu, tapez 2.")
    if int(method) == 1:
        generateLinkWithWeight(INPUTFILE)
    elif int(method)==2:
        generateLinksWithDatesAndPlaces(INPUTFILE)
    else:
        input("Methode inexistante. Veuillez taper 1 ou 2 pour lancer le traitement")