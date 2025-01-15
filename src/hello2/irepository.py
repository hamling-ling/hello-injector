from abc import ABCMeta, abstractmethod

class IRepository(metaclass=ABCMeta):
    @abstractmethod
    def get(self):
        raise NotImplementedError

class MemRepository(IRepository):
    def get(self):
        return "MemRepository"

class DBRepository(IRepository):
    def get(self):
        return "DBRepository"
