import os
import pandas as pd
import re
names = ["Nancy", "Vicky", "Tori", "Penny", "Jilly", "Cindy", "Laurie",
"Franny", "Brandy", "Betty", "Kylie", "Carrie", "Tracy", "Chloe",
"Annie", "Mindy", "Molly", "Sally", "Lacey", "Carlie", "Mandy",
"Hailey", "Lilly", "Jenny", "Judy", "Kerry", "Kelly", "Bonnie",
"Kimmy", "Freddy", "Ronnie", "Davey", "Jimmy", "Kenny", "Percy", "Sammy",
"Harvey", "Gary", "Ollie", "Danny", "Henry", "Teddy", "Wally",
"Johnny", "Jerry", "Timmy", "Benny", "Tommy", "Joey"]

verbs = ["Kissing", "Kicking", "Poking", "Lifting", "Pushing", "Pulling"]

status = []
words = names + verbs
WORDS = [x.upper() for x in words]
#with open(os.path.join('analysis', 'tmp', 'dict')) as f:
with open(os.path.join('analysis', 'model', 'dict')) as f:

    a = f.readlines()
    for iWord in WORDS:
        bFound = 0
        for iLine in a:
            b = re.search('^' + iWord + ' ', iLine)
#            print(b)
#            print(iLine)
#            if type(b.group(0)) is str:
            if not b is None:
                status = status + ["exist"]
                bFound = 1
                break
        if not bFound:
            
                
    
#            if not ' ' + iWord + ' ' in a:
                # print(iWord + ' is not in the dict')
            status = status + ["do not exist"]
#            else:
                

tWords_in_dict = pd.DataFrame(zip(WORDS, status), columns=['WORDS', 'status'])
tWords_in_dict.to_csv('tWords_in_dict.csv',  encoding='utf-8')
