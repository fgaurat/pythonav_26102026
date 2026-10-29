


from abc import ABC,ABCMeta,abstractmethod



# class ICalcGeo(ABC):
class ICalcGeo(metaclass=ABCMeta):


    @property
    @abstractmethod
    def surface(self)->float:
        pass

