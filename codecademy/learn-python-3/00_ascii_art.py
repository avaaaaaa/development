# letters are constructed in 7x5 dimension
# last letter is space
letters = [
"""
  A  
 A A 
A   A
AAAAA
A   A
A   A
A   A
""",

"""
BBBB 
B   B
B   B
BBBB 
B   B
B   B
BBBB 
""",

"""
 CCC 
C   C
C    
C    
C    
C   C
 CCC 
""",

"""
DDDD 
D   D
D   D
D   D
D   D
D   D
DDDD 
""",

"""
EEEEE
E    
E    
EEE  
E    
E    
EEEEE
""",

"""
FFFFF
F    
F    
FFF  
F    
F    
F    
""",

"""
 GGG 
G   G
G    
GGGGG
G   G
G   G
 GGG 
""",

"""
H   H
H   H
H   H
HHHHH
H   H
H   H
H   H
""",

"""
IIIII
  I  
  I  
  I  
  I  
  I  
IIIII
""",

"""
JJJJJ
  J  
  J  
  J  
J J  
J J  
 JJ  
""",

"""
K   K
K  K 
K K  
KK   
K K  
K  K 
K   K
""",

"""
L    
L    
L    
L    
L    
L    
LLLLL
""",

"""
M   M
MM MM
MM MM
M M M
M   M
M   M
M   M
""",

"""
N   N
NN  N
N N N
N  NN
N   N
N   N
N   N
""",

"""
 OOO 
O   O
O   O
O   O
O   O
O   O
 OOO 
""",

"""
PPPP 
P   P
P   P
PPPP 
P    
P    
P    
""",

"""
 QQQ 
Q   Q
Q   Q
Q   Q
Q   Q
Q  Q 
 QQ Q
""",

"""
RRRR 
R   R
R   R
RRRR 
R R  
R  R 
R   R
""",

"""
 SSS 
S   S
S    
 SSS 
    S
S   S
 SSS 
""",

"""
TTTTT
  T  
  T  
  T  
  T  
  T  
  T  
""",

"""
U   U
U   U
U   U
U   U
U   U
U   U
 UUU 
""",

"""
V   V
V   V
V   V
V   V
V   V
 V V 
  V  
""",

"""
W   W
W   W
W   W
W W W
WW WW
WW WW
W   W
""",

"""
X   X
X   X
 X X 
  X  
 X X 
X   X
X   X
""",

"""
Y   Y
 Y Y 
  Y  
  Y  
  Y  
  Y  
  Y  
""", 

"""
ZZZZZ
    Z
   Z 
  Z  
 Z   
Z    
ZZZZZ
""",

"""
     
     
     
     
     
     
     
"""
]

# get rid of leading '\n': """\n  A...""" --> """  A..."""
letters = [letter.lstrip("\n") for letter in letters]

# test letters
#for i in range(len(letters)):
#  print(letters[i])

# get name
name = input("enter name: ")
name_list = name.split()

# if name is not alphabetic, print error message and exit
for each_name in name_list:
  if not each_name.isalpha():
    print("entered non-alphabetic character(s)")
    exit()

name = " ".join(name_list)  # get rid of unnecessary space between names
name = name.upper()
#  get ascii codes
ascii_codes = [ord(letter) for letter in name]

# print row by row
space_between_letters = 3
space_list = [" " for i in range(space_between_letters)]

for i in range(7):
    for ascii_code in ascii_codes:
        index = ascii_code - 65
        if 0 <= index <= 25:  # letter
          print(letters[index][i*6:i*6+5], end="".join(space_list))
        else:  # space between names
           print(letters[-1][i*6:i*6+5], end="")
    
    # after printing each row, get to the next line
    print()

