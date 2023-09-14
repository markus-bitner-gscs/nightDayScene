# Markus Bitner - 224973@gscs.ca - Day/Night Scene

def setup():
    size(500, 500)
    background(0, 180, 255)
    #set canvas to 500x500 with a light blue background
    noStroke()
    #removes shape outlines

    fill(255, 255, 0)
    circle(70, 70, 50)
    #draws a yellow circle for the sun
    
    fill(200, 150, 100)
    rect(0, 400, 500, 100)
    #draws a light brown rectangle for the ground
    
    fill(255, 170, 0)
    square(70, 340, 60)
    #draws an orange square on the left
    
    fill(255, 0, 255)
    square(210, 340, 60)
    #draws pink/purple square in the middle
    
    fill(0, 255, 0)
    square(350, 340, 60)
    #draws a green square on the right
    
    
def mouseClicked():
    #when any key is pressed, the background and all shapes will be redrawn with darker colours. Except for the moon, which will turn white.
    background(0, 0, 120)
    #sets bg colour to darker blue
    
    
    fill(255)
    circle(70, 70, 50)
    #draws a white circle for the moon
    
    fill(100, 50, 0)
    rect(0, 400, 500, 100)
    #draws a darker brown rectangle for the ground
    
    fill(205, 120, 0)
    square(70, 340, 60)
    #draws an orange square on the left
    
    fill(155, 0, 155)
    square(210, 340, 60)
    #draws pink/purple square in the middle
    
    fill(0, 155, 0)
    square(350, 340, 60)
    #draws a green square on the right
    
