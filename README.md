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
