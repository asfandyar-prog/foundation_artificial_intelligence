<div align="center">

# 🤖 Foundation of Artificial Intelligence

**Classical AI search algorithms and constraint satisfaction — implemented in Python**

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat)
![Status](https://img.shields.io/badge/Status-Active-6366f1?style=flat)
![Framework](https://img.shields.io/badge/Framework-AIMA-f97316?style=flat)

*Built as part of a university-level Foundations of AI course, using the Russell & Norvig AIMA framework.*

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Problems Implemented](#-problems-implemented)
  - [Tower of Hanoi](#-tower-of-hanoi)
  - [Water Jug Problem](#-water-jug-problem)
  - [4-Queens Problem](#-4-queens-problem)
- [Search Algorithms](#-search-algorithms)
- [Getting Started](#-getting-started)
- [Key Concepts](#-key-concepts)
- [References](#-references)

---

## 🧠 Overview

This repository contains Python implementations of foundational AI problem-solving techniques, with a focus on **state space search**, **uninformed and informed search strategies**, and **constraint satisfaction problems (CSPs)**.

Each problem is modelled as a subclass of the `Problem` base class from [`search.py`](search.py), making all problems immediately compatible with every search algorithm in the framework.

---

## 📁 Repository Structure

```
foundation_artificial_intelligence/
│
├── search.py           # Core search algorithms (BFS, DFS, A*, UCS, Greedy)
├── utils.py            # Utility functions, queues, data structures
│
├── hanoi_base.py       # Tower of Hanoi — state space formulation
├── cup3_base.py        # Water Jug / Cup pouring problem
└── 4_queen_base.py     # 4-Queens constraint satisfaction problem
```

---

## 🧩 Problems Implemented

### 🗼 Tower of Hanoi

**File:** `hanoi_base.py`

Move all disks from peg A to peg B without placing a larger disk on a smaller one.

```
Initial state       Step 4              Goal state
    A  B  C             A  B  C             A  B  C
   [1]                     [1]                 [1]
   [2]              [3]    [2]                 [2]
   [3]                                         [3]
```

| Property | Detail |
|----------|--------|
| **State** | Tuple of disk lists on pegs A, B, C |
| **Actions** | Move top disk from any peg to any other |
| **Goal** | All disks on peg B |
| **Optimisation** | Forced first move A→B — solves in ~13 steps automatically |

---

### 💧 Water Jug Problem

**File:** `cup3_base.py`

Reach a target volume using jugs of fixed capacities by filling, emptying, or pouring between them.

```
Jugs: A=3L  B=4L  C=2L      Target: 2L in any jug

State 0:  (3, 0, 0)   → start
State 1:  (1, 0, 2)   → pour A into C
State 2:  (1, 2, 0)   → pour C into B
State 3:  (0, 2, 1)   → pour A into B
State n:  ...         → BFS finds optimal path
```

| Property | Detail |
|----------|--------|
| **State** | Tuple `(vol_A, vol_B, vol_C)` |
| **Actions** | Fill, empty, or pour between any two jugs |
| **Goal** | Target volume in at least one jug |
| **Algorithm** | BFS over full reachable state graph |

---

### 👑 4-Queens Problem

**File:** `4_queen_base.py`

Place 4 queens on a 4×4 board so that no two queens attack each other.

```
Solution 1          Solution 2
. Q . .             . . Q .
. . . Q             Q . . .
Q . . .             . . . Q
. . Q .             . Q . .
```

| Property | Detail |
|----------|--------|
| **State** | Partial column assignment of queens |
| **Constraints** | No shared row, column, or diagonal |
| **Solutions** | 2 valid solutions exist |
| **Strategy** | Backtracking with forced first-move optimisation |

---

## ⚙️ Search Algorithms

Implemented in `search.py` — all algorithms share the same `Problem` interface.

| Algorithm | Type | Strategy | Complete | Optimal |
|-----------|------|----------|----------|---------|
| **BFS** | Uninformed | Breadth-first (FIFO queue) | ✅ | ✅ (unit cost) |
| **DFS** | Uninformed | Depth-first (LIFO stack) | ❌ | ❌ |
| **UCS** | Uninformed | Uniform cost (priority queue) | ✅ | ✅ |
| **A\*** | Informed | Heuristic + path cost `f = g + h` | ✅ | ✅ (admissible h) |
| **Greedy** | Informed | Heuristic only `f = h` | ❌ | ❌ |

### The `Problem` Interface

Every problem implements these four methods:

```python
class Problem:
    def actions(self, state):
        """Return list of valid actions from this state."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from applying action."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if this state is a goal state."""
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return cost of path — used by UCS and A*."""
        return c + 1
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- No external dependencies — standard library only

### Installation

```bash
git clone https://github.com/asfandyar-prog/foundation_artificial_intelligence.git
cd foundation_artificial_intelligence
```

### Running the Problems

```bash
# Tower of Hanoi
python hanoi_base.py

# Water Jug Problem
python cup3_base.py

# 4-Queens Problem
python 4_queen_base.py
```

Each script prints the full solution path from initial state to goal state.

---

## 📚 Key Concepts

| Concept | Description |
|--------|-------------|
| **State space** | Graph of all configurations reachable from the initial state |
| **Uninformed search** | No domain knowledge — explores blindly (BFS, DFS, UCS) |
| **Informed search** | Uses a heuristic function to guide exploration (A*, Greedy) |
| **Admissible heuristic** | Never overestimates true cost — guarantees A* optimality |
| **CSP** | Constraint Satisfaction Problem — assign values subject to constraints |
| **Backtracking** | Systematically explore assignments, pruning invalid branches early |

---

## 📖 References

- Russell, S. & Norvig, P. — *Artificial Intelligence: A Modern Approach* (4th ed.)
- AIMA Python codebase — [github.com/aimacode/aima-python](https://github.com/aimacode/aima-python)

---

<div align="center">

MIT License · Made by [asfandyar-prog](https://github.com/asfandyar-prog)

</div>
