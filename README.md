# Elevator Simulation

## Overview
This project simulates an elevator system in a building. It uses a doubly linked list to represent the floors in the building, allowing the elevator to navigate between floors, add new floors, and select a specific floor to go to.

## Features
- **Add Floors**: Add floors to the elevator system.
- **Go to Floor**: Move to a specified floor within the elevator.
- **Interactive Menu**: Simple menu-driven interface to add floors and select a floor to go to.

## Code Structure
- **Node**: A struct representing each floor, containing:
  - `floor`: The floor number.
  - `next`: Pointer to the next floor.
  - `prev`: Pointer to the previous floor.
- **Elevator**: A class implementing the elevator functionality, with the following methods:
  - `addFloor(int f)`: Adds a floor to the building.
  - `goToFloor(int f)`: Moves the elevator to the specified floor.


