import PySimpleGUI as sg
from card import Card

cards = []
for i in range(1, 105):
    cards.append(Card(i))

image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc````\x00\x00\x00\x05\x00\x01\xa5\xf6E@\x00\x00\x00\x00IEND\xaeB`\x82'
layout = []
for r in range(8):
    buttons = []
    for c in range(13):
        card = cards[r*13 + c]
        button = sg.Button(str(card), image_data=image_data, font=("", 26, "bold"), image_size=(65, 65), button_color=card.get_color(), key=card.number)
        # info = sg.Text("Hello?", font=("", 18, "bold"), key=f'info{card.number}')
        buttons.append(button)
    layout.append(buttons)

    infos = []
    not_selected_cards = [card for card in cards if card.is_selected is False]
    for c in range(13):
        card = cards[r*13 + c]
        how_many_cards_are_lower = len([lower_card for lower_card in not_selected_cards if lower_card.number < card.number])
        text = f'{str(how_many_cards_are_lower)}<'
        info = sg.Text(text=str(text), font=("", 14, "") , key=f'info_{card.number}', size=(6, 1))
        infos.append(info)
    layout.append(infos)


def get_info():
    info = ""
    selected_cards = len([card for card in cards if card.is_selected])
    info += f'Selected cards: {str(selected_cards)} \n'
    info += f'Probability: {str(round(100 * 1/(104-selected_cards), 2))}% (1/{104-selected_cards})'
    return info


layout.append([sg.Text(get_info(), font=("", 18, "bold"), key='info')])
window = sg.Window('6 nimmt!', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    else:
        card = cards[int(event)-1]
        card.toggle()
        if card.is_selected:
            new_color = card.get_selected_color()
        else:
            new_color = card.get_color()

        window[event].update(button_color=new_color)
        window['info'].update(get_info())

        not_selected_cards = [card for card in cards if card.is_selected is False]
        for card in cards:
            how_many_cards_are_lower = len([lower_card for lower_card in not_selected_cards if lower_card.number < card.number])
            window[f'info_{card.number}'].update(how_many_cards_are_lower)

window.close()


