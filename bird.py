class bird:

    def _init_(self):
        print("bird is ready")

    def whoisThis(self):
        print("bird")

    def swim (self):
        print("swim faster")

class penguin(bird) :

    def _init_(self):
         super()._init_()
         print("penguin is ready")

    def  whoisThis(self):
        print("penguin")

    def run(self):
        print("run penguin")

peggy = penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()