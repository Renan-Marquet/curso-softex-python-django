emails=['a@mail.com','b@mail.com','a@mail.com','c@mail.com',]
emails_unicos=set()
print(emails)
for item in emails:
    for item2 in emails:
        if item2==item:
            emails_unicos.add(item2)
print(emails_unicos)
emails_unicos=list(emails_unicos)
print(emails_unicos)