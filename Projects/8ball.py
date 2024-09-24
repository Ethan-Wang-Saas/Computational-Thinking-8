import random

#8-ball responses
responses = [
    "Yes, for sure.",
    "idk",
    "You choose",
    "Yes, just wait.",
    "My sources say no",
    "Guaranteed.",
    "Its up to you.",
    "Yeah.",
    "Prob not.",
    "Maybe?",
    "For sure",
    "Thats a tough one...",
    "Who knows?",
    "Its complicated",
    "What do you think",
    "Not really.",
    "Anything could happen",
]

#8-Ball
def magic_8_ball():
    while True:
        question = input("Ask a yes or no question ('exit' to quit): ")
        if question.lower() == 'exit':
            print("Toodles!")
            break
        answer = random.choice(responses)  #random response
        print("Magic 8-Ball says:", answer)  #answer

############################
if __name__ == "__main__":
    magic_8_ball()
############################