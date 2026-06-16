sentence = 'I am, speed'

i=0
while i<len(sentence):
    if sentence[i] == ',':
        i +=1
        continue
    print(sentence[i])
    i+=1



# Jungle rescuer

available_exits = ['UpRight']
selected_exit = ''

while selected_exit not in available_exits:
    selected_exit = input('Where are you? ')
    if selected_exit == 'UpRight':
        print('You are saved. \n Game Over!')
        break

else:
    print('Already on exit path!')