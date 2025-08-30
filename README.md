# 🚀 Asteroids Game

A classic arcade-style Asteroids game built with Python and Pygame. Navigate your spaceship through an asteroid field, shoot asteroids to destroy them, and survive as long as possible!

## 🎮 Game Features

- **Player Movement**: Smooth spaceship rotation and thrust mechanics
- **Shooting System**: Fire bullets to destroy asteroids
- **Asteroid Physics**: Asteroids split into smaller pieces when shot
- **Collision Detection**: Game over when player collides with asteroids
- **Dynamic Asteroid Field**: Asteroids spawn continuously from screen edges
- **Realistic Physics**: Velocity-based movement with proper rotation

## 🕹️ Controls

| Key | Action |
|-----|--------|
| `A` | Rotate ship left |
| `D` | Rotate ship right |
| `W` | Thrust forward |
| `S` | Thrust backward |
| `SPACE` | Fire bullets |
| `ESC` or Close Window | Quit game |

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.12 or higher
- uv package manager (recommended) or pip

### Installation Steps

1. **Clone or download the project**
   ```bash
   cd /path/to/Asteroids
   ```

2. **Install dependencies using uv (recommended)**
   ```bash
   uv sync
   ```
   
   *Or using pip:*
   ```bash
   pip install pygame==2.6.1
   ```

3. **Run the game**
   ```bash
   python main.py
   ```
   
   *Or with uv:*
   ```bash
   uv run python main.py
   ```

## 📁 Project Structure

```
Asteroids/
├── main.py              # Main game loop and initialization
├── player.py            # Player spaceship class
├── asteroid.py          # Asteroid class with splitting mechanics
├── asteroidfield.py     # Asteroid spawning system
├── shoot.py             # Bullet/projectile class
├── circleshape.py       # Base class for all circular game objects
├── constants.py         # Game configuration and constants
├── pyproject.toml       # Project dependencies and metadata
├── uv.lock             # Lock file for dependencies
└── README.md           # This file
```

## 🎯 How to Play

1. **Objective**: Survive as long as possible by avoiding and destroying asteroids
2. **Movement**: Use WASD keys to maneuver your triangular spaceship
3. **Combat**: Press SPACE to fire bullets at asteroids
4. **Asteroid Mechanics**: 
   - Large asteroids split into 2 smaller ones when shot
   - Smaller asteroids are destroyed completely
   - New asteroids continuously spawn from screen edges
5. **Game Over**: Colliding with any asteroid ends the game

## ⚙️ Game Configuration

You can modify game settings in `constants.py`:

| Constant | Default | Description |
|----------|---------|-------------|
| `SCREEN_WIDTH` | 1280 | Game window width |
| `SCREEN_HEIGHT` | 720 | Game window height |
| `PLAYER_SPEED` | 200 | Player movement speed |
| `PLAYER_TURN_SPEED` | 300 | Player rotation speed |
| `PLAYER_SHOOT_SPEED` | 500 | Bullet velocity |
| `PLAYER_SHOOT_COOLDOWN` | 0.3 | Time between shots (seconds) |
| `ASTEROID_SPAWN_RATE` | 0.8 | Asteroid spawn interval (seconds) |
| `ASTEROID_MIN_RADIUS` | 20 | Smallest asteroid size |
| `ASTEROID_KINDS` | 3 | Number of asteroid size categories |

## 🏗️ Architecture

### Core Classes

1. **CircleShape**: Base class providing collision detection and sprite management
2. **Player**: Handles player input, movement, rotation, and shooting
3. **Asteroid**: Manages asteroid physics, rendering, and splitting behavior
4. **Shoot**: Bullet projectiles fired by the player
5. **AsteroidField**: Spawns asteroids at random screen edges

### Game Loop

1. **Event Handling**: Process player input and window events
2. **Update Phase**: Update all game objects (movement, physics)
3. **Collision Detection**: Check bullet-asteroid and player-asteroid collisions
4. **Rendering**: Draw all game objects to screen
5. **Frame Control**: Maintain 60 FPS

## 🔧 Development

### Adding New Features

- **Scoring System**: Modify `main.py` to track and display score
- **Power-ups**: Create new classes inheriting from `CircleShape`
- **Sound Effects**: Use `pygame.mixer` for audio
- **Multiple Lives**: Add life counter and respawn mechanics
- **Particle Effects**: Enhance visual feedback for explosions

### Code Style

- Follow PEP 8 Python style guidelines
- Use type hints for better code documentation
- Keep classes focused on single responsibilities
- Use constants for all configurable values

## 🐛 Troubleshooting

### Common Issues

1. **ImportError: No module named 'pygame'**
   - Solution: Install pygame with `pip install pygame==2.6.1`

2. **Game runs too fast/slow**
   - Check frame rate in main loop (`clock.tick(60)`)
   - Adjust delta time (`dt`) calculations

3. **Collision detection issues**
   - Verify `collides_with()` method in `CircleShape`
   - Check radius values in constants

## 📝 License

This project is created for educational purposes. Feel free to modify and distribute.

## 🎓 Learning Resources

This game demonstrates:
- Object-oriented programming in Python
- Game development with Pygame
- Physics simulation and collision detection
- Event-driven programming
- Sprite management and rendering

---

*Built with Python 🐍 and Pygame 🎮*