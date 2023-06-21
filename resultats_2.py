hematies =0
hemoglobines =0
hematocrites =0
VGM =0
TCMH =0
CCMH =0
Leucocytes =0
neutrophiles =0
eosinophiles =0
basophiles =0
Lymphocytes =0
Monocytes =0
Cholesterol =0
Triglycerides =0
HDL =0
Glycemie =0
Sodium =0
potassium =0
creatinine =0
DFG =0
bilirubine =0
TGO =0
TGP =0
gamma =0
PAL =0
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

@app.route('/formulaire', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        hematies = request.form.get('hematies')
        hemoglobines = request.form.get('hemoglobines')
        hematocrites = request.form.get('hematocrites')
        VGM = request.form.get('VGM')
        TCMH= request.form.get('TCMH')
        CCMH = request.form.get('CCMH')
        Leucocytes = request.form.get('Leucocytes')
        neutrophiles = request.form.get('neutrophiles')
        eosinophiles = request.form.get('eosinophiles')
        basophiles = request.form.get('basophiles')
        Lymphocytes = request.form.get('Lymphocytes')
        Monocytes = request.form.get('Monocytes')
        Plaquettes = request.form.get('Plaquettes')
        Cholesterol = request.form.get('Cholesterol')
        Triglycerides = request.form.get('Triglycerides')
        HDL = request.form.get('HDL')
        Glycemie = request.form.get('Glycemie')
        Sodium = request.form.get('Sodium')
        Potassium = request.form.get('Potassium')
        Creatinine = request.form.get('Creatinine')
        MRD = request.form.get('MRD')
        CDKEPI = request.form.get('CDKEPI')
        Bilirubine = request.form.get('Bilirubine')
        TGO = request.form.get('TGO')
        TGP = request.form.get('TGP')
        Gamma = request.form.get('Gamma')
        PAL = request.form.get('PAL')
        Ferritine = request.form.get('Ferritine')
        TSH = request.form.get('TSH')
        return 
       

#Création d'une boucle type pour analyse d'un résultat

if hematies_min >= hematies <= hematies_max :
    print("Votre taux de {format} est normal")
elif hematies <= hematies_min : 
    print("Votre taux de {name} est trop bas")
elif hematies >= hematies_max :
    print("Votre taux de {name} est trop elevé")


#Création du reste des boucles

if hemoglobine_min >= hemoglobines <= hemoglobine_max :
    print("Votre taux de {name} est normal")
elif hemoglobines < hemoglobine_min : 
    print("Votre taux de {name} est trop bas")
elif hemoglobines > hemoglobine_max :
    print("Votre taux de {name} est trop elevé")

if hematocrites_min >= hematocrites<= hematocrites_max :
    print("Votre taux de {name} est normal")
elif hematocrites< hematocrites_min : 
    print("Votre taux de {name} est trop bas")
elif hematocrites > hematocrites_max :
    print("Votre taux de {name} est trop elevé")    

if VGM_min >= VGM <= VGM_max :
    print("Votre taux de {name} est normal")
elif VGM < VGM_min : 
    print("Votre taux de {name} est trop bas")
elif VGM > VGM_max :
    print("Votre taux de {name} est trop elevé")    

if TCMH_min>= TCMH <= TCMH_max :
    print("Votre taux de {name} est normal")
elif TCMH< TCMH_min : 
    print("Votre taux de {name} est trop bas")
elif TCMH > TCMH_max :
    print("Votre taux de {name} est trop elevé") 

if CCMH_min>= CCMH <= CCMH_max :
    print("Votre taux de {name} est normal")
elif CCMH< CCMH_min : 
    print("Votre taux de {name} est trop bas")
elif CCMH > CCMH_max :
    print("Votre taux de {name} est trop elevé") 

if leucocytes_min>= Leucocytes <= leucocytes_max :
    print("Votre taux de {name} est normal")
elif Leucocytes< leucocytes_min : 
    print("Votre taux de {name} est trop bas")
elif Leucocytes > leucocytes_max :
    print("Votre taux de {name} est trop elevé") 

if neutrophiles_min>= neutrophiles<= neutrophiles_max :
    print("Votre taux de {name} est normal")
elif neutrophiles < neutrophiles_min : 
    print("Votre taux de {name} est trop bas")
elif neutrophiles > neutrophiles_max :
    print("Votre taux de {name} est trop elevé") 

if neutrophiles <= neutrophiles_max : 
    print("Votre taux de {name} est normal")
else :
    print("Votre taux de {name} est trop elevé") 

if basophiles <= basophiles_max : 
    print("Votre taux de {name} est normal")
else :
    print("Votre taux de {name} est trop elevé") 

if lymphocytes_min>= Lymphocytes<= lymphocytes_max :
    print("Votre taux de {name} est normal")
elif Lymphocytes < lymphocytes_min : 
    print("Votre taux de {name} est trop bas")
elif Lymphocytes > lymphocytes_max :
    print("Votre taux de {name} est trop elevé") 

if monocytes_min>= Monocytes<= monocytes_max :
    print("Votre taux de {name} est normal")
elif Monocytes < monocytes_min : 
    print("Votre taux de {name} est trop bas")
elif Monocytes > monocytes_max :
    print("Votre taux de {name} est trop elevé") 


if Cholesterol <= cholesterol_max : 
    print("Votre taux de {name} est normal")
else :
    print("Votre taux de {name} est trop elevé") 

if Triglycerides <= triglycerides_max : 
    print("Votre taux de {name} est normal")
else :
    print("Votre taux de {name} est trop elevé") 

if HDL >= HDL_min : 
    print("Votre taux de {name} est normal")
else :
    print("Votre taux de {name} est trop bas") 

if glycemie_min>= Glycemie<= glycemie_max :
    print("Votre taux de {name} est normal")
elif Glycemie < glycemie_min : 
    print("Votre taux de {name} est trop bas")
elif Glycemie > glycemie_max :
    print("Votre taux de {name} est trop elevé") 

if sodium_min>= Sodium<= sodium_max :
    print("Votre taux de {name} est normal")
elif Sodium < sodium_min : 
    print("Votre taux de {name} est trop bas")
elif Sodium > sodium_max :
    print("Votre taux de {name} est trop elevé") 

if potassium_min>= potassium<= potassium_max :
    print("Votre taux de {name} est normal")
elif potassium < potassium_min : 
    print("Votre taux de {name} est trop bas")
elif potassium > potassium_max :
    print("Votre taux de {name} est trop elevé") 

if creatinine_min>= creatinine <= creatinine_max :
    print("Votre taux de {name} est normal")
elif creatinine < creatinine_min : 
    print("Votre taux de {name} est trop bas")
elif creatinine > creatinine_max :
    print("Votre taux de {name} est trop elevé") 



if DFG_min>= DFG <= DFG_max :
    print("Votre taux de {name} est normal")
elif DFG < DFG_min : 
    print("Votre taux de {name} est trop bas")
elif DFG > DFG_max :
    print("Votre taux de {name} est trop elevé") 


if bilirubine_min>= bilirubine <= bilirubine_max :
    print("Votre taux de {name} est normal")
elif bilirubine < bilirubine_min : 
    print("Votre taux de {name} est trop bas")
elif bilirubine > bilirubine_max :
    print("Votre taux de {name} est trop elevé") 


if TGO_min>= TGO <= TGO_max :
    print("Votre taux de {name} est normal")
elif TGO < TGO_min : 
    print("Votre taux de {name} est trop bas")
elif TGO > TGO_max :
    print("Votre taux de {name} est trop elevé") 


if TGP <= TGP_max : 
    print("Votre taux de {name} est normal")
else :
    print("Votre taux de {name} est trop elevé") 


if gamma_min>= gamma <= gamma_max :
    print("Votre taux de {name} est normal")
elif gamma < gamma_min : 
    print("Votre taux de {name} est trop bas")
elif gamma > gamma_max :
    print("Votre taux de {name} est trop elevé") 
 

if PAL_min>= PAL <= PAL_max :
    print("Votre taux de {name} est normal")
elif PAL < PAL_min : 
    print("Votre taux de {name} est trop bas")
elif PAL > PAL_max :
    print("Votre taux de {name} est trop elevé") 
