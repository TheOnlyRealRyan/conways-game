from game2dboard import Board
import time
import random 

# Global consts
FIELD_WIDTH = 25
FIELD_HEIGHT = 20
BLOCK_SIZE = 25

# Global vars
global head_row, head_col
conway = []
head_row = []
head_col = []

def timer_fn():
    for x in conways:
        for y in x:
            # print(y)
            # print(y[0])
            head_row += y[0]
            head_col += y[1]
    print(head_row, head_col)
    
    # head_col -= 1

    # temp fix for out of bounds
    if head_col < 0 or head_col >= FIELD_WIDTH or head_row < 0 or head_row >= FIELD_HEIGHT or [head_row, head_col] in conway:      
        head_col = 5


    # Conway Logic here
    if field[head_row][head_col] == 'X':
        print("a")



    field[head_row][head_col] = 'X'
    conway.insert(0, (head_row, head_col))
    last_row, last_col = conway[-1]

    # Removes the old position
    field[last_row][last_col] = None
    conway.pop()




def init_conway_setup():
    global conways, head_row, head_col
    
    conways = []
    head_row = []
    head_col = []
    
    
    field.fill(None)

    
    # Create and populate conway 2d-arrays with x,y positions
    

    for i in range(10):
        w2 = random.randint(1,FIELD_WIDTH-1)
        h2 = random.randint(1,FIELD_HEIGHT-1)
        conways.append([[h2, w2]])

    # Draw conways
    for x in conways:
        for y in x:
            # print(y)
            field[y[0]][y[1]] = 'X'  # Draw the conway


    field.start_timer(3000)    

# Board setup
field = Board(FIELD_HEIGHT, FIELD_WIDTH)
field.cell_size = BLOCK_SIZE
field.title = "Conways Game of Life"
field.cursor = None                         # Hide the cursor
field.margin = 10
field.grid_color = "dark sea green"
field.margin_color = "dark sea green"
field.cell_color = "PaleGreen4"
# field.on_key_press = kbd_fn
field.on_timer = timer_fn # conway logic here?
init_conway_setup()
field.show()





