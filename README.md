# Word Game

## Overview
This repository contains a Python program that simulates scoring for a word game where two players find words within a matrix of letters. The game computes a score based on the words found by both players.

## Problem Statement
In this word game, two players independently find words within a given set of letters. After a time limit, they compare their lists, and only the words found by both players are scored. Words must be at least three letters long to count, and the score for each word is the number of letters it contains minus 2.

## Example
For example, if Tyrone and Alice play the game:
- Tyrone's list: "apple", "app", "pal", "leap", "a", "app"
- Alice's list: "pale", "pal", "a", "leap", "parlor"

After removing duplicates and comparing lists, the common words "pal" and "leap" are found:
- "pal" is worth 1 point (3 letters - 2)
- "leap" is worth 2 points (4 letters - 2)
- "a" is not counted as it is too short.

The total score is 3 points.

## How to Use

### Prerequisites
- Python 3.x

### Running the Program
1. Place the words found by player 1 in a text file (e.g., `player1_words.txt`), with one word per line.
2. Place the words found by player 2 in a text file (e.g., `player2_words.txt`), with one word per line.
3. Run the program from the command line with the paths to the two word files as arguments:

```sh
python word_game.py player1_words.txt player2_words.txt

The program will output the team's score to the console.

