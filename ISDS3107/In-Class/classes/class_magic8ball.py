import random

class Magic8Ball:
    answers = ["It is certain.", "It is decidedly so.", "Without a doubt.",
               "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
               "Most likely.", "Outlook good.", "Signs point to yes.",
               "Yes.", "Reply hazy, try again", "Ask again later.",
               "Better not tell you now.", "Cannot predict now.",
               "Concentrate and ask again.", "Cannot predict now.",
               "Concentrate and ask again.", "Don't count on it.",
               "My reply is no.", "My sources say no.",
               "Outlook not so good.", "Very doubtful."]

    # the __init__ method initializes the object.
    def __init__(self):
        self.answer = ""

    def shake(self):
        self.answer = random.choice(self.answers)

    def get_answer(self):
        return self.answer

# ***in terminal, change the directory to the current, then type "python"***
# >>> from class_magic8ball import Magic8Ball
# >>> ball = Magic8Ball()
# >>> type(ball)
# <class 'class_magic8ball.Magic8Ball'>
# >>> ball.get_answer()
# ''
# >>> ball.shake()
# >>> ball.get_answer()
# 'Yes - definitely.'
