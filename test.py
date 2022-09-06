class rectangle:
    def __init__(rect, length, breadth):
     rect.length = length
     rect.breadth = breadth
    def arearect(rect):
        print( rect.length * rect.breadth )

class circle:
    def __init__(cir, radius):
     cir.radius = radius
    def areacir(cir):
        print( 3.142 * cir.radius * cir.radius )
    
r1 = circle(1)
lb = rectangle(2, 3)
r1.areacir()
lb.arearect()