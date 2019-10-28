import tcod as libtcod
import pygame

pygame.init()

def menu(con, header, options, width, screen_width, screen_height):
    if len(options) > 26: raise ValueError('Cannot have a menu with more than 26 options.')

    # calculate total height for the header (after auto-wrap) and one line per option
    header_height = libtcod.console_get_height_rect(con, 0, 0, width, screen_height, header)
    height = len(options) + header_height

    # create an off-screen console that represents the menu's window
    window = libtcod.console_new(width, height)

    # print the header, with auto-wrap
    libtcod.console_set_default_foreground(window, libtcod.white)
    libtcod.console_print_rect_ex(window, 0, 0, width, height, libtcod.BKGND_NONE, libtcod.LEFT, header)

    # print all the options
    y = header_height
    letter_index = ord('a')
    for option_text in options:
        text = '(' + chr(letter_index) + ') ' + option_text
        libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, text)
        y += 1
        letter_index += 1

    # blit the contents of "window" to the root console
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)
    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)


def inventory_menu(con, header, player, inventory_width, screen_width, screen_height):
    # show a menu with each item of the inventory as an option
    if len(player.inventory.items) == 0:
        options = ['Inventory is empty.']
    else:
        options = []

        for item in player.inventory.items:
            if player.equipment.main_hand == item:
                options.append('{0} (on main hand)'.format(item.name))
            elif player.equipment.off_hand == item:
                options.append('{0} (on off hand)'.format(item.name))
            else:
                options.append(item.name)

    menu(con, header, options, inventory_width, screen_width, screen_height)


def main_menu(con, background_image, screen_width, screen_height):
    libtcod.image_blit_2x(background_image, 0, 0, 0)
        
    libtcod.console_set_default_foreground(0, libtcod.light_yellow)
    libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height / 2) - 4, libtcod.BKGND_NONE, libtcod.CENTER,
                             'TOMBS OF THE ANCIENT KINGS')
    libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height - 2), libtcod.BKGND_NONE, libtcod.CENTER,
                             'By Bailey Morris & Ryan Smith')

    menu(con, '', ['Play a new game', 'Continue last game', 'Quit'], 24, screen_width, screen_height)


def level_up_menu(con, header, player, menu_width, screen_width, screen_height):
    options = ['Constitution (+20 HP, from {0})'.format(player.fighter.max_hp),
               'Strength (+1 attack, from {0})'.format(player.fighter.power),
               'Agility (+1 defense, from {0})'.format(player.fighter.defense)]

    menu(con, header, options, menu_width, screen_width, screen_height)


def character_screen(player, character_screen_width, character_screen_height, screen_width, screen_height):
    window = libtcod.console_new(character_screen_width, character_screen_height)

    libtcod.console_set_default_foreground(window, libtcod.white)

    libtcod.console_print_rect_ex(window, 0, 1, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Character Information')
    libtcod.console_print_rect_ex(window, 0, 2, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Level: {0}'.format(player.level.current_level))
    libtcod.console_print_rect_ex(window, 0, 3, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Experience: {0}'.format(player.level.current_xp))
    libtcod.console_print_rect_ex(window, 0, 4, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Experience to Level: {0}'.format(player.level.experience_to_next_level))
    libtcod.console_print_rect_ex(window, 0, 6, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Maximum HP: {0}'.format(player.fighter.max_hp))
    libtcod.console_print_rect_ex(window, 0, 7, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Attack: {0}'.format(player.fighter.power))
    libtcod.console_print_rect_ex(window, 0, 8, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Defense: {0}'.format(player.fighter.defense))

    x = screen_width // 2 - character_screen_width // 2
    y = screen_height // 2 - character_screen_height // 2
    libtcod.console_blit(window, 0, 0, character_screen_width, character_screen_height, 0, x, y, 1.0, 0.7)

def help_menu(player, help_menu_width, help_menu_height, screen_width, screen_height):
    window = libtcod.console_new(help_menu_width, help_menu_height)

    libtcod.console_set_default_foreground(window, libtcod.white)

    libtcod.console_print_rect_ex(window, 0, 1, help_menu_width, help_menu_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Controls')
    libtcod.console_print_rect_ex(window, 0, 3, help_menu_width, help_menu_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, '1. Use arrow Keys or W, A, S, D to move as well as Q, E, Z, C to move diagonaly')
    libtcod.console_print_rect_ex(window, 0, 5, help_menu_width, help_menu_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, '2. Walk into enemies to attack (O is an Orc T is a Troll g is a Goblin)')
    libtcod.console_print_rect_ex(window, 0, 7, help_menu_width, help_menu_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, '3. Walk over items then press G to pick them up (# is a scroll, ! a potion, / is a sword, and ] is a shield)')
    libtcod.console_print_rect_ex(window, 0, 10, help_menu_width, help_menu_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, '4. Walk over stairs and press Shift to go down to the next level (> are stairs)')
    libtcod.console_print_rect_ex(window, 0, 12, help_menu_width, help_menu_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, '5. Press i to open inventory')
    libtcod.console_print_rect_ex(window, 0, 14, help_menu_width, help_menu_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, '6. Alt+Enter for fullscreen')
    libtcod.console_print_rect_ex(window, 0, 16, help_menu_width, help_menu_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, '7. Press C for Character Menu')
    libtcod.console_print_rect_ex(window, 0, 18, help_menu_width, help_menu_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, '8. Use the mouse to target enemies for confusion and fireball scrolls')
    libtcod.console_print_rect_ex(window, 0, 20, help_menu_width, help_menu_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, '9. Esc to return to Title Menu')
    libtcod.console_print_rect_ex(window, 0, 22, help_menu_width, help_menu_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, '10. Press l to drop items')

    x = screen_width // 2 - help_menu_width // 2
    y = screen_height // 2 - help_menu_height // 2
    libtcod.console_blit(window, 0, 0, help_menu_width, help_menu_height, 0, x, y, 1.0, 0.7)


def message_box(con, header, width, screen_width, screen_height):
    menu(con, header, [], width, screen_width, screen_height)