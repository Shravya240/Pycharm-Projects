# TODO 1:
# 1. Create function encrypt() : takes 'original_text' and 'shift_code'
# 2. Inside function : shift each letter of the 'original_text' by 'shift_code' and print the encrypted text.
# 3. Scenarios:
#    A. What happens at letter Z which can't shift forwards?
# 4. Call the Function
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q','r','s','t','u','v','w','x','y','z']

''' To remain under the range use the formula :  new index % len(alphabet_list)
print(4%25)   # 4
print(12%25)  # 12
print(25%25)  # 0
print(26%25)  # 1
print(27%25)  # 2    z + 2   = b
'''
def ceaser_cipher(original_text, shift_code, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_code = shift_code * -1                        # Decode : Negate the value

    for letter in original_text:
        new_index = alphabet_list.index(letter) + shift_code   # New Position of the letter
        new_index %= len(alphabet_list)                        # Keep under the range 0-25 - Handle IndexError is not out of range
        output_text += alphabet_list[new_index]
    print(f"Here is {encode_or_decode}d text: {output_text}")

ceaser_cipher("hello", 5, "encode")
ceaser_cipher("mjqqt", 5, "decode")


