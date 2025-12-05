---
Title: "Diagonal Grid Generator"
Submitted to: "Jonathan Lee"
Submitted by: "Younus Khan"
Date: "12-05-2025"
---

## Overview

This program recreates a small version of the Raspberry Pi light-grid assignment that we practiced in class.  
Instead of lighting LEDs on the Pi, the program builds a 2D list in Python and fills it with numbers in a diagonal pattern.  
The direction of the pattern depends on which corner the user chooses.

The goal is to build the grid efficiently, without hard-coding any patterns.  
The value in each cell comes from the diagonal that it sits on, and anything past the user's stop number is replaced with a zero.  
The program follows the same style and logic we used during Lecture 6.1 on dynamic programming style problems.

## How the Program Works

1. The user enters a grid size from 1–8.  
   This number controls both the rows and columns of the grid.

2. The user chooses a starting corner:  
   - **TL** (top-left)  
   - **TR** (top-right)  
   - **BL** (bottom-left)  
   - **BR** (bottom-right)

3. The user enters a stop number.  
   Any diagonal value larger than this number is turned into a 0.

4. The program first builds the grid as if the pattern starts in the top-left corner.  
   The value for each position is based on `row + column + 1`, which naturally creates diagonal numbering.

5. After building the base grid, the program flips it depending on the selected corner.  
   This keeps the logic simple while still matching the exact patterns shown in the assignment.
