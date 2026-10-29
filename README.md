# Wordle Solver

A command-line Wordle helper that filters a 5-letter dictionary based on the color feedback you give it after each guess.

## Setup

```bash
git clone https://github.com/udodi-n/wordle-solver.git
cd wordle-solver
python main.py
```

## How it works

1. The solver picks a random 5-letter word from `dict.txt` and prints it.
2. You play that word in Wordle, then come back and enter the color result for each position: `grey`, `green`, or `yellow`, separated by spaces.
3. The solver filters the word list in three passes:
   - Removes words containing letters marked `grey`
   - Keeps only words with `green` letters in the exact positions
   - Keeps only words that contain `yellow` letters but *not* in the positions you marked
4. The remaining possible words are printed. You type the word you want to try next, then repeat step 2 until you solve it.

## How to input

When prompted `Write the colors:`, enter exactly 5 space-separated values, one per letter position:

```
grey green yellow grey green
```

- `grey` or `gray` — the letter is not in the word
- `green` — the letter is correct and in the right position
- `yellow` — the letter is in the word but in a different position

Example: if your guess was `CRANE` and the result was grey-green-grey-yellow-grey, you'd type:

```
grey green grey yellow grey
```

After the list narrows down, you'll be asked `New word:`. Type whichever word from the remaining list you want to try next, then enter its color results.

## Important notes

- **There is no auto-correct.** If you mistype a color or give wrong feedback, the solver will filter based on that mistake and may eliminate the actual answer. It won't stop you or warn you.
- Input must match the expected words (`grey`/`gray`, `green`, `yellow`) and exactly 5 space-separated values, or the program will behave unexpectedly.
- You choose the next word yourself — the solver narrows the list but does not automatically suggest subsequent guesses after the first random one.

## Files

- `main.py` — the solver
- `dict.txt` — the full 5-letter word list
