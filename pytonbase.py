# # a,b = 25,"Neal"


# # Déclarer une variable et lui attribuer un nombre. Afficher le résultat de la multiplication de cette variable par 4
# # Déclarer une variable et lui attribuer un nombre. trouver ensuite 2 syntaxes différentes pour ajouter "1" à ce nombre. Afficher ce nombre à chaque fois que vous ajoutez "1".

# # print("je m'appelle",b, "et j'ai",a,"ans")
# # a=12
# # print(a*4)


# #d=23
# #d=d+1
# #print(d)


# #Même exercice qu'avant, mais cette fois en soustrayant "1" On peut utiliser variable= variable+1 ou utiliser variable = +=+1 
# #e=32
# #e=e-1
# #print(e)

# #Même exercice qu'avant, mais en multipliant par 2
# #f=25
# #f=f*2
# #print(f)

# #Même exercice qu'avant mais en divisant par 2
# #g=50
# #g=g/2
# # print(g)

# # Déclarer 2 variables "a" et "b", leur affecter des valeurs. Puis permuter ces variables.
# # a,b = 1,2
# # a,b = b,a
# # print(a)


# #Déclarer 2 variables prenant la meme valeur de 3 manières différentes au moins.
# # a,b = 1,1
# # a=1
# # b=1
# # a=b=1
# # b=a=1

# #Déclarer 1 variable "a" et lui affecter la valeur "10". Réaliser la suite dans l'ordre :

# #Afficher a
# #Afficher le résultat de la division de a par 2
# #Afficher le résultat entier de la division de a par 2
# #Afficher le reste de la division de a par 2
# #Afficher a puissance 3


# # a=10
# # print(a)
# # print(a/2)
# # print(a//2)
# # print(a%2)
# # print(a**3)


# # Ecrire un programme qui lit le prix HT d’un article, le nombre d’articles et qui définit une variable contenant le taux de TVA à 20%,
# # et qui fournit le prix total TTC correspondant. Se servir de la fonction "input()" pour demander a l'utilisateur de renseigner les informations.

# # prix = int(input("quel est le prix ?"))
# # nb = int(input("combien d'articles avez-vous ?"))
# # tva = (prix+nb)*0.2
# # total = prix*nb+tva
# # print("le prix de votre article est de",prix,"€","vous en avez:", nb,"ce qui vous fait",total,"€","dont", tva,"€ de TVA")





# # Ecrire une liste comportant les nombres "4" et "5" et l'afficher.
# # liste = [4,5]
# # print(liste)


# # Ecrire une liste avec 2 chaines de caractère et 2 nombres.
# # Afficher la liste
# # Afficher le premier élément de la liste
# # Afficher le type du 3eme élément de la liste

# # a = ["salut","bonjour",1,2]
# # print(a)
# # print(  a[0]  )
# # type(a[1])
# # print( type(a[2]) )

# # Créer 2 listes "x" et "y", avec 2 nombres dans chacune d'elle. Créer une troisième liste qui sera la concaténation de x et y. Afficher cette troisième liste


# # x= [1,2]
# # y= [3,4]
# # z=x+y
# # print(z)



# # Soit la liste suivante : x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# #Afficher la valeur du 4ème élément
# #Afficher les nombres entre l'indice 3 inclut et 5 exclut
# #Afficher les nombres entre l'indice 2 inclut et l'indice 8 exclut, par saut de 2
# #Afficher la longueur de la liste x
# #Affiher la valeur minimum de x
# #Afficher la valeur maximum de x
# #Afficher la somme des valeurs contenues dans la liste x
# #Supprimer les nombres entre l'indice 3 inclut et 5 exclut, afficher la liste x

# # x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(x[3])
# # print(x[3:5])
# # print(x[2:8:2])
# # len(x)
# # print(len (x))
# # min(x)
# # print(min (x))
# # max(x)
# # print(max (x))
# # sum(x)
# # print(sum(x))
# # del(x[3:5])
# # print(x)




# # Soit la liste suivante : x = ["ok", 4, 2, 78, "bonjour"]

# #Afficher le quatrième élément de la liste
# #Affecter la valeur "toto" au 2ème élément de la liste, afficher la liste

# # x= ["ok",4,2,78,"bonjour"]
# # print(x[3])
# # x[1]="toto"
# # print(x)





# #Créer un dictionnaire "x" avec les clés / valeurs suivantes :

# #"key" -> "valeur" "key2" -> "valeur2"

