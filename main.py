import arcade
from Spaceshooter import SpaceShooter

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Space Shooter"


def main():
    app = SpaceShooter(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    app.setup()
    arcade.run()


# Main
if __name__ == "__main__":
    main()
