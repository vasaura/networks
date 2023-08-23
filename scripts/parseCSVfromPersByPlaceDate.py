#!/usr/bin/env python
# coding:utf-8
"""
Name : parseCSVfromPersByPlaceDate.py
Author : Aurelia Vasile, MSH, UCA

Created on : 18/08/2023 18:49

"""

import csv

def parseDatabaseFile (inputFileBdd, FILEWITHDUPLICATES):
    """
    :param inputFileBdd: csv file
    :return:
    """
    # open to read the csv file from database
    with open (inputFileBdd, "r", newline='') as f:
        fileFromBdd = csv.DictReader(f, fieldnames=None)

        #open to write the txt file with duplicates
        with open(FILEWITHDUPLICATES, "w", encoding="UTF-8") as fichierDoublon:

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

    return dictionary

