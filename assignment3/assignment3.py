class ConfigDict(dict):
    def __init__(self, file_name):
        self.__file_name = file_name
        try:
            file = open(self.__file_name, 'r')
        except IOError:
            print("IOError: file doesn't exist")
            quit()
        print(file.readlines()[0].split(','))

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        file = open(self.__file_name, 'a')
        file.write('{0}:{1},'.format(key, value))
        file.close()


# dd = ConfigDict('dict.txt')
# bb = ConfigDict('dict.txt')
# dd['a'] = 1
# dd['d'] = 1
# dd['b'] = 1
# print(dd)
# bb['p'] = 2
# bb['j'] = 2
# bb['r'] = 2
# print(dd)
# print(bb)
# pp = open('dict.txt', 'r')
# for line in pp:
#     print(line)
