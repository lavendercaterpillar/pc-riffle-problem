def riffle(words):
    riffled = [] # Will hold the letters in riffled order
    max_len = 0 # Will hold the longest length of any word
    max_idx = None # Will hold the index of the last occurrence of a longest word

    # Find max_len and max_idx
    for i, word in enumerate(words):
        if len(word) >= max_len:
            max_len = len(word)
            max_idx = i

    # Iterate over each letter position
    for letter_idx in range(max_len):
        # Iterate over each word
        for word_idx, word in enumerate(words):
            # Append the letter at the appropriate position from the word
            # The modulo makes it so shorter words get repeated
            riffled.append(word[letter_idx % len(word)])
            # If we're at the last letter of the last longest word,
            # immediately break so that we do not continue to repeat
            # the shorter words
            if letter_idx == max_len-1 and word_idx == max_idx:
                break

    # Convert the list into a string
    return "".join(riffled)


words = ["abc", "xyz"]
expected = "axbycz"
assert riffle(words) == expected

words = ["abc", "mno", "xyz"]
expected = "amxbnycoz"
assert riffle(words) == expected

words = ["ab", "mississippi"]
expected = "ambiasbsaibsasbiapbpai"
assert riffle(words) == expected

words = ["mississippi", "ab"]
expected = "maibsasbiasbsaibpapbi"
assert riffle(words) == expected

words = ["choo", "a", "choo", "b"]
expected = "cacbhahboaoboao"
assert riffle(words) == expected

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
