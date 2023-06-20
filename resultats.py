#Définitions des variables telles qu'écrites dans Formulaire.html
hematies = 0
hemoglobines = 0
hematocrites = 0
VGM = 0
TCMH = 0
CCMH = 0
Leucocytes = 0
neutrophiles = 0
eosinophiles = 0
basophiles = 0
Lymphocytes = 0
Monocytes = 0
Plaquettes = 0
Cholesterol = 0
Triglycerides = 0
HDL = 0
Glycemie = 0
Sodium = 0
Potassium = 0
Creatinine = 0
MRD = 0
CDKEPI = 0
Bilirubine = 0
TGO = 0
TGP = 0
Gamma = 0
PAL = 0
Ferritine = 0
TSH = 0


#créations des variables min et max pour chaque type d'analyse - Les données sont celles du laboratoire Anabio
#Possibilités de les changer 

hematies_min=3.80
hematies_max=5.90

hemoglobine_min=11.5
hemoglobine_max=15

hematocrites_min = 34
hematocrites_max = 45

VGM_min=76
VGM_max=96

TCMH_min=24
TCMH_max=34

CCMH_min=31
CCMH_max=36.5

leucocytes_min=3.80
leucocytes_max=11

neutrophiles_min=1.7
neutrophiles_max=7.5

eosinophiles_max=0.58

basophiles_max=0.11

lymphocytes_min=1
lymphocytes_max=4.8

monocytes_min=0.15
monocytes_max=1

cholesterol_max=2

triglycerides_max=1.5

HDL_min=0.4

glycemie_min=0.7
glycemie_max=1.1

sodium_min=136
sodium_max=145

potassium_min=3.5
potassium_max=5.1

creatinine_min=5.5
creatinine_max=10.2

DFG_min=15
DFG_max=90

bilirubine_min=3
bilirubine_max=12

TGO_min=5
TGO_max=34

TGP_max=55

gamma_min=9
gamma_max=36

PAL_min=25
PAL_max=100


#Récupération des données du formulaire en utilisant le framework Flask

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("Projet_perso/formulaire", methods=["POST", "GET"])
def result(id, name):
    return render_template("formulaire.html", id=id, name=name)

#Création d'une boucle type pour analyse d'un résultat

if hematies_min >= hematies <= hematies_max :
    print("Votre taux de {name} est normal")
elif hematies <= hematies_min : 
    print("Votre taux de {name} est trop bas")
elif hematies >= hematies_max :
    print("Votre taux de {name} est trop elevé")


#Création du reste des boucles

if hemoglobine_min >= hemoglobines <= hemoglobine_max :
    print("Votre taux de {name} est normal")
elif hemoglobines <= hemoglobine_min : 
    print("Votre taux de {name} est trop bas")
elif hemoglobines >= hemoglobine_max :
    print("Votre taux de {name} est trop elevé")

if VGM_min >= VGM <= VGM_max :
    print("Votre taux de {name} est normal")
elif VGM <= VGM_min : 
    print("Votre taux de {name} est trop bas")
elif VGM >= VGM_max :
    print("Votre taux de {name} est trop elevé")    