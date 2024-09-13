import tkinter as tk

window = tk.Tk()
window.title("Game")

WIDTH, HEIGHT = 800,600
canvas =tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="pink")
canvas.pack()

player_size = 60
player_x = WIDTH // 2 - player_size // 2 
player_y = HEIGHT // 2 - player_size // 2
player_speed = 25

player = canvas.create_rectangle(player_x, player_y, player_x + player_size,
                                 playuer_y + player_size, fill="white")

def move_player(event):
    global player_x, player_y
    if event.keysym == "Left":
        player_x = max(0,player_x - player_speed)
    elif event.keysym == "Right":
        player_x = min(WIDTH - player_size, player_x + player_speed)
    elif event.keysym == "Up":
        player_y = max(0, player_y - player_speed)
    elif event.keysym == "Down":
        player_y = min(HEIGHT - player_size, player_y + player_speed)

    canvas.coords(player, player_x, player_y,
                   player_x + player_size, player_y + player_size)
    
window.bind("Left", move_player)
window.bind("Right", move_player)
window.bind("Up", move_player)
window.bind("Down", move_player)

window.mainloop()


