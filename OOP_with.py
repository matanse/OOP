class Human(object):
    def __enter__(self):
        print('This is a Human!')
        return self

    def __exit__(self, type, value, traceback):
        print(f'error type: {type}')
        print(f'error value: {value}')
        print(f'error traceback: {traceback}')

    def hey_there(self, human_name):
        print(f'Hello there new human, your name is {human_name}')


with Human() as hanna:
    hanna.hey_there('hanna')
