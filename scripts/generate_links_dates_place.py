#!/usr/bin/env python
# coding:utf-8
"""
Name : generate_links_dates_place.py
Author : Aurelia Vasile, MSH, UCA

Created on : 22/08/2023 18:52

"""
import csv
from itertools import combinations

from .parseCSVfromPersByPlaceDate import parseDatabaseFile
from .CONSTANTES import NETWORKFILEWITHDATES, DUPLICATES

def generateLinksWithDatesAndPlaces(INPUTFILE):

    # open to write the csv file for the network links containing dates and places
    with open(NETWORKFILEWITHDATES, 'w', newline='') as networkFile:
        fieldnames = ['source', 'target', "dateAndPlace"]
        writer = csv.DictWriter(networkFile, fieldnames=fieldnames)
        writer.writeheader()
        # call the method which parse the csv from the database
        dictionary = parseDatabaseFile(INPUTFILE, DUPLICATES)
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
    return print("Traitement terminé"
                "\nLe fichier qui contient les doublons se trouve à la racine du dossier network: " +DUPLICATES +
                 "\nLe fichier qui contient les liens du réseau se trouve à la racine du dossier network : "+NETWORKFILEWITHDATES)





