from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from classes import *

def update():
    player_pos.text = f'x: {int(player.x)}, y:{int(player.y)}, z: {int(player.z)}'
    camera.position = player.position + Vec3(0, scale//2, 0)

def input(key):
    if key == 'q':
        quit()
    if key == 'e':
        camera.enabled = True
        player.enabled = False
    if key == 'p':
        camera.enabled = False
        player.enabled = True

        
app = Ursina(fullscreen = True)

# ground voxels 
for z in range(-scale//2,scale//2):
    for x in range(-scale//2,scale//2):
        voxel = Voxel(True, (x, 0, z), color.rgba(255,255,255,0))
        
  
player = FirstPersonController()
sky = Sky()
camera = EditorCamera(rotation = (90, 0, 0), enabled = False)

player_pos = Text(
            text = f'   x: {int(player.x)}, y:{int(player.y)}, z: {int(player.z)}   ',
            origin = (0, -18),
            # text_origin = (-.5, .5),
            color = color.rgba(255, 255, 255, 200),
        )

app.run()