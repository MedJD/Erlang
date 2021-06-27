# Erlang B Calculator

## Mode d'utilisation:

### pour calculer A:

faut donner les valeurs de B et N,

exemple d'exécution (B=0.4% et N=27):  
`python3 erlangB.py -B 0.4 -N 27`

sortie:  
`A = 16.27 Erlangs`

### pour calculer B:

faut donner les valeurs de A et N,

exemple d'exécution (A=8.44 erlangs et N=20):  
`python3 erlangB.py -A 8.44 -N 20`

sortie:  
`B = 0.0299%`

### pour calculer N:

faut donner les valeurs de A et B,

exemple d'exécution (B=0.05% et A=30.5 erlangs):  
`python3 erlangB.py -B 0.05 -A 30.5`

sortie:  
`N = 49`

## Limites d'utilisation:

### Limites pour le calcul de B:
Pas de limites

### Limites pour le calcul de A et N:
Faut pas dépasser A=200 erlangs, et N=220

## Création des fichiers data

Pour créer de nouveaux fichiers de données et pouvoir dépasser les limites, il faut exécuter le script generator_B.py en modifiants les valeurs intérieurs de minA, minN, maxA, et maxN:   


pour l'instant les fichiers collectées sont pour:  
    - minN = 1  
    - maxN = 220  
    - minA = 0.01  
    - maxA = 200  
    - stepA = 0.01 (pas de A) 
    
Alors pour dépasser ces limite, il faut changer les valeurs des min et des max, par exemple:  
    - minN = 221  
    - maxN = XXX  
    - minA = 200  
    - maxA = YYY  
    - stepA = 0.01 (pas de A) 
    
puis changer la ligne 89 du fichier erlangB.py à: while N <= XXX.  
puis exécuter le script de calcul pour génerer les fichiers comme suit: 
    
`python3 data/ErlangB/generator_B.py`  


