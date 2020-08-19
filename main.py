import arcade
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Space Shooter"
JET_SCALING = 0.13


# Flying Sprite class
class FlyingSprite(arcade.Sprite):
    """Base class for all flying sprites
    """

    def update(self):
        """Removes the sprites
        when it moves out of screen"""

        # Move the sprite
        super().update()

        # Remove if sprite goes off screen
        if self.right < 0:
            self.remove_from_sprite_lists()


# Space Shooter Game Window Class
class SpaceShooter(arcade.Window):
    """Space shooter Game:
    Player starts on the left, and enemies appear on right
    Player can move anywhere on the screen as enemies fly towards the player
    If the two collide, the game ends
    """

    def __init__(self, width, height, title):
        """Initialize the window
        """

        # Calling parent class
        super().__init__(width, height, title)

        self.paused = False
        self.game_over = False
        self.scores = 0

        # Initializing the player
        self.player = None

        # Setting up empty sprite(objects on the screen) lists
        self.enemies_list = arcade.SpriteList()  # Stores generated enemies
        self.cloud_list = arcade.SpriteList()  # Stores clouds
        self.all_sprites = arcade.SpriteList()  # Stores all the sprites

    def setup(self):
        """Initializes game to a known starting point
        """

        # Setting background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Setting up the player
        # Image source: seekpng.com pngitem.com
        self.player = arcade.Sprite("images/spaceship.png", JET_SCALING)  # Player image
        self.player.center_y = self.height / 2  # placing player in the middle(Vertical)
        self.player.left = 10  # Placing player to left of the screen
        self.all_sprites.append(self.player)  # Appending player to all sprites list

        # Spawn a new enemy every 0.25 seconds
        arcade.schedule(self.add_enemy, 0.25)

        # Spawn a new cloud every second
        arcade.schedule(self.add_cloud, 1)

    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen

        Arguments:
            delta_time {float} -- How much time has passed since last call
        """

        # Create new enemy sprite
        enemy = FlyingSprite("images/jet.png", 0.08)

        # Set position to a random height and off screen right
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)

        # Set random speed
        enemy.velocity = (random.randint(-10, -2), 0)

        # Add it to enemies list
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)

    def add_cloud(self, delta_time: float):
        """Adds a new cloud to the screen
        :param delta_time: How much time has passed since the last call
        """

        # Creating a new cloud Flying sprite
        cloud = FlyingSprite("images/cloud.png", 0.1)

        # Set position to a random height and off screen right
        cloud.left = random.randint(self.width, self.width + 80)
        cloud.top = random.randint(10, self.height - 10)

        # Set random speed
        cloud.velocity = (random.randint(-3, -1), 0)

        # Add it to enemies list
        self.cloud_list.append(cloud)
        self.all_sprites.append(cloud)

    def on_key_press(self, symbol: int, modifiers: int):
        """Handle user keyboard input
        Q: Quit
        P: Pause/Unpause
        I/J/K//L: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        :arg symbol: which key was pressed
        :arg modifiers: which modifiers were pressed
        """

        if symbol == arcade.key.Q:
            # Quit the game
            arcade.close_window()

        if symbol == arcade.key.P:
            # Pause the game if not paused or
            # Play the game if paused
            self.paused = not self.paused

        if symbol == arcade.key.I or symbol == arcade.key.UP:
            self.player.change_y = 5
        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.player.change_y = -5
        if symbol == arcade.key.J or symbol == arcade.key.LEFT:
            self.player.change_x = -5
        if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo the vector when movement keys are released
        :arg symbol: which key was press
        :arg modifiers: which modifier was pressed
        """
        if (
            symbol == arcade.key.I
            or symbol == arcade.key.K
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if (
            symbol == arcade.key.J
            or symbol == arcade.key.L
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        """Update the positions and statuses of all the objects

        :arg delta_time: Time since last update call
        """

        # If paused, don't update anything
        if self.paused:
            return

        # Don't update the game once, the player gets out
        if self.game_over:
            return

        # End the game if player hits the enemy
        if self.player.collides_with_list(self.enemies_list):
            self.game_over = True
            # arcade.close_window()

        # Update all the sprites
        self.all_sprites.update()

        # Updating scores with
        self.scores = round(delta_time*1000)

        # Keep player on screen
        if self.player.top > self.height - 10:
            self.player.top = self.height - 10
        if self.player.right > self.width - 10:
            self.player.right = self.width - 10
        if self.player.bottom < 10:
            self.player.bottom = 10
        if self.player.left < 10:
            self.player.left = 10

    def on_draw(self):
        """Draws your main window
        """
        # Clearing the screen and drawing
        arcade.start_render()
        self.all_sprites.draw()

        # If game is over, then display the message along with scores
        if self.game_over:
            message = f"Game Over!"
            score_message = f"You Scored: {self.scores}"
            arcade.draw_text(message, self.width / 2 - 70, self.height / 2 + 10, arcade.color.BLACK, 25)
            arcade.draw_text(score_message, self.width / 2 - 60, self.height / 2 - 10, arcade.color.BLACK, 15)


# Main
if __name__ == "__main__":
    app = SpaceShooter(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    app.setup()
    arcade.run()
