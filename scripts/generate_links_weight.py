#!/usr/bin/env python
# coding:utf-8
"""
Name : generate_links_weight.py
Author : Aurelia Vasile, MSH, UCA

Created on : 22/08/2023 18:53

"""

import csv
from itertools import combinations
from .parseCSVfromPersByPlaceDate import parseDatabaseFile
from CONSTANTES import NETWORKFILEWITHWEIGHT, DUPLICATES


def generateLinkWithWeight(INPUTFILE, DUPLICATES, NETWORKFILEWITHWEIGHT):
    # open to write the csv file for the network links containing the weight of links
    with open(NETWORKFILEWITHWEIGHT, 'w', newline='') as networkFile:
        fieldnames = ['source', 'target', "weight"]
        writer = csv.DictWriter(networkFile, fieldnames=fieldnames)
        writer.writeheader()
        # call the method which parse the csv from the database
        dictionary = parseDatabaseFile(INPUTFILE, DUPLICATES)
        countWeight = {}
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
                    if i in countWeight:
                        countWeight[i]= countWeight[i]+1
                    else:
                        if countWeight :
                            for key in countWeight.copy().keys():
                                if key[0]==i[1] and key[1]==i[0]:
                                    countWeight[key]= countWeight[key]+1
                                else:
                                    countWeight[i]=1
                        else:
                            countWeight[i]=1


        # write into the output files containing the links of the network
        for key, value in countWeight.items():

            writer.writerow({fieldnames[0]: key[0],
                         fieldnames[1]: key[1],
                         fieldnames[2]: value
                         })

    return print("Traitement terminé"
                 "\nLe fichier qui contient les doublons se trouve ici: " + DUPLICATES +
                 "\nLe fichier qui contient les liens du réseau se trouve ici : " + NETWORKFILEWITHWEIGHT)

