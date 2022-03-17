"""
Nous allons récupérer la valeur clé "prenom"
le script doit donc retourner la chaine de caractères 'Pierre'
"""

employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
print(employes['01']['identite']['prenom'])

# 2e methode----meilleur methode-------------------------------------------------------------
print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))

"""
EXPLICATION

Bien que cette ligne de code semble complexe, elle ne l'est pas tant que ça, car elle répète trois fois de suite le même
principe.

Pour récupérer une valeur dans un dictionnaire, on peut tout d'abord utiliser les crochets de cette façon :

employes["01"]

L'inconvénient de cette façon de faire c'est que notre script va retourner une erreur si la clé n'existe pas.

Afin de palier à ce problème nous utilisons à la place la méthode get, qui va par défaut nous retourner None si la clé
n'existe pas.

Mais encore mieux, il est possible de spécifier un élément par défaut à retourner, autre que None, si la clé n'existe pas.

C'est ce principe que nous mettons en place ici. Nous récupérons la première clé et si celle-ci n'existe pas, nous
retournons un dictionnaire vide :

employes.get("01", {})

Ainsi, nous pouvons chaîner plusieurs get à la suite, sans risquer de faire planter le script. En effet, si nous ne
retournions par de valeur par défaut et que la clé n'existe pas dans le dictionnaire, la 2e méthode get ne
fonctionnerait pas car elle s'exécuterait sur None.

Donc si la première clé n'est pas trouvée, le get va agir sur un dictionnaire vide et ainsi de suite, évitant tout
risque d'erreur.

POINTS IMPORTANTS À RETENIR

Pour récupérer la valeur associée à une clé dans un dictionnaire, on peut utiliser la fonction get, qui permet de spécifier une valeur par défaut à retourner si la clé n'est pas trouvée.
"""
