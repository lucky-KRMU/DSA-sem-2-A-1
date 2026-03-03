# README: Algorithmic Efficiency and Recursive Toolkit (AERT)

## Project Overview

This project, titled **Data Structures (ETCCDS202): Foundations & Algorithmic Analysis**, is a comprehensive study and implementation of fundamental computer science algorithms and data structures. Authored by **Lucky Pawar** (Roll No: 2501730142), the toolkit explores the theoretical analysis and practical Python implementation of stacks, recursion, and search paradigms.

---

## Technical Specifications

* 
**Course Code:** ETCCDS202 


* **Language:** Python 3.14
* 
**Submission Date:** March 3, 2026 


* 
**Core Concepts:** Stack ADT, Recursion, Divide & Conquer, Dynamic Programming (Memoization).



---

## Components

### 1. Stack Abstract Data Type (ADT)

The toolkit defines a `StackADT` class that follows the "contract" of stack behavior—interactable only at a single, known memory location (the top).

* **Operations:** `push`, `pop`, `peek`, `is_empty`, and `size`.
* 
**Efficiency:** Operations are typically $O(1)$ because they do not require searching the collection or shifting elements.


* **Implementation:** Used to track moves in the Tower of Hanoi problem.

### 2. Recursive Analysis

The project analyzes three classic recursive problems:

* 
**Factorial ($n!$):** Calculated with $O(n)$ time complexity.


* 
**Fibonacci ($F_n$):** * **Naive:** Exponential complexity $O(2^n)$ due to redundant subproblem calculations.


* 
**Memoized:** Reduces complexity to linear $\Theta(n)$ by storing results of expensive function calls.




* 
**Tower of Hanoi:** Demonstrates exponential growth where the number of moves is exactly $2^n - 1$.



### 3. Binary Search

An implementation of the **Divide & Conquer** paradigm.

* 
**Logic:** Recursively breaks the search space in half by comparing a target key to the midpoint.


* 
**Complexity:** * **Best Case:** $O(1)$ (target at middle).


* 
**Average/Worst Case:** $O(\log n)$.





---

## File Structure

* `report.pdf`: Theoretical foundations and complexity analysis.
* `aert_toolkit.py`: Python implementations for Stack ADT, Factorial, Fibonacci, Tower of Hanoi, and Binary Search.
* 
`output.txt`: Execution logs showing results for various test cases, including edge cases like empty arrays in binary search.



---

## Real-World Paradigms

The project reflects on how these algorithms mirror real-life processes:

* 
**Divide & Conquer:** Dictionary searches.


* 
**Dynamic Programming:** Google Maps navigation (reusing shortest paths).


* 
**Greedy Algorithms:** Cashiers providing change with the largest denominations first.

---

