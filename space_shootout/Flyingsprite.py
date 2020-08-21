import arcade


# Flying Sprite class
class FlyingSprite(arcade.Sprite):
    """Base class for all flying sprites
    Updates and handles behavior for clouds and enemy
    """

    def update(self):
        """Update the position of the sprites and
        Remove the sprites once it moves out of the screen
        """

        # Move the sprite
        super().update()

        # Remove if sprite goes off screen
        if self.bottom < 0:
            self.remove_from_sprite_lists()
