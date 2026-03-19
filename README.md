# 🤖 Foundation of Artificial Intelligence

> A practical implementation of classical AI search algorithms and constraint satisfaction problems — built as part of a university-level AI foundations course.

---

## 📌 Overview

This repository contains Python implementations of foundational AI problem-solving techniques, focusing on **state space search**, **uninformed and informed search strategies**, and **constraint satisfaction problems (CSPs)**. Each module models a classic AI problem and solves it using general-purpose search infrastructure.

The codebase is built around a shared `search.py` framework (adapted from *Artificial Intelligence: A Modern Approach* by Russell & Norvig), with individual problem definitions layered on top.

---

## 📁 Repository Structure

```
foundation_artificial_intelligence/
│
├── search.py           # Core search algorithms (BFS, DFS, A*, etc.)
├── utils.py            # Utility functions and data structures
│
├── hanoi_base.py       # Tower of Hanoi — state space formulation
├── cup3_base.py        # Water Jug / Cup pouring problem
├── 4_queen_base.py     # 4-Queens constraint satisfaction problem
│
└── __pycache__/        # Python bytecode cache (auto-generated)
```

---

## 🧩 Problems Implemented

### 🗼 Tower of Hanoi (`hanoi_base.py`)
A classic recursive problem modelled as a state space search.

- **State**: Configuration of disks across three pegs (A, B, C)
- **Actions**: Move the top disk from one peg to another (if valid)
- **Goal**: Move all disks from peg A to peg B
- **Key detail**: Forced first move (A → B) to speed up exploration — reaches solution in ~13 steps automatically

### 💧 Water Jug Problem (`cup3_base.py`)
A liquid measurement puzzle formulated as BFS over reachable states.

- **State**: Volume of water in each jug
- **Actions**: Fill, empty, or pour between jugs
- **Goal**: Reach a target volume in one of the jugs
- **Algorithms**: Explores the full reachable state graph

### 👑 4-Queens Problem (`4_queen_base.py`)
A constraint satisfaction problem — place 4 queens on a 4×4 board with no two queens attacking each other.

- **State**: Partial assignment of queens to columns
- **Constraints**: No two queens share a row, column, or diagonal
- **Strategy**: Forced first move for deterministic exploration; backtracking search

---

## ⚙️ Search Infrastructure (`search.py`)

The `search.py` module provides a general-purpose problem-solving framework including:

| Algorithm | Type | Strategy |
|-----------|------|----------|
| BFS | Uninformed | Breadth-first (FIFO queue) |
| DFS | Uninformed | Depth-first (LIFO stack) |
| UCS | Uninformed | Uniform cost (priority queue) |
| A\* | Informed | Heuristic + path cost |
| Greedy Best-First | Informed | Heuristic only |

Problems are defined by subclassing the `Problem` class and implementing:
- `initial_state` — starting configuration
- `actions(state)` — valid moves from a state
- `result(state, action)` — resulting state after applying an action
- `goal_test(state)` — whether the state satisfies the goal
- `path_cost(...)` — optional cost function for weighted search

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8+
```

No external dependencies — uses only the Python standard library.

### Running a Problem

```bash
# Tower of Hanoi
python hanoi_base.py

# Water Jug Problem
python cup3_base.py

# 4-Queens Problem
python 4_queen_base.py
```

Each script prints the solution path from the initial state to the goal state.

---

## 🧠 Key Concepts Covered

- **State Space Representation** — modelling problems as graphs of states and transitions
- **Uninformed Search** — BFS, DFS, UCS without domain knowledge
- **Informed Search** — A\* and greedy search with heuristic functions
- **Constraint Satisfaction** — backtracking, pruning, arc consistency
- **Problem Abstraction** — defining problems in a general, reusable framework

---

## 📚 References

- Russell, S. & Norvig, P. — *Artificial Intelligence: A Modern Approach* (4th ed.)
- AIMA Python code — [github.com/aimacode/aima-python](https://github.com/aimacode/aima-python)

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

> 💡 *Part of an ongoing coursework series in Foundations of Artificial Intelligence. More problems and algorithms will be added as the course progresses.*
