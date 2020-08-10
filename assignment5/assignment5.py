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

        with open(self._file_name, 'r+') as file_handler:
            empty_file = True
            print('before load')
            file_content = pickle.load(file_handler)
            print('after load')
            print(file_content)
            for line in file_handler:
                empty_file = False
                line = line.strip()
                if line == '':
                    print(
                        'one line is empty.')
                else:
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)
            if empty_file:
                print('Empty dictunary!')

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        try:
            with open(self._file_name, 'w') as file_handler:
                print(self.items())
                for key, value in self.items():
                    file_handler.write('{0}={1}\n'.format(key, value))
        except:
            print('There is a problem with file name or directory!')
            quit()

    def __getitem__(self, key):
        print(self)
        if key in self:
            return dict.__getitem__(self, key)
        else:
            raise IOError('there is no "{0}" key!'.format(
                key) + '\navailable keys are: {0}'.format(self.keys()))
