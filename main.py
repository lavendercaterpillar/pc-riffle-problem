def riffle(words):
    # Your solution here!
    pass


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
