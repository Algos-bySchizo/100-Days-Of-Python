# 🐍 Snake Xenzia

A classic Snake game implementation built with Python's Turtle graphics library. Control a pink snake as it grows by eating blue food pellets while avoiding walls and your own tail.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)

## 📋 Table of Contents

- [Features](#-features)
- [Game Rules](#-game-rules)
- [Installation](#-installation)
- [Usage](#-usage)
- [Code Structure](#-code-structure)
- [Technologies Used](#-technologies-used)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **Smooth Controls**: Intuitive arrow key navigation
- **Real-time Scoring**: Live score display that updates with each food eaten
- **Collision Detection**: Game ends when hitting walls or your own tail
- **Dynamic Food Spawning**: Food appears randomly across the game area
- **Clean Graphics**: Black background with colorful snake and food elements
- **Object-Oriented Design**: Modular code structure for easy maintenance

## 🎮 Game Rules

1. **Objective**: Control the snake to eat as much food as possible
2. **Movement**: Use arrow keys to change direction
3. **Growth**: Snake grows longer with each food eaten
4. **Scoring**: Score increases by 1 for each food consumed
5. **Game Over**: Occurs when snake hits walls or its own tail
6. **Restart**: Click anywhere to close the game window

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- No additional packages required (uses built-in Turtle library)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/snake-xenzia.git
   cd snake-xenzia
   ```

2. Run the game:
   ```bash
   python main.py
   ```

## 🎯 Usage

1. **Start the Game**: Execute `python main.py` in your terminal
2. **Controls**:
   - ⬆️ **Up Arrow**: Move snake upward
   - ⬇️ **Down Arrow**: Move snake downward
   - ⬅️ **Left Arrow**: Move snake left
   - ➡️ **Right Arrow**: Move snake right
3. **Gameplay**: Guide the snake to eat blue food pellets
4. **Exit**: Click anywhere on the game window to close

## 🏗️ Code Structure

```
snake-xenzia/
├── main.py          # Main game loop and initialization
├── snake.py         # Snake class with movement and growth logic
├── food.py          # Food class for spawning and positioning
├── scoreboard.py    # Score tracking and display
└── README.md        # Project documentation
```

### File Descriptions

- **`main.py`**: Contains the main game loop, screen setup, and collision detection
- **`snake.py`**: Defines the Snake class with movement methods and segment management
- **`food.py`**: Handles food creation, positioning, and random spawning
- **`scoreboard.py`**: Manages score display and game over messages

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Turtle Graphics**: Built-in Python graphics library for game rendering
- **Object-Oriented Programming**: Modular class-based architecture
- **Random Module**: For food positioning
- **Time Module**: For game loop timing

## 📸 Screenshots

*[Screenshots would be added here showing gameplay, score display, and game over screen]*

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Suggested Improvements

- Add different difficulty levels
- Implement high score tracking
- Add sound effects
- Create different food types with varying points
- Add power-ups or obstacles
- Implement a pause feature
- Add different snake colors or themes

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the classic Snake game
- Built as a learning project for Python game development
- Uses Python's built-in Turtle graphics library

## 📞 Contact

- **Project Link**: [https://github.com/yourusername/snake-xenzia](https://github.com/yourusername/snake-xenzia)
- **Issues**: [https://github.com/yourusername/snake-xenzia/issues](https://github.com/yourusername/snake-xenzia/issues)

---

⭐ **Star this repository if you found it helpful!** 