import player
import initial_screen

def main():
    if initial_screen.init_screen() == 1:
        current_player = player.create_player()
        player.player_info(current_player)

if __name__ == "__main__":
    main()
