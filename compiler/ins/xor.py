from compiler.ins import Bin
class Xor(Bin):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.name = 'xor'
    def accept(self, translator):
        return translator.visit(self)
 
