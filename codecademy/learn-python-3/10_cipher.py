def caesar_cipher(string, offset, mode):
    # encode: shift <-----
    # decode: shift ----->
    if mode not in ("decode", "encode"):
        return "unsupported mode"
    string = string.strip().lower()
    offset %= 26
    new_str = ""
    for char in string:
        if not char.isalpha():
            new_str += char
            continue
        new_char_code = (ord(char) - offset
                         if mode == "encode"
                         else ord(char) + offset)
        if mode == "encode" and new_char_code < 97:
            new_char_code += 26
        elif mode == "decode" and new_char_code > 122:
            new_char_code -= 26
        new_str += chr(new_char_code)
    return new_str

def vingere_cipher(base_str, keyword, mode):
    # encode: shift <-----
    # decode: shift ----->
    if mode not in ("decode", "encode"):
        return "unsupported mode"
    base_str = base_str.strip().lower()
    new_str = ""
    keyword_index_counter = 0
    for char in base_str:
        if not char.isalpha():
            new_str += char
            continue
        offset = ord(keyword[keyword_index_counter]) - 97
        if mode == "encode":
            new_str += caesar_cipher(char, offset, "encode")
        else:
            new_str += caesar_cipher(char, offset, "decode")
        keyword_index_counter += 1
        keyword_index_counter %= len(keyword)
    return new_str
    

encoded = """
vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx.
px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
"""
decoded = """
computers have rendered all of these old ciphers obsolete.
we'll have to really step up our game if we want to keep our messages safe.
"""
print(caesar_cipher(decoded, 7, "encode"))
print(caesar_cipher(encoded, 7, "decode"))

print(vingere_cipher("barry is the spy", "dog", "encode"))
print(vingere_cipher("ymlok cp fbb ejv", "dog", "decode"))

base_str = "ciphers are awesome!!"
keyword = "cat"
encoded_str = vingere_cipher(base_str, keyword, "encode")
decoded_str = vingere_cipher(encoded_str, keyword, "decode")

print("base string:", base_str)
print("encoded string:", encoded_str)
print("decoded string:", decoded_str)

# brute force
"""
for i in range(1, 26):
    print(i)
    print(caesar_cipher(encoded, i, "decode"))
"""
