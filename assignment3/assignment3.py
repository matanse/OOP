import os


class ConfigDict(dict):
    def __init__(self, file_name):
        self._file_name = file_name
        if os.path.isfile(self._file_name):
            with open(self._file_name) as file_handler:
                for line in file_handler:
                    line = line.rstrip()
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)
        else:
            print('blaaaaaaaaaaaaa')

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._file_name, 'w') as file_handler:
            for key, value in self.items():
                file_handler.write('{0} = {1}\n'.format(key, value))
