def afficher_table_multiplication(n, min=1, max=12):
    if min > max:
        return print("Erreur: min est superieur au max")
    print("Table de multiplication par", n)
    for i in range(min, max+1):
        print(f"{i} x {n} = {i * n}")


# afficher_table_multiplication(5, max=20)
afficher_table_multiplication(3, 5, 2)
