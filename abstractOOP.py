import abc


class GetSetParent(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.value = [value]

    def SetValue(self, value):
        self.value.append(value)

    def GetLastValue(self):
        return self.value[-1]

    def GetValues(self):
        return self.value

    @abc.abstractmethod
    def showdoc(self):
        return


class GetSetInt(GetSetParent):
    def SetValue(self, value=0):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).SetValue(value)

    def showdoc(self):
        print(
            f'GetSetInt object {format(id(self))}, only accepts integer values')


x = GetSetInt(5)
print(x.GetValues())

x.SetValue(3)
print(x.GetValues())
print(x.GetLastValue())
