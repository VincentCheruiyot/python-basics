#working with strings as per video no. 10
#strings involve grouping up xters e.g numbers, texts, emojis
#it is any group of characters in between quotes
#if you forget the quotes you get a syntax error

print("He's right")

long_string="Here's a new line! It's right there!"
print(long_string)

name="Cheruiyot"
name+=" Vincent"
print(name)

combine='a' + str(5)
print(combine)

#multiplying signs and numbers
multiply ='|' * 60
print(multiply)

#status message

status_message="Hey we have 10 people using the site right now"

print(status_message)
status_message="Hey we have {} people using the site right now"
print(status_message)
print(status_message.format(8))
print("Hey, we have {} {} using the site right now".format(5, "dudes"))

