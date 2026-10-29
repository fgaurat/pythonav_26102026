from dataclasses import dataclass

@dataclass(slots=True,frozen=True)
class DataRectangle:

    longueur:int=1
    largeur:int=1
