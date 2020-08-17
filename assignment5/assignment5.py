import os
import pickle


class WritePickleDictToFile():
    def __init__(self, file_name):
        self._file_name = file_name
        self._file_content = {}
        if not os.path.isfile(self._file_name):
            try:
                with open(self._file_name, 'wb') as file_handler:
                    pickle.dump(self._file_content, file_handler)
            except FileNotFoundError as e:
                raise e

        with open(self._file_name, 'rb') as file_handler:
            try:
                while True:
                    item = pickle.load(file_handler)
                    self._file_content.update(item)
            except EOFError:
                pass

    def __setitem__(self, key, value):
        self._file_content.__setitem__(key, value)
        try:
            with open(self._file_name, 'ab') as file_handler:
                pickle.dump(self._file_content, file_handler)

        except:
            print('There is a problem with file name or directory!')
            quit()

    def __getitem__(self, key):
        error_message = ('there is no "{0}" key!'.format(
            key) + '\n        available keys are: {0}'.format(self._file_content.keys()))
        if key in self._file_content:
            return self._file_content.__getitem__(key)
        else:
            raise Exception(error_message)
