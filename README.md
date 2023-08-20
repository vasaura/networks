# Script qui permet de générer les liens d'un réseau à partir d'un fichier contenant des dates des lieux et des personnes. 
Le script prend en entrée un fichier csv qui contient une liste avec des dates, des lieux et des personnes et le nombre de fois que les personnes se trouvent au même lieu au même moment.
Il génère en sortie un fichier avec des liens entre chaque personne qui est présente au même moment au même endroit.

Il doit contenir au minimum les colonnes suivantes. Les noms des colonnes doivent être identiques à l'orthographie ci-dessous:
**date_evenement**,**nomLieuFr**,**nom**,**prenom**,**id_personne**
Il peut contenir d'autres colonnes qui ne seront pas traitées.
Voici un exemple avec quelques données:
```
date_evenement,nomLieuFr,nom,prenom,id_personne,countLieuCommunByPerson
1809-09-20,Agen,Mellet,Anne-Marie,120,2
1809-09-20,Agen,Fourastié,Pierre,12531,2
1809-09-04,Agen,Bellan,Barthélémy,4222,4
1809-09-04,Agen,Paillac,Jean-Michel,4421,4
1809-09-04,Agen,Suberville,François,4486,4
1809-09-04,Agen,Bellan,Bernard,4221,4
```
Le résultat attendu est un fichier csv avec des liens selon le modèle source-target
Voici la sortie attendue :
```
source,target,dateAndPlace
Mellet_Anne-Marie_120,Fourastié_Pierre_12531,1809-09-20_Agen
Bellan_Barthélémy_4222,Paillac_Jean-Michel_4421,1809-09-04_Agen
Bellan_Barthélémy_4222,Suberville_François_4486,1809-09-04_Agen
Bellan_Barthélémy_4222,Bellan_Bernard_4221,1809-09-04_Agen
Paillac_Jean-Michel_4421,Suberville_François_4486,1809-09-04_Agen
Paillac_Jean-Michel_4421,Bellan_Bernard_4221,1809-09-04_Agen
Suberville_François_4486,Bellan_Bernard_4221,1809-09-04_Agen
```
Un fichier contenant des doublons est généré automatiquement si une personne apparaît plusieurs fois au même endroit au même moment.

## Dossier output_data
Dossier dans lequel on trouve à la fin du traitement le fichier avec les liens du network et le fichier avec les doublons

## Script parseCSVfromPersByPlace-Date.py
Le script qu'il faut lancer depuis son terminal avec la commande 
`python3 parseCSVfromPersByPlace-Date.py`

Co code fonctionne avec la version Python 3.11. 