# #afficher x afficher la valeur de la clé "key" ajouter la valeur "toto" correspondante à la clé "titi" remplacer la valeur de la clé "titi" par "tata". 
# #afficher x. supprimer la clé "titi" et sa valeure correspondante supprimer la valeur "key" et afficher la valeure correspondante qui à été supprimée
# #afficher "x" créez un dictionnaire "y", lui affecter le dictionnaire "x" et afficher "y"

# # x={"key":"valeur","key2":"valeur2"}
# # print(x)
# # print(x["key"])
# # x["titi"]="toto"
# # x["titi"]="tata"
# # print(x)
# # del(x["titi"])
# # print(x)
# # y=x
# # print(y)






# #Ecrire un programme qui demande deux nombres à l’utilisateur et l’informe ensuite si leur produit est nul, négatif ou positif.



# #Variable n en Entier
# #Début
# #Ecrire "Entrez un nombre : "
# #Lire n
# #Si n > 0 Alors
# #Ecrire "Ce nombre est positif”
# #Sinon
# #Ecrire "Ce nombre est négatif"
# #Finsi


# # a,b = 4,10
# # if a*b > 0:
# #     print("positif")

# # elif a*b < 0:
# #     print("négatif")

# # elif a*b == 0:
# #     print("nul")


# #Ecrire un programme qui demande l'age de l'utilisateur, et qui lui dit s'il est majeur ou non

# # a = 20
# # if a >=18:
# #     print ("Vous êtes majeur")
# # elif a <18 :
# #     print ("Vous êtes mineur")

# # #Demandez un nombre à un utilisateur, créer une condition qui affichera si le nombre de l'utilisateur est comprit entre 5 et 10. 5 et 10 sont exclut 
# #(les nombres doivent donc etre 6, 7, 8 ou 9 pour que le programme afficher "vrai")


# # a = 12

# # if a > 5 and a < 10:

# #     print("vrai")
# # else :
# #     print("faux")


# # créez une boucle for qui affiche les numéros de 0 à 5

# # a = 0
# # for loop in range(5):
# #    print(a)
# #    a = a + 1

# # créez une liste de 3 mots. Parcourez la liste a l'aide d'une boucle "for" et pour chaque mot afficher le nombre de caractère du mot et le mot en question

# # a = ["Bonjour", "Merci", "Aurevoir"]
 
# # for element in a:
# #     print(element)
# #     print(len(element)) 

# #  Soit la variable a = "anticonstitutionnellement". A l'aide d'une boucle for, afficher les lettres présentes dans x.

# # a = ["anticonstitutionnellement"]

# # for element in a:
# #     print(a)
# #     print(len(element))





# # En utilisant la fonction range(), afficher tous les nombres de 0 à 5 en ordre décroissant

# # a = [0, 1, 2, 3, 4, 5]
 
# # for i in range(5,0,-1):
# #     print(i)
# # print(0)

# #  Grâce à la fonction range(1, 10), afficher tous les nombres de 1 à 3. La boucle doit s'arrêter une fois que le chiffre 3 est affiché

# # a = [1,2,3,4,5,6,7,8,9,10]

# # for i in range(1,3+1):
# #     print (i)


# # Refaire le même exercice que le précédent, mais cette fois variabiliser tous les nombres.

# # a = [1,2,3,4,5,6,7,8,9]



# # Grâce à la fonction range(1, 10), afficher tous les nombres de 1 à 9.
# # La boucle ne doit pas afficher le nombre "3" mais doit obligatoirement continuer jusqu'au bout. Le faire de 2 manières différentes.

# # a = [1,2,3,4,5,6,7,8,9,10]

# # for element in a:
# #     print(element)

# # créez une boucle for qui affiche les numéros de 0 à 5

# # a = [0,1,2,3,4,5]

# # for i in range (6) :
# #     print (i)


# # créez une liste de 3 mots. Parcourez la liste a l'aide d'une boucle "for" et pour chaque mot afficher le nombre de caractère du mot et le mot en question


# # a = ["bonjour" , "merci" , "stp"]

# # for element in a:
# #     print(element)
# #     print(len(element)) 


# # Soit la variable x = "anticonstitutionnellement". A l'aide d'une boucle for, afficher les lettres présentes dans x.
  
# # x = ["anticonstitutionnellement"]

# # for element in x:
# #     print(x)
# #     print(len(element))

# #  Soit la liste suivante : x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. parcourez l'ensemble pour afficher tous les nombres

# # x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # for nombre in x:
# #     for liste in nombre:
# #         print(liste)


# #    Soit la liste suivante : x = [1,10,20,30,40,50]. Définissez a et b, 2 variables prenant chacune la somme des nombres de la liste x.
# #     Les 2 sommes doivent être calculées différemment. Afficher a et b 

