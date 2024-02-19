today = input();
terms = input();
privacies = input()
if (int(today[1:5])==int(privacies[1:5])):
    if (int(today[6:8]) > int(privacies[6:8]) + int(terms[3:4])):
             print(0);  
