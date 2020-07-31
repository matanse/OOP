import abc
import datetime

datetime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')


class WriteToFile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, data, separator=""):
        last_element = data[len(data)-1]
        file = open(self.file_name, 'a')
        file.write(datetime_str + ": ")
        for element in data:
            if separator in element:
                file.write(f'"{element}"')
                if element != last_element:
                    file.write(separator)
                else:
                    file.write('\n')
            else:
                file.write(element)
                if element != last_element:
                    file.write(separator)
                else:
                    file.write('\n')
        file.close()


class LogFile(WriteToFile):
    pass


class DelimFile(WriteToFile):
    pass
