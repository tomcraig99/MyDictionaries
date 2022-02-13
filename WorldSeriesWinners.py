#open file
wins = open('WorldSeriesWinners.txt', 'r')
#initializing important items
winsList = []
year = 1903
winsCount = {}
winsYear = {}
#create list and strip \n
for win in wins:
    winner = win.rstrip('\n')
    winsList.append(winner)
#create dictionaries
for key in winsList:
    value = winsList.count(key)
    winsYear[year] = key
    winsCount[key] = value
    year += 1
    if year == 1904:
        keytemp = 'None'
        winsYear[year] = keytemp
        year += 1
    elif year == 1994:
        keytemp = 'None'
        winsYear[year] = keytemp
        year += 1
#loop for user input
x = True
while x:
    search = int(input('Please enter a year between 1903 and 2009: '))
    team = winsYear[search]
    if search == 1904 or search == 1994:
        print(str(search) + ':', str(team))
    else:
        count = winsCount[team]
        print(str(search) + ':', str(team) +',', str(count) + ' win(s)')
    cont = input('Press enter to search again or x exit: ')
    if cont == 'x':
        x = False
    