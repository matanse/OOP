import datetime


class WriteToFile(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_line(self, data):
        file = open(self.file_name, 'a')
        file.write(data + '\n')
        file.close()


class LogFile(WriteToFile):
    def write(self, text):
        date_time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.write_line(f'{date_time_str} : {text}')


class DelimFile(WriteToFile):
    def __init__(self, file_name, separator):
        super(DelimFile, self).__init__(file_name)
        self.separator = separator

    def write(self, this_list):
        for index in range(len(this_list)):
            if self.separator in this_list[index]:
                this_list[index] = f'"{this_list[index]}"'
        line = self.separator.join(this_list)
        self.write_line(line)
