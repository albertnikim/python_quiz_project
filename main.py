from questions_gothic import question_bank_gothic
questions = list(question_bank_gothic.keys())
answers = list(question_bank_gothic.values())

def gothic_quiz():
    print("Welcome to the Gothic quiz!")
    nickname()
    score = 0
    for i in range(8):
        print([i+1], questions[i])
        ans = str(input())
        if answers[i] == ans:
            score += 1
            print(f'Correct! Your score is now: {score}')
        else:
            score -= 1
            print(f'Wrong! Your score is now: {score}')
    if score < 4:
        print(f'Your final score is {score}. Try again!')
    else:
        print(f'Your final score is {score}. Well done!')

def witcher_quiz():
    print("Witcher")
    nickname()

def nickname():
    nick = str(input("Enter your nickname:"))
    print(f'Hello {nick}!')

def help():
    print("All helpful instructions here!")
    start = str(input("Type 'start' and press enter to continue"))
    if start=='start':
        main()

def options_menu():
    print("Here will be additional options like importing, highscores etc")
    start = str(input("Type 'start' and press enter to continue"))
    if start=='start':
        main()

def main():
    while True:
        choice= str(input("Welcome to Quizmania!. Press 1 to begin a Gothic quiz or press 2 to begin a Witcher quiz, then press enter. Type 'help' and press enter for more instructions. For more options: type 'options' and press enter."))
        if choice!="1" and choice!="2" and choice!='options' and choice!='help':
            print("Something went wrong. Try again.")
            continue
        else:
            if choice == "1":
                gothic_quiz()
            elif choice == "2":
                witcher_quiz()
            elif choice =="options":
                options_menu()
            elif choice =="help":
                help()
            break

main()