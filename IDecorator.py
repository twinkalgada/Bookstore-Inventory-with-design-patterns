from abc import abstractmethod
from Commands.ICommand import ICommand


class IDecorator(ICommand):
    def __init__(self, ICommand):
        self.icommand = ICommand

    @abstractmethod
    def execute(self, Book):
        pass