# # x = [1,10,20,30,40,50]
# # cpt = 0
# # for element in x: 
# #     print(element)
# #     cpt = cpt + element
# # print(cpt)


# #En utilisant la fonction range(), afficher tous les nombres de 0 à 5 en ordre décroissant.

# # a = [0,1,2,3,4,5]

# # for i in range(5,0,-1):
# #     print(i)
# # print(0)

# # Grâce à la fonction range(1, 10), afficher tous les nombres de 1 à 3. La boucle doit s'arrêter une fois que le chiffre 3 est affiché.

# # a = [1,2,3,4,5,6,7,8,9,10]

# # for i in a :
 
# #     if i in range (0,4) :
# #         print(i)





# #définir une variable et lui attribuer un nombre. Afficher cette variable

# # a = 1 
# # print(a)


# #  définir 2 variables : 1 contenant un age en nombre et l'autre contenant votre prénom. 
# #  Créez une troisième variable qui devra contenir la phrase suivante : "Je suis [NOM] et j'ai [AGE] ans." Enfin, afficher cette dernière variable


# # a = 25
# # b = "Dylan"
# # c = "je m'appelle",b, "et j'ai",a,"ans"
# # print("je m'appelle",b, "et j'ai",a,"ans")

# #Refaire l'exercice précédent, mais cette fois déclarer les 2 premières variables sur une seule ligne

# #a,b = 25,"Dylan"
# #c = "je m'appelle",b, "et j'ai" ,a, "ans"
# #print("je m'appelle",b, "et j'ai" ,a, "ans")



# # Déclarer une variable et lui attribuer un nombre. Afficher le résultat de la multiplication de cette variable par 4.

# #a = 4 
# #a = a*4
# #print(a)



# #Déclarer une variable et lui attribuer un nombre. trouver ensuite 2 syntaxes différentes pour ajouter "1" à ce nombre. Afficher ce nombre à chaque fois que vous ajoutez "1".


# #a = 1 
# #a = a+1
# #print(a)


# #Même exercice qu'avant, mais cette fois en soustrayant "1"
# #a = 6 
# #a = a-1
# #print(a)


# #Même exercice qu'avant, mais en multipliant par 2

# #a = 5
# #a = a*5
# #print(a)

# #a = 10
# #a = a/2
# #print(a)


# #Déclarer 2 variables "a" et "b", leur affecter des valeurs. Puis permuter ces variables.

# #a,b = 1,2
# #a,b= b,a
# #print(a)



# #Déclarer 2 variables prenant la meme valeur de 3 manières différentes au moins. 

# #a,b = 1,1
# #a = 1
# #b = 1
# #a = b = 1
# #b = a = 1



# #Déclarer 1 variable "a" et lui affecter la valeur "10". Réaliser la suite dans l'ordre :

 #Afficher "a"
 #Afficher le résultat de la division de a par 2
 #Afficher le résultat entier de la division de a par 2
 #Afficher le reste de la division de a par 2
 #Afficher a puissance 3


 # a = 10 
 # a = a/2
 # print(a)
 # a = a%2
 # print(a)



 #L'ensemble des exercices qui vont suivre sont destinés à parcourir une grande diversités de concepts sur les classes. 
 #Ces exercices sont à faire dans l'ordre, et pour chaque exercice, vous repartirez du code réalisé dans l'exercice précédant.

 #1 - Créez une classe "Carre", prennant en paramètre un élément "côté", représentant la longueur d'un côté en cm.

 #2 - A la fin de votre fichier, ajouter une condition permettant d'exécuter le code qui sera dans la condition si le fichier de la classe est appelé directement.
 #  Afficher "carré" lors de l'exécution du script.

 #A noté que pour la suite des exercices, vous serez ammené à modifier cette partie afin de tester les fonctionnalités que vous aurez développé.

 #De même pour la simplification des énnoncés à venir, nous appellerons cette partie du code, la partie "test".

 #3 - Créez une méthode "perimeter" qui va retourner la valeur du périmètre. Ajouter un attibut "perimeter" qui sera défini lors de l'instanciation de la classe "carre".

 #Dans la partie "test", créer une instance de "carre" et afficher le périmètre calculé

 #4 - Créez une méthode "area" qui va retourner l'aire du carré. Ajouter un attribut "area" qui sera défini lors de l'instanciation de la classe "carre". 
 # Dans la partie "test", créer une instance de carre et afficher l'aide calculé

