with open('readme.txt','r') as emails:
    
 for email in emails:
  if 'gmail' in email:
    print(email.rstrip())