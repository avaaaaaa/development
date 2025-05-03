import random

comments = [
  "Yes - definitely",
  "It is decidedly so",
  "My sources say yes",
  "Without a doubt",
  "Reply hazy, try again",
  "Ask again later",
  "Better not tell you now",
  "My sources say no",
  "Outlook not so good",
  "Very doubtful",
  "No - definitely"
  ]

name = "john"
question = "Did you sleep well last night"
answer = ""
random_number = random.randint(0, len(comments) - 1)

name = name.strip()
question = question.strip()
output = ""


if 0 > random_number or random_number > (len(comments) - 1):
    answer = "Error"
elif question == "":
    answer = "You didn't ask anything!"
else:
    answer = comments[random_number]


if name:
    output += f"{name} asks: " + question
else:
    output += "Question: " + question


output += "\nMagic 8-Ball's answer: " + answer

print(output)
