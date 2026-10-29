


class Rectangle:

    __slots__=['_longueur','_largeur']

    _cpt = 0

    def __init__(self,longueur:int,largeur:int):
        """
        Le contructeur
        """

        self._longueur = longueur
        self._largeur = largeur
        Rectangle._cpt += 1

    @staticmethod
    def cpt():
        return Rectangle._cpt


    @classmethod
    def build_from_str(cls,value):
        # values = value.split(";") # ["3","4"]
        # longueur,largeur = [int(i) for i in values]
        # values = [int(v) for v in value.split(";")] # ["3","4"]

        return cls(*[int(v) for v in value.split(";")])


    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self,largeur):
        self._largeur = largeur
    
    @property
    def surface(self):
        return self._largeur * self._longueur

    def __del__(self):
        pass

    def __eq__(self,o):
        if not isinstance(o,type(self)):
            return False
        
        return self.longueur == o.longueur and self.largeur == o.largeur

    def __str__(self):

        return f"{__class__.__name__}: {self._longueur=}, {self._largeur=}"