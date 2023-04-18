alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Get the plaintext and keyword from the user
# Message: THISISTHELASTTASKHOORDAY
# Keyword: KNIGHTS
plain_text = input("Message: ")
key = input("Keyword: ")

# Repeat the keyword to match the lenght of the plaintext
repeated_keyword = key * (len(plain_text) // len(key) + 1)
keyword = repeated_keyword[:len(plain_text)]
# Print output