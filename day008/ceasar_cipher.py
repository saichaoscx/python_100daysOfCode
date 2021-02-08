logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""
print(logo)
def ceasar(direction, text, shift):
  result = ""
  shift = shift % 26
  for letter in text:
    if direction == "encode":
        if ord(letter) + shift > 122:
          result += chr(ord(letter) + shift - 122 + 96)
        else:
          result += chr(ord(letter) + shift)
    elif direction == "decode":
        if ord(letter) - shift < 97:
          result += chr(ord(letter) - shift + 123 - 97)
        else:
          result += chr(ord(letter) - shift)
  print(f"The {direction}d text is {result}")

doAgain = "yes"
while doAgain == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceasar(direction, text, shift)
  doAgain = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if doAgain != "yes":
    print("Goodbye")

