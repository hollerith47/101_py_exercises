"""
Créer une classe pour manipuler des chemins
"""
import os


class Path(str):
    @property
    def ext(self):
        return os.path.splitext(self)[-1]
    
    def dirname(self):
        return Path(os.path.dirname(self))
    
    @property
    def name(self):
        basename = os.path.basename(self)
        name = os.path.splitext(basename)[0]
        return name


s = Path("/Users/thibh/Documents/test.txt")
print(s.dirname().dirname())
print(s.dirname())
print(s.name)
print(s.ext)
