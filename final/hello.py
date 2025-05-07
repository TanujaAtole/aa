# Define the string with backslash and newline
s = "\\Hello \nWorld"

print("Original String:")
print(repr(s))  # Show escaped characters

# Print header
print("\nCharacter\tASCII\tBinary\t\tAND 127\tBinary\t\tXOR 127\tBinary")
print("-" * 80)

for c in s:
    ascii_val = ord(c)
    and_result = ascii_val & 127
    xor_result = ascii_val ^ 127
    print(f"{repr(c):<10}\t{ascii_val:<5}\t{format(ascii_val, '08b')}\t"
          f"{and_result:<7}\t{format(and_result, '08b')}\t"
          f"{xor_result:<7}\t{format(xor_result, '08b')}")
