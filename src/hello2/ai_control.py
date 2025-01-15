from injector import inject

from irepository import IRepository

class AIControl():

    def __init__(self, repository: IRepository) -> None:
        self.repository = repository

    def process(self):
        print(self.repository.get())
