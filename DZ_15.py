# 1 задание

# violator_songs = {
# 'World in My Eyes': 4.86,
# 'Sweetest Perfection': 4.43,
# 'Personal Jesus': 4.56,
# 'Halo': 4.9,
# 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.20,
# 'Policy of Truth': 4.76,
# 'Blue Dress': 4.29,
# 'Clean': 5.83
# }
# Numbers = {1: 'первой', 2: 'второй', 3: 'третьей', 4: 'четвертой',
#            5: 'пятой', 6: 'шестой', 7: 'седьмой', 8: 'восьмой', 9: 'девятой'}
# time_music = 0
#
# choice = int(input('Сколько песен выбрать от 1 до 9? -> '))
# if 1 <= choice <= 9:
#     for i in range(choice):
#         name_song = input(f'Название {Numbers.get(i + 1)} песни: ')
#         if name_song in violator_songs.keys():
#             print(violator_songs.get(name_song))
#             time_music += violator_songs.get(name_song)
#
#         else:
#             print('Такой песни в списке нет!')
#             break
#
# else:
#     print('Такого количества песен нет!')
# print(f'Общее время звучания песен: {time_music} минуты')

# 2 задание

data = {
"address": "0x544444444444",
"ETH": {
"balance": 444,
"totalIn": 444,
"totalOut": 4
},
"count_txs": 2,
"tokens": [
{
"fst_token_info": {
"address": "0x44444",
"name": "fdf",
"decimals": 0,
"symbol": "dsfdsf",
"total_supply": "3228562189",
"owner": "0x44444",
"last_updated": 1519022607901,
"issuances_count": 0,
"holders_count": 137528,
"price": False
},
"balance": 5000,
"totalIn": 0,
"total_out": 0
},
{
"sec_token_info": {
"address": "0x44444",
"name": "ggg",
"decimals": "2",
"symbol": "fff",
"total_supply": "250000000000",
"owner": "0x44444",
"last_updated": 1520452201,
"issuances_count": 0,
"holders_count": 20707,
"price": False
},
"balance": 500,
"totalIn": 0,
"total_out": 0
}
]
}
#   1 - Вывести списки ключей и значений словаря.
# print(data.items())

#   2 - В ETH добавить ключ total_diff со значением 100.
# print(data.get("ETH"))
# data['ETH']['total_diff'] = 100
# print(data.get("ETH"))

#	3 - Внутри fst_token_info значение ключа name поменять с fdf на doge.

# print(data['tokens'][0]['fst_token_info']['name'])
# data['tokens'][0]['fst_token_info']['name'] = 'doge'
# print(data['tokens'][0]['fst_token_info']['name'])

#  4 - Удалить total_out из tokens и присвоить его значение в total_out внутри ETH.

# print(data['tokens'][0])
# data['ETH']['total_out'] = data['tokens'][0]['total_out']
# data['tokens'][0].pop('total_out')
# Или в одну строчку: data['ETH']['total_out'] = data['tokens'][0]['total_out'].pop('total_out')
# print(data['ETH'])
# print(data['tokens'][0])

#  5 - Внутри sec_token_info изменить название ключа price на total_price.

print(data['tokens'][1]['sec_token_info'])
data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
print(data['tokens'][1]['sec_token_info'])