#5 - Surchargez la méthode de représentation de la classe "Carre" pour afficher la phrase suivante
#  : "Le carré à un côté d'une longueur de Xcm, une aire de Xcm2 et un périmètre de Xcm." grâce à la fonction "print()".
#  Utilisez la fonction "print()" sur votre objet dans la partie "test".

#6 - Créez une fonctino "factor", qui va permettre de retourner un carré "x" fois + grand que celui en cours.

#Testez la fonctionalité

#7 - Créez une fonction permettant d'aditionner 2 carré, de telle manière que la syntaxe suivante "Carre(2) + Carre(3)" donne une résultat de "Carre(5)"

#Testez la fonctionnalité

#8 - Refaire la même chose que pour l'exercice n°7, mais avec une soustraction

#9 - Créer une fonction qui permet de retourner un entier lors de l'utilisation de la fonction "int(Carre(2))", de telle sorte que la longueur du côté soit retournée (dans notre cas "2")

#10 - Surchargez la méthode permettant de réaliser l'opération suivante : "Carre(2) < Carre(3)", et qui retourne True ou False en se basant sur la longueur des côtés de chaque carré.
#  Testez l'opérateur

#11 - Recommencer pour tous les opérateurs suivants :

#">"
#"<="
#">="
#"=="
#"!=" Pour chacune de ces fonctions, testez les opérateurs
#12 - Créer un attribut de classe "count" qui sera incrémenté à chaque instanciation de la classe "Carre". Dans la partie test, créer un objet "a" de la classe "Carre", afficher "count".
# Créer un deuxième objet "b" de la classe "Carre". Afficher "count" de l'objet "a".



# class Carre:
#   count = 0
#     def __init__(self, nb_cote, taille_cote):
#         self.nb_cote = nb_cote
#         self.taille_cote = taille_cote

#     def calculate_perimeter(self):
#       return self.nb_cote * self.taille_cote
    
#     def calculate_area(self):
#       return self.taille_cote * self.taille_cote

#     def factor(self):
#       return (self.nb_cote * self.taille_cote) * multi

#     def count(self):
#       return type(self)ct = count
#         count += 1
    
# """
#     def int(self):
#       return (self.nb_cote)

#     def Comp(self):
#       if self.taille_cote > C2.taille_cote2:
#         print("True")
#       else:
#         print("False")
# """

# if __name__ == "__main__":

#     a = int(input("Entrer Nombre de coter : "))
#     b = int(input("Entrer Tailler des coter : "))
#     d = int(input("Entrer Tailler des coter : "))

#     C = Carre(a, b)
#     C2 = Carre(a, d) 

#     multi = int(input("Entrer : "))
# #   multi2 = int(input("Entrer : "))

#     print(C.nb_cote)
#     print(C.taille_cote)
#     print(C.calculate_perimeter())
#     print(C.calculate_area())

#     print(C2.nb_cote)
#     print(C2.taille_cote)
#     print(C2.calculate_perimeter())
#     print(C2.calculate_area())
#     print(C.count())

#     print("Le carré n°1 est", multi, "fois plus grand, soit", C.factor(), "cm")
#     print("Les cotés du carré ont une longueur de", C.taille_cote,"cm, une aire de", C.calculate_area(),"cm², et un périmètre de", C.calculate_perimeter(),"cm.")

# """
# class Carre2:
   
#   def __init__(self, nb_cote2, taille_cote2):
#     self.nb_cote2 = nb_cote2
#     self.taille_cote2 = taille_cote2

#   def calculate_perimeter2(self):
#     return self.nb_cote2 * self.taille_cote2
  
#   def calculate_area2(self):
#     return self.taille_cote2 * self.taille_cote2

#   def factor2(self):
#     return (self.nb_cote2 * self.taille_cote2) * multi2
#   print(C2.nb_cote2)
#   print(C2.taille_cote2)
#   print(C2.calculate_perimeter2())
#   print(C2.calculate_area2())
#   print(C.int())
#   print(C.Comp())


#   print("Le carré n°2 est", multi2, "fois plus grand, soit", C2.factor2(), "cm")
#   print("Les cotés du carré ont une longueur de", C2.taille_cote2,"cm, une aire de", C2.calculate_area2(),"cm², et un périmètre de", C2.calculate_perimeter2(),"cm.")
  

#   print("Les deux carré additionnés ont un périmètre de", C.calculate_perimeter() + C2.calculate_perimeter2(),"cm")
#   print("Les deux carré soustrait ont un périmètre de", C.calculate_perimeter() - C2.calculate_perimeter2(),"cm")
# """





