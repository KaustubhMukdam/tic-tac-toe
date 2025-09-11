# 🎮 Advanced Tic Tac Toe Game

A feature-rich, text-based Tic Tac Toe game implemented in Python with multiple game modes including AI opponents of varying difficulty levels.

## 🚀 Features

### Game Modes
- **Human vs Human**: Classic two-player mode
- **Human vs Easy AI**: Play against a random-move AI opponent
- **Human vs Hard AI**: Challenge yourself against an unbeatable minimax AI
- **Easy AI vs Hard AI**: Watch AI opponents compete (simulation mode)
- **Hard AI vs Hard AI**: Observe optimal gameplay between two perfect players

### AI Implementation
- **Easy AI**: Makes random moves for unpredictable but beatable gameplay
- **Hard AI**: Uses the minimax algorithm with game theory for optimal play
- **Perfect Strategy**: The Hard AI analyzes all possible future moves recursively

### User Experience
- **Continuous Play**: Do-while loop structure allows multiple games in one session
- **Multiple Exit Options**: Type 'quit', 'q', or 'exit' at any time
- **Input Validation**: Robust error handling for invalid moves
- **Visual Board Display**: Clear 3x3 grid with position numbers (1-9)
- **Game Statistics**: Win/loss/tie tracking in simulation modes

## 🛠️ Technical Details

### Algorithm Implementation
The Hard AI uses the **Minimax Algorithm**:
- Recursively evaluates all possible game states
- Assumes optimal play from both players
- Maximizes AI's score while minimizing opponent's score
- Provides unbeatable gameplay when playing optimally

### Code Structure
- **Object-Oriented Design**: Clean class structure for game logic and players
- **Modular Functions**: Separated game logic, player management, and UI
- **Error Handling**: Comprehensive input validation and error management

## 🎯 How to Run

1. **Clone the repository**:
git clone https://github.com/KaustubhMukdam/tic-tac-toe.git
cd tic-tac-toe

2. **Run the game**:
python tic_tac_toe.py

3. **Select your preferred game mode** and start playing!

## 🎮 How to Play

1. The game displays a numbered grid (1-9) showing available positions
2. Players take turns entering numbers to place their marks (X or O)
3. First player to get three in a row (horizontal, vertical, or diagonal) wins
4. The game automatically detects wins, losses, and ties

### Game Controls
- Enter **1-9** to select your move position
- Type **'quit'**, **'q'**, or **'exit'** to leave the game
- Choose **'y'** to play again or **'n'** to return to menu

## 🤖 AI Difficulty Levels

### Easy AI (Random Strategy)
- Makes completely random moves
- Good for beginners and casual play
- Provides unpredictable but beatable gameplay

### Hard AI (Minimax Strategy)
- Implements perfect game theory strategy
- Nearly impossible to beat (can only tie with perfect play)
- Excellent for improving your Tic Tac Toe skills

## 📊 Simulation Modes

Watch AI opponents compete against each other:
- **5 games per simulation** with detailed move-by-move display
- **Real-time statistics** showing wins, losses, and ties
- **Educational value** to learn optimal strategies

## 🔧 Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## 🎯 Learning Outcomes

This project demonstrates:
- **Algorithm Implementation**: Minimax algorithm with game theory
- **Object-Oriented Programming**: Clean class design and inheritance
- **User Interface Design**: Intuitive text-based interface
- **Error Handling**: Robust input validation
- **Game Logic**: Win condition detection and game state management

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs or suggest improvements
- Add new features or game modes
- Improve code documentation
- Optimize AI algorithms

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Kaustubh Mukdam**
- GitHub: [@KaustubhMukdam](https://github.com/KaustubhMukdam)
- LinkedIn: [Connect with me!](www.linkedin.com/in/kaustubh-mukdam-ab0170340)

---

⭐ **Star this repository if you found it helpful!** ⭐