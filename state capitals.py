# State capitals quiz
# Sharon Kolo APCSP

import random
def main():
    state_capitals={"Alabama":"Montgomery","Alaska":"Juneau",\
                    "Arizona":"Phoenix","Arkansas":"Little Rock",\
                    "California":"Sacramento","Colorado":"Denver",\
                    "Connecticut":"Hartford","Delaware":"Dover",\
                    "Florida":"Tallahassee","Georgia":"Atlanta",\
                    "Hawaii":"Honolulu","Idaho":"Boise",\
                    "Illinois":"Springfield","Indiana":"Indianapolis",\
                    "Iowa":"Des Moines","Kansas":"Topeka",\
                    "Kentucky":"Frankfort","Louisiana":"Baton Rouge",\
                    "Maine":"Augusta","Maryland":"Annapolis",\
                    "Massachusetts":"Boston","Michigan":"Lansing",\
                    "Minnesota":"St. Paul","Mississippi":"Jackson",\
                    "Missouri":"Jackson City","Montana":"Helena",\
                    "Nebraska":"Lincoln","Nevada":"Carson City",\
                    "New Hampshire":"Concord","New Jersey":"Trenton",\
                    "New Mexico":"Santa Fe","New York":"Albany",\
                    "North Carolina":"Raleigh","North Dakota":"Bismarck",\
                    "Ohio":"Columbus","Oklahoma":"Oklahoma City",\
                    "Oregon":"Salem","Pennsylvania":"Harrisburg",\
                    "Rhode Island":"Providence","South Carolina":"Columbia",\
                    "South Dakota":"Pierre","Tennessee":"Nashville",\
                    "Texas":"Austin","Utah":"Salt Lake City",\
                    "Vermont":"Montpelier","Virginia":"Richmond",\
                    "Washington":"Olympia","West Virginia":"Charleston",\
                    "Wisconsin":"Madison","Wyoming":"Cheyenne"}
#
    incorrect_answers=[]

    print "U.S. State Capitals Quiz\n\n"
  

    while len(state_capitals)>0:
        choice=random.choice(state_capitals.keys())
        correct_answer=state_capitals.get(choice)
        
        print "What's the capital city of",choice,"?"
        answer=raw_input("# ")
        if answer.lower()==correct_answer.lower():
            print "That is correct!\n"
            del state_capitals[choice]
        else:
            print "Your answer is incorrect."
            print "The capital is",correct_answer
            incorrect_answers.append(choice)

    print "You missed",len(incorrect_answers),"states.\n"
    

    if incorrect_answers:
        print "Here are states and their capitals to try again:\n"
        for each in incorrect_answers:
            print each
    else:
        print "Good job on the quiz!"
response=""
while response<>"n":
    main()
    response=raw_input("\n\nDo you want to play again?(y/n)\n# ")