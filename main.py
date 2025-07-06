def riffle(words):
    # Your solution here!
    max_length = 0
    max_idx = 0

    for i, word in enumerate(words):
        if len(word) >= max_length:
            max_length = len(word)
            max_idx = i
    
    result = ""
    for letter_idx in range(max_length):
        for word_idx, word in enumerate(words):
            result += word[letter_idx % len(word)]

            # This condition is very important!!
            if letter_idx == max_length-1 and word_idx == max_idx:
                break
    print(result)
    return result


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

# words = ["choo", "a", "choo", "b"]
# expected = "cacbhahboaoboao"
# assert riffle(words) == expected

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
