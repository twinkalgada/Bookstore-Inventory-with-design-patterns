from IDecorator import IDecorator


class LogCommands(IDecorator):

    def __init__(self, ICommand):
        self.command_file = 'CommandLog.txt'
        super().__init__(ICommand)

    def write_to_file(self, new_data, filename):
        try:
            with open(filename, 'a') as file:
                new_data += "\n"
                print(new_data)
                file.write(new_data)
        except IOError:
            raise

    def execute(self, book, filename=None):
        if filename is None:
            filename = self.command_file
        result = self.icommand.execute(book)
        if result is not False:
            command_to_write = "{" + str(self.icommand) + ", \"book\":" + str(result) + "}"
            self.write_to_file(command_to_write, filename)
            return True
        else:
            return False
