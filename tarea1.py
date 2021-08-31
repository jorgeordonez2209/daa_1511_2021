class NodoTarea:
    def __init__(self, value, up = None, mid = None, down = None):
        self.data = value
        self.up = up
        self.mid = mid
        self.down = down


nodoHead = NodoTarea(20, NodoTarea(23, ' ', NodoTarea(57), ' '), NodoTarea(19, ' ', ' ', NodoTarea(67, ' ', NodoTarea(99), ' ')))
print(nodoHead.data)
print(nodoHead.mid.down.mid.data)
print(nodoHead.up.mid.data)
