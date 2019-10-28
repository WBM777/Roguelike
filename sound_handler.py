import tcod as libtcod
import winsound


from death_functions import kill_monster
from item_functions import cast_lightning, cast_fireball

fcount = 0
lcount = 0

if cast_fireball.has_been_called
    fcount += 1

if cast_lightning.has_been_called
    lcount += 1

if kill_monster.has_been_called 
    if fcount = 1
        winsound.PlaySound('fireball.wav', winsound.SND_ASYNC)
        fcount -= 1
    elif lcount = 1
        winsound.PlaySound('lightningspell.wav', winsound.SND_ASYNC)
        lcount -= 1
    else:
        winsound.PlaySound('monster_death.wav', winsound.SND_ASYNC)