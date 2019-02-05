from sys import exit
messages = ['Abso-fuckin-lutely',
    'Damn right',
    'Yes definitely',
    'Reply hazy try again',
    'I\'ll be back',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'No freakin way']

stop = True
while stop:
    question = input("I am very wise. Ask me a question, my child! (Press \"`\" to exit.) > ")
    answer_digits = len(question)

    def digital_root(number):
        x = sum(int(digit) for digit in str(number))

        if x < 10:
            return x
        else:
            return digital_root(x)

    digital_root(answer_digits)
    digital_answer = digital_root(answer_digits)
    print(messages[digital_answer])

    if question == '`':
        exit()
