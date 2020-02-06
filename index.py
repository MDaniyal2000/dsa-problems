#1
# players = []
# print('Enter names for 11 players!')
# for i in range(1,12):
#     name = input(f'Enter name for {i}th player: ')
#     players.append(name)
    
# for player in players:
#     print(player)
    
#3
# cards = 0
# sweets = 0
# stationary = 0
# toys = 0
# print('Enter 3 digit code for 280 products!')
# for i in range(1,281):
#     code = input(f'Enter code for {i}th product: ')
#     if code[0] == '0':
#         cards += 1
#     elif code[0] == '1':
#         sweets += 1
#     elif code[0] == '2':
#         stationary += 1
#     elif code[0] == '3':
#         toys += 1
        
# print('Results...')
# print(f'Number of cards: {cards}')
# print(f'Number of sweets: {sweets}')
# print(f'Number of stationary: {stationary}')
# print(f'Number of toys: {toys}')

#4
# salsas = ['Mild', 'Medium','Sweet','Hot','Zesty']
# sales = []
# for i in salsas:
#     count = int(input(f'Enter number of sales for {i}: '))
#     sales.append(count)
    
# print('Results...')
# for j,index in enumerate(sales):
#     print(f'{salsas[j]} was sold {index} times')
    
# max_ind = sales.index(max(sales))
# min_ind = sales.index(min(sales))

# print(f'Highest selling product: {salsas[max_ind]}')
# print(f'Lowest selling product: {salsas[min_ind]}')

#4
size = int(input('Enter the size of array: '))
array = []
for i in range(size):
    array.append(int(input('Enter value: ')))
d = int(input('Now enter number of rotattions needed: '))
for i in range(d):
    temp, element = array[1:], array[0]
    array = temp+[element]
    print(array)
print(f'Array after rotations: {array}')
