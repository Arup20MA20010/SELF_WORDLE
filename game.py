import random
a_file = open("words.txt", "r")
list_of_words = []
for line in a_file:
    for word in line.split(","):
        list_of_words.append(word)
a_file.close()
x=random.randint(0, 12971)
correct_word=list_of_words[x]
no=6
def fill_blank(x,actual,visited):
    letter_list=['_','_','_','_','_']
    i=0
    index=min(min(len(x),len(actual)),len(letter_list))
    while i<=index-1:
        if x[i]==actual[i]:
            letter_list[i]=x[i]
            visited.append(i)
        i=i+1
    str1=""
    return (str1.join(letter_list))
while no!=0:
    guess=input("write a 5 letter word in small letter: ")
    if len(guess)!=5:
        print("only 5 letters words are allowed try again")
        continue
    guess='"'+guess+'"'
    if guess==correct_word:
        print("Congratulation you have guessed the correct word")
        break
    else:
        if guess not in list_of_words:
            print("not an actual word,try again")
            continue
        guess_word=guess[1:6]
        corrected_word=correct_word[1:6]
        prev_visited=[]
        answer=fill_blank(guess_word, corrected_word,prev_visited)
        print(answer)
        pos=0
        index=0
        visited=[]
        letter=[]
        for i in range(5):
            for j in range(5):
                if(guess_word[i]==corrected_word[j]):
                    if i!=j:
                        if j not in visited and j not in prev_visited:
                            visited.append(j)
                            letter.append(corrected_word[j])
        if len(letter)>0:
            print(str(letter)+" are there but not in correct position")
        no=no-1
        print("you have "+str(no)+" guesses.Please try again")
if no==0:
    print("You cannot guess any more.The correct ans is :--> "+correct_word[1:6])









            
                

