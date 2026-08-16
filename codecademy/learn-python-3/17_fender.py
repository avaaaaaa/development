import csv
import json


with open("passwords.csv", newline="") as f:
  reader = csv.DictReader(f)
  compromised_users = [row for row in reader]
  user_names = [entry["Username"] for entry in compromised_users]

print(compromised_users)
print(user_names)

with open("compromised_users.txt", "w") as f:
  for user_name in user_names:
    f.write(user_name + "\n")

with open("boss_message.json", "w") as f:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, f)

# what happens if we don't use raw string?
slash_null_sig = r"""
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

"""
with open("new_passwords.csv", "w", newline="") as f:
  f.write(slash_null_sig)
