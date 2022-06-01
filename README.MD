[![Run on Repl.it](https://repl.it/badge/github/Sarath191181208/background_remove)](https://repl.it/github/Sarath191181208/background_remove)

# AI Flappy bird

Ahh! The classic flappy bird game where you could just tap the screen & avoid the pipes. It was so great back then. I tried to use NEAT Algorithm to create an AI capable of playing flappy bird.

# Description

This project mainly uses NEAT algorithm to achieve the task of AI playing the game. All the players are scored based on their distance therefore more distance intrun gives more score. Thus, more chance of having an offspring.

## Demo

![Image](https://github.com/Sarath191181208/background_remove/blob/master/images/Screenshot.png)

## Features

- AI playing the game of Flappy bird.
- Save the current best fit model for the current generation.

## Run Locally

Clone the project

```bash
  git clone https://github.com/Sarath191181208/background_remove
```

Go to the project directory

```bash
  cd ./background_remove
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Run the project Locally

```bash
  python main.py
```

## Usage

- You can find a small box above the slider it's a tool for replacing the backgorund with color.
- You can find a slider it's used to tell how much to cut higher the number higher the amount of background around you that's cut.
- up & down arrow keys are used to change the background which are from the stock pictures picked from the internet.
- A simple load image button can be found which is used to replace with your custom picture.

## Requirements

- python `Make sure to add to path`
- pygame `pip3 install pygame`
- tkinter `default`
- pyinstaller `pip3 install pyinstaller` this is to create an exe alternatively you can use auto-py-to-exe `pip install auto-py-to-exe`
- colorama `pip3 install colorama`

## Authors

- [Sarath](https://www.github.com/https://github.com/Sarath191181208)
