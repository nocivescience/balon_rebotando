from manim import *
class Ball(Circle):
    CONFIG0={
        'radius':0.4,
        'fill_color':YELLOW,
        'fill_opacity':1,
        'color':BLUE,   
    }
    def __init__(self,**kwargs):
        Circle.__init__(self,**kwargs)
        self.velocity=np.array([2,0,0])
    def get_top(self):
        return self.get_center()[1]+self.CONFIG['radius']
class Box(Rectangle):
    CONFIG0={
        
    }
    def __init__(self,**kwargs):
        Rectangle.__init__(self,**kwargs)
class BallScene(Scene):
    CONFIG={
        
    }
    def construct(self):
        ball=Ball()
        self.play(Create(ball))
        self.wait()