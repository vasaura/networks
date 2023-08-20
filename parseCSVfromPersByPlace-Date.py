#!/usr/bin/env python
# coding:utf-8
"""
Name : parseCSVfromPersByPlace-Date.py
Author : Aurelia Vasile, MSH, UCA

Created on : 18/08/2023 18:49

"""

import csv
from itertools import combinations
# library to move through the folders
import os

FILEWITHDUPLICATES = "output_data/doublons.txt"
NETWORKFILE = "output_data/networkLinks.csv"

def parseDatabaseFile (inputFileBdd):
    """
    :param inputFileBdd: csv file
    :return:
    """
    # open to read the csv file from database
    with open (inputFileBdd, "r", newline='') as f:
        fileFromBdd = csv.DictReader(f, fieldnames=None)

        #open to write the txt file with duplicates
        with open(FILEWITHDUPLICATES, "w", encoding="UTF-8") as fichierDoublon:

            #open to write the csv file for the network links
            with open(NETWORKFILE, 'w', newline='') as networkFile:
                fieldnames = ['source', 'target', "dateAndPlace"]
                writer = csv.DictWriter(networkFile, fieldnames=fieldnames)
                writer.writeheader()

                dictionary = {}

                for row in fileFromBdd:
                    # concatenate date and place for a unique value
                    concatPlaceDate = row["date_evenement"] + "_" + row["nomLieuFr"]
                    # concatenate nom, prenom, id for a unique value
                    concatNomPrenomId = row["nom"]+"_"+row["prenom"]+"_"+row["id_personne"]
                    # if the date and place is a key of the dictionary
                    if concatPlaceDate in dictionary :
                        # if the person exists in the list (as the value of the dictionary key)
                        if concatNomPrenomId in dictionary[concatPlaceDate]:
                                # writes in fichierDoublon the person and the date+place
                                fichierDoublon.write(concatNomPrenomId+", "+ concatPlaceDate+"\n")

                        # if the person doesn't exist, it will be added to the list
                        else:
                            dictionary[concatPlaceDate].append(concatNomPrenomId)

                    # if the date and place key doesn't exist
                    else:
                        # it will be created as a key in the dictionary
                        dictionary[concatPlaceDate] = [concatNomPrenomId]

                # loop over the dictionary
                for key in dictionary:
                    # if the list for each key contains more than a person, the information would be treated,
                    # else, it would be ignored
                    if len(dictionary[key]) > 1:
                        listOfMultiplesPerson = dictionary[key]
                        # for each list a combination object is created with two elements
                        comb = combinations(listOfMultiplesPerson, r=2)
                        # loop over the combination of two elements (ex ('Conio_Toussaint_1838', 'Leblanc_Pierre-Henri_1223'))
                        for i in list(comb):
                            # write into the output files containing the links of the network
                            writer.writerow({fieldnames[0]: i[0],
                                             fieldnames[1]: i[1],
                                             fieldnames[2]: key
                                             })

    return input("Traitement terminé"
                "\nLe fichier qui contient les doublons se trouve à la racine du dossier network: " +FILEWITHDUPLICATES +
                 "\nLe fichier qui contient les liens du réseau se trouve à la racine du dossier network : "+NETWORKFILE)


INPUTFILE = input("Renseigner le chemin du fichier csv qui contient l'extraction depuis la bdd : \n")

# test if the path given by users exists
while os.path.exists(INPUTFILE) == False:
    #if not, a message will be sent
    INPUTFILE = input("Chemin incorrect. Renseigner le chemin du fichier csv qui contient l'extraction depuis la bdd : \n")

# if the path is correct,  parseDatabaseFile will be called to launch the treatment
else:
    parseDatabaseFile (INPUTFILE)





