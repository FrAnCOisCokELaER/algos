import collections


# Hashmap implementation
class MyMap:
    def __init__(self, slots=8):
        self.slots = slots
        self.table = [None] * self.slots

    # return an int from
    def myhash(self, key):
        hashkey = int(key, base=32)
        return hashkey

    def add(self, key, value):
        if not isinstance(key, str):
            print('key must be a string')
            return -1
        else:
            hash = self.myhash(key)
            slot = hash % self.slots
            if self.table[slot] is None:
                dll = list()
                dll.append((key, value))
                self.table[slot] = dll
            else:
                elt = list(filter(lambda item: item[0] == key, self.table[slot]))
                if elt is not None:
                    curridx = self.table[slot].index(elt[0])
                    self.table[slot][curridx] = (key, value)
                else:
                    self.table[slot].append((key, value))

    def get(self, key):
        hash = self.myhash(key)
        slot = hash % self.slots
        for kv in self.table[slot]:
            if key in kv:
                return kv[1]


if __name__ == "__main__":
    mymap = MyMap()
    kv = ('ok', 42)
    mymap.add(*kv)
    val = mymap.get('ok')
    kv = ('ok', 73)
    mymap.add(*kv)
    print('toto')
