import pyautogui
import webcolors
from PIL import Image
from pynput.mouse import Listener
import time
# Posiciones de la paleta de colores en el juego
data = [(527, 146),(1787, 1084),(2441, 636),(2470, 634),(2436, 661),(2469, 665),(2500, 696),(2537, 695),(2503, 727),(2532, 729),(2437, 755),(2468, 756),(2437, 786),(2470, 784),(2435, 814),(2533, 815),(2436, 845),(2530, 846),(2515, 652),(2454, 705),(2518, 769),(2486, 830)]

def on_click(x, y, button, pressed):
    if pressed:
        print ('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        #data.append( (x,y) )
        if "{0}".format(button) == "Button.right":
        	print(data)
        	listener.stop()
        	time.sleep(5)
with Listener( on_click=on_click ) as listener:
    listener.join()

clickOrder = ["begin","end","green2","green3","green3","green1","cyan","aqua","brown1","brown2","yellow","pink","violet","orange","lightgrey","darkgrey","marine","black","green2","blue","red","white"]

def _reversedict(d: dict) -> dict:
    return {value: key for key, value in d.items()}


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = closest_colour(requested_colour)
    except ValueError:
        closest_name = "black";

    return closest_name

CSS3_NAMES_TO_HEX = {
    "white": "#e8eaea",
    "blue": "#3493cf",
    "red": "#f24728",
    "green1": "#15ed11",
    "green2": "#1fb85c",
    "green3": "#2c8c6d",
    "brown1": "#784830",
    "brown2": "#784830",
    "violet": "#9856b2",
    "yellow": "#f3c92b",
    "cyan": "#18d8f0",
    "aqua": "#48d8c0",
    "pink": "#a878c0",
    "orange": "#f07818",
    "lightgrey": "#90a8a8",
    "darkgrey": "#303030",
    "marine": "#304860",
    "black": "#181818",
}

CSS3_HEX_TO_NAMES = _reversedict(CSS3_NAMES_TO_HEX)


def select_brush_color(color):
	brushPos = data[clickOrder.index(color)]
	pyautogui.click(brushPos[0], brushPos[1])
	
def main():
	print("Begin")
	canvasResolution = (data[1][0]-data[0][0] , data[1][1]-data[0][0]);
	x = data[0][0]
	y = data[0][1]
	width = data[1][0]-data[0][0]
	xEnd = data[1][1]
	yEnd = data[1][0]
	level = 1

	im = Image.open("imagen.jpg", "r")
	im = im.resize( canvasResolution  )
	print("Resized to: ", canvasResolution )
	pyautogui.PAUSE = 0.06
	pix_val = list(im.getdata())
	#print(pix_val)

	selectedBrush = "white"
	for pixel in pix_val:
		closest_name = get_colour_name(pixel)
		if selectedBrush != closest_name:
			select_brush_color(closest_name)
			selectedBrush = closest_name
		pyautogui.click(x,y)
		x = x + 1
		if x == yEnd:
			x = data[0][0] + level
			y = y + 10
	
	#pyautogui.click(100, 100)
	#pyautogui.moveTo(100, 150)
	#pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
	input("Enter")

main()
