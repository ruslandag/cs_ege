from my_lib import Phone

with open('phones.txt', 'r') as f:
    phones_text  = f.read().splitlines()

phones = []
for phone in phones_text:
    phones.append(Phone(*phone.split()))

print(phones[0])

added some text