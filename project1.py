while True:
  My_Answer=input("Choose: rock ,paper or scissors:")
  My_Answer=My_Answer.lower()
  if My_Answer!='rock' and My_Answer!='paper' and My_Answer!='scissors':
   print("Chosse correct Answer: ")
   continue
  import random
  Computer_Answer=random.choice(['rock','paper','scissors'])
  print("computer choice:",Computer_Answer)
  if My_Answer==Computer_Answer:
    print("Match Ties")
    continue
  elif My_Answer=='rock' and Computer_Answer=='scissors':
    print("You Win!")
    break
  elif My_Answer=='paper' and Computer_Answer=='scissors':
    print("You Win!")
    break
  elif My_Answer=='scissors' and Computer_Answer=='paper':
    print("You Win!")
    break
  else:
    print("You Lose Tried Again!")
