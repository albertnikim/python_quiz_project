from question_bank_gothic import question_bank_gothic
questionsG = list(question_bank_gothic.keys())
answersG = list(question_bank_gothic.values())

from question_bank_witcher import question_bank_witcher
questionsW = list(question_bank_witcher.keys())
answersW = list(question_bank_witcher.values())

import random
question_numG = len((question_bank_gothic.keys()))
question_numW = len((question_bank_witcher.keys()))

import csv
import datetime
import json

def gothic_quiz():
    print("Welcome to the Gothic quiz!")

    nick = str(input("Enter your nickname:"))
    print(f'Hello {nick}!')

    score = 0

    randi = random.sample(range(0, question_numG), question_numG)
    for i in range(question_numG):

        print([i+1], questionsG[randi[i]])
        ans = str(input())
        if answersG[randi[i]] == ans:
            score += 1
            print(f'Correct! Your score is now: {score}')
        elif ans=='':
            print(f'No answer! Your score is now: {score}')
        elif answersG[randi[i]] != ans:
            score -= 1
            print(f'Wrong! Your score is now: {score}')

    max_half = question_numG/2
    if score < max_half:
        print(f'Your final score is {score}. Try again!')
    else:
        print(f'Your final score is {score}. Well done!')

        outputFile = open('resultsG.csv', 'a', newline='')
        outputWriter = csv.writer(outputFile)
        currentDateTime = datetime.datetime.now()
        outputWriter.writerow([currentDateTime, nick, score])
        outputFile.close()

def witcher_quiz():
    print("Welcome to the Witcher quiz!")

    nick = str(input("Enter your nickname:"))
    print(f'Hello {nick}!')

    score = 0
    randi = random.sample(range(0, question_numW), question_numW)
    for i in range(question_numW):

        print([i + 1], questionsW[randi[i]])
        ans = str(input())
        if answersW[randi[i]] == ans:
            score += 1
            print(f'Correct! Your score is now: {score}')
        elif ans == '':
            print(f'No answer! Your score is now: {score}')
        elif answersW[randi[i]] != ans:
            score -= 1
            print(f'Wrong! Your score is now: {score}')

    max_half = question_numW / 2
    if score < max_half:
        print(f'Your final score is {score}. Try again!')

    else:
        print(f'Your final score is {score}. Well done!')

        outputFile = open('resultsW.csv', 'a', newline='')
        outputWriter = csv.writer(outputFile)
        currentDateTime = datetime.datetime.now()
        outputWriter.writerow([currentDateTime, nick, score])
        outputFile.close()

def options_menu():
    print("To view the scores for the Gothic quiz type 'scoresG'. To view the scores for the Witcher quiz type 'scoresW'."
          " To export questions into a JSON file, type 'exportG' or 'exportW'. To play type 'start'.")
    option = str(input())
    if option=='start':
        main()
    elif option=='scoresG':
        scores = open('resultsG.csv')
        scoreReader = csv.reader(scores)
        scoreData = list(scoreReader)
        print(scoreData)
        scores.close()
    elif option=='scoresW':
        scores = open('resultsW.csv')
        scoreReader = csv.reader(scores)
        scoreData = list(scoreReader)
        print(scoreData)
        scores.close()
    elif option=='exportG':
        exportG = open('exportG.json', 'w')
        json.dump(question_bank_gothic, exportG, indent=6)
        exportG.close()
    elif option=='exportW':
        exportW = open('exportW.json', 'w')
        json.dump(question_bank_witcher, exportW, indent=6)
        exportW.close()

def main():
    while True:
        choice= str(input("Welcome to Quizmania!. Press 1 to begin a Gothic quiz or press 2 to begin a Witcher quiz, then press enter."
                          " For more options: type 'options' and press enter."))
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

if __name__ == '__main__':
    main()
