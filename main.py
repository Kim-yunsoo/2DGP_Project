from pico2d import open_canvas, delay, close_canvas
import game_framework
# import logo_mode as start_mode
import title_mode as start_mode
# import play_mode as start_mode
# import select_mode as start_mode
# import player1win as start_mode



open_canvas(1000 ,700)
game_framework.run(start_mode)
close_canvas()
