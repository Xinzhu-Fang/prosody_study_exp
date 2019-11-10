import os
import pandas as pd
names = ["Nancy", "Vicky", "Tori", "Penny", "Jilly", "Cindy", "Laurie",
"Franny", "Brandy", "Betty", "Kylie", "Carrie", "Tracy", "Chloe",
"Annie", "Mindy", "Molly", "Sally", "Lacey", "Carlie", "Mandy",
"Hailey", "Lilly", "Jenny", "Judy", "Kerry", "Kelly", "Bonnie",
"Kimmy", "Freddy", "Ronnie", "Davey", "Jimmy", "Kenny", "Percy", "Sammy",
"Harvey", "Gary", "Ollie", "Danny", "Henry", "Teddy", "Wally",
"Johnny", "Jerry", "Timmy", "Benny", "Tommy", "Joey"]

status = []
NAMES = [x.upper() for x in names]
with open(os.path.join('analysis', 'model', 'dict')) as f:
    a = f.read()
    for iName in NAMES:
        if not iName in a:
            # print(iName + ' is not in the dict')
            status = status + ["do not exist"]
        else:
            status = status + ["exist"]

tNames_in_dict = pd.DataFrame(zip(NAMES, status), columns=['names', 'status'])
tNames_in_dict.to_csv('tNames_in_dict.csv',  encoding='utf-8')
