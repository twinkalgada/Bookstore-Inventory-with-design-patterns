class Memento:
    def __init__(self, mstate, filename=None):
        self.mstate = mstate
        if filename is None:
            filename = 'Snapshot.txt'
        self.write_to_file(mstate, filename)

    def write_to_file(self, new_data, filename):
        with open(filename, 'w') as file:
            for item in new_data:
                file.write("%s\n" % item)