# 15 - Créer 2 listes "x" et "y", avec 2 nombres dans chacune d'elle. Créer une troisième liste qui sera la concaténation de x et y. Afficher cette troisième liste

# x = [1,2]
# y = [3,4]
# z = x + y 
# print (z)

# 16 - Soit la liste suivante : x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Afficher la valeur du 4ème élément
# Afficher les nombres entre l'indice 3 inclut et 5 exclut
# Afficher les nombres entre l'indice 2 inclut et l'indice 8 exclut, par saut de 2
# Afficher la longueur de la liste x
# Affiher la valeur minimum de x
# Afficher la valeur maximum de x
# Afficher la somme des valeurs contenues dans la liste x
# Supprimer les nombres entre l'indice 3 inclut et 5 exclut, afficher la liste x



# x = [0,1,2,3,4,5,6,7,8,9]

#print (x[3])
#print (x[3:5])
#print (x[2:8:2])

# print (len(x))
# print (min(x))
# print (max(x))
# print (sum(x))
# del(x[3:5])
# print (x)

# x = ["ok", 4, 2, 78, "bonjour"]

# Afficher le quatrième élément de la liste
# Affecter la valeur "toto" au 2ème élément de la liste, afficher la liste

# print (x[3])
# x[1]="toto"
# print (x)

# Créez une liste des nombres allant de 0 à 5, le faire de 2 manières possible et afficher les résultats
#  a = [0,1,2,3,4,5]
#  print (a)


# 19 - Créer un dictionnaire "x" avec les clés / valeurs suivantes :

#  "key" = "valeur" "key2" = "valeur2"

# afficher x afficher la valeur de la clé "key" ajouter la valeur "toto" correspondante à la clé "titi" remplacer la valeur de la clé "titi"
# par "tata". afficher x. supprimer la clé "titi" et sa valeure correspondante supprimer la valeur "key" et afficher la valeure
# correspondante qui à été supprimée afficher "x" créez un dictionnaire "y", lui affecter le dictionnaire "x" et afficher "y"

# x ={"key":"valeur","key2":"valeur2"}

# print(x["key"])
# x["titi"]="toto"
# x["titi"]="tata"
# print(x)
# del(x["titi"])
# print(x)
# y=x
# print(y)


# 20 - Créez une liste "x" de 4 tuples de forme (x, y)

# afficher x
# ajouter la string "a" à la fin de la liste, afficher x
# ajouter la string "b" à la fin de la liste d'une manière différente, afficher x
# créer une liste "y" avec les valeurs "1", "2", "3". Ajouter tous les éléments de la liste y à la liste x. Afficher x
# Ajouter "2" à l'index n°4 de la liste x, sans supprimer l'index existant, ni le remplacer. Afficher x
# Supprimer la première valeur uniquement de x qui correspond à "2". afficher x
# Afficher y
# créez une liste "z" et lui affecter les meme valeurs qu'à y, afficher z
# supprimer tous les éléments dans y, afficher y
# supprimer tous les éléments dans z, d'une manière différente, puis afficher z 


# x = ["l","y","u","j"]
# print(x)
# (x).append('a')
# print(x)
# x.insert(5,'b')
# print(x)
# y = ["1","2","3"]
# (x).append(y)
# print(x)
# x.insert(3,2)
# print(x)
# x.pop(3)
# print(x)
# print(y)
# z = ["1","2","3"]
# print (z)
# print(y)
# y.clear()
# print(y)




# 1 - Ecrire un programme qui demande deux nombres à l’utilisateur et l’informe ensuite si leur produit est nul, négatif ou positif.


# nb1=input("1er nombre:")
# print(nb1)
# nb2=input("2ème nombre:")
# print(nb2)
# x= int(nb1)+int(nb2)
# print(x)
# if x<0:print("le produit est négatif")
# elif x>0:print("le produit est positif")
# else:print("le produit est nul")

#Ecrire un programme qui demande l'age de l'utilisateur, et qui lui dit s'il est majeur ou non


# age =(input("Saisir age:"))
# print(age)
# if age >="18": 
#     print ("Vous êtes majeurs")
# else: 
#     print ("vous êtes mineurs")


#3 - Demandez un nombre à un utilisateur, créer une condition qui affichera si le nombre de l'utilisateur est comprit entre 5 et 10. 5 et 10 sont exclut
# (les nombres doivent donc etre 6, 7, 8 ou 9 pour que le programme afficher "vrai")

# a = int(input("Donnez un nombre"))
# print (a)
# if a > 5 and a < 10:
#     print("vrai")
# else:
#     print("faux")

