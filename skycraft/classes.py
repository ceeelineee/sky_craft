from ursina import *
from color_schemes import color_scheme

scale = 40

class Voxel(Button):
    def __init__(self, grounded, position = (0, 0, 0), color = color.rgba(color_scheme[1][0],
                                                                          color_scheme[1][1],
                                                                          color_scheme[1][2],
                                                                          color_scheme[1][3])):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'sky_sunset',
            color = color
        )
        self.grounded = grounded
        
                
    def input(self,key):
        global theme
        if self.hovered:
            self.highlight_color = color.rgba(color_scheme[2][0],
                                            color_scheme[2][1],
                                            color_scheme[2][2],
                                            color_scheme[2][3])
            if key == 'left mouse down':
                voxel = Voxel(False, self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)
        
        
class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'cube',
            color = color.rgba(color_scheme[0][0],
                                color_scheme[0][1],
                                color_scheme[0][2],
                                color_scheme[0][3]),
			texture = 'sky_sunset',
            collider = 'box',
            position = (0, scale*5, 0),
			scale = (scale, scale*10, scale),
			double_sided = True)
    
  