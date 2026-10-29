from typing import Protocol

class ISurface(Protocol):

    @property
    def surface(self)->float:...

