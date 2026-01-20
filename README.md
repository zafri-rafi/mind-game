# 🧠 The Python Mentalist

[![Python Unit Tests](https://github.com/zafri-rafi/Mind-Game/actions/workflows/python-tests.yml/badge.svg)](https://github.com/zafri-rafi/Mind-Game/actions)

### *A Mathematical Mind-Reading Game*

**The Python Mentalist** is a sleek command-line application that demonstrates the power of algebra through an interactive "mind-reading" experience. By guiding the user through a series of randomized mathematical operations, the program accurately predicts the final result every time.

---

## 🔮 How It Works

The game logic is built upon a deterministic algebraic proof. While it appears to be magic, the code follows this formula:

1. **The Secret:** You choose a hidden number ().
2. **The Double:** The app asks you to multiply it by 2 ().
3. **The Modifier:** You select a random even number () provided by the app.
4. **The Result:** After dividing by 2 and subtracting your original, you are always left with half of the modifier ().

---

## 🚀 Features

* **Object-Oriented Design:** Built using a modular `MindGame` class for clean, maintainable code.
* **Dynamic UI:** Randomly samples from a bank of 50+ even numbers to ensure a unique experience every play.
* **Input Validation:** Robust error handling for non-numeric and out-of-bounds user inputs.
* **Unit Tested:** Includes a full suite of tests to verify mathematical accuracy and data integrity.

---

## 🛠️ Installation & Usage

### Prerequisites

* Python 3.6 or higher.

### Setup

1. Clone the repository:
```bash
git clone https://github.com/zafri-rafi/Mind-Game.git
cd Mind-Game

```


2. Run the game:
```bash
python mindgame.py

```



### Running Tests

To verify the logic and code quality, run the built-in test suite:

```bash
python -m unittest test_mind.py

```

---

## 📂 Project Structure

```text
python-mentalist/
├── mindgame.py    # Main application logic (OOP)
├── test_mind.py    # Unit tests (unittest framework)
├── README.md       # Project documentation
├── .gitignore      # Metadata exclusion
└── LICENSE         # MIT Open Source License

```

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👋 Contact

**Zafri Ahmed** - https://github.com/zafri-rafi/
