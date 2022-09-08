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
        return self.get_center()[1]+self.CONFIG0['radius']
    def get_bottom(self):
        return self.get_center()[1]-self.CONFIG0['radius']
    def get_right_edge(self):
        return self.get_center()[0]+self.CONFIG0['radius']
    def get_left_edge(self):
        return self.get_center()[0]-self.CONFIG0['radius']
class Box(Rectangle):
    CONFIG0={
        'height':10,
        'width':config['frame_width']-2,
        'color':BLUE_A,
    }
    def __init__(self,**kwargs):
        Rectangle.__init__(self,width=8,height=6,**kwargs)
        self.top=.5*self.CONFIG0['height']
        self.bottom=-0.5*self.CONFIG0['height']
        self.right_edge=.5*self.CONFIG0['width']
        self.left_edge=.5*self.CONFIG0['width']
class BallScene(Scene):
    CONFIG={
        
    }
    def construct(self):
        ball=Ball()
        box=Box()
        self.play(Create(ball),Create(box))
        def update_ball(ball,dt):
            ball.aceleration=np.array([0,-5,0])
            ball.velocity=ball.velocity+ball.aceleration*dt
            ball.shift(ball.velocity*dt)
            if ball.get_bottom()<=box.bottom*0.96 or ball.get_top()>=box.top*0.96:
                ball.velocity[1]=-ball.velocity[1]
            if ball.get_left_edge()<=box.left_edge or ball.get_right_edge()>=box.right_edge:
                ball.velocity[0]=-ball.velocity[0]
        ball.add_updater(update_ball)
        self.add(ball)
        ball.clear_updaters()
        self.wait(3)