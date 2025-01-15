# Riffle Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in combining words. We will do this by 'riffling' their letters together.

When we riffle words together, we take the first letter of each of the words, then the second letter of each of the words, and so on.

For example, if we riffle the following words:

```py
["abc", "mno", "xyz"]
```

We get:

```py
"amxbnycoz"
```

This is achieved by taking the first letter from `"abc"`, then the first letter from `"mno"`, then the first letter from `"xyz"`, then the second letter from `"abc"`, the second letter from `"mno"`, etc.

If the words are of unequal length, the shorter words should repeat their letters until every word is finished.

For example, if we riffle:

```py
["mississippi", "ab"]
```

We get:

```py
"maibsasbiasbsaibpapbi"
```

Note that the 'a' and 'b' from `"ab"` are repeatedly riffled into the longer word. Also note that we immediately stop adding letters once we reach the final 'i' in `"mississippi"`.

Write a function that riffles a list of words together and returns the resulting string.

## Examples

### Example 1

```py
words = ["abc", "xyz"]
riffle(words)
```

Produces

```py
"axbycz"
```

### Example 2

```py
words = ["abc", "mno", "xyz"]
riffle(words)
```

Produces

```py
"amxbnycoz"
```

### Example 3

```py
words = ["ab", "mississippi"]
riffle(words)
```

Produces

```py
"ambiasbsaibsasbiapbpai"
```

### Example 4

```py
words = ["mississippi", "ab"]
riffle(words)
```

Produces

```py
"maibsasbiasbsaibpapbi"
```

### Example 5

```py
words = ["choo", "a", "choo", "b"]
riffle(words)
```

Produces

```py
"cacbhahboaoboao"
```

## Notes for the Interviewer

### Clarifying Questions

#### Q: What should I do if there's only one string in the list or an empty list?

A: You can assume the list will have at least two strings

#### Q: What should I do if invalid input is passed in?

A: You can assume that the input will be valid.

#### Q: When should I stop riffling the letters?

A: The letters should be riffled until the end of every word has been reached at least once. Once all words have finished, the riffling should stop immediately; it should not continue to repeat the shorter words after this point (See test cases #4 and #5)

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper

- If the candidate struggles to determine how to make it work for more than two words, encourage them to implement a solution that only works for two words first, then improve their solution if they have time remaining. The first test case has only two words.

- If the candidate struggles to determine how to make it work for words of unequal length, encourage them to implement a solution that only works for equal length words first, then improve their solution if they have time remaining. The first test case has words of equal length.

- If the candidate's code passes the first 3 test cases but fails the last two, it is likely because they continued iterating even once the longest words had finished. Encourage the candidate to compare the last few characters of their output to the expected output to help them see the difference.

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- Why does the sample solution join strings in a list instead of concatenating the strings directly? Do research on what impact this has on performance, and what caveats exist for different Python implementations.

- Can you write a solution using the functions from `itertools`? Which do you prefer, an implementation with or without `itertools`?
