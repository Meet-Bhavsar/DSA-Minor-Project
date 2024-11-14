# About the Project: Elevator Simulation

## Project Description
The Elevator Simulation project is a simple C++ program designed to mimic the basic functionality of an elevator system in a building. This simulation leverages a **doubly linked list** data structure to represent floors in the building, allowing bidirectional navigation between floors. By adding and selecting floors, users can simulate elevator movements and floor management in a straightforward way.

## Key Features
- **Add Floor**: Users can add new floors to the elevator system. Each floor is represented as a node in a doubly linked list, enabling efficient movement up or down between floors.
- **Go to Floor**: Users can navigate the elevator to any specified floor.
- **Interactive Menu**: The program provides a simple, menu-driven interface for a smooth, user-friendly experience.

## Doubly Linked List Structure
The doubly linked list is central to the program:
- Each floor is represented as a node with pointers to the next and previous floors.
- This structure allows efficient movement both upwards (next) and downwards (previous), replicating the way an elevator can travel between floors in either direction.
  
### How it Works
- **Node Structure**: Each node has a `floor` value (floor number) and pointers to the `next` and `prev` nodes.
- **Elevator Class**: Manages the doubly linked list of floors and provides methods for adding and moving between floors.

## How to Use the Project

### Compilation and Execution
1. **Compile the Code**:
   ```bash
   g++ -o elevator elevator.cpp


## Example Usage
Enter choice: 
    1) Add Floor 
    2) Go to a Floor
1
Enter the floor number you want to add: 5
Do you want to continue (y/n)? y

Enter choice: 
    1) Add Floor 
    2) Go to a Floor
2
Enter the floor number you want to go to: 5
Arrived at floor 5
