# SPACE SHOOTER

Space shooter is a small game based on python arcade library. The game is to avoid the the lazers from the oppsite and by moving our player, the longer you avoid the laser the more you'll score.

## Getting Started

### Pre-requisites

- python 3.7 or above
- arcade version 2.4.1 or greater
```bash
pip install arcade
```
OR
```bash
pip install arcade==2.4.1
```

### Installing
You can install the library from test.pypi.org
```bash
pip install -i https://test.pypi.org/simple/ space-shootout
```

### Usage

```python
import arcade
from space_shootout import SpaceShooter

app = SpaceShooter()
app.setup()
arcade.run()
```

### Game Instructions
- **Pause/Un-pause** the Game: P
- **Quit** the Game: Q
- **Player movement**: Arrows

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors
[Aakriti Sharma](https://github.com/itirkaa)

## Acknowledgment
This project was made for completion of Udacity's Machine Learning Engineer Nanodegree Program
- Images and Sprites used: [kenny.nl] (https://kenney.nl/)
- Inspiration: [Real Python] (https://realpython.com/arcade-python-game-framework/)

## License
[MIT](https://choosealicense.com/licenses/mit/)
