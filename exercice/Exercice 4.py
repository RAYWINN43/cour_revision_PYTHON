# Écrivez un programme Python qui accepte une chaîne et calcule le nombre de chiffres et de lettres



# Saisissez une chaîne IPSSI2024
# Lettres 5                                                                                                                    
# Chiffres 4

a='IPSSI2024'
nb_chiffres = len([i for i in a if i.isdigit()])
print(nb_chiffres)

nb_lettre = len([i for i in a if not i.isdigit()])
print(nb_lettre)