# format: 
# 'color_name' : (sky_color, blocks_color, highlight_color)

sky_opacity = 255
block_opacity = 180
highlight_opacity = 255

colors = {
    'purple': [(255,0,255,sky_opacity), (123,44,191,block_opacity), (123,44,191,highlight_opacity)],
    'red': [(255,0,0,sky_opacity),(255,10,84,block_opacity), (255,10,84,highlight_opacity)],
    'blue': [(0,0,255,sky_opacity),(0,150,200,block_opacity), (0,150,200,highlight_opacity)],
    'green': [(0,255,0,sky_opacity),(56,176,0,block_opacity), (56,176,0,highlight_opacity)],
    'white': [(255,255,255,sky_opacity),(255,255,255,block_opacity), (255,255,255,highlight_opacity)],
}

theme = 'green'

color_scheme = colors[theme]