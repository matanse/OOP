class MaxSizeList(object):
    def __init__(self, max):
        self.max_size = max
        self.innerlist = []

    def push(self, obj):
        self.innerlist.append(obj)
        if len(self.innerlist) > self.max_size:
            self.innerlist.pop(0)

    def get_list(self):
        return self.innerlist


shortList = MaxSizeList(4)
shortList.push('m')
shortList.push('a')
shortList.push('t')
shortList.push('a')
shortList.push('n')

print(shortList.get_list())
