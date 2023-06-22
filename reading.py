with open('emails.txt','r') as emails:
    emails=emails.readline()
    for email in emails:
      if "gmail" in email:
         print(email)