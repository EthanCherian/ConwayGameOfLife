# Conway's Game of Life
**Simulating [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) using [pygame](https://github.com/pygame/pygame)**

## Run Instructions
I recommend using a [virtual environment](https://docs.python.org/3/library/venv.html) to run this simulation.

In the root directory, run the following commands:
```sh
> python -m venv venv

> venv\Scripts\activate

> pip install -r requirements.txt

> python main.py
```

## About
Conway's Game of Life is a one-player cellular automaton, considered foundational to computer science and graph theory.

In theory, Life is played using an infinite 2-dimensional grid, though in practice the size is constrained (in my case, 25x25). Each cell may be considered either "*live*" or "*dead*".

The game plays out in generations, which are deterministically created based on the previous generation. Each cell's state in the following generation depends on the state of their 8 neighbors, according to the following rules:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Prior to the start of the first generation, the player determines the starting configuration of live cells, called the "seed". The [Wiki](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns) shows interesting patterns that often emerge from random seeds, such as oscillators and spaceships. Naturally, many seeds will instantly die out, but it is quite easy to create a seed that continues indefinitely.
