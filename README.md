# Fancy FizzBuzz

Looking to learn GUI development? This repo is my personal project to build a fancy FizzBuzz interface. Join me on my learning journey and explore how to create a visually appealing application. Let's learn together!

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Folder Structure](#folder-structure)

## About the Project

The app showcases FizzBuzz logic alongside the Python code used to generate it. On the left side, the window displays the Python code (`if`, `while`, `class`, `def`) necessary for the FizzBuzz algorithm, while on the right side, the window presents the actual results of FizzBuzz.

## Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

You'll need `Python 3.10+`, `pip`, and a virtual environment setup to run the app.

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/fancy-fizz-buzz.git
   cd fancy-fizz-buzz/fizzbuzz_app

2. Set up your virtual environment:

    ```bash
    python -m venv venv
        source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
   
3. Install the dependencies listed in requirements.txt:
    
    ```bash
    pip install -r requirements.txt

### Running the Application
    After setting up your environment, run the app with the following command:

    bash
   
    python main.py

### Folder Structure
```bashHere's a breakdown of the folder structure in the project:

bash
Copy code
fizzbuzz_app/
│
├── main.py               # Entry point for the application
├── views/
│   ├── auth_window.py     # Contains the Auth window UI logic
│   ├── dashboard.py       # The main dashboard logic
│
├── utils/
│   └── fizzbuzz_implementations.py  # Contains the FizzBuzz logic
│
├── venv/                 # Virtual environment directory
├── requirements.txt      # Project dependencies
├── .gitignore            # Git ignore file
└── README.md             # You're reading it now!

### Let's Build Together!
Feel free to fork this repository, experiment with the code, and contribute. This is a learning project, and collaboration is welcome! Let’s grow our Python and GUI development skills together.

Happy coding!