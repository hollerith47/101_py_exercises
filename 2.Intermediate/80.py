"""
Vérificateur de code Python
ici nous essayons juste de voir s'il n'y a pas d'erreur de syntaxe dans notre code
( de plus ou de moins
"""

code = "print(any((('py' or 'txt') in ext for ext in ['.py', '.obj', '.json']))"

print(code.count('(') == code.count(')'))
