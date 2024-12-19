from class_A import A, C

class B(A, C):
    def __init__(self):
        A.__init__(self)
        C.__init__(self)
        self.x = 2
    
    def outputs(self):
        print(self.x)
        print(self.a)
        print(A.c)
        print(self.xxx)

if __name__ == '__main__':
    b = B()
    b.outputs()