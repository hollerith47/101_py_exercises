from time import time

current_time = time()
# times_tour = 50000000000
# b = [i*times_tour for i in range(9999999)]
_ = [i*2 for i in range(9999999)]
# print(b)
# print(f"Temps d'exécution : {time()- a}s")
print(f"Temps d'exécution : {time()- current_time} s")
