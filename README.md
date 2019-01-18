# Simple Strategy Game

A simple strategy game environment.  Start at one side of a randomly generated map and use actions to get to the other side.

## Legend

- 0 - Walkable space
- 1 - Your character
- 2 - Wall
- 3 - Water
- 9 - Unknown


## Declarations

### Game

The environment to interact with

- A Game has a Level as its current state
- A Game has a set of actions that can be performed

### Level

The area you can move

- A Level is a two dimensional array containing values 0-9