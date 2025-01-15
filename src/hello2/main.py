

from injector import Injector, Module, provider, singleton
from ai_control import AIControl
from irepository import DBRepository, IRepository, MemRepository

def configure_for_testing(binder):
    repo = MemRepository()
    binder.bind(IRepository, to=repo, scope=singleton)

def configure_for_production(binder):
    repo = DBRepository()
    binder.bind(IRepository, to=repo, scope=singleton)

class Dependency(Module):
    @singleton
    @provider
    def provide_ai_control(self, repository: IRepository) -> AIControl:
        return AIControl(repository)


if __name__ == "__main__":
    injector1 = Injector([configure_for_testing, Dependency()])
    aicon1 = injector1.get(AIControl)
    aicon1.process()

    injector2 = Injector([configure_for_production, Dependency()])
    aicon2 = injector2.get(AIControl)
    aicon2.process()
