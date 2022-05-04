#!/usr/bin/python3
from brownie import Token, accounts, UsIncome
import pandas as pd

def main():
    usIncome = UsIncome.deploy({'from': accounts[0]})
    #token = Token.deploy("Test Token", "TST", 18, 1e23, {'from': accounts[0]})
    return usIncome

# def distribute_tokens(sender=accounts[0], receiver_list=accounts[1:]):
#     token = main()
#     for receiver in receiver_list:
#         token.transfer(receiver, 1e18, {'from': sender})

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
       'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
       'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
       'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
       'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
       'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
       'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
       'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
       'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
       'Virginia', 'Independent cities', 'Combination areas',
       'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


def reportUsIncome():
    import csv
    usIncome = main()
    with open("../../data/lapi1121.csv", 'r') as r:
        csv_reader = csv.reader(r)
        next(csv_reader)
        all(next(csv_reader) for i in range(2900))
        for row in csv_reader:
            usIncome.reportCountyIncome(row[0],row[1],row[2],row[3],row[4])
        income = usIncome.getIncomeData()
        print(income)
        # with open('usIncome.txt', 'w') as f:
        #     f.write(str(income))
        for state in states:
            stateIncome = usIncome.getStateIncomeData(state)
            # with open('usIncome.txt', 'w') as f:
            #      f.write(str(stateIncome))
            print('\n', "WTF",'\n')
            print(stateIncome)
            print(type(stateIncome))
            state_list=[]
            for i in stateIncome:
                if i[0] == '':
                    continue
                list_i = list(i)
                print(list_i)
                print(type(list_i))
                state_list.append(list_i)
            state_df = pd.DataFrame(state_list, columns=['stateName', 'countyName', 'perCapitaIncome2018', 'perCapitaIncome2019', 'perCapitaIncome2020'])
    
            print(state_df)

def saveUsIncome():
    usIncome = main()
    print(usIncome.getIncomeData())
    with open('usIncome.txt', 'w') as f:
        f.write(income)

reportUsIncome()
#saveUsIncome()


