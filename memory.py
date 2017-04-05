# implementation of card game - Memory

# import simplegui
import random

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    cards = range(1, 9) * 2
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
               False]


    # count = 0

    # helper function to initialize globals
    def new_game():
        global count, state, exposed, cards, first_card, second_card, card_click_index1, card_click_index2, card_click_index3, count
        state = 0
        count = 0
        label.set_text('Turns = 0')
        first_card = []
        second_card = []
        card_click_index1 = []
        card_click_index2 = []
        exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                   False, False]
        random.shuffle(cards)
        print(cards)


    # define event handlers
    def mouseclick(pos):
        # add game state logic here

        global count, state, exposed, cards, first_card, second_card, card_click_index1, card_click_index2, count
        if state == 0:
            card_click_index1 = pos[0] // 50
            exposed[card_click_index1] = True
            first_card = cards[card_click_index1]
            print("step1", first_card, second_card)
            state = 1
        elif state == 1:
            card_click_index2 = pos[0] // 50
            if exposed[card_click_index2] == False:
                exposed[card_click_index2] = True
                second_card = cards[card_click_index2]
                # print "step2", card_click_index2, card_click_index1
                state = 2
            else:
                state = 1
                # print "cards", first_card, second_card, "state", state

        elif state == 2:
            card_click_index3 = pos[0] // 50
            if exposed[card_click_index3] == False:
                if second_card != first_card:
                    exposed[card_click_index1] = False
                    exposed[card_click_index2] = False
                exposed[card_click_index3] = True
                first_card = cards[card_click_index3]
                card_click_index1 = card_click_index3
                state = 1
                count = count + 1
                label.set_text('Turns =' + str(count))
                # print "step3.1",card_click_index3, card_click_index2, card_click_index1, "state", state
                # print "cards", first_card, second_card
            else:
                state = 2
                # print "step3.2",card_click_index3, card_click_index2, card_click_index1, "state", state
                # print "cards", first_card, second_card
                # print count


    # cards are logically 50x100 pixels in size
    def draw(canvas):
        global count
        for card_index in range(len(cards)):
            card_pos = 50 * card_index
            if exposed[card_index] == False:
                # print (exposed[card_index])
                canvas.draw_polygon([(card_pos + 25, 5), (card_pos + 25, 95)], 48, 'Green')
            else:
                canvas.draw_text(str(cards[card_index]), [card_pos + 15, 60], 30, 'White')


    # create frame and add a button and labels
    frame = simplegui.create_frame("Memory", 800, 100)
    frame.add_button("Reset", new_game)
    label = frame.add_label("Turns = 0")

    # register event handlers
    frame.set_mouseclick_handler(mouseclick)
    frame.set_draw_handler(draw)

    # get things rolling
    new_game()
    frame.start()


    # Always remember to review the grading rubric
