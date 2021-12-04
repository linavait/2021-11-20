"""Write a function that takes two strings and checks to see if they are
anagrams of each other.
For example:
"Army" and "Mary",
"Sharing" and "Sunday",
"Quid est veritas?" and "Vir est qui adest",
"Jim Morrison" and "Mr. Mojo Risin"
"Tom Marvolo Riddle" and "I am Lord Voldemort"""


if __name__ == "__main__":
    check = {"Army": "Mary",
             "Sharing": "Sunday",
             "Quid est veritas?": "Vir est qui adest",
             "Jim Morrison": "Mr. Mojo Risin",
             "Tom Marvolo Riddle": "I am Lord Voldemort"}
for a,b in check.items():
  #kad patikrinti ar anagram, reikia visu mazu raidziu, panaikinti tarpus ir tada sorted()
  str1=sorted(a.lower().replace("",""))
  str2=sorted(b.lower().replace("",""))
  if str1 == str2:
    print("\""+a+"\" and \""+b+"\" are anagrams")
  else:
    print("\""+a+"\" and \""+b+"\" are NOT anagrams")
