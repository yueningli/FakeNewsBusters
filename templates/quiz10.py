class Question:
    def __init__ (self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# I just use the : to make this a set not a list and I dont know why and I am so stupid
#import random, copy
#from Question import Question

question_prompts = [
     "Type BFF in a comment on Facebook and it appears green, your account is allegedly protected.",
     "McDonalds Offering First Marijuana Friendly Smoking Section In Colorado.",
     "Google pledges $300 million to support journalism and fight fake news.",
     "A gas station explosion caught on camera was caused by children using a mobile phone in the backseat of a car.",
     "Donald Trump decided to ban schools in an effort to curb school shootings.",
     "A U.S. District Court judge granted an injunction on an ordinance banning female toplessness in Fort Collins, Colorado.",
     "A woman managed to call 911 during a domestic abuse incident by pretending to order a pizza.",
     "Baby carrots are often treated with small amounts of chlorine to reduce contamination.",
     "Police discovered a drug lab in the back room of a Walmart in Decatur, Alabama.",
     "The world's most-pierced person, Gerard Rogers, died while passing through a metal detector at LAX airport."
]

questions = [
     Question(question_prompts[0], "F"),
     Question(question_prompts[1], "F"),
     Question(question_prompts[2], "R"),
     Question(question_prompts[3], "F"),
     Question(question_prompts[4], "F"),
     Question(question_prompts[5], "R"),
     Question(question_prompts[6], "R"),
     Question(question_prompts[7], "R"),
     Question(question_prompts[8], "F"),
     Question(question_prompts[9], "F"),
]

#just need to figure out the shuffle part

#Question(question_prompts[0], "a")

# the code below is okay...ish
def run_test(questions):
    score = 0
    for question in questions:
        print question.prompt
        answer = raw_input("Is this news real? Type R for Real or F for Fake:")
        if answer == question.answer:
            score += 1
    print ("You got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)



#def shuffle(q):
    #i = 0
    #while i < len(q):
    #    current_selection = random.choice(question_prompts)
    #    if current_selection not in question_prompts:
    #        question_prompts.append(current_selection)
    #        i = i + 1
    #return question_prompts

#questions_shuffled = shuffle(questions)

#for i in questions_shuffled:
#    random.shuffle(question[i])
#    print ("Is This News Real? {}. ").format(i,questions[i], question_prompts[i][0])
