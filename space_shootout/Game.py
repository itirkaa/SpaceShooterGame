import arcade
from space_shootout.Spaceshooter import SpaceShooter


def play():
    app = SpaceShooter()
    app.setup()
    arcade.run()