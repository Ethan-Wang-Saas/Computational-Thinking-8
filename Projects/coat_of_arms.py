###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("park")


sq1 = codesters.Square(100, 100, 200, 'Pink')
sq2 = codesters.Square(-100, 100, 200, 'LightGreen')
sq3 = codesters.Square(-100, -100, 200, 'LightBlue')
sq4 = codesters.Square(100, -100, 200, 'IndianRed')


basketball = codesters.Sprite("basketball", 100, 100)
basketball.set_size(1.5)
spotify = codesters.Sprite("spotify",-100, 100)
spotify.set_size(0.2)
taiwan = codesters.Sprite("taiwan", -100, -100)
taiwan.set_size(0.15)
saas = codesters.Sprite("cardinal", 100, -100)
saas.set_size(0.7)


msg1 = codesters.Text("Ethan Wang",0,220,"Black")
msg1.set_size(5)

msg2 = codesters.Text("Hello", 0, -220,"Black")