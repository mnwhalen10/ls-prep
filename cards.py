# suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
# ranks = [
#     '2', '3', '4', '5', '6', '7', '8', '9', '10',
#     'Jack', 'Queen', 'King', 'Ace',
# ]
# 
# deck = [f'{rank} of {suit}'
#         for suit in suits
#         for rank in ranks]
# 
# print(deck)

squares = { f'{number}-squared': number * number
            for number in range(1, 6) }
print(squares)
# pretty-printed for clarity.
{
    '1-squared': 1,
    '2-squared': 4,
    '3-squared': 9,
    '4-squared': 16,
    '5-squared': 25
}