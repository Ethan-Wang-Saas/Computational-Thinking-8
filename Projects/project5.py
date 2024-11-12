import codesters, random
from codesters import StageClass
stage = StageClass()

# section 1 setup
player = codesters.Sprite("catty")
player.set_size(0.25)
player.go_to(0, -200)
stage.disable_floor()
stage.set_background("moon")

gameOver = False
lives = 3
score = 0  
msg4 = codesters.Text(f"Lives remaining: {lives}", 0,230,"White")
msg5 = codesters.Text(f"Your score: {score}", 0,170,"White")
# Section 2 objects
def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250, 250)
        object_type = "milkjug" if random.random() < 0.8 else "bomb"  #choose between milk jug or bomb
        
        object = codesters.Sprite(object_type, x_position, 250)
        object.set_size(0.2)
        object.set_y_speed(-5)
    

stage.event_interval(falling_object, 0.5)

# Section 3 Collision

def collision(player, object):
    global lives, gameOver, collected_milk, score, msg4, msg5
    
    if object.get_image_name() == "milkjug":
        stage.remove_sprite(object)
        score += 10 
        stage.remove_sprite(msg5)
        msg5 = codesters.Text(f"score: {score}", 0,170,"White")
        
    

    elif object.get_image_name() == "bomb":
        stage.remove_sprite(object)
        
        lives -= 1  #lose a life when bomb
    
        stage.remove_sprite(msg4)
        msg4 = codesters.Text(f"Lives remaining: {lives}", 0,200,"White")
        
        if lives == 0: 
            player.goto(0,-220)
            gameOver = True
            msg1 = codesters.Text("donezo", 0, 0,"White")
            msg2 = codesters.Text("boom boom", -123, 47,"White")
            msg3 = codesters.Text("kablamo", 69, -100,"White")
            

player.event_collision(collision)


# Section 4 - Controls
def move_right(player):
    global gameOver
    if not gameOver:
        player.move_right(5)

def move_left(player):
    global gameOver
    if not gameOver:
        player.move_left(5)

# Set up player controls
player.event_key("right", move_right)
player.event_key("left", move_left)
