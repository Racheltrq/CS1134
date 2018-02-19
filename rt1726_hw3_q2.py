import ctypes


def make_arr(n):
    return (n * ctypes.py_object)()


class MyList:
    def __init__(self):
        self.data = make_arr(1)
        self.n = 0
        self.capacity = 1

    def append(self, val):
        if self.n == self.capacity:
            self.resize(2*self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_arr(new_size)
        for i in range(self.n):
            new_arr[i] = self.data[i]
        self.data = new_arr
        self.capacity = new_size

    def __len__(self):
        return self.n

    def __add__(self, other):
        new_MyList = MyList()
        for i in self.data:
            new_MyList.append(i)
        for i in other.data:
            new_MyList.append(i)
        return new_MyList

    def __iadd__(self, other):
        for i in other:
            self.append(i)
        return self

    def __getitem__(self, item):
        if(isinstance(item, int)):            
            if item < self.n or item > -(self.n):
                if item < 0:
                    item += self.n
            else:
                raise IndexError("invalid index")
            return self.data[item]
            '''
            elif(isinstance(item, slice)):
            if item.start == None:
                start = 0
            else:
                start = item.start
            if item.stop == None:
                stop = len(self) - 1
            else:
                stop = item.stop - 1
            if item.step == None:
                step = 1
            else:
                step = item.step
            if(start)
            '''
    def __setitem__(self, key, value):
        print(key, self.n,)
        if key < self.n or key > -(self.n):
            if key < 0:
                key += self.n
                self.data[key] = value
        else:
            raise IndexError("invalid index")

    def __mul__(self, other):
        newList = MyList()
        for i in range(self.n * other):
            newList.append(i % self.n)
        return newList

    def __rmul__(self, other):
        newList = MyList()
        for i in range(self.n * other):
            newList.append(i % self.n)
        return newList

    def __repr__(self):
        res = '['
        for i in range(self.n):
            res += str(self.data[i]) + ','
        res = res[0: -1]
        res += ']'
        return res

    def insert(self, index, val):
        if index <= self.n and index >= -self.n:
            newList = MyList()
            if self.n == self.capacity:
                newList.resize(2*self.capacity)
            else:
                newList.resize(self.capacity)
            for i in range(index):
                newList.append(self[i])
            newList.append(val)
            for i in range(index, self.n):
                newList.append(self[i])
            return newList
        else:
            raise IndexError

    def pop(self, index = None):
        if index is None:
            newList = MyList()
            newList.resize(self.capacity - 1)
            for i in range(len(self) - 1):
                newList.append(self[i])
            return newList
        else:
            if index <= self.n and index >= -self.n:
                newList = MyList()
                newList.resize(self.capacity - 1)
                for i in range(index):
                    newList.append(self[i])
                for i in range(index + 1, len(self)):
                    newList.append(self[i])
                return newList
            else:
                raise IndexError




a = MyList()
a.resize(5)
a.append(12)
a.append(5)
a.append(33)
a.append(6)
b = MyList()
b.append(7)
print(a)
#print(a + b)
#print(a[-1])
#print(2 * a)
print(a.insert(1, 4))
print(a.pop(0))
print(a + b)
