import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("grid")

s1 = codesters.Sprite("person2",0,0)
s1.set_size(0.3)

s2 = codesters.Sprite("person1",0,0)
s2.set_size(0.3)

def move_left(sprite):
    sprite.move_left(2)

def move_up(sprite):
    sprite.move_up(2)

def move_down(sprite):
    sprite.move_down(2)

def move_right(sprite):
    sprite.move_right(2)


def hide(sprite):
    sprite.hide()
    stage.wait(0.5)
    s2.show()

def show(sprite):
    sprite.show()


s1.event_key("up", move_up)

s1.event_key("down", move_down)

s1.event_key("right", move_right)

s1.event_key("left", move_left)


s2.event_key("w", move_up)

s2.event_key("s", move_down)

s2.event_key("d", move_right)

s2.event_key("a", move_left)

s2.event_key("e", hide)
