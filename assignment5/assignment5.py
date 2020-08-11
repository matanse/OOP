import os
import pickle


class ConfigPickleDict(dict):
    def __init__(self, file_name):
        self._file_name = file_name
        if not os.path.isfile(self._file_name):
            try:
                with open(self._file_name, 'w') as file_handler:
                    pickle.dump({}, file_handler)
            except IOError:
                raise IOError("File name type or path gets an error!")

        with open(self._file_name) as file_handler:
            empty_file = True
            try:
                while True:
                    item = pickle.load(file_handler)
                    self.update(item)
                    empty_file = False
            except EOFError:
                pass
        if empty_file:
            print('Empty dictunary!')

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        try:
            with open(self._file_name, 'a') as file_handler:
                pickle.dump(self, file_handler)

        except:
            print('There is a problem with file name or directory!')
            quit()

    def __getitem__(self, key):
        if key in self:
            return dict.__getitem__(self, key)
        else:
            print('        there is no "{0}" key!'.format(
                key) + '\n        available keys are: {0}'.format(self.keys()))
            quit()
