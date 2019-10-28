import tcod as libtcod
from playsound import playsound
import winsound

from game_messages import Message

from game_states import GameStates

from render_functions import RenderOrder




def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red
    playsound('player_death.wav')

    return Message('You died!', libtcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    kill_monster.has_been_called = True
    pass
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), libtcod.orange)
    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    #winsound.PlaySound('monster_death.wav', winsound.SND_ASYNC)
    monster.name = 'remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message    
kill_monster.has_been_called = False