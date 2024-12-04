# Replace ^I with tabs and $ with newlines
encoded_text = """ ^I   ^I  $
  ^I^I    $
 ^I  ^I^I^I $
 ^I ^I ^I  $
 ^I ^I^I^I^I^I$
 ^I ^I ^I^I^I$
  ^I^I    $
 ^I ^I  ^I $
 ^I ^I  ^I $
 ^I ^I^I  ^I$
 ^I ^I^I^I^I^I$
 ^I   ^I^I^I$
 ^I ^I ^I ^I$
 ^I ^I^I  ^I$
  ^I^I ^I ^I$
 ^I ^I^I^I^I^I$
$
$
$
^I   $
   ^I^I$
  ^I^I ^I$
^I   $
    ^I$
^I ^I $
^I ^I$
  ^I^I ^I$
   $
^I^I^I^I^I$
^I^I^I^I^I$
^I $
^I ^I ^I^I$
  ^I^I ^I$
$
$
$
   ^I   ^I^I^I$
^I$
      ^I^I    $
^I$
     ^I ^I ^I  $
^I$
     ^I ^I ^I  $
^I$
      ^I^I ^I  $
^I$
     ^I ^I^I^I^I^I$
^I$
     ^I ^I ^I  $
^I$
      ^I^I ^I  $
^I$
     ^I  ^I ^I^I$
^I$
      ^I^I  ^I^I$
^I$
     ^I ^I^I^I^I^I$
^I$
     ^I    ^I^I$
^I$
      ^I^I ^I  $
^I$
     ^I ^I  ^I $
^I$
      ^I^I  ^I^I$
^I$
     ^I ^I^I^I^I^I$
^I$
      ^I^I    $
^I$
     ^I   ^I^I $
^I$
     ^I ^I^I^I^I^I$
^I$
     ^I ^I  ^I^I$
^I$
      ^I^I    $
^I$
     ^I  ^I^I ^I$
^I$
     ^I   ^I ^I$
^I$
     ^I ^I^I^I^I^I$
^I$
     ^I    ^I $
^I$
     ^I ^I ^I ^I$
^I$
      ^I^I ^I ^I$
^I$
      ^I^I   ^I$
^I$
     ^I  ^I^I^I $
^I$
      ^I^I  ^I^I$
^I$
      ^I^I ^I ^I$
^I$
      ^I^I ^I ^I$
^I$
     ^I ^I^I^I^I^I$
^I$
     ^I     ^I$
^I$
     ^I ^I  ^I $
^I$
      ^I^I    $
^I$
     ^I ^I ^I ^I$
^I$
     ^I  ^I^I^I $
^I$
     ^I   ^I  $
^I$
     ^I ^I^I^I^I^I$
^I$
     ^I  ^I   $
^I$
      ^I^I  ^I^I$
^I$
     ^I ^I  ^I $
^I$
      ^I^I  ^I^I$
^I$
      ^I^I^I ^I $
^I$
      ^I ^I  ^I$
^I$
"""
decoded_text = encoded_text.replace("^I", "\t").replace("$", "\n")

# Convert tabs and spaces to binary
binary = decoded_text.replace("\t", "1").replace(" ", "0").replace("\n", "")

# Split binary into 8-bit chunks
chunks = [binary[i:i+8] for i in range(0, len(binary), 8)]

# Convert binary chunks to ASCII
ascii_text = "".join([chr(int(chunk, 2)) for chunk in chunks if len(chunk) == 8])

print("Decoded text:", ascii_text)
