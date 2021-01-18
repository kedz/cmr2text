import re
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize


def check_name(tokens, tags):
    for i, t in enumerate(tokens):
        if t == "NAME":
            tags[i] = "name=PLACEHOLDER"

def check_exp_release_date(tokens, tags):
    for i, t in enumerate(tokens):
        if t == "EXP_RELEASE_DATE":
            tags[i] = "exp_release_date=PLACEHOLDER"


def check_perspective(tokens, tags):
    for i, t in enumerate(tokens):
        if tokens[i-4:i+1] == ['bird', "'s", '-', 'eye', 'view']:
            for j in range(i-4,i+1):
                tags[j] = 'player_perspective=bird_view'
        if tokens[i:i+2] == ["side", "view"]:
            tags[i] = "player_perspective=side_view"
            tags[i+1] = "player_perspective=side_view"
        if tokens[i:i+2] == ["side", "scrolling"]:
            tags[i] = "player_perspective=side_view"
            tags[i+1] = "player_perspective=side_view"
        if tokens[i:i+3] == ["side", "-", "scrolling"]:
            tags[i] = "player_perspective=side_view"
            tags[i+1] = "player_perspective=side_view"
            tags[i+2] = "player_perspective=side_view"
        if tokens[i:i+2] == ["bird", "view"]:
            tags[i] = "player_perspective=bird_view"
            tags[i+1] = "player_perspective=bird_view"
        if tokens[i:i+3] == ["bird", "-", "view"]:
            tags[i] = "player_perspective=bird_view"
            tags[i+1] = "player_perspective=bird_view"
            tags[i+2] = "player_perspective=bird_view"
        if tokens[i:i+4] == ["bird", "and", "side", "view"]:
            tags[i] = "player_perspective=bird_view"
            tags[i+2] = "player_perspective=side_view"
            tags[i+3] = "player_perspective=side_view"
        if tokens[i:i+4] == ["bird", "and", "third", "person"]:
            tags[i] = "player_perspective=bird_view"
            tags[i+2] = "player_perspective=third_person"
            tags[i+3] = "player_perspective=third_person"


        if tokens[i:i+2] == ["bird", "perspective"]:
            tags[i] = "player_perspective=bird_view"

        if tokens[i:i+3] == ["bird", "'s", "eye"]:
            tags[i] = "player_perspective=bird_view"
            tags[i+1] = "player_perspective=bird_view"
            tags[i+2] = "player_perspective=bird_view"
        if tokens[i:i+3] == ["bird", "'s", "view"]:
            tags[i] = "player_perspective=bird_view"
            tags[i+1] = "player_perspective=bird_view"
            tags[i+2] = "player_perspective=bird_view"

        if tokens[i:i+4] == ["third", "or", "first", "person"]:
            tags[i] = "player_perspective=third_person"
            tags[i+2] = "player_perspective=first_person"
            tags[i+3] = "player_perspective=first_person"
        if tokens[i:i+4] == ["third", "and", "first", "person"]:
            tags[i] = "player_perspective=third_person"
            tags[i+2] = "player_perspective=first_person"
            tags[i+3] = "player_perspective=first_person"


        if tokens[i:i+4] == ["first", "or", "third", "person"]:
            tags[i] = "player_perspective=first_person"
            tags[i+2] = "player_perspective=third_person"
            tags[i+3] = "player_perspective=third_person"
        if tokens[i:i+2] == ["first", "person"]:
            tags[i] = "player_perspective=first_person"
            tags[i+1] = "player_perspective=first_person"
        if tokens[i] == "fp__":
            tags[i] = "player_perspective=first_person"
        if tokens[i:i+2] == ["third", "person"]:
            tags[i] = "player_perspective=third_person"
            tags[i+1] = "player_perspective=third_person"
        if t == "side-scrolling":
            tags[i] = "player_perspective=side_view"
        if tokens[i:i+4] == ["first", "and", "third", "person"]:
            tags[i] = "player_perspective=first_person"
            tags[i+2] = "player_perspective=third_person"
            tags[i+3] = "player_perspective=third_person"
        if tokens[i:i+3] == ["third", "-", "person"]:
            tags[i] = "player_perspective=third_person"
            tags[i+1] = "player_perspective=third_person"
            tags[i+2] = "player_perspective=third_person"

        if tokens[i-6:i+1] == ["'s", 'views', 'are', 'bird', 'and', 'third', '.']:
            tags[i-3] = 'player_perspective=bird_view'
            tags[i-1] = 'player_perspective=third_person'

def check_action_genres(tokens, tags):
    for i, t in enumerate(tokens):
        if tokens[i-2:i+1] == ['real', '-', 'time']:
            for j in range(i-2,i+1):
                tags[j] = 'genres=real-time strategy'



        if t == 'adventure':
            tags[i] = 'genres=adventure'
        if tokens[i-2:i+1] == ['action', '-', 'packed']:
            for j in range(i-2,i+1):
                tags[j] = 'genres=action'
        if t == 'adventure-style':
            tags[i] = 'genres=adventure'
        if tokens[i:i+3] == ["platformer", "and", "adventure"]:
            tags[i+2] = "genres=adventure"


        if t == "action-adventure":
            tags[i] = "genres=action-adventure"
        if tokens[i-2:i+1] == ["action", "-", "adventure"]:
            tags[i] = "genres=action-adventure"
            tags[i-1] = "genres=action-adventure"
            tags[i-2] = "genres=action-adventure"


        if tokens[i-1:i+1] == ["action", "adventure"]:
            tags[i] = "genres=action-adventure"
            tags[i-1] = "genres=action-adventure"

        #if t == "adventure" and tokens[i-1:i] not in [["and",], ["action"]]:
            #tags[i] = "genres=adventure"

        if tokens[i:i+3] == ["action", "and", "strategy"]:
            tags[i] = "genres=action"
            tags[i+2] = "genres=strategy"
        if tokens[i:i+2] == ["action", "strategy"]:
        
            tags[i] = "genres=action"
            tags[i+1] = "genres=strategy"
        if tokens[i:i+2] == ["real-time", "strategy"]:
            tags[i] = "genres=real-time_strategy"
            tags[i+1] = "genres=real-time_strategy"

        if tokens[i-3:i+1] == ["real", "-", "time", "strategy"]:
            tags[i] = "genres=real-time_strategy"
            tags[i-1] = "genres=real-time_strategy"
            tags[i-2] = "genres=real-time_strategy"
            tags[i-3] = "genres=real-time_strategy"

        if tokens[i-4:i+1] == ["real", "-", "time", ',', "strategy"]:
            tags[i] = "genres=real-time_strategy"
            tags[i-1] = "genres=real-time_strategy"
            tags[i-2] = "genres=real-time_strategy"
            tags[i-3] = "genres=real-time_strategy"
            tags[i-4] = "genres=real-time_strategy"


        if tokens[i:i+2] == ["real-time", "strategies"]:
            tags[i] = "genres=real-time_strategy"
            tags[i+1] = "genres=real-time_strategy"
            
        if tokens[i-1:i+1] == ["text", "adventure"]:
            tags[i-1] = "genres=text_adventure"
            tags[i] = "genres=text_adventure"
        if tokens[i-1:i+1] == ["text", "adventures"]:
            tags[i-1] = "genres=text_adventure"
            tags[i] = "genres=text_adventure"
        if tokens[i-1:i+1] == ["indie", "adventures"]:
            tags[i] = "genres=adventure"
        if tokens[i-1:i+1] == ["mmorpg", "adventures"]:
            tags[i] = "genres=adventure"




        if tokens[i:i+4] == ["turn", "-", "based", "strategy"]:
            tags[i] = "genres=turn-based_strategy"
            tags[i+1] = "genres=turn-based_strategy"
            tags[i+2] = "genres=turn-based_strategy"
            tags[i+3] = "genres=turn-based_strategy"

        if tokens[i:i+4] == ["turn", "-", "based", "strategies"]:
            tags[i] = "genres=turn-based_strategy"
            tags[i+1] = "genres=turn-based_strategy"
            tags[i+2] = "genres=turn-based_strategy"
            tags[i+3] = "genres=turn-based_strategy"
        
        if tokens[i:i+2] == ['simulated', 'driving']:
            tags[i] = 'genres=simulation'
            tags[i+1] = 'genres=driving/racing'
        if tokens[i-1:i+1] == ['driving', 'simulation']:
            tags[i-1] = 'genres=driving/racing'
            tags[i] = 'genres=simulation'
        if tokens[i:i+3] == ['racing', 'and', 'driving']:
            tags[i] = 'genres=driving/racing'
            tags[i+1] = 'genres=driving/racing'
            tags[i+2] = 'genres=driving/racing'
        if tokens[i:i+3] == ['driving', 'and', 'racing']:
            tags[i] = 'genres=driving/racing'
            tags[i+1] = 'genres=driving/racing'
            tags[i+2] = 'genres=driving/racing'
        if tokens[i:i+3] == ['driving', 'or', 'racing']:
            tags[i] = 'genres=driving/racing'
            tags[i+1] = 'genres=driving/racing'
            tags[i+2] = 'genres=driving/racing'

        if tokens[i:i+3] == ['driving', ',', 'racing']:
            tags[i] = 'genres=driving/racing'
            tags[i+1] = 'genres=driving/racing'
            tags[i+2] = 'genres=driving/racing'

        if tokens[i:i+3] == ['drive', 'and', 'fight']:
            tags[i] = 'genres=driving/racing'
            tags[i+2] = 'genres=fighting'
        if tokens[i-3:i+1] == ['fight', 'your', 'way', 'through']:
            for j in range(i-3,i+1):
                tags[j] = 'genres=fighting'

        if tokens[i:i+7] == ['in', 'which', 'you', 'can', 'also', 'drive', 'around']:
            for j in range(i,i+7):
                tags[j] = 'genres=driving/racing'

        if tokens[i-2:i+1] == ["action", "and", "adventure"]:
            tags[i] = "genres=action-adventure"
            tags[i-1] = "genres=action-adventure"
            tags[i-2] = "genres=action-adventure"
        if tokens[i-3:i+1] == ["strategic", "turn", "-", "based"]:
            tags[i] = "genres=turn-based_strategy"
            tags[i-1] = "genres=turn-based_strategy"
            tags[i-2] = "genres=turn-based_strategy"
            tags[i-3] = "genres=turn-based_strategy"

        if tokens[i:i+2] == ["loves", "adventures"]:
            tags[i+1] = "genres=adventure"
        if tokens[i:i+2] == ["role-playing", "adventures"]:
            tags[i] = "genres=role-playing"
            tags[i+1] = "genres=adventure"
        if tokens[i:i+4] == ["role", "-", "playing", "adventures"]:
            tags[i] = "genres=role-playing"
            tags[i+1] = "genres=role-playing"
            tags[i+2] = "genres=role-playing"
            tags[i+3] = "genres=adventure"


        if tokens[i:i+2] == ["point-and-click", "adventures"]:
            tags[i+1] = "genres=adventure"
        if tokens[i-5:i+1] == ["point", "-", "and", "-", "click", "adventures"]:
            tags[i] = "genres=adventure"
        if tokens[i-3:i+1] == ['action', '-', 'packed', "adventure"]:
            tags[i-3] = 'genres=action-adventure'
            tags[i-2] = 'genres=action-adventure'
            tags[i-1] = 'genres=action-adventure'
            tags[i] = 'genres=action-adventure'
        if tokens[i-2:i+1] == ["puzzles", "and", "adventure"]:
            tags[i] = 'genres=adventure'

        if tokens[i-2:i+1] == ['real-time', ',', 'strategy']:
            for j in range(i-2,i+1):
                tags[j] = 'genres=real-time_strategy'
        if tokens[i] == 'action-based':
            tags[i] = 'genres=action'

        if tokens[i-1:i+1] == ["hack-and-slash", "adventures"]:
            tags[i-1] = "genres=hack-and-slash"
            tags[i] = "genres=adventure"
        if tokens[i-5:i+1] == ["hack", "-", "and", "-", "slash", "adventures"]:
            tags[i-5] = "genres=hack-and-slash"
            tags[i-4] = "genres=hack-and-slash"
            tags[i-3] = "genres=hack-and-slash"
            tags[i-2] = "genres=hack-and-slash"
            tags[i-1] = "genres=hack-and-slash"
            tags[i] = "genres=adventure"

        if tokens[i-2:i+1] == ["hack-and-slash", 'and', "adventure"]:
            tags[i-2] = "genres=hack-and-slash"
            tags[i] = "genres=adventure"
        if tokens[i-2:i+1] == ['racing', 'or', 'driving']:
            tags[i-2] = 'genres=driving/racing'
            tags[i-1] = 'genres=driving/racing'
            tags[i] = 'genres=driving/racing'

        if tokens[i-6:i+1] == ["action", "game", "loaded", "with", "tons", 
                               "of", "adventure"]:
            for j in range(i-6,i+1):
                tags[j] = 'genres=action-adventure'

        if tokens[i-2:i+1] == ["turn", "based", "rpg"]:
            for j in range(i-2,i):
                tags[j] = 'genres=turn-based_strategy' 
        if tokens[i-3:i+1] == ["turn", "-", "based", "rpg"]:
            for j in range(i-3,i):
                tags[j] = 'genres=turn-based_strategy' 


        if tokens[i-4:i+1] == ["of", 'action', ',', 'adventure', 'and']:
            for j in range(i-3,i):
                tags[j] = 'genres=action-adventure'

        if tokens[i-6:i+1] == ['features', 'hack', '-', 'and', '-', 'slash', 'action']:
            for j in range(i-5,i+1):
                tags[j] = 'genres=hack-and-slash'
        if tokens[i-6:i+1] == ['engaging', 'hack', '-', 'and', '-', 'slash', 'action']:
            for j in range(i-6,i+1):
                tags[j] = 'genres=hack-and-slash'
#
        if tokens[i-3:i+1] == ['tactically', 'completing', 'your', 'objective']:
            for j in range(i-3, i+1):
                tags[j] = 'genres=tactical'


def fix_sports(tokens, tags):
    for i, t in enumerate(tokens):
        if tokens[i:i+3] == ["and", "sports", "the"]:
            tags[i+1] = '0'
        if tokens[i:i+3] == ["it", "sports", "a"]:
            tags[i+1] = '0'
        if tokens[i:i+3] == ["that", "sports", "a"]:
            tags[i+1] = '0'

        if tokens[i:i+3] == ["which", "sports", "a"]:
            tags[i+1] = '0'
        if tokens[i:i+3] == ["which", "sports", "the"]:
            tags[i+1] = '0'
        if tokens[i:i+3] == ["it", "sports", "the"]:
            tags[i+1] = '0'

        if tokens[i-2:i+1] == ['view', 'the', 'action']:
            tags[i] = '0'


def fix_crossings(tokens, tags):

    for i, t in enumerate(tokens):
        if tokens[i-4:i+1] == ["turn", "-", "based", "simulation", "strategy"]:
            tags[i-4] = 'genres=turn-based_strategy'
            tags[i-3] = 'genres=turn-based_strategy'
            tags[i-2] = 'genres=turn-based_strategy'
            tags[i-1] = 'genres=simulation'
            tags[i] = '0'
        if tokens[i-5:i+1] == ["turn", "-", "based", "simulation", '-', "strategy"]:
            tags[i-5] = 'genres=turn-based_strategy'
            tags[i-4] = 'genres=turn-based_strategy'
            tags[i-3] = 'genres=turn-based_strategy'
            tags[i-2] = 'genres=simulation'
            tags[i] = '0'

        if tokens[i-4:i+1] == ["turn", "-", "based", "rpg", "strategy"]:
            tags[i-4] = 'genres=turn-based_strategy'
            tags[i-3] = 'genres=turn-based_strategy'
            tags[i-2] = 'genres=turn-based_strategy'
            tags[i-1] = 'genres=role-playing'
            tags[i] = '0'
        if tokens[i-6:i+1] == ["turn", "-", "based", "role", "-", "playing", "strategy"]:
            tags[i-6] = 'genres=turn-based_strategy'
            tags[i-5] = 'genres=turn-based_strategy'
            tags[i-4] = 'genres=turn-based_strategy'
            tags[i-3] = 'genres=role-playing'
            tags[i-2] = 'genres=role-playing'
            tags[i-1] = 'genres=role-playing'
            tags[i] = '0'

        if tokens[i-6:i+1] == ["real", "-", "time", "role", "-", "playing", "strategy"]:
            tags[i-6] = 'genres=real-time_strategy'
            tags[i-5] = 'genres=real-time_strategy'
            tags[i-4] = 'genres=real-time_strategy'
            tags[i-3] = 'genres=role-playing'
            tags[i-2] = 'genres=role-playing'
            tags[i-1] = 'genres=role-playing'
            tags[i] = '0'


        if tokens[i-2:i+1] == ['hack-and-slash', 'role', 'playing']:
            tags[i-1] = 'genres=role-playing'
            tags[i] = 'genres=role-playing'
        if tokens[i-3:i+1] == ['puzzles', 'and', 'role', 'playing']:
            tags[i-1] = 'genres=role-playing'
            tags[i] = 'genres=role-playing'
            

        if tokens[i-4:i+1] == ['real-time', ',', 'bird', 'view', 'strategy']:
            tags[i-4] = 'genres=real-time_strategy'
            tags[i] = '0'
        if tokens[i-6:i+1] == ['real', '-', 'time', ',', 'bird', 'view', 'strategy']:
            #tags[i-4] = 'genres=real-time_strategy'
            tags[i] = '0'

        if tokens[i-5:i+1] == ['take', 'a', 'traditionally', 'single', '-', 'player']:
            for j in range(i-5,i+1):
                tags[j] = '0'

def check_genres(tokens, tags):
    check_simple_genres(tokens, tags)
    check_action_genres(tokens, tags)
    fix_sports(tokens, tags)
    fix_crossings(tokens, tags)


def check_simple_genres(tokens, tags):
    for i, t in enumerate(tokens):
        
        if tokens[i-2:i+1] == ['role', '-', 'player']:
            tags[i] = 'genres=role-playing'
            tags[i-1] = 'genres=role-playing'
            tags[i-2] = 'genres=role-playing'
        if t == "turn-based":
            tags[i] = "genres=turn-based_strategy"
        if t == "action":
            tags[i] = "genres=action"
        if t == "action-filled":
            tags[i] = "genres=action"
        if t == 'strategic':
            tags[i] = 'genres=strategy'
        if t == "tactical":
            tags[i] = "genres=tactical"
        if t in ["mmorpg", "mmorpgs"]:
            tags[i] = "genres=MMORPG"
        if tokens[i:i+2] == ["vehicular", "combat"]:
            tags[i] = "genres=vehicular_combat"
            tags[i+1] = "genres=vehicular_combat"
        if tokens[i:i+2] == ["vehicle", "combat"]:
            tags[i] = "genres=vehicular_combat"
            tags[i+1] = "genres=vehicular_combat"

        if tokens[i] == "strategy":
            tags[i] = "genres=strategy"
        if tokens[i] in ["rts"]:
            tags[i] = "genres=real-time_strategy"
        if tokens[i-4:i+1] == ["hack", "-", "and", "-", "slash"]:
            tags[i] = "genres=hack-and-slash"
            tags[i-1] = "genres=hack-and-slash"
            tags[i-2] = "genres=hack-and-slash"
            tags[i-3] = "genres=hack-and-slash"
            tags[i-4] = "genres=hack-and-slash"
        if tokens[i-4:i+1] == ["point", "-", "and", "-", "click"]:
            tags[i] = "genres=point-and-click"
            tags[i-1] = "genres=point-and-click"
            tags[i-2] = "genres=point-and-click"
            tags[i-3] = "genres=point-and-click"
            tags[i-4] = "genres=point-and-click"
        if tokens[i:i+3] == ["point", "and", "click"]:
            tags[i] = "genres=point-and-click"
            tags[i+1] = "genres=point-and-click"
            tags[i+2] = "genres=point-and-click"
        if tokens[i:i+3] == ['role', '-', 'playing']:
            tags[i] = 'genres=role-playing'
            tags[i+1] = 'genres=role-playing'
            tags[i+2] = 'genres=role-playing'
        if tokens[i:i+3] == ['role', '-', 'play']:
            tags[i] = 'genres=role-playing'
            tags[i+1] = 'genres=role-playing'
            tags[i+2] = 'genres=role-playing'


        if tokens[i] in ["rpg", "rpgs", "role-playing", "role-play"]:
            tags[i] = "genres=role-playing"
        if tokens[i] in ["indie"]:
            tags[i] = "genres=indie"
        if tokens[i] in ["fighting"]:
            tags[i] = "genres=fighting"
        if tokens[i] in ["shooters", "shooter", "shooting", "__s"]:
            tags[i] = "genres=shooter"
        if tokens[i:i+3] == ["with", "shooting", "elements"]:
            tags[i] = "genres=shooter"
            tags[i+1] = "genres=shooter"
            tags[i+2] = "genres=shooter"
            
        if tokens[i] in ["simulator", "sim", "simulation", "simulators", "simulatior", "simulator-styled", "simulations"]:
            tags[i] = "genres=simulation"


        if tokens[i-7:i+1] == ["a", "board", "game", "where", "you", "answer",
                               "trivia", "questions"]:
            for j in range(i-7, i+1):
                tags[j] = "genres=trivia/board_game"
        if tokens[i-2:i+1] == ['trivia', '/', 'board']:
            tags[i] = 'genres=trivia/board_game'
            tags[i-1] = 'genres=trivia/board_game'
            tags[i-2] = 'genres=trivia/board_game'
        if tokens[i-3:i+1] == ["trivia", "/", "board", "game"]:
            tags[i] = "genres=trivia/board_game"
            tags[i-1] = "genres=trivia/board_game"
            tags[i-2] = "genres=trivia/board_game"
            tags[i-3] = "genres=trivia/board_game"

        if tokens[i:i+2] == ["trivia/board", "game"]:
            tags[i] = "genres=trivia/board_game"
            tags[i+1] = "genres=trivia/board_game"
        if tokens[i:i+3] == ["trivia", "board", "games"]:
            tags[i] = "genres=trivia/board_game"
            tags[i+1] = "genres=trivia/board_game"
            tags[i+2] = "genres=trivia/board_game"
        if tokens[i:i+4] == ["trivia", "or", "board", "games"]:
            tags[i] = "genres=trivia/board_game"
            tags[i+1] = "genres=trivia/board_game"
            tags[i+2] = "genres=trivia/board_game"
            tags[i+3] = "genres=trivia/board_game"
        if tokens[i-3:i+1] == ["trivia", "/", "board", "games"]:
            tags[i] = "genres=trivia/board_game"
            tags[i-1] = "genres=trivia/board_game"
            tags[i-2] = "genres=trivia/board_game"
            tags[i-3] = "genres=trivia/board_game"
        if tokens[i:i+2] == ["trivia", "games"]:
            tags[i] = "genres=trivia/board_game"
            tags[i+1] = "genres=trivia/board_game"
        if tokens[i] in ["sport", "sports"]:
            tags[i] = "genres=sport"
        if tokens[i] in ["arcade"]:
            tags[i] = "genres=arcade"
        if tokens[i] in ["arcade-style"]:
            tags[i] = "genres=arcade"
        if tokens[i] in ["music"]:
            tags[i] = "genres=music"
        if tokens[i] in ["pinball"]:
            tags[i] = "genres=pinball"
        if tokens[i] in ["driving", "racing", "driving/racing"]:
            tags[i] = "genres=driving/racing"
        if tokens[i] in ["platforming", "platformer", "platformers"]:
            tags[i] = "genres=platformer"
        if tokens[i] in ["puzzles", "puzzle", "puzzler"]:
            tags[i] = "genres=puzzle"
        if tokens[i-6:i+1] == ['massively', 'multiplayer', 'online', 'role', '-', 'playing', 'game']:
            for j in range(i-6, i+1):
                tags[j] = "genres=MMORPG"
        if tokens[i-4:i+1] == ["in", "which", "you", "can", "drive"]:
            for j in range(i-4,i+1):
                tags[j] = 'genres=driving/racing'
        if t == 'music-related':
            tags[i] = 'genres=music'
        if tokens[i-4:i+1] == ['your', 'clever', 'strategies', 'and', 'tactics']:
            tags[i-2] = 'genres=strategy'
            tags[i] = 'genres=tactical' 
        if tokens[i-1:i+1] == ['role', 'playing']:
            for j in range(i-1,i+1):
                tags[j] = 'genres=role-playing'

        if tokens[i-2:i+1] == ['engaging', 'hack-and-slash', 'action']:
            for j in range(i-2,i+1):
                tags[j] = 'genres=hack-and-slash'

def check_platforms(tokens, tags):
    for i, t in enumerate(tokens):
        if t == "xbox":
            tags[i] = "platforms=Xbox"
        if t in ["playstation", "playstations"]:
            tags[i] = "platforms=PlayStation"
        if t == "pc":
            tags[i] = "platforms=PC"
        if t == "pc-exclusive":
            tags[i] = "platforms=PC"
        if t == "nintendo":
            if tokens[i+1:i+2] == ["switch"]:
                tags[i] = "platforms=Nintendo_Switch"
                tags[i+1] = "platforms=Nintendo_Switch"
            else:
                tags[i] = "platforms=Nintendo"
            

 
def check_developer(tokens, tags):
    for i, t in enumerate(tokens):
        if t == "DEVELOPER":
            tags[i] = "developer=PLACEHOLDER"
def check_release_year(tokens, tags):
    for i, t in enumerate(tokens):
        if t == "RELEASE_YEAR":
            tags[i] = "release_year=PLACEHOLDER"
                    
def check_esrb(tokens, tags):
    rated_idxs = [i for i, t in enumerate(tokens) if t == "rated"]
    for rated_idx in rated_idxs:
        if tokens[rated_idx + 1:rated_idx+3] == ["e", "10+"]:
            tags[rated_idx] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[rated_idx+1] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[rated_idx+2] = "esrb=E_10+_(for_Everyone_10_and_Older)"
        elif tokens[rated_idx + 1:rated_idx+2] == ["e"]:
            tags[rated_idx] = "esrb=E_(for_Everyone)"
            tags[rated_idx+1] = "esrb=E_(for_Everyone)"
        elif tokens[rated_idx + 1:rated_idx+2] == ["m"]:
            tags[rated_idx] = "esrb=M_(for_Mature)"
            tags[rated_idx+1] = "esrb=M_(for_Mature)"
        elif tokens[rated_idx + 1:rated_idx+2] == ["t"]:
            tags[rated_idx] = "esrb=T_(for_Teen)"
            tags[rated_idx+1] = "esrb=T_(for_Teen)"
        
    esrb_rating_of_idxs = [i for i in range(len(tokens)) 
                           if tokens[i:i+3] == ['esrb', "rating", "of"]]
    for rated_idx in esrb_rating_of_idxs:
        if tokens[rated_idx + 3:rated_idx+5] == ["e", "10+"]:
            tags[rated_idx] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[rated_idx+1] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[rated_idx+2] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[rated_idx+3] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[rated_idx+4] = "esrb=E_10+_(for_Everyone_10_and_Older)"
        elif tokens[rated_idx + 3:rated_idx+4] == ["e"]:
            tags[rated_idx] = "esrb=E_(for_Everyone)"
            tags[rated_idx+1] = "esrb=E_(for_Everyone)"
            tags[rated_idx+2] = "esrb=E_(for_Everyone)"
            tags[rated_idx+3] = "esrb=E_(for_Everyone)"
        elif tokens[rated_idx + 3:rated_idx+4] == ["m"]:
            tags[rated_idx] = "esrb=M_(for_Mature)"
            tags[rated_idx+1] = "esrb=M_(for_Mature)"
            tags[rated_idx+2] = "esrb=M_(for_Mature)"
            tags[rated_idx+3] = "esrb=M_(for_Mature)"
        elif tokens[rated_idx + 3:rated_idx+4] == ["t"]:
            tags[rated_idx] = "esrb=T_(for_Teen)"
            tags[rated_idx+1] = "esrb=T_(for_Teen)"
            tags[rated_idx+2] = "esrb=T_(for_Teen)"
            tags[rated_idx+3] = "esrb=T_(for_Teen)"
    for i, t in enumerate(tokens):
        if tokens[i-2:i+1] == ['game', 'for', 'everyone']:
            tags[i] = 'esrb=E_(for_Everyone)'
            tags[i-1] = 'esrb=E_(for_Everyone)'


        if tokens[i:i+2] == ["e", "rated"]:
            tags[i] = "esrb=E_(for_Everyone)"
            tags[i+1] = "esrb=E_(for_Everyone)"
        if tokens[i-2:i+1] == ["e", "-", "rated"]:
            for j in range(i-2,i+1):
                tags[j] = "esrb=E_(for_Everyone)"
        if tokens[i-2:i+1] == ["m", "-", "rated"]:
            for j in range(i-2,i+1):
                tags[j] = "esrb=M_(for_Mature)"
        if tokens[i-2:i+1] == ["m", "-", "rating"]:
            for j in range(i-2,i+1):
                tags[j] = "esrb=M_(for_Mature)"
        if tokens[i:i+6] == ['rated', 'to', 'be', 'good', 'for', 'everyone']:
            for j in range(i, i+6):
                tags[j] = "esrb=E_(for_Everyone)"


        if tokens[i-2:i+1] == ["e", "10+", "rating"]:
            for j in range(i-2, i+1):
                tags[j] = "esrb=E_10+_(for_Everyone_10_and_Older)"

        if tokens[i:i+2] == ["e", "rating"]:
            tags[i] = "esrb=E_(for_Everyone)"
            tags[i+1] = "esrb=E_(for_Everyone)"
        if tokens[i:i+2] == ["teen", "rating"]:
            tags[i] = "esrb=T_(for_Teen)"
            tags[i+1] = "esrb=T_(for_Teen)"
        if tokens[i:i+6] == ["t", "(", "for", "teen", ")", "rating"]:
            tags[i] = "esrb=T_(for_Teen)"
            tags[i+1] = "esrb=T_(for_Teen)"
            tags[i+2] = "esrb=T_(for_Teen)"
            tags[i+3] = "esrb=T_(for_Teen)"
            tags[i+4] = "esrb=T_(for_Teen)"
            tags[i+5] = "esrb=T_(for_Teen)"
        if tokens[i:i+5] == ["t", "(", "for", "teen", ")"]:
            tags[i] = "esrb=T_(for_Teen)"
            tags[i+1] = "esrb=T_(for_Teen)"
            tags[i+2] = "esrb=T_(for_Teen)"
            tags[i+3] = "esrb=T_(for_Teen)"
            tags[i+4] = "esrb=T_(for_Teen)"
        if tokens[i:i+6] == ["good", "for", "everyone", "10", "and", "older"]:
            tags[i] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+1] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+2] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+3] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+4] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+5] = "esrb=E_10+_(for_Everyone_10_and_Older)"
        if t == "mature":
            tags[i] = "esrb=M_(for_Mature)"
        if tokens[i:i+2] == ["m", "rating"]:
            tags[i] = "esrb=M_(for_Mature)"
            tags[i+1] = "esrb=M_(for_Mature)"
        if tokens[i:i+4] == ["(", "for", "mature", ")"]:
            tags[i] = "esrb=M_(for_Mature)"
            tags[i+1] = "esrb=M_(for_Mature)"
            tags[i+2] = "esrb=M_(for_Mature)"
            tags[i+3] = "esrb=M_(for_Mature)"
        if tokens[i:i+6] == ["m", "(", "for", "mature", ")", "rating"]:
            tags[i] = "esrb=M_(for_Mature)"
            tags[i+1] = "esrb=M_(for_Mature)"
            tags[i+2] = "esrb=M_(for_Mature)"
            tags[i+3] = "esrb=M_(for_Mature)"
            tags[i+4] = "esrb=M_(for_Mature)"
            tags[i+5] = "esrb=M_(for_Mature)"
        if tokens[i:i+6] == ["m", "(", "for", "mature", ")", "ratings"]:
            tags[i] = "esrb=M_(for_Mature)"
            tags[i+1] = "esrb=M_(for_Mature)"
            tags[i+2] = "esrb=M_(for_Mature)"
            tags[i+3] = "esrb=M_(for_Mature)"
            tags[i+4] = "esrb=M_(for_Mature)"
            tags[i+5] = "esrb=M_(for_Mature)"
            
        if tokens[i:i+9] == ["e", "10+", "(", "for", "everyone", "10", "and", "older", ")"]:

            for j in range(i, i+9):
                tags[j] = "esrb=E_10+_(for_Everyone_10_and_Older)"
        if tokens[i:i+2] == ["t", "rating"]: 
            tags[i] = "esrb=T_(for_Teen)"
            tags[i+1] = "esrb=T_(for_Teen)"
        if tokens[i:i+4] == ["e", "for", "everyone", "rating"]: 
            tags[i] = "esrb=E_(for_Everyone)"
            tags[i+1] = "esrb=E_(for_Everyone)"
            tags[i+2] = "esrb=E_(for_Everyone)"
            tags[i+3] = "esrb=E_(for_Everyone)"
        if tokens[i:i+5] == ["e", "(", "for", "everyone", ")"]: 
            tags[i] = "esrb=E_(for_Everyone)"
            tags[i+1] = "esrb=E_(for_Everyone)"
            tags[i+2] = "esrb=E_(for_Everyone)"
            tags[i+3] = "esrb=E_(for_Everyone)"
            tags[i+4] = "esrb=E_(for_Everyone)"
        if tokens[i:i+3] == ["suitable", "for", "teenagers"]: 
            tags[i] = "esrb=T_(for_Teen)"
            tags[i+1] = "esrb=T_(for_Teen)"
            tags[i+2] = "esrb=T_(for_Teen)"
        if tokens[i:i+4] == ["suitable", "for", "all", "ages"]:
            tags[i] = "esrb=E_(for_Everyone)"
            tags[i+1] = "esrb=E_(for_Everyone)"
            tags[i+2] = "esrb=E_(for_Everyone)"
            tags[i+3] = "esrb=E_(for_Everyone)"
 
        if tokens[i:i+4] == ["rated", "suitable", "for", "teens"]: 
            tags[i] = "esrb=T_(for_Teen)"
            tags[i+1] = "esrb=T_(for_Teen)"
            tags[i+2] = "esrb=T_(for_Teen)"
            tags[i+3] = "esrb=T_(for_Teen)"

        if tokens[i:i+2] == ["teen", "rated"]: 
            tags[i] = "esrb=T_(for_Teen)"
            tags[i+1] = "esrb=T_(for_Teen)"
        if tokens[i:i+2] == ["t", "rated"]: 
            tags[i] = "esrb=T_(for_Teen)"
            tags[i+1] = "esrb=T_(for_Teen)"
        if tokens[i-2:i+1] == ["t", "-", "rated"]: 
            for j in range(i-2,i+1):
                tags[j] = "esrb=T_(for_Teen)"
        if tokens[i:i+2] == ["m", "rated"]: 
            tags[i] = "esrb=M_(for_Mature)"
            tags[i+1] = "esrb=M_(for_Mature)"
          
        if tokens[i:i+6] == ["suitable", "for", "everyone", "10", "and", "above"]:
            tags[i] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+1] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+2] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+3] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+4] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+5] = "esrb=E_10+_(for_Everyone_10_and_Older)"
        if tokens[i:i+5] == ["for", "everyone", "10", "and", "older"]:
            tags[i] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+1] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+2] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+3] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i+4] = "esrb=E_10+_(for_Everyone_10_and_Older)"
        if tokens[i-10:i+1] == ["needs", "an", "m", "rating", ",", "and", "it", 
                              "only", "had", "a", "t"]:
            for j in range(i-10,i+1):
                tags[j] = "esrb=T_(for_Teen)"

        if tokens[i:i+2] == ["rated", "e."]:
            tags[i] = "esrb=E_(for_Everyone)"
            tags[i+1] = "esrb=E_(for_Everyone)"
        if tokens[i] == "e10+":
            tags[i] = "esrb=E_10+_(for_Everyone_10_and_Older)"
        if tokens[i-3:i+1] == ["for", "everyone", "over", "10"]:
            for j in range(i-3, i+1):
                tags[j] = "esrb=E_10+_(for_Everyone_10_and_Older)"

        if tokens[i-2:i+1] == ["multiplayer", "teen", "games"]:
           tags[i-1] = "esrb=T_(for_Teen)"
        if tokens[i-2:i+1] == ["appropriate", "for", "everyone"]:
            for j in range(i-2, i+1):
                tags[j] = "esrb=E_(for_Everyone)"
        if tokens[i-2:i+1] == ['teen', '-', 'rated']:
            for j in range(i-2,i+1):
                tags[j] = 'esrb=T_(for_Teen)'
        if tokens[i-6:i+1] == [",", "is", "a", "suitable", "game", "for", "teenagers"]:
            for j in range(i-4,i+1):
                tags[j] = "esrb=T_(for_Teen)"

        if tokens[i-3:i+1] == ['the', 'e', '10+', 'game']:
            tags[i-2] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i-1] = "esrb=E_10+_(for_Everyone_10_and_Older)"

        if tokens[i-3:i+1] == ["suitable", "for", "all", "audiences"]:
            for j in range(i-3,i+1):
                tags[j] = "esrb=E_(for_Everyone)"
        if tokens[i-3:i+1] == ['declared', "suitable", "for", "everyone"]:
            for j in range(i-2,i+1):
                tags[j] = "esrb=E_(for_Everyone)"

        if tokens[i-1:i+1] == ['e', '10+']:
            tags[i-1] = "esrb=E_10+_(for_Everyone_10_and_Older)"
            tags[i] = "esrb=E_10+_(for_Everyone_10_and_Older)"

        if tokens[i-2:i+1] == ['e', '10+', 'rated']:
            for j in range(i-2,i+1):
                tags[j] = 'esrb=E_10+_(for_Everyone_10_and_Older)'
        if tokens[i-4:i+1] == ['for', 'anyone', '10', 'and', 'older']:
            for j in range(i-4,i+1):
                tags[j] = 'esrb=E_10+_(for_Everyone_10_and_Older)'

        if tokens[i-8:i+1] == ["content", "your", "whole", "family", "can", 
                               "get", "on", "board", "with"]:
            for j in range(i-8,i+1):
                tags[j] = "esrb=E_(for_Everyone)"
        if tokens[i-3:i+1] == ['a', 'teen', 'content', 'rating']:
            for j in range(i-3,i+1):
                tags[j] = 'esrb=T_(for_Teen)'
        if tokens[i-3:i+1] == ['is', 'ideal', 'for', 'teenagers']:
            for j in range(i-2,i+1):
                tags[j] = 'esrb=T_(for_Teen)'
        if tokens[i-4:i+1] == ['appropriate', 'for', 'all', 'age', 'groups']:
            for j in range(i-4,i+1):
                tags[j] = "esrb=E_(for_Everyone)"
        if tokens[i-2:i+1] == ['game', 'for', 'teens']:
            for j in range(i-1,i+1):
                tags[j] = 'esrb=T_(for_Teen)'
        if tokens[i-3:i+1] == ['with', 't', 'content', 'rating']:
            for j in range(i-2,i+1):
                tags[j] = 'esrb=T_(for_Teen)'

        if tokens[i-2:i+1] == ['teenagers', 'will', 'love']:
            for j in range(i-2,i+1):
                tags[j] = 'esrb=T_(for_Teen)'
        if tokens[i-11:i+1] == ['still', 'a', 'good', 'choice', 'for', 
                                'everyone', 'according', 'to', 'the', 
                                'entertainment', 'rating', 'board']:
            for j in range(i-11,i+1):
                tags[j] = "esrb=E_(for_Everyone)"
        if tokens[i-3:i+1] == ["gritty", ",", "adult", "content"]:
            for j in range(i-3,i+1):
                tags[j] = 'esrb=M_(for_Mature)'

        if tokens[i-2:i+1] == ["e", "content", "rating"]:
            for j in range(i-2,i+1):
                tags[j] = "esrb=E_(for_Everyone)"

       
         

def tagger(tokens):
    tags = ['0'] * len(tokens)
    check_name(tokens, tags)
    check_exp_release_date(tokens, tags)
    check_developer(tokens, tags)
    check_release_year(tokens, tags)
    check_platforms(tokens, tags)
    check_genres(tokens, tags)
    check_esrb(tokens, tags)
    check_perspective(tokens, tags)
    check_opts(tokens, tags)

    return tags


def fix_hyphens(tokens):
    x = " ".join(tokens)
    x = x.replace("adventure-shooters", "adventure - shooters")
    x = x.replace('top-down', 'top - down')
    x = x.replace('third-', 'third -')
    x = x.replace('-person', '- person')
    x = x.replace('puzzle-based', 'puzzle - based')
    x = x.replace("puzzle-oriented", 'puzzle - oriented')
    x = x.replace("adventure-filled", 'adventure - filled')
    x = x.replace("non-availability", "non - availability")
    x = x.replace("bird's-eye", "bird 's - eye")
    x = x.replace("n't not", "not")
    x = x.replace('release_year-released', 'RELEASE_YEAR released')
    x = x.replace('puzzle-platforming','puzzle platforming')
    x = x.replace('shooter-rpg','shooter - rpg')
    x = x.replace("\\name", "NAME")
    x = x.replace('m- rated', 'm-rated')
    x = x.replace('bird- view', 'bird - view')
    x = x.replace('action- adventure', 'action-adventure')
    x = x.replace("role-playing-text", "role-playing - text")
    x = x.replace(" m. ", " m . <sent> ")
    x = x.replace(" t. ", " t . <sent> ")
    x = x.replace('third-person', 'third - person')
    x = x.replace('strategy-simulation', 'strategy - simulation')
    x = x.replace('pc-only', 'pc - only')
    x = x.replace('bird- and', 'bird and')
    x = x.replace('music-game', 'music - game')
    x = x.replace("simulation-sports", "simulation - sports")
    x = x.replace('single-player-only', 'single-player - only')
    x = x.replace('action-platformers', 'action - platformers')
    x = x.replace('nfs : payback', 'NAME')

    return x.split(' ')

def check_opts(tokens, tags):


    for i, t in enumerate(tokens):
        if tokens[i-3:i+1] == ['available', 'on', 'either', 'steam']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=yes'


        if t == 'steam':
            tags[i] = 'available_on_steam=yes'
        if t == 'linux':
            tags[i] = 'has_linux_release=yes'
        if t == 'mac':
            tags[i] = 'has_mac_release=yes'
        if tokens[i-6:i+1] == ['on', 'steam', ',', 'linux', ',', 'or', 'mac']:
            print("FIRING")
            tags[i] = 'has_mac_release=yes'
            tags[i-3] = 'has_linux_release=yes'
            tags[i-5] = 'available_on_steam=yes'

        if tokens[i-7:i+1] == ['not', 'on', 'steam', ',', 'linux', ',', 'or', 'mac']:
            print("FIRING")
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-5] = 'available_on_steam=no'
            tags[i-6] = 'available_on_steam=no'
            tags[i-7] = 'available_on_steam=no'


        if tokens[i-8:i+1] == ['not', 'available', 'on', 'steam', ',', 'linux', ',', 'or', 'mac']:
            print("FIRING")
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-5] = 'available_on_steam=no'
            tags[i-6] = 'available_on_steam=no'
            tags[i-7] = 'available_on_steam=no'
            tags[i-8] = 'available_on_steam=no'


        if tokens[i-5:i+1] == ['has', 'a', 'mac', 'and', 'linux', 'release']:
            for j in range(i-5,i-2):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'

    

        if tokens[i-3:i+1] == ['play', 'with', 'other', 'people',]:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-1:i+1] == ['lacks', 'multiplayer']:
            for j in range(i-1,i+1):
                tags[j] = 'has_multiplayer=no'
        if tokens[i-2:i+1] == [ 'with', 'linux', 'games']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-2:i+1] == ['available', 'for', 'steam']:
            for j in range(i-2,i+1):       
                tags[j] = 'available_on_steam=yes'

        if tokens[i-7:i+1] == ["'re", 'looking', 'for', 'a', 'game', 'to', 'play', 'alone']:
            for j in range(i-7,i+1):
                tags[j] = 'has_multiplayer=no'
        if tokens[i-2:i+1] == ['with', 'linux', 'releases']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-6:i+1] == ['do', 'you', 'ever', 'game', 'on', 'a', 'mac']:
            for j in range(i-6,i+1):
                tags[j] = 'has_mac_release='

        if tokens[i-3:i+1] == ['for', 'linux', 'or', 'mac']:
            tags[i-3] = 'has_linux_release=yes'
            tags[i-2] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'


        if tokens[i-2:i+1] == ['a', 'steam', 'game']:
            for j in range(i-2,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-1:i+1] == ['for', 'linux']:
            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'

        if tokens[i-3:i+1] == ['via', 'the', 'steam', 'platform']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-3:i+1] == ['steam', 'has', 'the', 'game']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=yes'


        if tokens[i-3:i+1] == ['on', 'mac', 'and', 'steam']:
            tags[i-3] = 'has_mac_release=yes'
            tags[i-2] = 'has_mac_release=yes'
            tags[i] = 'available_on_steam=yes'

        if tokens[i-7:i+1] == ['both', 'a', 'mac', 'release', 'and', 'a', 'linux', 'release']:
            for j in range(i-7,i-3):
                tags[j] = 'has_mac_release=yes'
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-3:i+1] == ['for', 'mac', 'and', 'linux']:
            tags[i-3] = 'has_mac_release=yes'
            tags[i-2] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'

        if tokens[i-2:i+1] == ['a', 'mac', 'release']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-1:i+1] == ['on', 'mac']:
            for j in range(i-1,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ['on', 'my', 'mac']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['have', 'linux', 'and', 'mac', 'releases']:
            for j in range(i-4,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['both', 'on', 'mac', 'and', 'linux']:
            for j in range(i-4,i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ['on', 'both', 'mac', 'and', 'linux']:
            for j in range(i-4,i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'

        if tokens[i-2:i+1] == ['released', 'on', 'linux']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-1:i+1] == ['on', 'linux']:
            for j in range(i-1,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-2:i+1] == ['on', 'the', 'mac']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-3:i+1] == ['have', 'a', 'mac', 'port']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'
        if tokens[i-1:i+1] == ['which', 'perspective']:
            tags[i] = 'player_perspective='
            tags[i-1] = 'player_perspective='

        if tokens[i-5:i+1] == ['is', 'there', 'a', 'certain', 'player', 'perspective']:
            for j in range(i-5,i+1):
                tags[j] = 'player_perspective='


        if tokens[i-5:i+1] == ['what', 'is', 'your', 'favorite', 'gaming', 'perspective']:
            for j in range(i-5,i+1):
                tags[j] = 'player_perspective='
            
        if tokens[i-9:i+1] == ['do', 'you', 'prefer', 'any', 'specific', 'player', 'perspective', 'over', 'the', 'others']:
            for j in range(i-9,i+1):
                tags[j] = 'player_perspective='


        if tokens[i-5:i+1] == ['what', 'is', 'your', 'preferred', 'player', 'perspective']:
            for j in range(i-5,i+1):
                tags[j] = 'player_perspective='

        if tokens[i-6:i+1] == ['do', 'you', 'have', 'a', 'player', 'perspective', 'preference']:
            for j in range(i-6,i+1):
                tags[j] = 'player_perspective='

        if tokens[i-3:i+1] == ['what', 'player', 'perspective', 'type']:
            for j in range(i-3,i+1):
                tags[j] = 'player_perspective='
            
        if tokens[i-2:i+1] == ['which', 'player', 'perspective']:
            for j in range(i-2,i+1):
                tags[j] = 'player_perspective='

        if tokens[i-4:i+1] == ['from', 'a', 'certain', 'player', 'perspective']:
            for j in range(i-4,i+1):
                tags[j] = 'player_perspective='

        if tokens[i-4:i+1] == ['what', 'is', 'the', 'player', 'perspective']:
            for j in range(i-4,i+1):
                tags[j] = 'player_perspective='

        if tokens[i-4:i+1] == ['there', 'is', 'a', 'player', 'perspective']:
            for j in range(i-4,i+1):
                tags[j] = 'player_perspective='

        if tokens[i-3:i+1] == ['is', 'the', 'player', 'perspective']:
            for j in range(i-3,i+1):
                tags[j] = 'player_perspective='

        if tokens[i-5:i+1] == ["n't", 'even', 'come', 'to', 'the', 'mac']:
            for j in range(i-5,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ["n't", 'available', 'for', 'my', 'mac']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ['on', 'both', 'my', 'mac', 'and', 'my', 'pc']:
            for j in range(i-6,i-2):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-3:i+1] == ['was', 'ported', 'to', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ['supported', 'on', 'mac']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-3:i+1] == ['with', 'additional', 'mac', 'support']:
            for j in range(i-3, i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ['not', 'linux', 'though']:
            for j in range(i-2, i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ['xbox', ',', 'mac']:
            tags[i] = 'has_mac_release=yes'

        if tokens[i-3:i+1] == ['not', 'released', 'on', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['as', 'well', 'as', 'mac']:
            for j in range(i-3, i+1):
                tags[j] = 'has_mac_release=yes'



        if tokens[i-3:i+1] == ['is', 'a', 'linux', 'version']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ['both', 'on', 'linux', 'and', 'mac']:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[j] = 'has_mac_release=yes'      
 
        if tokens[i-2:i+1] == ['xbox', ',', 'linux',]: 
            tags[i] = 'has_linux_release=yes'

        if tokens[i-3:i+1] == ['even', 'available', 'on', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-1:i+1] == ['for', 'mac']:
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'
    
        if tokens[i-2:i+1] == ['released', 'on', 'mac']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'
        if tokens[i-1:i+1] == ['on', 'steam']:
            for j in range(i-1,i+1):
                tags[j] = 'available_on_steam=yes'
        if tokens[i-4:i+1] == ['runs', 'on', 'linux', 'and', 'mac']:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
        if tokens[i-6:i+1] == ['can', 'play', 'it', 'on', 'mac', 'and', 'linux']:
            for j in range(i-6,i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'


        if tokens[i-4:i+1] == ['does', 'boast', 'a', 'linux', 'version']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=yes'
            

        if tokens[i-4:i+1] == ['supported', 'on', 'linux', 'and', 'mac']:    
            for j in range(i-4, i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'


        if tokens[i-6:i+1] == ['supported', 'on', 'both', 'mac', 'and', 'linux', 'systems']:    
            for j in range(i-6,i-2):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'

        if tokens[i-3:i+1] == ['has','a', 'mac', 'version']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ['is', 'mac', 'support']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['can', 'even', 'find', 'it', 'on', 'steam']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=yes'
        if tokens[i-5:i+1] == ['can', 'also', 'get', 'it', 'for', 'steam']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=yes'


        if tokens[i-3:i+1] == ['through', 'the', 'steam', 'store']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-6:i+1] == ['not', 'out', 'for', 'linux', 'or', 'even', 'mac']:
            for j in range(i-6,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            

        if tokens[i-5:i+1] == ['can', 'also', 'get', 'it', 'from', 'steam']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=yes'
          
        if tokens[i-4:i+1] == ['not', 'on', 'linux', 'or', 'mac']:
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['available', 'on', 'mac', 'and', 'linux', 'platforms']:
            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'
        if tokens[i-5:i+1] == ['releases', 'for', 'both', 'linux', 'and', 'mac']:
            tags[i] = 'has_mac_release=yes'
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-6:i+1] == ['available', 'for', 'purchase', 'and', 'download', 'on', 'steam']: 
            for j in range(i-6,i+1):
                tags[j] = 'available_on_steam=yes'
        if tokens[i-5:i+1] == ['not', 'supported', 'on', 'linux', 'and', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
        if tokens[i-5:i+1] == ['no', 'support', 'for', 'linux', 'and', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['available', 'for', 'download', 'on', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=yes'
        if tokens[i-5:i+1] == ['not', 'available', 'for', 'download', 'on', 'steam']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=no'


        if tokens[i-2:i+1] == ['has', 'linux', 'support']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-2:i+1] == ['no', 'mac', 'support']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['is', 'a', 'linux', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-3:i+1] == ['not', 'offered', 'on', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-2:i+1] == ["runs", 'on', 'linux']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-5:i+1] == ['including', 'releases', 'for', 'linux', 'and', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['as', 'well', 'as', 'linux', 'and', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['not', 'have', 'a', 'mac', 'release']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=no'



        if tokens[i-4:i+1] == ['also', 'on', 'mac', 'and', 'linux']:
            for j in range(i-4,i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'

        if tokens[i-10:i+1] == ['steam', ',', 'linux', ',', 'and', 'mac', 'all', 'have', 'the', 'game', 'available']:
            tags[i-10] = 'available_on_steam=yes'
            tags[i-8] = 'has_linux_release=yes'
            tags[i-5] = 'has_mac_release=yes'
            tags[i-4] = 'has_mac_release=yes'
            tags[i-3] = 'has_mac_release=yes'
            tags[i-2] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'
            tags[i] = 'has_mac_release=yes'


        if tokens[i-5:i+1] == ['available', 'both', 'on', 'mac', 'and', 'linux']:
            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'

        if t == 'multiplayer':
            tags[i] = 'has_multiplayer=yes'

        if tokens[i-1:i+1] == ['lacks', 'multiplayer']:
            for j in range(i-1,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-2:i+1] == ['single', '-', 'player']:
            tags[i] = 'has_multiplayer=no'
            tags[i-1] = 'has_multiplayer=no'
            tags[i-2] = 'has_multiplayer=no'
        if t == 'single-player':
            tags[i] = 'has_multiplayer=no'
        if tokens[i-9:i+1] == ["'s", "not", "available", "on", "steam", ",", 
                               "linux", ",", "or", "mac"]:
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-5] = 'available_on_steam=no'
            tags[i-5] = 'available_on_steam=no'
            tags[i-6] = 'available_on_steam=no'
            tags[i-7] = 'available_on_steam=no'
            tags[i-8] = 'available_on_steam=no'
        if tokens[i-12:i+1] == ["is", "not", "yet", "available", "as", "a", 
                               "steam", ",", "linux", ",", "or", "mac",
                               "release"]:
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i-4] = 'has_linux_release=no'
            tags[i-6] = 'available_on_steam=no'
            tags[i-7] = 'available_on_steam=no'
            tags[i-8] = 'available_on_steam=no'
            tags[i-9] = 'available_on_steam=no'
            tags[i-10] = 'available_on_steam=no'
            tags[i-11] = 'available_on_steam=no'

        if tokens[i-8:i+1] == ["but", "not", "on", "steam", ",", 
                               "mac", ",", "or", "linux"]:
            tags[i] = 'has_linux_release=no'
            tags[i-3] = 'has_mac_release=no'
            tags[i-5] = 'available_on_steam=no'
            tags[i-6] = 'available_on_steam=no'
            tags[i-7] = 'available_on_steam=no'

        if tokens[i-14:i+1] == ['not', 'available', 'to', 'play', 'on', 'steam', 'and', 
                      'does', 'not', 'offer', 'support', 'for', 'mac', 'or', 
                      'linux']:
            tags[i] = 'has_linux_release=no'
            tags[i-2] = 'has_mac_release=no'
            tags[i-3] = 'has_mac_release=no'
            tags[i-4] = 'has_mac_release=no'
            tags[i-5] = 'has_mac_release=no'
            tags[i-6] = 'has_mac_release=no'
            tags[i-7] = 'has_mac_release=no'
            tags[i-9] = 'available_on_steam=no'
            tags[i-10] = 'available_on_steam=no'
            tags[i-11] = 'available_on_steam=no'
            tags[i-12] = 'available_on_steam=no'
            tags[i-13] = 'available_on_steam=no'
            tags[i-14] = 'available_on_steam=no'
        if tokens[i-10:i+1] == ["is", "not", "available", "on", "either", 
                                "steam", ",", "linux", ",", "or", "mac"]:
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'
            for j in range(i-9,i-4):
                tags[j] = 'available_on_steam=no'
        if tokens[i-8:i+1] == ["is", "not", "available", "on", 
                                "steam", ",", "linux", "or", "mac"]:
            tags[i] = 'has_mac_release=no'
            tags[i-2] = 'has_linux_release=no'
            for j in range(i-7,i-3):
                tags[j] = 'available_on_steam=no'

        if tokens[i-3:i+1] == ["but", "not", "on", "steam"]:
            tags[i-3] = 'available_on_steam=no'
            tags[i-2] = 'available_on_steam=no'
            tags[i-1] = 'available_on_steam=no'
            tags[i] = 'available_on_steam=no'

        if tokens[i-2:i+1] == ['the', 'multiplayer', 'sport']:  
            tags[i-1] = 'has_multiplayer=yes'

        if tokens[i-3:i+1] == ['is', 'a', 'multiplayer', 'sport']:  
            tags[i-1] = 'has_multiplayer=yes'

        if tokens[i-3:i+1] == ['is', 'no', 'steam', 'release']:
            tags[i-2] = 'available_on_steam=no'
            tags[i-1] = 'available_on_steam=no'
            tags[i] = 'available_on_steam=no'
        if tokens[i-2:i+1] == ['no', 'steam', 'release']:
            tags[i-2] = 'available_on_steam=no'
            tags[i-1] = 'available_on_steam=no'
            tags[i] = 'available_on_steam=no'

        if tokens[i-4:i+1] == ['not', 'have', 'a', 'steam', 'release']:
            tags[i-4] = 'available_on_steam=no'
            tags[i-3] = 'available_on_steam=no'
            tags[i-2] = 'available_on_steam=no'
            tags[i-1] = 'available_on_steam=no'
            tags[i] = 'available_on_steam=no'
        if tokens[i-4:i+1] == ['not', 'have', 'a', 'linux', 'release']:
            tags[i-4] = 'has_linux_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-2] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'
            tags[i] = 'has_linux_release=no'
        if tokens[i-4:i+1] == ['not', 'have', 'a', 'mac', 'release']:
            tags[i-4] = 'has_mac_release=no'
            tags[i-3] = 'has_mac_release=no'
            tags[i-2] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i] = 'has_mac_release=no'








        if tokens[i-2:i+1] == ['available','on', 'steam']: 
            print("HERE!")
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes' 
        if tokens[i-3:i+1] == ['not', 'available', 'on', 'steam']:
            print("THEN ME")
            tags[i-3] = 'available_on_steam=no'
            tags[i-2] = 'available_on_steam=no'
            tags[i-1] = 'available_on_steam=no'
            tags[i] = 'available_on_steam=no'
        if tokens[i-3:i+1] == ["n't", 'available', 'on', 'steam']:
            tags[i-3] = 'available_on_steam=no'
            tags[i-2] = 'available_on_steam=no'
            tags[i-1] = 'available_on_steam=no'
            tags[i] = 'available_on_steam=no'
        if tokens[i-4:i+1] == ["n't", 'have', 'a', 'linux', 'release']:
            tags[i-4] = 'has_linux_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-2] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ["does", "have", "a", "mac", "version"]:
            for j in range(i-4, i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ["you", "can", "get", "it", "through", "steam"]:
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes'
        if tokens[i-3:i+1] == ['game', 'has', 'multiplayer', 'available']:
            tags[i-2] = 'has_multiplayer=yes'
            tags[i-1] = 'has_multiplayer=yes'
            tags[i] = 'has_multiplayer=yes'
        if tokens[i-2:i+1] == ["'s", "no", "multiplayer"]:
            tags[i] = 'has_multiplayer=no'
            tags[i-1] = 'has_multiplayer=no'
        if tokens[i-2:i+1] == ["has", "no", "multiplayer"]:
            tags[i] = 'has_multiplayer=no'
            tags[i-1] = 'has_multiplayer=no'
        if tokens[i-2:i+1] == ['is', 'a', 'single-player']: 
            tags[i] = 'has_multiplayer=no'
            tags[i-1] = 'has_multiplayer=no'
        if tokens[i-3:i+1] == ['is', 'also','on', 'steam']: 
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes'
            tags[i-2] = 'available_on_steam=yes'

        if tokens[i-6:i+1] == ['was', "n't", "released", "on", "linux", "or", 
                               "mac"]:
            tags[i-2] = 'has_linux_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-4] = 'has_linux_release=no'
            tags[i-5] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ["play", "together", "with", "your", "friends"]:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer=yes'


        if tokens[i-10:i+1] == ['whose', 'multiplayer', 'mode', 'allows', 
                                'you', 'to', 'play', 'with', 'your',
                                'friends', 'online']:
            for j in range(i-9, i+1):
                tags[j] = 'has_multiplayer=yes'
        if tokens[i-6:i+1] == ['but', 'has', 'no', 'linux', 'or', 'mac',
                               'release']:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ["with", "a", "multiplayer", "mode"]:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-5:i+1] == ["not", "available", "on", "mac", "or", "linux"]:
            for j in range(i-5, i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'
            

        if tokens[i-6:i+1] == ["it", "really", "raised", "the", "bar", "for", 
                               "multiplayer"]:
            tags[i] = 'has_multiplayer=yes'
            tags[i-1] = 'has_multiplayer=yes'
        if tokens[i-3:i+1] == ['is', 'an', 'excellent', 'multiplayer']:
            tags[i] = 'has_multiplayer=yes'
        if tokens[i-8:i+1] == ['with', 'bird', "'s", 'eye', 'view', 'player',
                               'perspective', 'and', 'multiplayer']:
            tags[i] = 'has_multiplayer=yes'

        if tokens[i-4:i+1] == ["you", "can", "also", "play", "multiplayer"]:
            tags[i] = 'has_multiplayer=yes'
        if tokens[i-2:i+1] == ['game', 'with', 'multiplayer']:
            tags[i] = 'has_multiplayer=yes'
        if tokens[i-3:i+1] == ["can", "be", "played", "multiplayer"]:
            tags[i] = 'has_multiplayer=yes'
        if tokens[i-2:i+1] == ['is', 'a', 'multiplayer']:
            tags[i] = 'has_multiplayer=yes'
        if tokens[i-2:i+1] == ['strategy', "with", 'multiplayer']:
            tags[i] = 'has_multiplayer=yes'

        if tokens[i-4:i+1] == ["can", "be", "found", "on", "steam"]:
            tags[i] = 'available_on_steam=yes'
        
        if tokens[i-5:i+1] == ["does", "n't", "support", "linux", "or", "mac"]:
            for j in range(i-5, i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
        if tokens[i-6:i+1] == ["there", "is", "no", "linux", "or", "mac", 'release']:
            tags[i-3] = 'has_linux_release=no'
            tags[i-4] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ["not", "available", "for", "linux", "or", 
                               "mac"]:
            tags[i] = 'has_mac_release=no'
            tags[i-2] = 'has_linux_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-4] = 'has_linux_release=no'
            tags[i-5] = 'has_linux_release=no'
        if tokens[i-5:i+1] == ["not", "available", "for", "mac", "or", 
                               "linux"]:
            tags[i] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ['released', 'on', 'steam']:
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes'
            tags[i-2] = 'available_on_steam=yes'

        if tokens[i-1:i+1] == ['via', 'steam']:
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes'

        if tokens[i-2:i+1] == ['DEVELOPER', 'on', 'steam']:
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes'

        if tokens[i-5:i+1] == ["you", "can", "get", "it", "on", "steam"]:
            for j in range(i-5, i+1):
                tags[j] = 'available_on_steam=yes'
        if tokens[i-5:i+1] == ["you", "can", "get", "in", "on", "steam"]:
            for j in range(i-5, i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-3:i+1] == ['is', 'not', 'on', 'steam']:
            tags[i] = 'available_on_steam=no'
            tags[i-1] = 'available_on_steam=no'
            tags[i-2] = 'available_on_steam=no'
        if tokens[i-6:i+1] == ["but", "does", "not", "have", "a", "steam",
                               "release"]:
            for j in range(i-5, i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-2:i+1] == ['pc', 'and', 'mac']:
            tags[i] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ['but', 'not', 'linux']:
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ["ca", "n't", "get", "it", "on", "steam"]:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-5:i+1] == ["you", "can", "play", "it", "on", "mac"]:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ["and", "has", "multiplayer"]:
            tags[i] = 'has_multiplayer=yes'
            tags[i-1] = 'has_multiplayer=yes'

        if tokens[i-4:i+1] == ["it", "has", "a", "multiplayer", "mode"]:
            tags[i] = 'has_multiplayer=yes'
            tags[i-1] = 'has_multiplayer=yes'
            tags[i-2] = 'has_multiplayer=yes'

        if tokens[i-7:i+1] == ["you", "can", "get", "it", "on", "linux", 
                               ",", "mac"]:
            tags[i] = 'has_mac_release=yes'
            tags[i-2] = 'has_linux_release=yes'
            tags[i-3] = 'has_linux_release=yes'

        if tokens[i-8:i+1] == ["runs", "on", "pc", ",", "mac", ",", "and", "linux", "platforms"]:
            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'
            tags[i-4] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ["there", "'s", "linux", "and", "mac", "support"]:
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'
            tags[i-3] = 'has_linux_release=yes' 
        if tokens[i-7:i+1] == ["does", "n't", "have", "a", "linux", "or", "mac", "release"]:
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no' 
            tags[i-4] = 'has_linux_release=no' 
            tags[i-5] = 'has_linux_release=no' 
            tags[i-6] = 'has_linux_release=no' 
            tags[i-7] = 'has_linux_release=no' 
            
        if tokens[i-5:i+1] == ['is', 'not', 'on', 'linux', 'or', 'mac']:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ["not", "released", "for", "linux", "or", "mac"]:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-2:i+1] == ["in", "multiplayer", "mode"]:
            tags[i] = 'has_multiplayer=yes'
            tags[i-1] = 'has_multiplayer=yes'
            tags[i-2] = 'has_multiplayer=yes'

        if tokens[i-2:i+1] == ["it", "has", "multiplayer"]:
            tags[i] = 'has_multiplayer=yes'

        if tokens[i-2:i+1] == ["with", "multiplayer", "capabilities"]:
            tags[i] = 'has_multiplayer=yes'
            tags[i-1] = 'has_multiplayer=yes'
        if tokens[i-4:i+1] == ["there", "is", "no", "multiplayer", "mode"]:
            tags[i] = 'has_multiplayer=no'
            tags[i-1] = 'has_multiplayer=no'
            tags[i-2] = 'has_multiplayer=no'
        if tokens[i-2:i+1] == ["with", "no", "multiplayer"]:
            tags[i] = 'has_multiplayer=no'
            tags[i-1] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ["did", "not", 'offer', 'multiplayer']:
            for j in range(i-3, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-1:i+1] == ["a", "single-player"]:
            tags[i] = 'has_multiplayer=no'
        if tokens[i-1:i+1] == ["RELEASE_YEAR", "single-player"]:
            tags[i] = 'has_multiplayer=no'

        if tokens[i-2:i+1] == ['multiplayer', 'is', 'available']:
            tags[i-2] = 'has_multiplayer=yes'
            tags[i-1] = 'has_multiplayer=yes'
            tags[i] = 'has_multiplayer=yes'

        if tokens[i-3:i+1] == ["does", "n't", "have", "multiplayer"]:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-2:i+1] == ['is', 'on', 'steam']:
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes'
        if tokens[i-1:i+1] == ['through', 'steam']:
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes'
        if tokens[i-8:i+1] == ["does", "n't", "have", "a", "linux", "or", "a", "mac", "release"]:
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i-2] = 'has_mac_release=no'
            for j in range(i-8, i-3):
                tags[j] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ["steam", "has", "this", "game", "available"]:
            for j in range(i-4, i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-2:i+1] == ["pc", "and", "steam"]:
            tags[i] = 'available_on_steam=yes'

        if tokens[i-6:i+1] == ["does", "n't", "have", "linux", "or", "mac", 
                               "support"]:
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-4] = 'has_linux_release=no'
            tags[i-5] = 'has_linux_release=no'
            tags[i-6] = 'has_linux_release=no'
        if tokens[i-5:i+1] == ["with", "no", "linux", "or", "mac", 
                               "releases"]:
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-4] = 'has_linux_release=no'
            tags[i-5] = 'has_linux_release=no'


        if tokens[i-2:i+1] == ["that", "has", "multiplayer"]:
            tags[i] = 'has_multiplayer=yes'
        if tokens[i-7:i+1] == ["does", "n't", "have", "a", "mac", "or", "linux", "release"]:
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'
            for j in range(i-7, i-2):
                tags[j] = 'has_mac_release=no'
        if tokens[i-7:i+1] == ["does", "not", "have", "a", "mac", "or", "linux", "release"]:
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'
            for j in range(i-7, i-2):
                tags[j] = 'has_mac_release=no'


        if tokens[i-2:i+1] == ["'s", "a", "multiplayer"]:
            tags[i] = 'has_multiplayer=yes'

        if tokens[i-1:i+1] == ["for", "single-player"]:
            tags[i] = 'has_multiplayer=no'

        if tokens[i-5:i+1] == ["is", "available", "for", "purchase", "on",
                               "steam"]:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-4:i+1] == ["is", "not", "supported", "on", "mac"]:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'
        if tokens[i-4:i+1] == ["is", "not", "supported", "on", "mac", 'or', 'linux']:
            tags[i] = 'has_linux_release=no'

        if tokens[i-6:i+1] == ["you", "can", "play", "it", "even", "on",
                               "linux"]:
            for j in range(i-6,i+1):
                tags[j] = 'has_linux_release=yes'
        if tokens[i-2:i+1] == ['pc', 'and', 'linux']:
            tags[i] = 'has_linux_release=yes'

        if tokens[i-3:i+1] == ['but', 'not', 'for', 'mac']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ["is", "supported", "on", "linux"]:
            for j in range(i-2, i+1):
                tags[j] = 'has_linux_release=yes'
        if tokens[i-3:i+1] == ['is', 'not', 'on', 'mac']:
            for j in range(i-2, i+1):
                tags[j] = 'has_mac_release=no'
        if tokens[i-5:i+1] == ['is', 'not', 'on', 'mac', 'or', 'linux']:
            tags[i] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ["can", "find", "on", "steam"]:
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes'

        if tokens[i-7:i+1] == ["does", "not", "have", "a", "linux", "or",
                               "mac", "release"]:
            for j in range(i-7, i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ["but", "not", "for", "linux", "or", "mac"]:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
        if tokens[i-5:i+1] == ['is', 'no', 'linux', 'or', 'mac', 'support']:
            tags[i-4] = 'has_linux_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ["is", "not", "on", "linux"]:
            for j in range(i-2, i+1):
                tags[j] = 'has_linux_release=no'
            
        if tokens[i-4:i+1] == ["is", "not", "supported", "on", "mac"]:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'
        if tokens[i-6:i+1] == ["is", "not", "supported", "on", "mac", 'or', 'linux']:
            tags[i] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ["is", "supported", "on", "mac"]:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'
        if tokens[i-5:i+1] == ["is", "supported", "on", "mac", "and", "linux"]:
            tags[i] = 'has_linux_release=yes'


        if tokens[i-6:i+1] == ["may", "not", "be", "on", "steam", "or", 
                               "linux"]:
            for j in range(i-6,i-1):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_linux_release=no'


        if tokens[i-3:i+1] == ['pc', ',', 'and', 'mac']:
            tags[i] = 'has_mac_release=yes'


        if tokens[i-1:i+1] == ["single-player", "only"]:
            tags[i] = 'has_multiplayer=no'
            tags[i-1] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ["has", "no", "linux", "release"]:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=no'
        if tokens[i-4:i+1] == ["does", "have", "a", "mac", "release"]:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-6:i+1] == ["can", "not", "purchase", "the", "game",
                               "on", "steam"]:
            for j in range(i-6,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-1:i+1] == ['a', 'multiplayer']:
            tags[i] = 'has_multiplayer=yes'
        
        if tokens[i-3:i+1] == ["if", "you", "like", "multiplayer"]:
            tags[i] = 'has_multiplayer=yes'

        if tokens[i-5:i+1] == ["wo", "n't", "find", "it", "on", "steam"]:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-5:i+1] == ["does", "not", "run", "on", "linux", "systems"]:
            for j in range(i-5,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['the', 'game', 'has', 'a', 'mac', 'version']:
            for j in range(i-5,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ["ca", "n't", "play", 'on', 'linux']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=no'
        if tokens[i-6:i+1] == ["ca", "n't", "play", 'on', 'linux', 'or', 'mac']:
            tags[i] = 'has_mac_release=no'


        if tokens[i-5:i+1] == ['unavailable', 'on', 'linux', 'and', 'mac',
                               'systems']:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['pc', 'games', 'from', 'steam']:
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes'
                

        if tokens[i-4:i+1] == ['but', 'not', 'linux', 'or', 'mac']:
            tags[i] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ["you", "can", "still", "get", "it", "on",
                               "steam"]:
            for j in range(i-6, i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-3:i+1] == ['you', 'can', 'play', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-2:i+1] == ['features', 'multiplayer', 'modes']:
            for j in range(i-2, i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-4:i+1] == ["'s", "not", "available", "on", "linux"]:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ["pc", ",", "mac"]:
            tags[i] = 'has_mac_release=yes'

        if tokens[i-1:i+1] == ["features", "multiplayer"]:
            tags[i] = 'has_multiplayer=yes'
            tags[i-1] = 'has_multiplayer=yes'

        if tokens[i-4:i+1] == ['a', 'mac', 'version', 'is', 'available']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=yes'
        if tokens[i-2:i+1] == ['no', 'linux', 'release']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-8:i+1] == ['has', 'no', 'steam', ',', 'linux', ',', 'or', 
                               'mac', 'support']:
            tags[i-8] = 'available_on_steam=no'
            tags[i-7] = 'available_on_steam=no'
            tags[i-6] = 'available_on_steam=no'
            tags[i-4] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ["nor", "for", "linux", "or", "mac"]:
            for j in range(i-4, i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-7:i+1] == ['but', 'not', 'steam', ',', 'linux', ',', 'or', 'mac']:
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-5] = 'available_on_steam=no'
            tags[i-6] = 'available_on_steam=no'


        if tokens[i-4:i+1] == ["does", "not", "have", "a", "multiplayer"]:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer=no'
               
        if tokens[i-4:i+1] == ["by", "visiting", "your", "steam", "account"]: 
            for j in range(i-4, i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-2:i+1] == ["currently", "not", "linux"]:
            for j in range(i-2, i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['available', 'on', 'steam', 'and', 'mac']:
            tags[i] = 'has_mac_release=yes'
        if tokens[i-6:i+1] == ['available', 'on', 'steam', 'as', 'well', 'as', 'linux']:
            tags[i] = 'has_linux_release=yes'


        if tokens[i-2:i+1] == ['has', 'mac', 'support']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ["does", "not", "run", "on", "linux"]:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['does', "n't", 'feature', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'


        if tokens[i-3:i+1] == ['does', 'not', 'have', 'multiplayer']:
            for j in range(i-3, i+1):
                tags[j] = 'has_multiplayer=no'
        if tokens[i-4:i+1] == ['does', "n't", 'have', 'a', 'multiplayer']:
            for j in range(i-4, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ['pc', ',', 'and', 'linux']:
            tags[i] = 'has_linux_release=yes'

        if tokens[i-3:i+1] == ['not', 'on', 'a', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['not', 'available', 'for', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['has', 'no', 'mac', 'support']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'


        if tokens[i-3:i+1] == ['is', 'no', 'multiplayer', 'option']:
            for j in range(i-2, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-4:i+1] == ['is', 'not', 'out', 'on', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-2:i+1] == ['no', 'mac', 'release']:
            for j in range(i-2, i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['has', 'one', 'for', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ['but', 'not', 'one', 'for', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['there', 'is', 'a', 'mac', 'release']:
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'


        if tokens[i-4:i+1] == ['no', 'release', 'for', 'mac', 'systems']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-7:i+1] == ["does", "not", "have", "a", "steam", "or",
                               "linux", "release"]:
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'
            for j in range(i-7, i-2):
                tags[j] = 'available_on_steam=no'


        if tokens[i-5:i+1] == ['not', 'available', 'on', 'steam', 'or', 'linux']:
            tags[i] = 'has_linux_release=no'
            for j in range(i-5,i-1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-5:i+1] == ['not', 'available', 'on', 'linux', 'or', 'mac']:
            tags[i] = 'has_mac_release=no'
            for j in range(i-5, i-1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['does', 'not', 'offer', 'a', 'multiplayer', 'mode']:
            for j in range(i-5,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-8:i+1] == ['does', "n't", 'have', 'multiplayer', 'or', 'linux', 'or', 'mac', 'support']:
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['has', 'no', 'linux', 'or', 'mac', 'version']:
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-4] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['massively', 'multiplayer', 'online', 'role-playing']:
            tags[i-2] = 'genres=MMORPG'
        if tokens[i-5:i+1] == ['massively', 'multiplayer', 'online', 'role', '-', 'playing']:
            for j in range(i-5,i+1):
                tags[j] = 'genres=MMORPG'


        if tokens[i-3:i+1] == ['no', 'release', 'on', 'steam']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-5:i+1] == ['no', 'release', 'on', 'steam', 'or', 'linux']:
            tags[i] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ['without', 'linux', 'support']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ["not", "on", "linux"]:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=no'


        if tokens[i-5:i+1] == ['nor', 'is', 'it', 'available', 'on', 'steam']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-6:i+1] == ['nor', 'can', 'you', 'find', 'it', 'on', 'steam']:
            for j in range(i-6,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-6:i+1] == ['does', 'not', 'have', 'linux', 'or', 'mac', 'releases']:
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            for j in range(i-6, i-2):
                tags[j] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['never', 'released', 'on', 'mac', 'or', 'linux']:
            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['has', 'a', 'mac', 'release']:
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ['lack', 'of', 'multiplayer']:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ["not", "a", "multiplayer", "game"]:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ['does', 'not', 'feature', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-6:i+1] == ['is', 'also', 'available', 'in', 'the', 'steam', 'store']:
            for j in range(i-6,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-6:i+1] == ['it', 'has', 'a', 'linux', 'and', 'mac', 'release']:
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'
            tags[i-3] = 'has_linux_release=yes'
            tags[i-4] = 'has_linux_release=yes'
            tags[i-5] = 'has_linux_release=yes'

        if tokens[i-7:i+1] == ['pc', ',', 'steam', ',', 'linux', 'and', 'even', 'mac']:
            tags[i-5] = 'available_on_steam=yes'
            tags[i-3] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-6:i+1] == ['has', 'full', 'support', 'for', 'linux', 'and', 'mac']:
            tags[i] = 'has_mac_release=yes'
            tags[i-2] = 'has_linux_release=yes' 
            tags[i-3] = 'has_linux_release=yes' 
            tags[i-4] = 'has_linux_release=yes' 
            tags[i-5] = 'has_linux_release=yes' 
            tags[i-6] = 'has_linux_release=yes' 

        if tokens[i-2:i+1] == ['without', 'a', 'multiplayer']:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=no'
        if tokens[i-2:i+1] == ['without', 'multiplayer', 'support']:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-7:i+1] == ["n't", 'have', 'a', 'mac', 'or', 'a', 'linux', 'release']:
            for j in range(i-7,i-3):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'
        if tokens[i-5:i+1] == ["n't", 'compatible', 'with', 'linux', 'and', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'


        if tokens[i-6:i+1] == ['both', 'a', 'linux', 'and', 'a', 'mac', 'release']:
            for j in range(i-5,i-3):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-7:i+1] == ['was', 'also', 'a', 'release', 'for', 'linux', 'and', 'mac']:
            for j in range(i-7,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-7:i+1] == ['has', 'not', 'been', 'released', 'for', 'linux', 'or', 'mac']:
            for j in range(i-7,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['not', 'released', 'for', 'mac', 'or', 'linux']:
            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['not', 'released', 'on', 'mac', 'or', 'linux']:
            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['including', 'availability', 'on', 'steam']:
            for j in range(i-3, i+1):
                tags[j] = 'available_on_steam=yes'
        if tokens[i-3:i+1] == ['is', 'available', 'for', 'steam']:
            for j in range(i-3, i+1):
                tags[j] = 'available_on_steam=yes'
        if tokens[i-6:i+1] == ['is', 'available', 'on', 'steam', 'and', 'on', 'mac']:
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'


        if tokens[i-4:i+1] == ['pc', ',', 'and', 'on', 'steam']:
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes'



        if tokens[i-2:i+1] == ['but', 'not', 'mac']:
            for j in range(i-1,i+1):
                tags[j] = 'has_mac_release=no'
        if tokens[i-3:i+1] == ['though', 'not', 'on', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['can', 'also', 'run', 'on', 'linux']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ['it', 'is', 'supported', 'by', 'linux']:
            for j in range(i-4, i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-6:i+1] == ["currently", "available", "on", "major", "platforms",
                               "including", "mac"]:
            for j in range(i-6,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-7:i+1] == ['did', 'get', 'a', 'mac', 'release', 'but', 'no', 'linux']:
            for j in range(i-7, i-2):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'


        if tokens[i-4:i+1] == ['pc', ',', 'with', 'mac', 'support']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['does', 'not', 'have', 'a', 'linux', 'release']:
            for j in range(i-5,i+1):
                tags[j] = 'has_linux_release=no'
        if tokens[i-5:i+1] == ['has', 'not', 'been', 'released', 'on', 'steam']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-3:i+1] == ["'s", 'not', 'on', 'steam']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-5:i+1] == ["'s", "no", "linux", "or", "mac", "support"]:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['can', 'not', 'be', 'played', 'multiplayer']:
            for j in range(i-4, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-4:i+1] == ["is", "not", "available", "on", "linux"]:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['is', 'available', 'for', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['has', 'been', 'released', 'on', 'mac']:
            for j in range(i-4, i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['there', 'is', 'mac', 'and', 'linux', 'support']:
            for j in range(i-5,i-2):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'

        if tokens[i-5:i+1] == ['this', 'includes', 'linux', 'and', 'mac', 'systems']:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ["xbox", ',', 'linux', ',', 'mac']:
            tags[i] = 'has_mac_release=yes'
            tags[i-2] = 'has_linux_release=yes'

        if tokens[i-6:i+1] == ['has', 'both', 'a', 'linux', 'and', 'mac', 'release']:
            for j in range(i-6,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-9:i+1] == ["while", "being", 'available', 'on', 'mac', ',', 'linux', ',', 'and', 'steam']:
            for j in range(i-9,i-4):
                tags[j] = 'has_mac_release=yes'
            tags[i-3] = 'has_linux_release=yes'
            tags[i] = 'available_on_steam=yes'

        if tokens[i-5:i+1] == ['is', 'supported', 'by', 'mac', 'and', 'linux']:
            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'


        if tokens[i-5:i+1] == ['not', 'supported', 'by', 'mac', 'or', 'linux']:

            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['pc', ',', 'and', 'steam']:
            tags[i] = 'available_on_steam=yes'

        if tokens[i-4:i+1] == ["no", "linux", "or", "mac", "release"]:
            tags[i-4] = 'has_linux_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
        if tokens[i-4:i+1] == ["can", "find", "it", "on", "steam"]:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-7:i+1] == ['it', 'was', 'not', 'released', 'on', 'linux', 'or', 'mac']:
            for j in range(i-5, i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['has', 'linux', 'and', 'mac', 'support']:
            tags[i-4] = 'has_linux_release=yes'
            tags[i-3] = 'has_linux_release=yes'
            tags[i-1] = 'has_mac_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-10:i+1] == ['can', 'also', 'get', 'it', 'for', 'steam', ',', 'linux', ',', 'and', 'mac']:
            for j in range(i-10, i-4):
                tags[j] = 'available_on_steam=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-3] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ['multiplayer', 'mode', 'is', 'not', 'available']:
            for j in range(i-4, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-7:i+1] == ['pc', ',', 'steam', ',', 'linux', ',', 'and', 'mac']:
            tags[i] = 'has_mac_release=yes'
            tags[i-3] = 'has_linux_release=yes'
            tags[i-5] = 'available_on_steam=yes'

        if tokens[i-7:i+1] == ['does', 'not', 'support', 'the', 'linux', 'and', 'mac', 'systems']:
            for j in range(i-7,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ['it', 'has', 'no', 'linux', 'or', 'mac', 'versions']:
            for j in range(i-6,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'


        if tokens[i-5:i+1] == ['is', 'not', 'linux', 'or', 'mac', 'release']:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ['there', 'is', 'no', 'mac', 'or', 'linux', 'release',]:
            for j in range(i-6,i-2):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['can', 'be', 'downloaded', 'on', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-6:i+1] == ['not', 'available', 'on', 'either', 'linux', 'or', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ['you', 'can', 'not', 'download', 'it', 'from', 'steam']:
            for j in range(i-6,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-5:i+1] == ['currently', 'available', 'on', 'steam', 'and', 'linux']:
            tags[i] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ['not', 'currently', 'available', 'on', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-2:i+1] == ["not", "on", "steam"]:
            for j in range(i-2, i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-4:i+1] == ['it', 'has', 'a', 'linux', 'release']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ['no', 'steam', 'or', 'mac', 'release']:
            tags[i-4] = 'available_on_steam=no'
            tags[i-3] = 'available_on_steam=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i] = 'has_mac_release=no'
        if tokens[i-4:i+1] == ['you', 'can', 'play', 'on', 'linux']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=yes'
        if tokens[i-5:i+1] == ['wo', "n't", 'run', 'on', 'a', 'mac']:
            for j in range(i-5,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ['is', 'playable', 'on', 'both', 'linux', 'and', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['there', 'are', 'mac', 'and', 'linux', 'versions']:
            for j in range(i-5,i-2):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'

        if tokens[i-7:i+1] == ['does', 'even', 'have', 'a', 'linux', 'and', 'mac', 'release']:
            for j in range(i-7,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens == ['has', 'a', 'linux', 'and', 'mac', 'release']:
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'
            tags[i-3] = 'has_linux_release=yes'
            tags[i-4] = 'has_linux_release=yes'
            tags[i-5] = 'has_linux_release=yes'

        if tokens[i-5:i+1] == ['has', 'a', 'linux', 'and', 'mac', 'release']:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-3:i+1] == ['mac', ',', 'and', 'linux']:
            tags[i] = 'has_linux_release=yes'

        if tokens[i-6:i+1] == ['has', 'been', 'released', 'on', 'linux', 'and', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-6:i+1] == ['never', 'got', 'a', 'mac', 'or', 'linux', 'release']:
            for j in range(i-6,i-2):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-6:i+1] == ['never', 'released', 'on', 'the', 'linux', 'or', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ["n't", 'available', 'on', 'linux', 'or', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-7:i+1] == ['you', 'can', 'find', 'it', 'at', 'the', 'steam', 'store']:
            for j in range(i-7,i+1):
                tags[j] = 'available_on_steam=yes'
        if tokens[i-5:i+1] == ['with', 'availability', 'on', 'steam', 'and', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'available_on_steam=yes'
            tags[i] = 'has_mac_release=yes'
            
        if tokens[i-5:i+1] == ["with", "no", "linux", "or", "mac", "variant"]:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['is', 'available', 'on', 'the', 'mac']:
            for j in range(i-4, i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-7:i+1] == ['has', 'a', 'mac', 'version', 'but', 'no', 'linux', 'version']:
            for j in range(i-7,i-3):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'
            tags[i-2] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['not', 'out', 'on', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['mac', 'users', 'are', 'lucky']:
            for j in range(i-3, i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-6:i+1] == ['does', 'not', 'have', 'a', 'release', 'for', 'mac']:
            for j in range(i-6,i+1):
                tags[j] = 'has_mac_release=no'
             
        if tokens[i-2:i+1] == ['does', 'for', 'linux']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-5:i+1] == ['pc', ',', 'steam', 'and', 'even', 'linux']:
            tags[i-3] = 'available_on_steam=yes'
            tags[i] = 'has_linux_release=yes'

        if tokens[i-5:i+1] == ['mac', 'users', 'are', 'out', 'of', 'luck']:
            for j in range(i-5, i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['does', 'not', 'have', 'mac', 'support']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ['was', 'never', 'released', 'on', 'linux', 'or', 'mac']:
            for j in range(i-6, i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['with', 'support', 'for', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['has', 'been', 'released', 'for', 'mac']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-3:i+1] == ['did', "n't", 'have', 'multiplayer']:
            for j in range(i-3, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-6:i+1] == ['has', 'no', 'releases', 'on', 'linux', 'or', 'mac']:
            for j in range(i-6, i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
        if tokens[i-2:i+1] == ["'s", "not", 'multiplayer']:
            for j in range(i-1, i+1):
                tags[j] = 'has_multiplayer=no'
        if tokens[i-4:i+1] == ['xbox', ',', 'and', 'on', 'steam']:
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes'

        if tokens[i-6:i+1] == ['is', 'also', 'available', 'for', 'download', 'on', 'steam']:
            for j in range(i-6, i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-3:i+1] == ['does', "n't", "support", 'multiplayer']:
            for j in range(i-3, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-5:i+1] == ['with', 'no', 'linux', 'or', 'mac', 'versions']:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['not', 'available', 'for', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['can', 'buy', 'it', 'on', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-5:i+1] == ['are', 'also', 'linux', 'and', 'mac', 'releases']:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'
        if tokens[i-2:i+1] == ['pc', 'trough', 'steam']:
            tags[i] = 'available_on_steam=yes'
        if tokens[i-6:i+1] == ['will', 'work', 'with', 'mac', 'or', 'linux', 'systems']:
            for j in range(i-6,i-2):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'
        if tokens[i-5:i+1] == ['is', 'a', 'linux', 'and', 'mac', 'release']:
            for j in range(i-5, i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ["no", "multiplayer", "mode"]:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-5:i+1] == ['does', "n't", 'offer', 'a', 'multiplayer', 'mode']:
            for j in range(i-5,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-5:i+1] == ['also', 'works', 'on', 'mac', 'and', 'linux']:
            for j in range(i-5, i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'
        if tokens[i-4:i+1] == ['has', 'linux', 'and', 'mac', 'releases']:
            for j in range(i-4,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-6:i+1] == ['can', 'be', 'played', 'on', 'linux', 'and', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['that', 'came', 'out', 'on', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-5:i+1] == ['not', 'supported', 'on', 'linux', 'or', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['does', "n't", 'offer', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-8:i+1] == ['can', 'also', 'buy', 'this', 'game', 'on', 'the', 'steam', 'store']:
            for j in range(i-8, i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-7:i+1] == ['this', 'game', 'has', 'a', 'linux', 'or', 'mac', 'release']:
            for j in range(i-7,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-9:i+1] == ['was', 'also', 'released', 'for', 'steam', ',', 'linux', ',', 'and', 'mac']:
            for j in range(i-9,i-4):
                tags[j] = 'available_on_steam=yes'
            tags[i-3] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['not', 'available', 'to', 'play', 'as', 'multiplayer']:
            for j in range(i-5,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-5:i+1] == ['can', 'also', 'play', 'this', 'on', 'steam']:
            for j in range(i-5, i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-7:i+1] == ['can', 'not', 'play', 'it', 'on', 'linux', 'or', 'mac']:
            for j in range(i-7, i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
        if tokens[i-7:i+1] == ['is', 'not', 'support', 'for', 'linux', 'and', 'mac', 'systems']:
            for j in range(i-7,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-7:i+1] == ['can', 'not', 'be', 'played', 'on', 'mac', 'or', 'linux']:
            for j in range(i-7,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['pc', ',', 'linux', ',', 'and', 'mac']:
            tags[i] = 'has_mac_release=yes'
            tags[i-3] = 'has_linux_release=yes'

        if tokens[i-7:i+1] == ['as', 'well', 'as', 'a', 'linux', 'and', 'mac', 'version']:
            for j in range(i-7,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes' 

        if tokens[i-5:i+1] == ['pc', ',', 'linux', 'and', 'the', 'mac']:
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'
            tags[i-3] = 'has_linux_release=yes'

        if tokens[i-2:i+1] == ['pc', 'on', 'steam']:
            tags[i] = 'available_on_steam=yes'
            tags[i-1] = 'available_on_steam=yes'
        if tokens[i-4:i+1] == ['or', 'on', 'steam', 'for', 'pc']:
            tags[i-3] = 'available_on_steam=yes'
            tags[i-2] = 'available_on_steam=yes'

        if tokens[i-3:i+1] == ['also', 'released', 'for', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ['not', 'for', 'linux']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ['with', 'mac', 'support']:
            for j in range(i-2, i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-3:i+1] == ['but', 'not', 'on', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ["'s", "no", 'steam', 'or', 'linux', 'availability']:
            for j in range(i-5,i-2):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'
        if tokens[i-4:i+1] == ["'s", "also", 'available', 'on', 'linux']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=yes'
        if tokens[i-5:i+1] == ['does', "n't", 'have', 'a', 'mac', 'release']:
            for j in range(i-5,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['does', 'have', 'a', 'release', 'for', 'linux']:
            for j in range(i-5,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-3:i+1] == ['has', 'a', 'linux', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=yes'
        if tokens[i-3:i+1] == ["'s", 'available', 'for', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'


        if tokens[i-3:i+1] == ["'s", 'available', 'on', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-6:i+1] == ["'s", 'not', 'available', 'on', 'linux', 'or', 'steam']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'available_on_steam=no'

        if tokens[i-3:i+1] == ['not', 'released', 'for', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['can', 'operate', 'on', 'mac']:
            for j in range(i-3, i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-7:i+1] == ['not', 'currently', 'available', 'through', 'steam', 'or', 'on', 'linux']:
            for j in range(i-7,i-2):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['with', 'both', 'linux', 'and', 'mac', 'releases']:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'
        if tokens[i-4:i+1] == ['will', 'find', 'it', 'on', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=yes'
        if tokens[i-5:i+1] == ['is', 'available', 'for', 'mac', 'and', 'linux']:
            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ['pc', ',', 'linux', 'and', 'mac']:
            tags[i] = 'has_mac_release=yes'
            tags[i-2] = 'has_linux_release=yes'

        if tokens[i-6:i+1] == ['nor', 'play', 'it', 'on', 'linux', 'or', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-7:i+1] == ['you', 'can', 'not', 'get', 'this', 'game', 'on', 'steam']:
            for j in range(i-7,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-8:i+1] == ['is', 'available', 'on', 'steam', ',', 'linux', ',', 'and', 'mac']:
            for j in range(i-8,i-4):
                tags[j] = 'available_on_steam=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-3] = 'has_linux_release=yes' 

        if tokens[i-4:i+1] == ['has', 'mac', 'and', 'linux', 'ports']:
            tags[i-3] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'

        if tokens[i-5:i+1] == ['there', 'is', 'linux', 'and', 'mac', 'support']:
            for j in range(i-4,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'
        if tokens[i-7:i+1] == ['with', 'no', 'option', 'to', 'play', 'with', 'multiple', 'players']:
            for j in range(i-7,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ['does', 'not', 'offer', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-1:i+1] == ['no', 'multiplayer']:
            for j in range(i-1,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ['but', 'not', 'for', 'steam']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-3:i+1] == ["n't",  'available', 'for', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=no'
        if tokens[i-3:i+1] == ['also', 'released', 'on', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'
        if tokens[i-3:i+1] == ['is', 'supported', 'by', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ["n't", 'a', 'mac', 'or', 'linux', 'release']:
            for j in range(i-5,i-2):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'
        if tokens[i-4:i+1] == ['it', 'is', 'available', 'on', 'mac',]:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['does', 'not', 'offer', 'a', 'linux', 'release']:
            for j in range(i-5,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['has', 'no', 'linux', 'or', 'mac', 'versions']:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['no', 'release', 'for', 'linux', 'or', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['not', 'supported', 'for', 'linux', 'or', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['you', 'can', 'grab', 'it', 'on', 'steam']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-2:i+1] == ['no', 'online', 'multiplayer']:
            for j in range(i-2,i+1):
                tags[j]  = 'has_multiplayer=no'
        if tokens[i-10:i+1] == ['no', 'online', 'multiplayer', ',', 'or', 'of', 'course', 'linux', 'or', 'mac', 'releases']:
                tags[i] = 'has_mac_release=no'
                tags[i-1] = 'has_mac_release=no'
                tags[i-3] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ['not', 'through', 'steam']:
            for j in range(i-2, i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-8:i+1] == ['not', 'available', 'on', 'steam', ',', 'linux', ',', 'or', 'mac']:
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['nor', 'linux', 'or', 'mac']:
            tags[i-3] = 'has_linux_release=no'
            tags[i-2] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['no', 'steam', 'release', 'or', 'linux', 'release']:
            for j in range(i-5,i-2):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ["n't", 'run', 'on', 'linux', 'systems']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['without', 'being', 'on', 'steam']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-3:i+1] == ['was', 'released', 'on', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'
        if tokens[i-4:i+1] == ['but', 'not', 'linux', 'or', 'steam']:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'available_on_steam=no'

        if tokens[i-5:i+1] == ['without', 'a', 'linux', 'or', 'mac', 'release']:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['ca', "n't", 'find', 'it', 'on', 'steam']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-5:i+1] == ['not', 'available', 'for', 'steam', 'or', 'linux']:
            for j in range(i-5,i-1):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-9:i+1] == ['there', 'is', 'a', 'mac', 'version', 'but', 'no', 'equivalent', 'linux', 'option']:
            for j in range(i-9,i-4):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'
            tags[i-2] = 'has_linux_release=no'
            tags[i-3] = 'has_linux_release=no'
        if tokens[i-2:i+1] == ['and', 'supports', 'mac']:
            for j in range(i-2, i+1):
                tags[j] = 'has_mac_release=yes'
        if tokens[i-4:i+1] == ['not', 'on', 'mac', 'or', 'linux']:
            for j in range(i-4,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['no', 'linux', 'or', 'mac', 'support']:
            for j in range(i-4,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['no', 'mac', 'or', 'linux']:
            for j in range(i-3,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'


        if tokens[i-7:i+1] == ['not', 'on', 'steam', ',', 'linux', ',', 'or', 'mac']:
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'
        if tokens[i-9:i+1] == ['not', 'currently', 'available', 'on', 'steam', ',', 'linux', ',', 'or', 'mac']:
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'

        if tokens[i-8:i+1] == ["n't", 'play', 'it', 'on', 'steam', ',', 'linux', 'or', 'mac']:
            tags[i] = 'has_mac_release=no'
            tags[i-2] = 'has_linux_release=no'
            for j in range(i-8,i-3):
                tags[j] = 'available_on_steam=no'
        if tokens[i-8:i+1] == ['nor', 'does', 'it', 'have', 'a', 'linux', 'or', 'mac', 'release']:
            for j in range(i-8,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
        if tokens[i-7:i+1] == ["'s", 'no', 'steam', ',', 'linux', 'or', 'mac', 'support']:
            for j in range(i-7,i-4):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['has', 'a', 'steam', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-7:i+1] == ['not', 'have', 'a', 'release','on', 'linux', 'or', 'mac']:
            for j in range(i-7, i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ["n't", "play", "it", "on", "linux", "or", "mac"]:
            for j in range(i-6, i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['pc', ',', 'linux', ',', 'or', 'mac']:
            tags[i] = 'has_mac_release=yes'
            tags[i-3] = 'has_linux_release=yes'


        if tokens[i-8:i+1] == ['you', 'can', 'even', 'play', 'it', 'on', 'linux', 'or', 'mac']:
            for j in range(i-8,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['also', 'available', 'on', 'linux', 'and', 'mac']: 
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['can', 'play', 'multiplayer', 'with', 'friends']:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-4:i+1] == ['can', 'play', 'mutiplayer', 'with', 'friends']:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-3:i+1] == ['does', 'not', 'support', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-4:i+1] == ['pc', ',', 'mac', 'and', 'linux']:
            tags[i] = 'has_linux_release=yes'

        if tokens[i-5:i+1] == ['runs', 'even', 'on', 'linux', 'and', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-7:i+1] == ['and', 'for', 'the', 'mac', 'and', 'linux', 'operating', 'systems']:
            for j in range(i-6,i-3):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'
            tags[i-2] = 'has_linux_release=yes'

        if tokens[i-3:i+1] == ["n't", 'be', 'played', 'multiplayer']:
            for j in range(i-3, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ['is', 'available', 'on', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['not', 'on', 'steam', 'or', 'linux']:
            tags[i] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['but', 'no', 'linux', 'support']:
            for j in range(i-3, i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['can', 'be', 'played', 'with', 'your', 'friends']:
            for j in range(i-5,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-4:i+1] == ['but', 'not', 'a', 'mac', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'
        if tokens[i-2:i+1] == ['operates', 'on', 'mac']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-1:i+1] == ['no', 'linux']:
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ["'s",'mac', 'support']:
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['not', 'available', 'as', 'a', 'multiplayer', 'game']:
            for j in range(i-5,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-7:i+1] == ['with', 'linux', ',', 'mac', ',', 'and', 'steam', 'support']:
            tags[i-7] = 'has_linux_release=yes'
            tags[i-6] = 'has_linux_release=yes'
            tags[i-4] = 'has_mac_release=yes'
            tags[i-1] = 'available_on_steam=yes'
            tags[i] = 'available_on_steam=yes'

        if tokens[i-5:i+1] == ['including', 'support', 'for', 'mac', 'and', 'linux']:
            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'
        if tokens[i-4:i+1] == ['with', 'mac', 'and', 'linux', 'support']:
            tags[i-4] = 'has_mac_release=yes'
            tags[i-3] = 'has_mac_release=yes'
            tags[i-1] = 'has_linux_release=yes'
            tags[i] = 'has_linux_release=yes'

        if tokens[i-7:i+1] == ['both', 'a', 'linux', 'release', 'and', 'a', 'mac', 'release']:
            for j in range(i-7,i-3):
                tags[j] = 'has_linux_release=yes'
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'
        if tokens[i-5:i+1] == ['is', 'available', 'for', 'linux', 'and', 'mac']:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-6:i+1] == ['with', 'a', 'linux', 'and', 'mac', 'release', 'too']:
            for j in range(i-6,i-3):
                tags[j] = 'has_linux_release=yes'
            tags[i-2] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-6:i+1] == ['has', 'a', 'linux', 'and', 'a', 'mac', 'release']:
            tags[i-6] = 'has_linux_release=yes'
            tags[i-5] = 'has_linux_release=yes'
            tags[i-4] = 'has_linux_release=yes'
            tags[i-2] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-3:i+1] == ['not', 'offer', 'any', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'
        if tokens[i-2:i+1] == ['lacks', 'multiplayer', 'support']:
            for j in range(i-3, i+1):
                tags[j] = 'has_multiplayer=no'

            

        if tokens[i-1:i+1] == ['nor', 'linux']:
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-7:i+1] == ['not', 'an', 'option', 'for', 'linux', 'or', 'mac', 'users']:
            for j in range(i-7,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
        if tokens[i-4:i+1] == ["n't", 'have', 'a', 'multiplayer', 'mode']:
            for j in range(i-4, i+1):
                tags[j] = 'has_multiplayer=no'
        if tokens[i-5:i+1] == ['with', 'releases', 'for', 'linux', 'and', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'


        if tokens[i-9:i+1] == ['has', 'not', 'been', 'supported', 'for', 'release', 'on', 'linux', 'or', 'mac']:
            for j in range(i-9,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'


        if tokens[i-8:i+1] == ["n't", "available", 'on', 'steam', ',', 'linux', ',', 'or', 'mac']:        
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['as', 'well', 'as', 'on', 'steam']:
            for j in range(i-4, i+1):
                tags[j] = 'available_on_steam=yes'
        if tokens[i-5:i+1] == ['not', 'released', 'on', 'linux', 'or', 'mac']:
            for j in range(i-5, i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
        
        if tokens[i-6:i+1] == ['not', 'equip', 'it', 'with', 'a', 'multiplayer', 'mode']:
            for j in range(i-6,i+1):
                tags[j] = 'has_multiplayer=no'
        if tokens[i-4:i+1] == ['no', 'linux', 'release', 'or', 'multiplayer']:
            tags[i] = 'has_multiplayer=no'

        if tokens[i-2:i+1] == ['mac', 'and', 'pc']:
            tags[i-2] = 'has_mac_release=yes'
    
        if tokens[i-3:i+1] == ['not', 'even', 'feature', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no' 

        if tokens[i-5:i+1] == ['not', 'offer', 'a', 'release', 'for', 'linux']:
            for j in range(i-5,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-1:i+1] == ['without', 'multiplayer']:
            for j in range(i-1,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ["n't", 'have', 'any', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-5:i+1] == ['linux', 'and', 'mac', 'support', 'was', 'dropped']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'
            tags[i-5] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['can', 'download', 'the', 'game', 'from', 'steam']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=yes'
        
        if tokens[i-5:i+1] == ['not', 'out', 'on', 'mac', 'or', 'linux',]:        
            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-9:i+1] == ['not', 'available', 'on', 'steam', 'or', 'for', 'the', 'mac', 'and', 'linux',]:
            for j in range(i-9,i-5):
                tags[j] = 'available_on_steam=no'
            for j in range(i-4, i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-6:i+1] == ["n't", 'have', 'a', 'linux', 'or', 'mac', 'version',]:
            for j in range(i-6,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['not', 'become', 'available', 'on', 'steam',]:
            for j in range(i-4, i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-4:i+1] == ['not', 'on', 'linux', 'and', 'mac']:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
        if tokens[i-6:i+1] == ["n't", 'be', 'played', 'on', 'linux', 'or', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['not', 'out', 'for', 'linux', 'or', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['not', 'supported', 'on', 'linux']:
            for j in range(i-3, i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['pc', ',', 'including', 'mac']:
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'
        if tokens[i-4:i+1] == ['pc', ',', 'steam', 'and', 'mac']:
            tags[i] = 'has_mac_release=yes'
            tags[i-2] = 'available_on_steam=yes'

        if tokens[i-6:i+1] == ['not', 'available', 'on', 'the', 'steam', 'gaming', 'platform']:
            for j in range(i-6, i+1):
                tags[j] = 'available_on_steam=no'
       
        if tokens[i-4:i+1] == ['not', 'play', 'it', 'on', 'steam']: 
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-3:i+1] == ['not', 'out', 'on', 'steam']: 
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-3:i+1] == ['not', 'one', 'for', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['not', 'for', 'mac', 'users']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['pc', ',', 'including', 'linux', 'systems']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=yes'
        if tokens[i-4:i+1] == ['no', 'linux', 'or', 'mac', 'releases',]:
            tags[i-4] = 'has_linux_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'


        if tokens[i-10:i+1] == ['not', 'available', 'on', 'console', ',', 'linux', 'release', ',', 'or', 'mac', 'release']:
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i-4] = 'has_linux_release=no'
            tags[i-5] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['both', 'a', 'linux', 'and', 'mac', 'release']:
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'
            tags[i-5] = 'has_linux_release=yes'
            tags[i-4] = 'has_linux_release=yes'
            tags[i-3] = 'has_linux_release=yes'

        if tokens[i-8:i+1] == ['not', 'avialable', 'on', 'steam', ',', 'linux', ',', 'or', 'mac']:
            for j in range(i-8,i-4):
                tags[j] = 'available_on_steam=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
        if tokens[i-5:i+1] == ['never', 'released', 'for', 'linux', 'or', 'mac',]:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['can', 'run', 'on', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-3:i+1] == ['does', 'have', 'mac', 'support',]:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['not', 'be', 'downloaded', 'through', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=no'


        if tokens[i-5:i+1] == ['offers', 'support', 'for', 'mac', 'and', 'linux']:
            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'


        if tokens[i-2:i+1] == ['pc', 'on', 'linux']:
            for j in range(i-1,i+1):
                tags[j] = 'has_linux_release=yes'
        
        if tokens[i-2:i+1] == ['not', 'on', 'mac']:
            for j in range(i-2, i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['never', 'gotten', 'a', 'linux', 'version']:
            for j in range(i-4, i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-14:i+1] == ['if', 'you', 'are', 'looking', 'to', 'run', 'this', 'on', 'linux', ',', 'you', 'are', 'out', 'of', 'luck',]:
            for j in range(i-14,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['an', 'option', 'for', 'mac', 'users']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['not', 'cater', 'to', 'linux', 'users']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['get', 'it', 'for', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-3:i+1] == ['not', 'mac', 'or', 'linux']:
            tags[i-3] = 'has_mac_release=no'
            tags[i-2] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ['released', 'for', 'mac']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-7:i+1] == ['not', 'available', 'on', 'steam', ',', 'or', 'for', 'linux',]:
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-1:i+1] == ['not', 'steam']:
            tags[i] = 'available_on_steam=no'
            tags[i-1] = 'available_on_steam=no'
        if tokens[i-3:i+1] == ["'s", 'a', 'mac', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-1:i+1] == ['not', 'multiplayer']:
            tags[i] = 'has_multiplayer=no'
            tags[i-1] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ['can', 'get', 'on', 'steam']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-7:i+1] == ['steam', 'has', 'the', 'game', 'available', 'on', 'its', 'platform']:
            for j in range(i-7,i+1):
                tags[j] = 'available_on_steam=yes'
        if tokens[i-3:i+1] == ['never', 'released', 'for', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'
        if tokens[i-5:i+1] == ['never', 'released', 'for', 'mac', 'or', 'linux']:
            tags[i] = 'has_linux_release=no'

        if tokens[i-9:i+1] == ['out', 'on', 'pc', ',', 'linux', ',', 'mac', ',', 'and', 'steam']:
            tags[i] = 'available_on_steam=yes'
            tags[i-3] = 'has_mac_release=yes'
            tags[i-5] = 'has_linux_release=yes'
        if tokens[i-8:i+1] == ['on', 'steam', 'for', 'pc', ',', 'mac', ',', 'or', 'linux']:
            tags[i] = 'has_linux_release=yes'
            tags[i-3] = 'has_mac_release=yes'
            tags[i-8] = 'available_on_steam=yes'
            tags[i-7] = 'available_on_steam=yes'
        if tokens[i-6:i+1] == ['not', 'been', 'released', 'on', 'linux', 'or', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ["n't", 'been', 'supported', 'on', 'linux', 'systems']:
            for j in range(i-5,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['no', 'support', 'for', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ['not', 'play', 'multiplayer']:
            for j in range(i-2, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ['not', 'currently', 'on', 'steam']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-2:i+1] == ['no', 'steam', 'support']:
            for j in range(i-2, i+1):            
                tags[j] = 'available_on_steam=no'

        if tokens[i-5:i+1] == ["n't", 'available', 'on', 'steam', 'or', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ['not', 'offered', 'on', 'steam', 'or', 'for', 'mac']:
            for j in range(i-6,i-2):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['pc', ',', 'mac', 'and', 'steam']:
            tags[i] = 'available_on_steam=yes'
            tags[i-2] = 'has_mac_release=yes'

        
        if tokens[i-8:i+1] == ['not', 'available', 'for', 'steam', ',', 'linux', ',', 'or', 'mac']:
            for j in range(i-8,i-4):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'

        if tokens[i-8:i+1] == ["n't", 'excpect', 'it', 'to', 'work', 'on', 'linux', 'or', 'mac']:
            for j in range(i-8,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'


        if tokens[i-6:i+1] == ['nor', 'can', 'you', 'purchase', 'it', 'on', 'steam']:
            for j in range(i-6, i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-6:i+1] == ['not', 'available', 'on', 'either', 'mac', 'or', 'linux']:
            for j in range(i-6,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['can', 'be', 'played', 'from', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-7:i+1] == ['can', 'play', 'it', 'on', 'either', 'pc', 'or', 'mac']:
            tags[i] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['has', 'no', 'steam', 'or', 'linux', 'support']:
            for j in range(i-5,i-2):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-7:i+1] == ['not', 'have', 'a', 'release', 'for', 'linux', 'or', 'mac']:
            for j in range(i-7,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['without', 'mac', 'or', 'linux', 'support']:
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'
            tags[i-4] = 'has_mac_release=no'
            tags[i-3] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['steam', 'does', 'not', 'have', 'this', 'game']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-5:i+1] == ['also', 'available', 'for', 'linux', 'and', 'mac',]:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['with', 'both', 'linux', 'and', 'mac', 'support']:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ['xbox', ',', 'steam']:
            tags[i] = 'available_on_steam=yes'

        if tokens[i-6:i+1] == ['also', 'had', 'a', 'linux', 'and', 'mac', 'release']:
            for j in range(i-6, i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-6:i+1] == ['was', 'also', 'released', 'for', 'linux', 'and', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['out', 'for', 'mac', 'and', 'linux']:
            for j in range(i-4,i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'

        if tokens[i-6:i+1] == ["'s", 'even', 'available', 'on', 'mac', 'and', 'linux']:
            tags[i] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ['can', 'be', 'downloaded', 'from', 'steam']:
            for j in range(i-4, i+1):
                tags[j] = 'available_on_steam=yes'


        if tokens[i-4:i+1] == ['not', 'include', 'a', 'multiplayer', 'mode']:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer=no'


        if tokens[i-5:i+1] == ['not', 'be', 'played', 'with', 'other', 'players']:
            for j in range(i-5,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-4:i+1] == ['lacks', 'linux', 'or', 'mac', 'releases']:
            tags[i-4] = 'has_linux_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-7:i+1] == ['not', 'have', 'a', 'version', 'for', 'mac', 'or', 'linux']:
            for j in range(i-7,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'


        if tokens[i-6:i+1] == ['not', 'yet', 'available', 'on', 'linux', 'or', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-11:i+1] == ["'re", 'a', 'linux', 'or', 'mac', 'user', ',', 'you', "'re", 'out', 'of', 'luck',]:
            for j in range(i-11,i-8):
                tags[j] = 'has_linux_release=no'
            for j in range(i-7,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['pc', ',', 'steam', ',', 'and', 'mac']:
            tags[i] = 'has_mac_release=yes'
            tags[i-3] = 'available_on_steam=yes'


        if tokens[i-7:i+1] == ["n't", 'have', 'multiplayer', 'support', 'or', 'a', 'linux', 'release']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['can', 'be', 'played', 'on', 'mac']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=yes'


        if tokens[i-6:i+1] == ['not', 'currently', 'have', 'linux', 'or', 'mac', 'support']:
            for j in range(i-6,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ['linux', 'and', 'mac', 'do', 'not', 'support', 'it']:
            tags[i-6] = 'has_linux_release=no'
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=no'


        if tokens[i-4:i+1] == ['not', 'support', 'linux', 'and', 'mac',]:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'


        if tokens[i-5:i+1] == ['pc', ',', 'as', 'well', 'as', 'steam']:
            tags[i] = 'available_on_steam=yes'

        if tokens[i-5:i+1] == ['not', 'run', 'on', 'mac', 'or', 'linux']:
            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'


        if tokens[i-4:i+1] == ['not', 'for', 'mac', 'or', 'linux']:
            for j in range(i-4,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'
#

        if tokens[i-6:i+1] == ['does', 'not', 'feature', 'linux', 'or', 'mac', 'options']:
            for j in range(i-6, i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'


        if tokens[i-6:i+1] == ['with', 'no', 'release', 'on', 'mac', 'or', 'linux']:
            for j in range(i-6,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['lacks', 'a', 'multiplayer', 'mode']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'
                

        if tokens[i-5:i+1] == ['nor', 'on', 'mac', 'or', 'linux', 'systems']:
            for j in range(i-5,i-2):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'


        if tokens[i-4:i+1] == ['neither', 'find', 'it', 'on', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=no'


        if tokens[i-5:i+1] == ['game', 'to', 'play', 'with', 'your', 'friends']:
            for j in range(i-5,i+1):
                tags[j] = 'has_multiplayer=yes'


        if tokens[i-8:i+1] == ["'s", 'not', 'on', 'steam', ',', 'mac', ',', 'or', 'linux']:
            for j in range(i-8,i-4):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_linux_release=no'
            tags[i-3] = 'has_mac_release=no'

            
        if tokens[i-3:i+1] == ['through', 'the', 'steam', 'platform']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=yes'
        

        if tokens[i-5:i+1] == ["n't", 'available', 'on', 'linux', 'or', 'steam']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'available_on_steam=no'

        

        if tokens[i-5:i+1] == ['can', 'play', 'it', 'on', 'your', 'mac']:
            for j in range(i-5, i+1):
                tags[j] = 'has_mac_release=yes' 

        if tokens[i-4:i+1] == ['linux', ',', 'mac', 'and', 'pc',]: 
            tags[i-4] = 'has_linux_release=yes'
            tags[i-2] = 'has_mac_release=yes'


        if tokens[i-6:i+1] == ["n't", 'have', 'any', 'steam', 'or', 'linux', 'support']:
            for j in range(i-6, i-2):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-7:i+1] == ['nor', 'does', 'it', 'run', 'on', 'linux', 'or', 'mac']:
            for j in range(i-7,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ['not', 'have', 'releases', 'for', 'linux', 'or', 'mac']:
            for j in range(i-6, i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ["n't", 'have', 'online', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-6:i+1] == ['available', 'for', 'download', 'on', 'the', 'steam', 'platform']:
            for j in range(i-6,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-5:i+1] == ['linux', 'and', 'mac', 'are', 'not', 'supported']:
            tags[i-5] = 'has_linux_release=no'
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-7:i+1] == ['yet', 'to', 'see', 'any', 'linux', 'or', 'mac', 'release']:
            for j in range(i-7,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'


        if tokens[i-7:i+1] == ['including', 'the', 'linux', 'processor', 'but', 'not', 'the', 'mac']:
            for j in range(i-7,i-3):
                tags[j] = 'has_linux_release=yes'
            for  j in range(i-2, i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-2:i+1] == ['with', 'linux', 'support']:
            for j in range(i-2, i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ['not', 'have', 'any', 'multiplayer', 'modes']:
            for j in range(i-4, i+1):
                tags[j] = 'has_multiplayer=no'


        if tokens[i-4:i+1] == ['pc', 'as', 'well', 'as', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=yes'


        if tokens[i-4:i+1] == ['can', 'be', 'played', 'on', 'linux',]:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-5:i+1] == ["n't", 'play', 'this', 'game', 'on', 'linux']:
            for j in range(i-5, i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-7:i+1] == ["n't", 'play', 'this', 'game', 'on', 'linux', 'or', 'mac']:
            tags[i] = 'has_mac_release=no'


        if tokens[i-5:i+1] == ['not', 'out', 'on', 'linux', 'or', 'mac']:
            tags[i] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['has', 'a', 'mac', 'support']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['can', 'not', 'be', 'played', 'on', 'linux']:
            for j in range(i-5,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ["n't", 'on', 'steam']:
            for j in range(i-2,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-6:i+1] == ['not', 'expect', 'to', 'find', 'it', 'on', 'steam']:
            for j in range(i-6,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-4:i+1] == ['not', 'offer', 'it', 'on', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-8:i+1] == ['not', 'released', 'for', 'steam', ',', 'linux', ',', 'or', 'mac']:
            for j in range(i-8,i-4):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['not', 'have', 'the', 'capabilities', 'of', 'multiplayer']:
            for j in range(i-5,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ['not', 'play', 'it', 'multiplayer']:
            for j in range(i-3, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-4:i+1] == ['also', 'on', 'linux', 'and', 'mac']:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-10:i+1] == ['can', 'not', 'play', 'this', 'on', 'steam', ',', 'linux', ',', 'or', 'mac']:
            for j in range(i-10, i-4):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'

        if tokens[i-10:i+1] == ['mac', ',', 'linux', ',', 'and', 'steam', 'do', 'not', 'have', 'the', 'game']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=no'
            tags[i-10] = 'has_mac_release=no'
            tags[i-8] = 'has_linux_release=no'


        if tokens[i-5:i+1] == ["n't", 'run', 'on', 'linux', 'or', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-2:i+1] == ['with', 'steam', 'availability']:
            for j in range(i-2,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-9:i+1] == ["n't", 'expect', 'it', 'to', 'run', 'on', 'either', 'linux', 'or', 'mac']:
            for j in range(i-9,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['on', 'both', 'mac', 'and', 'linux', 'platforms']:
            for j in range(i-5,i-2):
                tags[j] = 'has_mac_release=yes'

            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'


        if tokens[i-4:i+1] == ['available', 'on', 'linux', 'and', 'mac']:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ["n't", 'any', 'multiplayer']:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=no'


           

        if tokens[i-6:i+1] == ['linux', 'and', 'mac', 'systems', 'are', 'not', 'supported']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=no'
            tags[i-6] = 'has_linux_release=no'



        if tokens[i-6:i+1] == ['pc', 'with', 'a', 'linux', 'and', 'mac', 'release']:
            tags[i-5] = 'has_linux_release=yes'
            tags[i-4] = 'has_linux_release=yes'
            tags[i-3] = 'has_linux_release=yes'
            tags[i-1] = 'has_mac_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['no', 'support', 'for', 'linux', 'or', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['lack', 'of', 'a', 'mac', 'release']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ["n't", 'run', 'on', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ['if', 'only', 'it', 'had', 'a', 'mac', 'release']:
            for j in range(i-6,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-9:i+1] == ['i', 'know', 'you', 'got', 'some', 'steam', 'credits', 'for', 'your', 'birthday']:
            for j in range(i-9,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-4:i+1] == ["n't", 'try', 'to', 'include', 'multiplayer']:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer=no'
    


        if tokens[i-8:i+1] == ['do', 'you', 'play', 'video', 'games', 'on', 'the', 'mac', 'os']:
            for j in range(i-8,i+1):
                tags[j] = 'has_mac_release='

        if tokens[i-4:i+1] == ['is', 'mac', 'your', 'favorite', 'platform']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release='
            
        if tokens[i-6:i+1] == ['do', 'you', 'play', 'your', 'games', 'on', 'mac',]:
            for j in range(i-6,i+1):
                tags[j] = 'has_mac_release='

        if tokens[i-3:i+1] == ['do', 'you', 'use', 'mac',]:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release='

    
        if tokens[i-5:i+1] == ['do', 'you', 'play', 'games', 'on', 'mac']:
            for j in range(i-5,i+1):
                tags[j] = 'has_mac_release='

        if tokens[i-8:i+1] == ['do', 'you', 'generally', 'play', 'games', 'on', 'the', 'mac', 'os']:
            for j in range(i-8,i+1):
                tags[j] = 'has_mac_release='

        if tokens[i-6:i+1] == ['does', 'a', 'game', 'need', 'a', 'mac', 'release']:
            for j in range(i-6,i+1):
                tags[j] = 'has_mac_release='

        if tokens[i-3:i+1] == ['do', 'you', 'think', 'mac',]:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release='

        if tokens[i-3:i+1] == ["n't", 'on', 'the', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ["n't", 'have', 'a', 'mac', 'release']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['without', 'a', 'mac', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ["n't", 'have', 'a', 'version', 'for', 'mac']:
            for j in range(i-5,i+1):
                tags[j] = 'has_mac_release=no'


        if tokens[i-3:i+1] == ["n't", 'come', 'to', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['with', 'a', 'mac', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'


        if tokens[i-3:i+1] == ['with', 'other', 'mac', 'games']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'


        if tokens[i-2:i+1] == ['available', 'on', 'mac']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-1:i+1] == ['which', 'platform']:
            for j in range(i-1,i+1):
                tags[j] = 'platforms='
        if tokens[i-2:i+1] == ['what', 'gaming', 'platform']:
            for j in range(i-2,i+1):
                tags[j] = 'platforms='

        if tokens[i-4:i+1] == ['what', "'s", 'your', 'favorite', 'platform']:
            for j in range(i-4,i+1):
                tags[j] = 'platforms='

    
        if tokens[i-7:i+1] == ['do', 'you', 'mostly', 'game', 'on', 'a', 'single', 'platform']:
            for j in range(i-7,i+1):
                tags[j] = 'platforms='
        if tokens[i-3:i+1] == ['your', 'preferred', 'gaming', 'platform']:
            for j in range(i-3,i+1):
                tags[j] = 'platforms='

        if tokens[i-9:i+1] == ["n't", 'have', 'either', 'a', 'mac', 'release', 'or', 'a', 'linux', 'release']:
            for j in range(i-9, i-3):
                tags[j] = 'has_mac_release=no'
            for j in range(i-2, i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ['neither', 'a', 'mac']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-6:i+1] == ['just', 'wish', 'it', 'were', 'available', 'on', 'steam']:
            for j in range(i-6,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-6:i+1] == ['just', 'wish', 'it', 'was', 'available', 'on', 'steam']:
            for j in range(i-6,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-4:i+1] == ['your', 'favorite', 'esrb', 'content', 'rating']:
            for j in range(i-4,i+1):
                tags[j] = 'esrb='

        if tokens[i-4:i+1] == ['a', 'particular', 'esrb', 'content', 'rating']:
            for j in range(i-4,i+1):
                tags[j] = 'esrb='

        if tokens[i-3:i+1] == ['what', 'esrb', 'content', 'rating']:
            for j in range(i-3,i+1):
                tags[j] = 'esrb='

        if tokens[i-4:i+1] == ['is', 'there', 'an', 'esrb', 'rating']:
            for j in range(i-4,i+1):
                tags[j] = 'esrb='

        if tokens[i-3:i+1] == ['a', 'specific', 'esrb', 'rating']:
            for j in range(i-3,i+1):
                tags[j] = 'esrb='

        if tokens[i-11:i+1] == ['if', 'the', 'content', 'rating', 'is', 'important', 'to', 'you', ',', 'which', 'esrb', 'label']:
            for j in range(i-11,i+1):
                tags[j] = 'esrb='

        if tokens[i-4:i+1] == ['with', 'a', 'particular', 'esrb', 'rating']:
            for j in range(i-4,i+1):
                tags[j] = 'esrb='

        if tokens[i-9:i+1] == ['if', 'the', 'esrb', 'rating', 'of', 'a', 'game', 'matters', 'to', 'you']:
            for j in range(i-9,i+1):
                tags[j] = 'esrb='

        if tokens[i-8:i+1] == ['do', 'you', 'generally', 'look', 'at', 'the', 'esrb', 'content', 'rating']:
            for j in range(i-8,i+1):
                tags[j] = 'esrb='

        if tokens[i-5:i+1] == ['which', 'is', 'your', 'preferred', 'esrb', 'rating']:
            for j in range(i-5,i+1):
                tags[j] = 'esrb='

        if tokens[i-2:i+1] == ['which', 'esrb', 'rating']:
            for j in range(i-2,i+1):
                tags[j] = 'esrb='

        if tokens[i-3:i+1] == ['which', 'esrb', 'content', 'label']:
            for j in range(i-3,i+1):
                tags[j] = 'esrb='
        if tokens[i-3:i+1] == ["n't", 'get', 'on', 'steam']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-8:i+1] == ['is', 'there', 'something', 'about', 'multiplayer', 'that', 'puts', 'you', 'off']:
            for j in range(i-8,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-19:i+1] == ['the', 'omission', 'of', 'multiplayer', 'means', 'they', 'were', 'able', 'to', 'really', 'focus', 'on', 'making', 'the', 'best', 'possible', 'single', '-', 'player', 'experience']:
            for j in range(i-19,i+1):
                tags[j] = 'has_multiplayer=no'


        if tokens[i-9:i+1] == ['do', 'you', 'prefer', 'that', 'a', 'game', 'be', 'available', 'on', 'steam']:
            for j in range(i-9,i+1):
                tags[j] = 'available_on_steam='

        if tokens[i-6:i+1] == ['do', 'you', 'mostly', 'play', 'games', 'on', 'steam']:
            for j in range(i-6,i+1):
                tags[j] = 'available_on_steam='

        if tokens[i-14:i+1] == ['would', 'you', 'say', 'it', "'s", 'important', 'to', 'you', 'that', 'a', 'game', 'is', 'available', 'on', 'steam']:
            for j in range(i-14,i+1):
                tags[j] = 'available_on_steam='

        if tokens[i-11:i+1] == ['is', 'a', 'game', 'being', 'on', 'steam', 'or', 'not', 'a', 'dealbreaker', 'to', 'you']:
            for j in range(i-11,i+1):
                tags[j] = 'available_on_steam='
        if tokens[i-15:i+1] == ['would', 'you', 'say', 'steam', 'makes', 'it', 'more', 'convenient', 'for', 'you', 'to', 'get', 'new', 'games', 'to', 'play']:
            for j in range(i-15,i+1):
                tags[j] = 'available_on_steam='
            
        if tokens[i-9:i+1] == ['has', 'steam', 'been', 'the', 'major', 'source', 'of', 'your', 'video', 'games',]:
            for j in range(i-9,i+1):
                tags[j] = 'available_on_steam='

        if tokens[i-10:i+1] == ['does', 'it', 'matter', 'to', 'you', 'if', 'a', 'game', 'is', 'on', 'steam']:
            for j in range(i-10,i+1):
                tags[j] = 'available_on_steam='


        if tokens[i-10:i+1] == ['is', 'it', 'more', 'convenient', 'for', 'you', 'to', 'play', 'games', 'on', 'steam']:
            for j in range(i-10,i+1):
                tags[j] = 'available_on_steam='

        if tokens[i-15:i+1] == ['are', 'games', 'that', 'are', 'available', 'on', 'steam', 'more', 'likely', 'to', 'make', 'it', 'into', 'your', 'game', 'library']:
            for j in range(i-15,i+1):
                tags[j] = 'available_on_steam='

        if tokens[i-3:i+1] == ['with', 'a', 'linux', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-7:i+1] == ["n't", 'available', 'on', 'either', 'the', 'mac', 'or', 'linux']:
            for j in range(i-7,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-6:i+1] == ["n't", 'released', 'for', 'the', 'mac', 'and', 'linux']:
            for j in range(i-6,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['without', 'a', 'mac', 'or', 'linux', 'release']:
            for j in range(i-5,i-2):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'
        if tokens[i-3:i+1] == ['having', 'a', 'mac', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-8:i+1] == ['who', 'are', 'some', 'of', 'your', 'favorite', 'video', 'game', 'developers',]:
            for j in range(i-8,i+1):
                tags[j] = 'developer='

        if tokens[i-3:i+1] == ['from', 'a', 'specific', 'developer']:
            for j in range(i-3,i+1):
                tags[j] = 'developer='

        if tokens[i-3:i+1] == ['which', 'video', 'game', 'developer']:
            for j in range(i-3,i+1):
                tags[j] = 'developer='

        if tokens[i-6:i+1] == ['who', 'are', 'your', 'favorite', 'video', 'game', 'developers']:
            for j in range(i-6,i+1):
                tags[j] = 'developer='

        if tokens[i-5:i+1] == ['who', 'is', 'your', 'favorite', 'game', 'developer',]:
            for j in range(i-5,i+1):
                tags[j] = 'developer='

        if tokens[i-4:i+1] == ['are', 'there', 'any', 'game', 'developers']:
            for j in range(i-4,i+1):
                tags[j] = 'developer='


        if tokens[i-4:i+1] == ['a', 'specific', 'video', 'game', 'developer']:
            for j in range(i-4,i+1):
                tags[j] = 'developer='


        if tokens[i-3:i+1] == ['for', 'certain', 'game', 'developers']:
            for j in range(i-3,i+1):
                tags[j] = 'developer='

        if tokens[i-4:i+1] == ['your', 'favorite', 'video', 'game', 'developer']:
            for j in range(i-4,i+1):
                tags[j] = 'developer='

        if tokens[i-3:i+1] == ['with', 'a', 'steam', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-2:i+1] == ['with', 'mac', 'games']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-8:i+1] == ['do', 'you', 'play', 'games', 'on', 'mac', ',', 'like', 'NAME']:
            for j in range(i-8,i-2):
                tags[j] = 'has_mac_release=yes'
        if tokens[i-3:i+1] == ['play', 'the', 'mac', 'version']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-3:i+1] == ['got', 'a', 'mac', 'release']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-10:i+1] == ['i', 'disdain', 'steam', 'and', 'do', "n't", 'want', 'to', 'play', 'games', 'there']:
            for j in range(i-10, i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-3:i+1] == ['without', 'even', 'a', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-5:i+1] == ['released', 'on', 'both', 'linux', 'and', 'mac']:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['both', 'mac', 'and', 'linux', 'releases']:
            for j in range(i-4,i-2):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'

        if tokens[i-6:i+1] == ['the', 'mac', 'and', 'linux', 'game', ',', 'NAME',]:
            tags[i-6] = 'has_mac_release=yes'
            tags[i-5] = 'has_mac_release=yes'
            tags[i-3] = 'has_linux_release=yes'
            tags[i-2] = 'has_linux_release=yes'

        if tokens[i-10:i+1] == ['do', 'you', 'have', 'any', 'experience', 'with', 'gaming', 'on', 'a', 'linux', 'system']:
            for j in range(i-10,i+1):
                tags[j] = 'has_linux_release='
    
        if tokens[i-7:i+1] == ['do', 'you', 'play', 'games', 'on', 'linux', 'at', 'all',]:
            for j in range(i-7,i+1):
                tags[j] = 'has_linux_release='

        if tokens[i-6:i+1] == ['do', 'you', 'like', 'to', 'game', 'on', 'linux']:
            for j in range(i-6,i+1):
                tags[j] = 'has_linux_release='

        if tokens[i-3:i+1] == ['would', 'you', 'recommend', 'linux',]:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release='

        if tokens[i-6:i+1] == ['is', 'linux', 'your', 'gaming', 'os', 'of', 'choice',]:
            for j in range(i-6,i+1):
                tags[j] = 'has_linux_release='

        if tokens[i-8:i+1] == ['do', 'you', 'ever', 'play', 'games', 'on', 'a', 'linux', 'system']:
            for j in range(i-8,i+1):
                tags[j] = 'has_linux_release='

        if tokens[i-7:i+1] == ['have', 'you', 'ever', 'played', 'a', 'game', 'on', 'linux']:
            for j in range(i-7,i+1):
                tags[j] = 'has_linux_release='

        if tokens[i-5:i+1] == ['is', 'linux', 'your', 'os', 'for', 'gaming']:
            for j in range(i-5,i+1):
                tags[j] = 'has_linux_release='


        if tokens[i-4:i+1] == ['do', 'you', 'like', 'linux', 'games']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release='

        if tokens[i-5:i+1] == ['do', 'you', 'game', 'often', 'on', 'linux']:
            for j in range(i-5,i+1):
                tags[j] = 'has_linux_release='


        if tokens[i-4:i+1] == ['are', 'you', 'a', 'linux', 'gamer']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release='

        if tokens[i-14:i+1] == ['does', 'it', 'matter', 'to', 'you', 'if', 'you', 'can', 'play', 'a', 'game', 'on', 'a', 'linux', 'os',]:
            for j in range(i-14,i+1):
                tags[j] = 'has_linux_release='


        if tokens[i-4:i+1] == ['love', 'the', 'convenience', 'of', 'steam',]:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-5:i+1] == ['was', 'ported', 'to', 'mac', 'and', 'linux']:
            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ['both', 'mac', 'and', 'linux', 'versions',]:
            for j in range(i-4,i-2):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'
            tags[i-1] = 'has_linux_release=yes'
        if tokens[i-4:i+1] == ['for', 'porting', 'it', 'to', 'linux']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-3:i+1] == ['having', 'a', 'linux', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-10:i+1] == ['would', 'you', 'say', 'you', 'prefer', 'playing', 'games', 'with', 'a', 'multiplayer', 'mode']:
            for j in range(i-10,i+1):
                tags[j] = 'has_multiplayer='

        if tokens[i-7:i+1] == ['would', 'you', 'say', 'multiplayer', 'is', 'an', 'important', 'feature']:
            for j in range(i-7,i+1):
                tags[j] = 'has_multiplayer='

        if tokens[i-7:i+1] == ['would', 'you', 'tend', 'to', 'enjoy', 'the', 'multiplayer', 'experience']:
            for j in range(i-7,i+1):
                tags[j] = 'has_multiplayer='

        if tokens[i-11:i+1] == ['do', 'you', 'prefer', 'to', 'game', 'with', 'others', ',', 'i', 'mean', ',', 'multiplayer']:
            for j in range(i-11,i+1):
                tags[j] = 'has_multiplayer='
        if tokens[i-4:i+1] == ['do', 'you', 'like', 'multiplayer', 'gaming',]:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer='

        if tokens[i-6:i+1] == ['do', 'you', 'enjoy', 'playing', 'games', 'in', 'multiplayer',]:
            for j in range(i-6,i+1):
                tags[j] = 'has_multiplayer='

        if tokens[i-2:i+1] == ['i', 'use', 'linux']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-6:i+1] == ['pc', 'and', 'a', 'mac', 'on', 'my', 'laptop']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-6:i+1] == ['non', '-', 'availability', 'on', 'linux', 'and', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-7:i+1] == ['without', 'either', 'a', 'mac', 'or', 'a', 'linux', 'release']:
            for j in range(i-7,i-3):
                tags[j] = 'has_mac_release=no'
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-6:i+1] == ['neither', 'a', 'linux', 'nor', 'a', 'mac', 'release']:
            for j in range(i-6,i-3):
                tags[j] = 'has_linux_release=no'
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['speaking', 'of', 'steam', 'games']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-5:i+1] == ['that', 'you', 'can', 'get', 'for', 'steam']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=yes'
        if tokens[i-5:i+1] == ['since', 'you', "'ve", 'got', 'a', 'mac']:
            for j in range(i-5,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['if', 'you', 'like', 'mac', 'games',]:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-1:i+1] == ['which', 'year']:
            for j in range(i-1,i+1):
                tags[j] = 'release_year='

        if tokens[i-6:i+1] == ['do', 'you', 'have', 'a', 'favorite', 'release', 'year']:
            for j in range(i-6,i+1):
                tags[j] = 'release_year='

        if tokens[i-4:i+1] == ['do', 'you', 'remember', 'a', 'year']:
            for j in range(i-4,i+1):
                tags[j] = 'release_year='

        if tokens[i-4:i+1] == ['what', 'was', 'the', 'best', 'year']:
            for j in range(i-4,i+1):
                tags[j] = 'release_year='

        if tokens[i-7:i+1] == ['what', 'do', 'you', 'think', 'was', 'the', 'best', 'year']:
            for j in range(i-7,i+1):
                tags[j] = 'release_year='

        if tokens[i-8:i+1] == ['what', 'would', 'you', 'say', 'was', 'the', 'best', 'release', 'year']:
            for j in range(i-8,i+1):
                tags[j] = 'release_year='

        if tokens[i-3:i+1] == ['what', 'are', 'the', 'genres']:
            for j in range(i-3,i+1):
                tags[j] = 'genres='

        if tokens[i-1:i+1] == ['what', 'genre',]:
            for j in range(i-1,i+1):
                tags[j] = 'genres='

        if tokens[i-3:i+1] == ['what', 'video', 'game', 'genre']:
            for j in range(i-3,i+1):
                tags[j] = 'genres='

        if tokens[i-1:i+1] == ['which', 'genre']:
            for j in range(i-1,i+1):
                tags[j] = 'genres='

        if tokens[i-3:i+1] == ['what', 'kind', 'of', 'genres']:
            for j in range(i-3,i+1):
                tags[j] = 'genres='

        if tokens[i-6:i+1] == ['wish', 'they', 'had', 'released', 'a', 'linux', 'version']:
            for j in range(i-6,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['lacks', 'a', 'linux', 'release',]:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ["n't", 'released', 'for', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-11:i+1] == ['the', 'only', 'thing', 'better', 'than', 'a', 'nintendo', 'game', 'is', 'a', 'nintendo', 'game']:
            for j in range(i-11,i+1):
                tags[j] = 'platforms=Nintendo'
        if tokens[i-4:i+1] == ['i', 'can', 'play', 'with', 'others']:
            for j in range(i-4,i+1):         
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-3:i+1] == ['lack', 'a', 'mac', 'release',]:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-2:i+1] == ['it', 'hit', 'steam']:
            for j in range(i-2,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-2:i+1] == ['rated', 'mac', 'game']:
            for j in range(i-1,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ['RELEASE_YEAR', 'mac', 'release']:
            for j in range(i-1,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['not', 'having', 'a', 'mac', 'release']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=no'


        if tokens[i-11:i+1] == ['not', 'many', 'mac', 'games', 'out', 'there', ',', 'but', 'a', 'solid', 'one', 'is']:
            for j in range(i-11,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['a', 'bunch', 'of', 'steam', 'games']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-3:i+1] == ['knowing', 'you', 'have', 'steam',]:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-2:i+1] == ['the', 'steam', 'game']:
            for j in range(i-2,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-3:i+1] == ["n't", 'have', 'multiplayer', 'modes']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ['it', "'s", 'mac', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ['with', 'friends', 'online']:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-15:i+1] == ['i', 'know', 'you', 'use', 'steam', 'a', 'lot', ',', 'so', 'i', 'wonder', 'if', 'you', "'ve", 'tried', 'NAME']:
            for j in range(i-15,i):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-3:i+1] == ['DEVELOPER', "'s", 'steam', 'games']:
            tags[i-1] = 'available_on_steam=yes'

        if tokens[i-3:i+1] == ['play', 'with', 'my', 'friends']:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=yes'
        if tokens[i-4:i+1] == ['released', 'for', 'the', 'linux', 'os']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-16:i+1] == ['just', 'cool', 'enough', 'to', 'not', 'be', 'for', 'kids', 'and', 'just', 'mediocre', 'enough', 'to', 'not', 'be', 'for', 'adults',]:
            for j in range(i-16,i+1):
                tags[j] = 'esrb=T_(for_Teen)'

        if tokens[i-4:i+1] == ['without', 'the', 'availability', 'of', 'multiplayer']:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-12:i+1] == ['a', 'nice', 'balance', 'between', 'being', 'family', '-', 'friendly', 'and', 'dealing', 'with', 'mature', 'themes']:
            for j in range(i-12,i+1):
                tags[j] = 'esrb=T_(for_Teen)'

        if tokens[i-15:i+1] == ['means', 'it', "'s", 'a', 'nice', 'balance', 'between', 'being', 'family', '-', 'friendly', 'and', 'dealing', 'with', 'mature', 'themes']:
            for j in range(i-15,i+1):
                tags[j] = 'esrb=T_(for_Teen)'


        if tokens[i-2:i+1] == ['games', 'from', 'steam']:
            for j in range(i-1,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-4:i+1] == ['thanks', 'to', 'its', 'mac', 'port']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-3:i+1] == ['NAME', 'for', 'the', 'mac']:
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ["'s", 'mac', 'games']:
            for j in range(i-1,i+1):
                tags[j] = 'has_mac_release=yes'


        if tokens[i-2:i+1] == ["n't", 'have', 'multiplayer']:
            for j in range(i-2, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ['not', 'available', 'on', 'mac']:
            for j in range(i-3, i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-8:i+1] == ["n't", 'need', 'multiplayer', 'because', 'of', 'it', "'s", 'engaging', 'story',]:
            for j in range(i-8,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-4:i+1] == ['for', 'both', 'mac', 'and', 'linux',]:
            for j in range(i-4,i-1):
                tags[j] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ["'s", 'on', 'linux', 'and', 'mac']:
            tags[i] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['have', 'gotten', 'a', 'linux', 'release']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-5:i+1] == ['the', 'lack', 'of', 'a', 'linux', 'release']:
            for j in range(i-5,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-9:i+1] == [ 'do', 'you', 'typically', 'miss', 'some', 'kind', 'of', 'a', 'multiplayer', 'mode', ]:
            for j in range(i-9,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-2:i+1] == ['steam', 'text', 'adventure']:
            tags[i-2] = 'available_on_steam=yes'

        if tokens[i-3:i+1] == ['both', 'steam', 'and', 'linux']:
            tags[i-3] = 'available_on_steam=yes'
            tags[i-2] = 'available_on_steam=yes'
            tags[i] = 'has_linux_release=yes'
    
        if tokens[i-6:i+1] == ['both', 'a', 'mac', 'and', 'a', 'linux', 'release']:
            for j in range(i-6,i-3):
                tags[j] = 'has_mac_release=yes'
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-4:i+1] == ['it', 'not', 'coming', 'to', 'mac']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release=no'


        if tokens[i-3:i+1] == ['not', 'a', 'linux', 'release']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=no'


        if tokens[i-7:i+1] == ['not', 'available', 'on', 'steam', 'or', 'playable', 'on', 'mac',]:
            for j in range(i-7,i-3):
                tags[j] = 'available_on_steam=no'
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-2:i+1] == ['unavailable', 'on', 'steam']:
            for j in range(i-2,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-6:i+1] == ['not', 'currently', 'available', 'on', 'steam', 'or', 'linux']:
            for j in range(i-6, i-1):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['appropriate', 'for', 'all', 'ages']:
            for j in range(i-3,i+1):
                tags[j] = 'esrb=E_(for_Everyone)'


        if tokens[i-3:i+1] == ["n't", 'interested', 'in', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-6:i+1] == ['is', 'mac', 'the', 'platform', 'of', 'your', 'choice']:
            for j in range(i-6,i+1):
                tags[j] = 'has_mac_release='

        if tokens[i-6:i+1] == ['i', 'also', 'think', 'that', 'steam', 'is', 'obnoxious',]:
            for j in range(i-6, i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-2:i+1] == ['for', 'single', 'players']:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-4:i+1] == ['do', 'you', 'play', 'multiplayer', 'games']:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer='

        if tokens[i-4:i+1] == ['no', 'linux', 'or', 'mac', 'compatibility']:
            tags[i-4] = 'has_linux_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['not', 'on', 'either', 'linux', 'or', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'


        if tokens[i-6:i+1] == ['no', 'planned', 'release', 'for', 'linux', 'or', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'


        if tokens[i-4:i+1] == ['lack', 'multiplayer', 'and', 'linux', 'support']:
            for j in range(i-4,i-2):
                tags[j] = 'has_multiplayer=no'
            tags[i-1] = 'has_linux_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ["n't", 'even', 'offer', 'a', 'multiplayer', 'mode']:
            for j in range(i-5,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ["n't", 'expect', 'any', 'multiplayer']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-3:i+1] == ['a', 'top', 'down', 'view']:
            for j in range(i-3,i+1):
                tags[j] = 'player_perspective=bird_view'

        if tokens[i-7:i+1] == ["n't", 'release', 'these', 'm', 'rated', 'games', 'for', 'linux']:
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ["n't", 'released', 'for', 'linux', 'or', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-1:i+1] == ['third', 'player']:
            tags[i] = 'player_perspective=third_person'
            tags[i-1] = 'player_perspective=third_person'

        if tokens[i-4:i+1] == ['action', 'game', 'filled', 'with', 'adventure',]:
            for j in range(i-4,i+1):
                tags[j] = 'genres=action-adventure'

        if tokens[i-6:i+1] == ['the', 'first', 'or', 'the', 'third', 'person', 'perspective']:
            tags[i-6] = 'player_perspective=first_person'
            tags[i-5] = 'player_perspective=first_person'

        if tokens[i-2:i+1] == ['in', 'what', 'year']:
            for j in range(i-2,i+1):
                tags[j] = 'release_year='

        if tokens[i-4:i+1] == ['what', 'is', 'your', 'preferred', 'platform']:
            for j in range(i-4,i+1):
                tags[j] = 'platforms='

        if tokens[i-9:i+1] == ['i', 'wish', 'there', 'was', 'multiplayer', ',', 'but', 'there', 'is', "n't"]:
            for j in range(i-9,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-5:i+1] == ["n't", 'released', 'for', 'linux', 'and', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'


        if tokens[i-3:i+1] == ['adventure', '-', 'filled', 'action']:
            for j in range(i-3,i+1):
                tags[j] = 'genres=action-adventure'

        if tokens[i-7:i+1] == ['not', 'have', 'a', 'linux', 'or', 'a', 'mac', 'release']:
            for j in range(i-7,i-3):
                tags[j] = 'has_linux_release=no'
            for j in range(i-2,i+1):
                tags[j] = 'has_mac_release=no'
            

        if tokens[i-6:i+1] == ["n't", 'been', 'released', 'for', 'linux', 'or', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'


        if tokens[i-17:i+1] == ['do', 'you', 'find', 'availability', 'on', 'steam', 'to', 'be', 'important', 'to', 'you', 'when', 'deciding', 'about', 'getting', 'a', 'new', 'game']:
            for j in range(i-17,i+1):
                tags[j] = 'available_on_steam='

        if tokens[i-8:i+1] == ['what', 'is', 'the', 'game', 'genre', 'you', 'like', 'the', 'best',]:
            for j in range(i-8,i+1):
                tags[j] = 'genres='

        if tokens[i-4:i+1] == ['neither', 'on', 'steam', 'nor', 'linux']:
            for j in range(i-4,i-1):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ["n't", 'available', 'for', 'mac', 'or', 'linux',]:
            for j in range(i-5,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ['ideal', 'for', 'teens']:
            for j in range(i-2,i+1):
                tags[j] = 'esrb=T_(for_Teen)'


        if tokens[i-4:i+1] == ["n't", 'miss', 'any', 'multiplayer', 'options']:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-1:i+1] == ['which', 'developer',]:
            for j in range(i-1,i+1):
                tags[j] = 'developer='

        if tokens[i-4:i+1] == ['never', 'brought', 'it', 'to', 'linux']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['no', 'linux', 'or', 'mac', 'versions']:
            tags[i-4] = 'has_linux_release=no'
            tags[i-3] = 'has_linux_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-10:i+1] == ['no', 'version', 'of', 'the', 'game', 'was', 'released', 'for', 'linux', 'or', 'mac']:                
            for j in range(i-10, i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-8:i+1] == ['not', 'available', 'for', 'steam', ',', 'mac', ',', 'or', 'linux']:
            for j in range(i-8,i-4):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_linux_release=no'
            tags[i-3] = 'has_mac_release=no'


        if tokens[i-8:i+1] == ['not', 'supported', 'by', 'steam', ',', 'linux', ',', 'or', 'mac']:
            for j in range(i-8,i-4):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'

        if tokens[i-9:i+1] == ['not', 'play', 'it', 'with', 'your', 'friends', 'in', 'a', 'multiplayer', 'mode']:
            for j in range(i-9, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-6:i+1] == ["n't", 'been', 'released', 'on', 'linux', 'or', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-8:i+1] == ['on', 'steam', 'for', 'windows', ',', 'mac', ',', 'and', 'linux']:
            tags[i] = 'has_linux_release=yes'
            tags[i-3] = 'has_mac_release=yes'


        if tokens[i-3:i+1] == ['not', 'available', 'for', 'steam']:
            for j in range(i-3, i+1):
                tags[j] = 'available_on_steam=no'


        if tokens[i-6:i+1] == ['pc', ',', 'as', 'well', 'as', 'for', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-3:i+1] == ['not', 'appear', 'on', 'steam']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-3:i+1] == ['not', 'released', 'for', 'mac']:
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ["n't", 'even', 'have', 'a', 'steam', 'release']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-5:i+1] == ['not', 'run', 'on', 'linux', 'or', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-11:i+1] == [ 'a', 'good', 'single-player', 'game', 'for', 'all', 'ages', ',', 'but', 'it', 'lacks', 'multiplayer',]:
            for j in range(i-11,i+1):
                tags[j] = 'has_multiplayer=no'
        if tokens[i-5:i+1] == ['are', 'there', 'any', 'esrb', 'content', 'ratings']:
            for j in range(i-5, i+1):
                tags[j] = 'esrb='

        if tokens[i-2:i+1] == ['top', '-', 'down']:
            for j in range(i-2,i+1):
                tags[i] = 'player_perspective=bird_view'

        if tokens[i-3:i+1] == ['from', 'the', 'steam', 'store']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-4:i+1] == ["n't", 'play', 'it', 'on', 'linux']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=no'
    
        if tokens[i-4:i+1] == ['not', 'get', 'it', 'on', 'steam', ]:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-2:i+1] == ['not', 'via', 'steam']:
            for j in range(i-2,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-5:i+1] == ['not', 'via', 'steam', 'or', 'mac', 'platforms']:
            for j in range(i-5,i-2):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['not', 'run', 'on', 'mac']: 
            for j in range(i-3,i+1):
                tags[j] = 'has_mac_release=no'
    

        if tokens[i-5:i+1] == ['pc', ',', 'as', 'well', 'as', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=yes'


        if tokens[i-3:i+1] == ['that', 'have', 'linux', 'releases']:
            for j in range(i-3, i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-2:i+1] == ['turn', 'based', 'strategy']:
            for j in range(i-2,i+1):
                tags[j] = 'genres=turn-based_strategy'

        if tokens[i-3:i+1] == ['on', 'multiplayer', 'steam', 'games']:
            tags[i-1] = 'available_on_steam=yes'
        if tokens[i-5:i+1] == ['can', 'you', 'think', 'of', 'a', 'year']:
            for j in range(i-5,i+1):
                tags[j] = 'release_year='

        if tokens[i-12:i+1] == ['is', 'it', 'a', 'dealbreaker', 'for', 'you', 'if', 'a', 'game', 'does', 'not', 'support', 'linux']:
            for j in range(i-12,i+1):
                tags[j] = 'has_linux_release='

        if tokens[i-4:i+1] == ['unavailable', 'on', 'mac', 'and', 'linux']:
            for j in range(i-4,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['first', 'and', 'third', '-', 'person']:
            tags[i-4] = 'player_perspective=first_person'

        if tokens[i-6:i+1] == ['not', 'released', 'on', 'the', 'linux', 'or', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-8:i+1] == ['do', 'you', 'prefer', 'playing', 'games', 'with', 'friends', 'in', 'multiplayer']:
            for j in range(i-8,i+1):
                tags[j] = 'has_multiplayer='

        if tokens[i-6:i+1] == ["n't", 'available', 'on', 'the', 'linux', 'or', 'mac']:
            for j in range(i-6,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-4:i+1] == ['not', 'the', 'linux', 'or', 'mac']:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-3:i+1] == ['not', 'available', 'on', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['for', 'a', 'teen', 'audience']:
            for j in range(i-3,i+1):
                tags[j] = 'esrb=T_(for_Teen)'

        if tokens[i-5:i+1] == ['was', 'released', 'in', 'linux', 'and', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-4:i+1] == ['on', 'both', 'linux', 'and', 'mac']:
            for j in range(i-4,i-1):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == ['which', 'game', 'developer']:
            for j in range(i-2,i+1):
                tags[j] = 'developer='

        if tokens[i-6:i+1] == ['especially', 'when', 'they', 'come', 'to', 'the', 'mac']:
            for j in range(i-6,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-6:i+1] == ['i', 'can', 'play', 'it', 'with', 'my', 'friends']:
            for j in range(i-6,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-11:i+1] == ['i', 'have', 'a', 'mac', 'and', 'it', "'s", 'hard', 'to', 'find', 'good', 'games',]:
            for j in range(i-11,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-9:i+1] == ['ignore', 'multiplayer', 'to', 'just', 'focus', 'on', 'a', 'good', 'single-player', 'experience']:
            for j in range(i-9, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-4:i+1] == ['if', 'you', 'find', 'linux', 'releases']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-3:i+1] == ['no', 'multiplayer', 'is', 'available']:
            for j in range(i-3,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-8:i+1] == ['do', 'you', 'like', 'linux', 'games', 'from', 'RELEASE_YEAR', 'like', 'NAME']:
            for j in range(i-8,i-3):
                tags[j] = 'has_linux_release=yes'

        if t == 'fighter':
            tags[i] = 'genres=fighting'

        if tokens[i-14:i+1] == ['a', 'good', 'single-player', 'game', '.', '<sent>', 'it', 'can', 'not', 'be', 'played', 'as', 'a', 'multiplayer', 'game',]:
            for j in range(i-14,i+1):
                tags[j] = 'has_multiplayer=no'


        if tokens[i-3:i+1] == ['are', 'there', 'any', 'genres']:
            for j in range(i-3,i+1):
                tags[j] = 'genres='

        if tokens[i-2:i+1] == ['trivia', 'and', 'board']:
            for j in range(i-2,i+1):
                tags[j] = 'genres=trivia/board_game'

        if tokens[i-4:i+1] == ["n't", 'have', 'a', 'steam', 'release']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-6:i+1] == ['why', 'do', 'you', 'think', 'that', 'mac', 'games']:
            for j in range(i-6,i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-4:i+1]  == ['nintendo', ',', 'mac', ',', 'linux',]:
            tags[i-2] = 'has_mac_release=yes'
            tags[i] = 'has_linux_release=yes'

        if tokens[i-5:i+1] == ['have', 'a', 'linux', 'and', 'mac', 'release']:
            for j in range(i-5,i-2):
                tags[j] = 'has_linux_release=yes'
            tags[i] = 'has_mac_release=yes'
            tags[i-1] = 'has_mac_release=yes'

        if tokens[i-2:i+1] == [',', 'switch', ',']:
            tags[i-1] = 'platforms=Nintendo_Switch'

        if tokens[i-4:i+1] == ['everything', 'but', 'mac', 'and', 'linux']:
            for j in range(i-4,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-2:i+1] == ['drive', 'and', 'race']:
            for j in range(i-2,i+1):
                tags[j] = 'genres=driving/racing'

        if tokens[i-5:i+1] == ['action', 'game', 'with', 'lots', 'of', 'adventure']:
            for j in range(i-5,i+1):
                tags[j] = 'genres=action-adventure'

        if tokens[i-6:i+1] == ["n't", 'have', 'a', 'mac', 'or', 'linux', 'release']:
            for j in range(i-6,i-2):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ["n't", 'available', 'on', 'linux', 'and', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-5:i+1] == ['what', 'is', 'your', 'favorite', 'player', 'perspective']:
            for j in range(i-5,i+1):
                tags[j] = 'player_perspective='

        if tokens[i-2:i+1] == ['rated', 'for', 'teenagers']:
            for j in range(i-2,i+1):
                tags[j] = 'esrb=T_(for_Teen)'

        if tokens[i-4:i+1] == [ 'no', 'steam', 'or', 'linux', 'release']:
            for j in range(i-4,i-2):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_linux_release=no'
            tags[i-1] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['neither', 'linux', 'nor', 'mac']:
            for j in range(i-3,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'

        if tokens[i-14:i+1] == ['with', 'multiplayer', ',', 'as', 'the', 'single', '-', 'player', 'then', 'tends', 'to', 'be', 'lacking', 'in', 'depth']:
            for j in range(i-14,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-6:i+1] == ['does', 'a', 'game', 'having', 'a', 'mac', 'release']:
            for j in range(i-6,i+1):
                tags[j] = 'has_mac_release='

        if tokens[i-9:i+1] == ['nor', 'does', 'it', 'have', 'a', 'linux', 'or', 'a', 'mac', 'release']:
          
            for j in range(i-9, i-3):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i-2] = 'has_mac_release=no'

        if tokens[i-8:i+1] == ['should', 'have', 'been', 'made', 'm', '(', 'for', 'mature', ')']:
            for j in range(i-8,i+1):
                tags[j] = '0'

        if tokens[i-5:i+1] == ['use', 'linux', 'on', 'my', 'home', 'pc']:
            for j in range(i-5,i+1):
                tags[j] = 'has_linux_release=yes'

        if tokens[i-16:i+1] == ['do', 'you', 'think', 'making', 'it', 'a', 'single', '-', 'player', 'only', 'game', 'would', 'have', 'been', 'a', 'better', 'idea']:
            for j in range(i-16,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-10:i+1] == ['developer', 'that', 'is', 'terrible', 'at', 'doing', 'anything', 'other', 'than', 'maybe', 'multiplayer',]:
            tags[i] = '0'

        if tokens[i-3:i+1] == ["'s", 'omission', 'of', 'multiplayer']:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=no'


        if tokens[i-21:i+1] == ['i', 'just', 'much', 'prefer', 'single', '-', 'player', 'only', 'games', ',', 'rather', 'than', 'ones', 'that', 'throw', 'in', 'a', 'multiplayer', 'mode', 'like', 'it', 'did',]:
            for j in range(i-21,i+1):
                tags[j] = 'has_multiplayer=yes'


        if tokens[i-10:i+1] == ['t', 'rating', 'to', 'balance', 'being', 'family', 'friendly', 'and', 'having', 'mature', 'themes']:
            for j in range(i-10,i+1):
                tags[j] = 'esrb=T_(for_Teen)'

        if tokens[i-12:i+1] == ['i', "'m", 'a', 'mac', 'guy', 'and', 'it', 'was', "n't", 'released', 'for', 'this', 'system']:
            for j in range(i-12,i+1):
                tags[j] = 'has_mac_release=no'


        if tokens[i-6:i+1] == ['not', 'have', 'a', 'linux', 'and', 'mac', 'release']:
            for j in range(i-6,i-2):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'

        if tokens[i-20:i+1] == ['i', 'do', "n't", 'like', 'steam', 'and', 'i', 'think', 'focusing', 'on', 'a', 'linux', 'release', 'takes', 'time', 'away', 'from', 'making', 'a', 'game', 'good']:
            for j in range(i-20,i-15):
                tags[j] = 'available_on_steam=no'
            for j in range(i-14,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-8:i+1] == ["n't", 'have', 'a', 'linux', 'version', 'or', 'a', 'steam', 'release']:
            for j in range(i-8,i-3):
                tags[j] = 'has_linux_release=no'
            for j in range(i-2,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-14:i+1] == ['i', "'d", 'rather', 'just', 'play', 'an', 'actual', 'real', 'life', 'one', 'instead', 'of', 'a', 'virtual', 'simulation']:
            for j in range(i-14,i+1):
                tags[j] = '0'

        if tokens[i-2:i+1] == ['offers', 'multiplayer', 'action']:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-2:i+1] == ['features', 'multiplayer', 'action']:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-10:i+1] == ['do', 'you', 'miss', 'such', 'role-playing', 'tactical', 'shooters', 'being', 'released', 'for', 'mac']:
            for j in range(i-2, i+1):
                tags[j] = 'has_mac_release=no'

        if tokens[i-19:i+1] == ['i', 'like', 'third', 'person', 'player', 'perspective', 'games', ',', 'but', 'NAME', 'felt', 'like', 'it', 'might', 'have', 'been', 'better', 'in', 'first', 'person',]:
            tags[i] = '0'
            tags[i-1] = '0'


        if tokens[i-11:i+1] == ['first', 'person', 'is', 'too', 'close', 'and', 'bird', "'s", 'eye', 'is', 'too', 'far']:
            for j in range(i-11,i+1):
                tags[j] = '0'

        if tokens[i-7:i+1] == ['you', 'seem', 'to', 'find', 'all', 'mac', 'releases', 'unacceptable',]:
            for j in range(i-7, i+1):
                tags[j] = 'has_mac_release=yes'

        if tokens[i-5:i+1] == ['what', 'is', 'it', 'about', 'mac', 'games']:
            for j in range(i-5,i+1):
                tags[j] = 'has_mac_release=yes'
        if tokens[i-5:i+1] == ['why', 'do', 'you', 'feel', 'steam', 'games']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=yes'


        if tokens[i-5:i+1] == ['what', 'is', 'it', 'about', 'steam', 'games']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=yes'

        if tokens[i-10:i+1] == ['do', 'you', 'prefer', 'playing', 'games', 'that', 'you', 'can', 'get', 'on', 'steam']:
            for j in range(i-10,i+1):
                tags[j] = 'available_on_steam='

        if tokens[i-8:+1] == ['not', 'available', 'on', 'steam', ',', 'linux',
                              ',', 'and', 'mac']:
            for j in range(i-8,i-4):
                tags[j] = 'available_on_steam=no'
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'

        if tokens[i-8:i+1] == ['not', 'available', 'on', 'steam', ',', 
                               'linux', ',', 'and', 'mac']:
            tags[i] = 'has_mac_release=no'
            tags[i-3] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['lack', 'of', 'a', 'multiplayer', 'mode']:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-6:i+1] == ['not', 'offer', 'support', 'for', 'mac', 'or', 'linux']:
            for j in range(i-6,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['not', 'available', 'to', 'play', 'on', 'steam']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-4:i+1] == ['not', 'currently', 'available', 'on', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=no'

def check_specifier(tokens, tags):

    for i, t in enumerate(tokens):
        if t.startswith('SPECIFIER'):
            tags[i] = f'specifier={t}'
#    S = 'SPECIFIER'
#    OBJS = ['games', 'graphics', 'shooters', 'storylines', 'platformers',
#            'simulators', 'titles', 'game', 'releases']
#    ADV = [
#        "plain", "totally", "really", "very", "pretty", 
#        "rather", "simply", "most", "particularly", 
#        "overly", "genuinely", "just", #favorite
#        "somewhat", "so", "way", "totally", 'truly']
#    for i, t in enumerate(tokens):
#        for obj in OBJS:
#            if tokens[i-1:i+1] == ['SPECIFIER', obj]:
#                tags[i-1] = f'specifier=PLACEHOLDER'
#                tags[i] = f'specifier_obj={obj}'
#
#        for quant in ['any']:
#            for obj in OBJS:
#                if tokens[i-2:i+1] == [quant, 'SPECIFIER', obj]:
#                    tags[i-2] = f'specifier_quant={quant}'
#                    tags[i-1] = f'specifier=PLACEHOLDER'
#                    tags[i] = f'specifier_obj={obj}'
#
#        for quant in ['any']:
#            for obj in OBJS:
#                if tokens[i:i+1] == [quant] and tokens[i+2:i+4] == ['SPECIFIER', obj]:
#                    tags[i] = f'specifier_quant={quant}'
#                    tags[i+2] = f'specifier=PLACEHOLDER'
#                    tags[i+3] = f'specifier_obj={obj}'
#
#        for quant in ['any']:
#            for obj in OBJS:
#                if tokens[i:i+1] == [quant] and tokens[i+2:i+5] == ['SPECIFIER', 'video', obj]:
#                    tags[i] = f'specifier_quant={quant}'
#                    tags[i+2] = f'specifier=PLACEHOLDER'
#                    tags[i+3] = f'specifier_obj=video {obj}'
#                    tags[i+3] = f'specifier_obj=video {obj}'
#
#
#
#
#        for det in ['a', 'an', 'the', 'yours', 'your']:
#            for obj in OBJS:
#                if tokens[i-2:i+1] == [det, 'SPECIFIER', obj]:
#                    tags[i-2] = f'specifier_det={det}'
#                    tags[i-1] = f'specifier=PLACEHOLDER'
#                    tags[i] = f'specifier_obj={obj}'
#
#        for det in ['a', 'an', 'the', 'yours', 'your']:
#            for obj in OBJS:
#                if tokens[i-3:i-2] == [det] and tokens[i-1:i+1] == ['SPECIFIER', obj]:
#                    tags[i-3] = f'specifier_det={det}'
#                    tags[i-1] = f'specifier=PLACEHOLDER'
#                    tags[i] = f'specifier_obj={obj}'
#
#                for adj in ['favorite', 'good', 'nice']:
#                    if tokens[i-2:i+1] == [det, adj, 'SPECIFIER']:
#                        for s in range(1,8):
#                            if all([tags[d] != '0' for d in range(i+1,min(i+1+s,len(tags)))]):
#                                if tokens[i+1+s:i+1+s+1] == [obj]:
#
#                                    tags[i-2] = f'specifier_det={det}'
#                                    tags[i] = f'specifier=PLACEHOLDER'
#                                    
#                                    
#                                    tags[i+1+s] = f'specifier_obj={obj}'
#
#
#        for det in ['a', 'an', 'the', 'yours', 'your']:
#            for obj in OBJS:
#                if tokens[i-3:i-2] == [det] and tokens[i-1:i+2] == ['SPECIFIER', 'video', obj]:
#                    tags[i-3] = f'specifier_det={det}'
#                    tags[i-1] = f'specifier=PLACEHOLDER'
#                    tags[i] = f'specifier_obj=video {obj}'
#                    tags[i+1] = f'specifier_obj=video {obj}'
#
#
#
#        for det in ['a', 'an', 'the', 'yours', 'your']:
#            for adv in ADV:
#                for obj in OBJS:
#                    if tokens[i-3:i+1] == [det, adv, 'SPECIFIER', obj]:
#                        tags[i-3] = f'specifier_det={det}'
#                        tags[i-2] = f'specifier_adv={adv}'
#                        tags[i-1] = f'specifier=PLACEHOLDER'
#                        tags[i] = f'specifier_obj={obj}'
#
#
#        for det in ['a', 'an', 'the', 'yours', 'your']:
#            for obj in OBJS:
#                for s in range(1,8):
#                    if tokens[i-1:i+1] == [det, 'SPECIFIER'] \
#                            and all([tags[d] != '0' for d in range(i+1,min(i+s+1,len(tags)))]) \
#                            and tokens[i+s+1:i+s+2] == [obj]:
#                         
#                        tags[i-1] = f'specifier_det={det}'
#                        tags[i] = f'specifier=PLACEHOLDER'
#                        tags[i+s+1] = f'specifier_obj={obj}'
#        #####
#        for obj in OBJS:
#            if tokens[i-2:i+1] == ['SPECIFIER', 'video', obj]:
#                tags[i-2] = f'specifier=PLACEHOLDER'
#                tags[i-1] = f'specifier_obj=video {obj}'
#                tags[i] = f'specifier_obj=video {obj}'
#
#        for quant in ['any']:
#            for obj in OBJS:
#                if tokens[i-3:i+1] == [quant, 'SPECIFIER', 'video', obj]:
#                    tags[i-3] = f'specifier_quant={quant}'
#                    tags[i-2] = f'specifier=PLACEHOLDER'
#                    tags[i-1] = f'specifier_obj=video {obj}'
#                    tags[i] = f'specifier_obj=video {obj}'
#
#
#        for det in ['a', 'an', 'the', 'yours', 'your']:
#            for obj in OBJS:
#                if tokens[i-3:i+1] == [det, 'SPECIFIER', 'video', obj]:
#                    tags[i-3] = f'specifier_det={det}'
#                    tags[i-2] = f'specifier=PLACEHOLDER'
#                    tags[i-1] = f'specifier_obj=video {obj}'
#                    tags[i] = f'specifier_obj=video {obj}'
#
#        for det in ['a', 'an', 'the', 'yours', 'your']:
#            for adv in ADV:
#                for obj in OBJS:
#                    if tokens[i-4:i+1] == [det, adv, S, 'video', obj]:
#                        tags[i-4] = f'specifier_det={det}'
#                        tags[i-3] = f'specifier_adv={adv}'
#                        tags[i-2] = f'specifier=PLACEHOLDER'
#                        tags[i-1] = f'specifier_obj=video {obj}'
#                        tags[i] = f'specifier_obj=video {obj}'
#
#                    if tokens[i-6:i+1] == [det, 'video', obj, 'you', 'found', adv, S]:
#                        tags[i-6] = f'specifier_det={det}'
#                        tags[i-5] = f'specifier_obj=video {obj}'
#                        tags[i-4] = f'specifier_obj=video {obj}'
#                        tags[i-1] = f'specifier_adv={adv}'
#                        tags[i] = f'specifier=PLACEHOLDER'
#
#                    if tokens[i-5:i+1] == [det, obj, 'you', 'found', adv, S]:
#                        tags[i-5] = f'specifier_det={det}'
#                        tags[i-4] = f'specifier_obj={obj}'
#                        tags[i-1] = f'specifier_adv={adv}'
#                        tags[i] = f'specifier=PLACEHOLDER'
#
#
#
#
#        #####
#
#
#
#        for det in ['a', 'an', 'the', 'yours', 'your']:
#            for obj in OBJS:
#                for s in range(1,8):
#                    if tokens[i-1:i+1] == [det, 'SPECIFIER'] \
#                            and all([tags[d] != '0' for d in range(i+1,min(i+s+1,len(tags)))]) \
#                            and tokens[i+s+1:i+s+2] == [obj]:
#                         
#                        tags[i-1] = f'specifier_det={det}'
#                        tags[i] = f'specifier=PLACEHOLDER'
#                        tags[i+s+1] = f'specifier_obj={obj}'
#
#        
#        for det in ['a', 'an', 'the', 'yours', 'your']:
#            for obj in OBJS:
#                for adv in ADV:
#                    for s in range(1,8):
#                        if tokens[i-2:i+1] == [det, adv, 'SPECIFIER'] \
#                                and all([tags[d] != '0' for d in range(i+1,min(i+s+1, len(tags)))]) \
#                                and tokens[i+s+1:i+s+2] == [obj]:
#                             
#                            tags[i-2] = f'specifier_det={det}'
#                            tags[i-1] = f'specifier_adv={adv}'
#                            tags[i] = f'specifier=PLACEHOLDER'
#                            tags[i+s+1] = f'specifier_obj={obj}'
#
#        for obj in OBJS:
#            for adv in ADV:
#                if tokens[i-5:i+1] == [obj, 'recently', 'that', 'was', adv, S]:
#                    tags[i-5] = f'specifier_obj={obj}'
#                    tags[i-1] = f'specifier_adv={adv}'
#                    tags[i] = f'specifier=PLACEHOLDER'
#
#        for obj in OBJS:
#            for adv in ADV:
#                if tokens[i-4:i+1] == [obj, 'that', 'was', adv, S]:
#                    tags[i-4] = f'specifier_obj={obj}'
#                    tags[i-1] = f'specifier_adv={adv}'
#                    tags[i] = f'specifier=PLACEHOLDER'
#        
#
#        PHRASES = [
#            ['that', 'you', 'just', 'found', 'to', 'be', S],
#            ['that', 'you', 'felt', 'was', S],
#            ['that', 'was', 'just', 'plain', S],
#        ]
#        for obj in OBJS:
#            for prep in ["with", "from"]:
#                if tokens[i-1:i+1] == [obj, prep]:
#                    for s in range(1,8):
#                        if all([tags[d] != '0' for d in range(i+1,min(i+1+s, len(tags)))]):
#                            print(tokens[i+1+s:])
#                            for phrase in PHRASES:
#
#                                if tokens[i+1+s:i+1+len(phrase)+s] == phrase:
#                                    tags[i+len(phrase)+s] = 'specifier=PLACEHOLDER'
#                                    tags[i-1] = f'specifier_obj={obj}'
#                if tokens[i-4:i+1] == [obj, 'you', 'know', 'of', prep]:
#                    for s in range(1,8):
#                        if all([tags[d] != '0' for d in range(i+1,min(i+1+s, len(tags)))]):
#                            print(tokens[i+1+s:])
#                            for phrase in PHRASES:
#
#                                if tokens[i+1+s:i+1+len(phrase)+s] == phrase:
#                                    tags[i+len(phrase)+s] = 'specifier=PLACEHOLDER'
#                                    tags[i-4] = f'specifier_obj={obj}'
#
#
#        for obj in OBJS:
#            for adv in ADV:
#                if tokens[i-8:i+1] == ['what', obj, 'do', 'you', 'think', 'is',
#                                       'just', adv, S]:
#                    tags[i-7] = f'specifier_obj={obj}'
#                    tags[i] = 'specifier=PLACEHOLDER'
#                    tags[i-1] = f'specifier_adv={adv}'
#                if tokens[i-10:i+1] == ['what', obj, 'you', "'ve", 'played', 
#                                        'do', 'you', 'think', 'is', adv, S]:
#                    tags[i-9] = f'specifier_obj={obj}'
#                    tags[i] = 'specifier=PLACEHOLDER'
#                    tags[i-1] = f'specifier_adv={adv}'
#                if tokens[i-8:i+1] == ['what', obj, 'did', 'you', 'find', 
#                                        'to', 'be', adv, S]:
#                    tags[i-7] = f'specifier_obj={obj}'
#                    tags[i] = 'specifier=PLACEHOLDER'
#                    tags[i-1] = f'specifier_adv={adv}'
#        
#                if tokens[i-7:i+1] == ['any', obj, 'this', 'year', 'to', 'be',
#                                       adv, S]:
#                    tags[i-7] = f'specifier_quant=any'
#                    tags[i-6] = f'specifier_obj={obj}'
#                    tags[i] = 'specifier=PLACEHOLDER'
#                    tags[i-1] = f'specifier_adv={adv}'
# 
#            if tokens[i-1:i+1] == ['any', S]:
#                for s in range(1,8):
#                    if all([tags[d] != '0' for d in range(i+1,min(i+1+s, len(tags)))]):
#                        if tokens[i+1+s:i+2+s] == [obj]:
#                            tags[i-1] = f'specifier_quant=any'
#                            tags[i] = 'specifier=PLACEHOLDER'
#                            tags[i+1+s] = f'specifier_obj={obj}'
#            if tokens[i-2:i+1] == ['any', S, ","]:
#                for s in range(1,8):
#                    if all([tags[d] != '0' for d in range(i+1,min(i+1+s, len(tags)))]):
#                        if tokens[i+1+s:i+2+s] == [obj]:
#                            tags[i-2] = f'specifier_quant=any'
#                            tags[i-1] = 'specifier=PLACEHOLDER'
#                            tags[i+1+s] = f'specifier_obj={obj}'
#
#        
#        tokens == obj, 'with', 'multiplayer', 
        
def fix_weird(tokens, tags):
    for i, t in enumerate(tokens):
        if tokens[i-5:i+1] == ['take', 'a', 'traditionally', 'single', '-', 'player']:
            for j in range(i-5,i+1):
                tags[j] = '0'
        if tokens[i-4:i+1] == ['not', 'currently', 'available', 'on', 'steam']:
            for j in range(i-4,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-3:i+1] == ['not', 'available', 'on', 'steam']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-3:i+1] == ["n't", 'available', 'on', 'steam']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-2:i+1] == ["n't", 'on', 'linux']:
            for j in range(i-2,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-5:i+1] == ['without', 'the', 'unnecessary', 'release', 'for', 'linux']:
            for j in range(i-5,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-8:i+1] == ['wish', 'had', 'a', 'linux', 'release', 'but', 'sadly', 'does', "n't"]:
            for j in range(i-8,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-4:i+1] == ['never', 'got', 'released', 'on', 'linux']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=no'
        if tokens[i-3:i+1] == ['without', 'a', 'linux', 'release']:
            for j in range(i-3, i+1):
                tags[j] = 'has_linux_release=no'
        if tokens[i-2:i+1] == ['offers', 'multiplayer', 'action']:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-2:i+1] == ['features', 'multiplayer', 'action']:
            for j in range(i-2,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-2:i+1] == ['strategic', 'bird', 'view']:
            tags[i-2] = '0'
        if tokens[i-4:i+1] == ['not', 'on', 'steam', 'or', 'mac']:
            tags[i] = 'has_mac_release=no'
        if tokens[i-3:i+1] == ["n't", 'available', 'on', 'linux']:
            for j in range(i-3,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-10:i+1] == ['is', 'it', 'important', 'for', 'you', 'that', 'games', 'have', 'a', 'mac', 'release']:
            for j in range(i-10, i+1):
                tags[j] = 'has_mac_release='

        if tokens[i-4:i+1] == ['are', 'you', 'a', 'mac', 'gamer']:
            for j in range(i-4,i+1):
                tags[j] = 'has_mac_release='
        if tokens[i-10:i+1] == ['do', 'you', 'like', 'to', 'play', 'games', 'that', 'have', 'a', 'multiplayer', 'option']:
            for j in range(i-10,i+1):
                tags[j] = 'has_multiplayer='
        if tokens[i-5:i+1] == ['do', 'you', 'find', 'multiplayer', 'games', 'enjoyable']:
            for j in range(i-5,i+1):
                tags[j] = 'has_multiplayer='

        if tokens[i-7:i+1] == ['not', 'have', 'a', 'release', 'on', 'mac', 'and', 'linux']:
            for j in range(i-7,i-1):
                tags[j] = 'has_mac_release=no'
            tags[i] = 'has_linux_release=no'

        if tokens[i-7:i+1] == ['would', 'have', 'been', 'so', 'much', 'better', 'with', 'multiplayer']:
            for j in range(i-7,i+1):
                tags[j] = 'has_multiplayer=no'
        if tokens[i-13:i+1] == ['just', 'do', "n't", 'truly', 'enjoy', 'a', 'game', 'unless', 'it', "'s", 'got', 'a', 'multiplayer', 'mode']:
            for j in range(i-13, i+1):
                tags[j] = 'has_multiplayer=no'

        if tokens[i-5:i+1] == ['which', 'you', 'can', 'play', 'with', 'friends']:
            for j in range(i-5,i+1):
                tags[j] = 'has_multiplayer=yes'

        if tokens[i-8:i+1] == ['what', 'is', 'your', 'favorite', 'year', 'that', 'games', 'came', 'out']:
            for j in range(i-8,i+1):
                tags[j] = 'release_year='

        if tokens[i-5:i+1] == ['what', 'platform', 'do', 'you', 'game', 'on']:
            for j in range(i-5,i+1):
                tags[j] = 'platforms='

        if tokens[i-5:i+1] == ['do', 'you', 'purchase', 'games', 'from', 'steam']:
            for j in range(i-5,i+1):
                tags[j] = 'available_on_steam='

        if tokens[i-7:i+1] == ['do', 'you', 'like', 'games', 'with', 'availability', 'on', 'steam']:
            for j in range(i-7,i+1):
                tags[j] = 'available_on_steam='

        if tokens[i-8:i+1] == ['are', 'there', 'certain', 'genres', 'you', 'just', 'love', 'to', 'play']:
            for j in range(i-8,i+1):
                tags[j] = 'genres='
        if tokens[i-7:i+1] == ['what', 'would', 'you', 'say', 'is', 'your', 'favorite', 'genre']:
            for j in range(i-7,i+1):
                tags[j] = 'genres='

        if tokens[i-2:i+1] == ['suitable', 'for', 'teens']:
            for j in range(i-2,i+1):
                tags[j] = 'esrb=T_(for_Teen)'

        if tokens[i-4:i+1] == ["n't", 'even', 'playable', 'on', 'linux']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-8:i+1] == ['not', 'available', 'on', 'steam', ',', 'mac', ',', 'or', 'linux']:
            tags[i] = 'has_linux_release=no'
            tags[i-3] = 'has_mac_release=no'
            tags[i-5] = 'available_on_steam=no'
            tags[i-6] = 'available_on_steam=no'
            tags[i-7] = 'available_on_steam=no'
            tags[i-8] = 'available_on_steam=no'

        if tokens[i-7:i+1] == ["n't", 'even', 'give', 'the', 'game', 'a', 'linux', 'release']:
            for j in range(i-7,i+1):
                tags[j] = 'has_linux_release=no'

        if tokens[i-3:i+1] == ['is', 'there', 'a', 'developer']:
            for j in range(i-3,i+1):
                tags[j] = 'developer='
        if tokens[i-4:i+1] == ['is', 'there', 'a', 'particular', 'developer']:
            for j in range(i-4,i+1):
                tags[j] = 'developer='
        if tokens[i-5:i+1] == ['i', 'wish', 'NAME', 'was', 'on', 'steam']:
            tags[i] = 'available_on_steam=no'
            tags[i-1] = '0'

        if tokens[i-19:i+1] == ['it', 'has', 'a', 'great', 'single', '-', 'player', 'campaign', ',', 'but', 'you', 'can', 'jump', 'online', 'and', 'enjoy', 'it', 'that', 'way', 'too']:
            for j in range(i-19,i+1):
                tags[j] = '0'
        if tokens[i-3:i+1] == ["n't", 'have', 'steam', 'releases']:
            for j in range(i-3,i+1):
                tags[j] = 'available_on_steam=no'

        if tokens[i-2:i+1] == ['lack', 'steam', 'support']:
            for j in range(i-2,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-1:i+1] == ['teen', 'action']:
            tags[i-1] = 'esrb=T_(for_Teen)'

        if tokens[i-9:i+1] == ['would', 'you', 'not', 'consider', 'a', 'game', 'without', 'a', 'mac', 'release']:
            for j in range(i-9,i+1):
                tags[j] = 'has_mac_release='
        if tokens[i-6:i+1] == ['do', 'you', 'enjoy', 'gaming', 'on', 'a', 'mac',]:
            for j in range(i-6,i+1):
                tags[j] = 'has_mac_release='
        if tokens[i-7:i+1] == ['do', 'you', 'have', 'a', 'favorite', 'esrb', 'content', 'rating']:
            for j in range(i-7,i+1):
                tags[j] = 'esrb='
        if tokens[i-11:i+1] == ['are', 'you', 'at', 'all', 'bothered', 'by', 'the', 'esrb', 'rating', 'of', 'a', 'game']:
            for j in range(i-11,i+1):
                tags[j] = 'esrb='

        if tokens[i-10:i+1] == ['what', 'would', 'you', 'say', 'was', 'a', 'memorable', 'year', 'for', 'video', 'games']:
            for j in range(i-10, i+1):
                tags[j] = 'release_year='
        if tokens[i-4:i+1] == ['is', 'there', 'a', 'particular', 'year',]:
            for j in range(i-4, i+1):
                tags[j] = 'release_year='
        if tokens[i-10:i+1] == ['do', 'you', 'do', 'any', 'of', 'your', 'gaming', 'on', 'a', 'linux', 'system']:
            for j in range(i-10,i+1):
                tags[j] = 'has_linux_release='
        if tokens[i-12:i+1] == ['is', 'it', 'important', 'for', 'you', 'that', 'a', 'game', 'is', 'also', 'available', 'on', 'linux',]:
            for j in range(i-12,i+1):
                tags[j] = 'has_linux_release='
        if tokens[i-7:i+1] == ['do', 'you', 'prefer', 'getting', 'your', 'games', 'on', 'steam']:
            for j in range(i-7,i+1):
                tags[j] = 'available_on_steam='
        if tokens[i-6:i+1] == ['are', 'you', 'more', 'of', 'a', 'multiplayer', 'type']:
            for j in range(i-6,i+1):
                tags[j] = 'has_multiplayer='
        if tokens[i-4:i+1] == ['do', 'you', 'enjoy', 'multiplayer', 'games']:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer='

        if tokens[i-4:i+1] == ['are', 'you', 'into', 'multiplayer', 'gaming']:
            for j in range(i-4,i+1):
                tags[j] = 'has_multiplayer='

        if tokens[i-7:i+1] == ['do', 'you', 'often', 'check', 'out', 'the', 'multiplayer', 'mode',]:
            for j in range(i-7,i+1):
                tags[j] = 'has_multiplayer='
        if tokens[i-9:i+1] == ['do', 'you', 'like', 'games', 'that', 'you', 'can', 'play', 'in', 'multiplayer']:
            for j in range(i-9,i+1):
                tags[j] = 'has_multiplayer='
        if tokens[i-22:i+1] == ['you', 'do', "n't", 'seem', 'to', 'be', 'into', 'multiplayer', 'games', ',', 'so', 'tell', 'me', ',', 'have', 'you', 'heard', 'of', 'the', 'single', '-', 'player', 'game']:
            for j in range(i-22,i+1):
                tags[j] = 'has_multiplayer=no'
            
            
        if tokens[i-1:i+1] == ['lack', 'multiplayer']:
            tags[i] = 'has_multiplayer=no'
            tags[i-1] = 'has_multiplayer=no'

        if tokens[i-7:i+1] == ['features', 'non', '-', 'stop', 'action', 'and', 'vehicular', 'combat']:
            for j in range(i-7,i+1):
                tags[j] = 'genres=vehicular_combat'

        if tokens[i-4:i+1] == ['wish', 'was', 'released', 'for', 'linux']:
            for j in range(i-4,i+1):
                tags[j] = 'has_linux_release=no'
        if tokens[i-7:i+1] == ['would', 'you', 'say', 'you', 'prefer', 'a', 'certain', 'developer',]:
            for j in range(i-7,i+1):
                tags[j] = 'developer='
        if tokens[i-2:i+1] == ['what', 'developer', 'is']:
            for j in range(i-2,i+1):
                tags[j] = 'developer='
        if tokens[i-12:i+1] == ['that', 'ignore', 'multiplayer', 'to', 'just', 'focus', 'on', 'a', 'good', 'single', '-', 'player', 'experience']:
            for j in range(i-12,i+1):
                tags[j] = 'has_multiplayer=no'
        if tokens[i-6:i+1] == ['not', 'be', 'played', 'as', 'a', 'multiplayer', 'game']:
            for j in range(i-6,i+1):
                tags[j] = 'has_multiplayer=no'
        if tokens[i-4:i+1] == ['what', 'is', 'your', 'favorite', 'genre']:
            for j in range(i-4,i+1):
                tags[j] = 'genres='
        if tokens[i-6:i+1] == ['what', "'s", 'your', 'favorite', 'video', 'game', 'genre',]:
            for j in range(i-6,i+1):
                tags[j] = 'genres='
        if tokens[i-4:i+1] == ['what', "'s", 'your', 'favorite', 'genre']:
            for j in range(i-4,i+1):
                tags[j] = 'genres='
        if tokens[i-2:i+1] == ['what', 'genres', 'are']:
            for j in range(i-2,i+1):
                tags[j] = 'genres='
        if tokens[i-3:i+1] == ['which', 'is', 'the', 'genre']:
            for j in range(i-3,i+1):
                tags[j] = 'genres='
        if tokens[i-6:i+1] == [ "n't", 'care', 'about', 'getting', 'games', 'on', 'steam']:
            for j in range(i-6,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-7:i+1] == ["n't", 'care', 'about', 'your', 'games', 'being', 'on', 'steam']:
            for j in range(i-7,i+1):
                tags[j] = 'available_on_steam=no'
        if tokens[i-9:i+1] == ['should', 'have', 'been', 'released', 'for', 'linux', 'and', 'mac', 'as', 'well']:
            for j in range(i-9,i-3):
                tags[j] = 'has_linux_release=no'
            tags[i-2] = 'has_mac_release=no'
        if tokens[i-4:i+1] == ['gaming', 'platform', 'you', 'definitely', 'prefer']:
            for j in range(i-4,i+1):
                tags[j] = 'platforms='
        if tokens[i-3:i+1] == ['is', 'there', 'a', 'platform']:
            for j in range(i-3,i+1):
                tags[j] = 'platforms='

        if tokens[i-2:i+1] == ['what', 'player', 'perspective']:
            for j in range(i-2,i+1):
                tags[j] = 'player_perspective='

        if tokens[i-4:i+1] == ['is', 'there', 'a', 'player', 'perspective',]:
            for j in range(i-4,i+1):
                tags[j] = 'player_perspective='

        if tokens[i-3:i+1] == ['everyone', '10', 'and', 'up']:
            for j in range(i-3,i+1):
                tags[j] = "esrb=E_10+_(for_Everyone_10_and_Older)"
        if tokens[i-7:i+1] == ['is', 'availability', 'of', 'a', 'game', 'on', 'steam', 'important']:
            for j in range(i-7,i+1):
                tags[j] = 'available_on_steam='

        if tokens[i-5:i+1] == ["n't", 'available', 'for', 'linux', 'and', 'mac']:
            for j in range(i-5,i-1):
                tags[j] = 'has_linux_release=no'
            tags[i] = 'has_mac_release=no'
        if tokens[i-12:i+1] == ['do', 'you', 'miss', 'such', 'role', '-', 'playing', 'tactical', 'shooters', 'being', 'released', 'for', 'mac']:
            tags[i] = 'has_mac_release=no'
            tags[i-1] = 'has_mac_release=no'
            tags[i-2] = 'has_mac_release=no'

def tag_slots(tokens):
    tags = ['0'] * len(tokens)
    check_name(tokens, tags)
    check_exp_release_date(tokens, tags)
    check_developer(tokens, tags)
    check_release_year(tokens, tags)
    check_genres(tokens, tags)
    check_platforms(tokens, tags)
    check_esrb(tokens, tags)
    check_perspective(tokens, tags)
    check_opts(tokens, tags)
    check_specifier(tokens, tags)
    fix_weird(tokens, tags)

    for i, t in enumerate(tags):
        if t.startswith('esrb'):
            tags[i] = t.replace('_', ' ')
            
        if t.startswith('genres'):
            tags[i] = t.replace('_', ' ')
 
        if t.startswith('platforms'):
            tags[i] = t.replace('_', ' ')
            
        if t.startswith('player_perspective'):
            k,v = t.split('=')
            tags[i] = k + '=' + v.replace('_', ' ')
    return tags

def tags2mrseq(tags):
    nonull_tags = [x for x in tags if x != '0']
    mrseq = [t for i, t in enumerate(nonull_tags)
             if nonull_tags[i-1:i] != [t]]
    return mrseq

def slots2mr(slots):
    mr = set()
    for k, v in slots.items():
        if k in ['name', 'developer', 'release_year', 'exp_release_date']:
            if v != '':
                mr.add(f'{k}=PLACEHOLDER')
            else:
                mr.add(f'{k}=')
        elif k == 'specifier':
            mr.add(f'{k}={get_specifier_feats(v)}')
        elif not isinstance(v, list):
            mr.add(f'{k}={v}')
        else:
            for vi in v:
                mr.add(f'{k}={vi}')
    return mr

def get_specifier_feats(specifier):
    sup_feat = 'S' if 'worst' in specifier or specifier[-2:] == 'st' else 'R'
    start_feat = 'V' if specifier[0] in 'aeiou' else 'C'
    return f'SPECIFIER_{start_feat}_{sup_feat}'

def tokenize(text):
    delex_ref = text
    delex_ref = re.sub(r"fps\.", r"fp__ __s.", delex_ref)
    delex_ref = re.sub(r"fps", r"fp__ __s", delex_ref)
    delex_ref = re.sub(r"FPS\.", r"FP__ __S.", delex_ref)
    delex_ref = re.sub(r"FPS", r"FP__ __S", delex_ref)
    delex_ref = re.sub(r"(\w)/(\w)", r"\1 / \2", delex_ref)
    delex_ref = re.sub(r"(\w)-(\w)", r"\1 - \2", delex_ref)
    delex_sents = sent_tokenize(delex_ref)
    delex_tokens = " <sent> ".join(
        [" ".join(word_tokenize(delex_sent)) 
         for delex_sent in delex_sents]).split()

    return delex_tokens


LEXICON = {
    "name": [
        'Age of Empires II: The Age of Kings',
        'God of War',
        'Stronghold 2',
        'Rollcage',
        "Alan Wake's American Nightmare",
        'Never Alone',
        'Superhot',
        'Mass Effect 2',
        'The Last of Us',
        'The Witcher 3: Wild Hunt',
        'Portal 2',
        'Warcraft III: Reign of Chaos',
        'Tomb Raider: The Angel of Darkness',
        'The Wolf Among Us',
        'Ancient Cities',
        'Shadow of the Tomb Raider',
        "Assassin's Creed II",
        'RollerCoaster Tycoon',
        'Need for Speed: Most Wanted',
        'StarCraft',
        "Sid Meier's Civilization V",
        "Tom Clancy's Splinter Cell: Chaos Theory",
        'Grand Theft Auto V',
        "Tom Clancy's The Division",
        "Assassin's Creed Chronicles: India",
        'Football Manager 2015',
        'Call of Duty: Advanced Warfare',
        'Anthem',
        'Metro 2033',
        'Need for Speed: Shift',
        'Transport Tycoon',
        'The Vanishing of Ethan Carter',
        'World of Warcraft',
        'Undertale',
        'Rise of the Tomb Raider',
        'Diablo II',
        'Worms: Reloaded',
        "Uncharted 4: A Thief's End",
        'Battlefield V',
        "Mirror's Edge Catalyst",
        'F1 2014',
        "Hellblade: Senua's Sacrifice",
        'Rocket League',
        'Small World 2',
        'Tomb Raider: The Last Revelation',
        'Might & Magic: Heroes VI',
        'Driver',
        'NBA 2K19',
        'The Sims',
        'Heroes of Might and Magic III: The Restoration of Erathia',
        'Spider-Man',
        'Tetris',
        'Final Fantasy VII',
        'Lara Croft and the Temple of Osiris',
        'Little Nightmares',
        'The Forest of Doom',
        'Dirt: Showdown',
        'Super Bomberman',
        'A Way Out',
        'Need for Speed: The Run',
        'Metal Gear Solid 3: Snake Eater',
        'The Legend of Zelda: Ocarina of Time',
        'Metroid Prime Pinball',
        'MotorStorm: Apocalypse',
        'Horizon: Zero Dawn',
        'Assetto Corsa',
        'Payday 2',
        'Mafia',
        'Half-Life 2',
        'Skyforge',
        'Metro Exodus',
        'Bus Driver',
        'Commandos: Behind Enemy Lines',
        'Hitman 2',
        'Max Payne',
        'SpellForce 3',
        "Tony Hawk's Pro Skater 3",
        'Dance Dance Revolution Universe 3',
        'World of Warcraft: Battle for Azeroth',
        'Life is Strange',
        'Need for Speed: Payback',
        'Guitar Hero: Smash Hits',
        'Crysis',
        'The Elder Scrolls V: Skyrim',
        'Ori and the Blind Forest',
        'Far Cry 3',
        'BioShock',
        'Euro Truck Simulator',
        'Silent Hill 2',
        'Madden NFL 15',
        "Age of Wonders II: The Wizard's Throne",
        'Trivial Pursuit',
        'Layers of Fear',
        'The Room',
        'Outlast II',
        'FIFA 12',
        'Little Big Adventure',
        'NBA 2K16',
        'The Crew 2',
        'Nightshade',
        'Resident Evil 4',
        'Quantum Break',
        'The Elder Scrolls Online',
        'NHL 15',
        'Super Mario World',
        'TrackMania Turbo',
    ],
    "developer": [
        "Ivory Tower",
        "Adeline Software International",
        "EA Canada",
        "CD Projekt RED",
        "Fuse Games",
        "Ghost Games",
        "Upper One Games",
        "4A Games",
        "Beenox",
        "Blizzard Entertainment",
        "Bethesda Game Studios",
        "Ensemble Studios",
        "Blizzard North",
        "Neversoft Entertainment",
        "Visual Concepts",
        "Naughty Dog",
        "Nadeo",
        "Core Design",
        "EA Digital Illusions CE",
        "Crytek Frankfurt",
        "Spectrum HoloByte, Inc.",
        "SCS Software",
        "Black Hole Entertainment",
        "Dontnod Entertainment",
        "Nintendo EAD",
        "Konami Computer Entertainment Japan",
        "Red Entertainment Corporation",
        "Rockstar North",
        "Firaxis Games",
        "Allods Online",
        "Chris Sawyer",
        "Capcom Production Studio 4",
        "Kunos Simulazioni",
        "SIE Santa Monica Studio",
        "Konami",
        "Uncasual Games",
        "Loki Software",
        "Firebrand Games",
        "Massive Entertainment",
        "Telltale Games",
        "Electronic Arts",
        "Overkill Software",
        "Sports Interactive",
        "Firefly Studios",
        "Eidos Montréal",
        "Spectrum HoloByte, Inc",
        "Sledgehammer Games",
        "Fireproof Games",
        "Days of Wonder",
        "Codemasters Birmingham",
        "Konami Computer Entertainment Tokyo",
        "Ninja Theory",
        "Crystal Dynamics",
        "Team17 Digital Ltd",
        "Codemasters Southam",
        "Tarsier Studios",
        "Psyonix",
        "Hazelight Studios",
        "Hudson Soft",
        "EA Redwood Shores",
        "Valve Corporation",
        "Slightly Mad Studios",
        "Ubisoft Montreal",
        "Tin Man Games",
        "Illusion Softworks",
        "Reflections Interactive",
        "tobyfox",
        "Moon Studios",
        "MicroProse",
        "Red Barrels",
        "SUPERHOT Team",
        "Evolution Studios",
        "Pyro Studios",
        "Square",
        "Climax Studios",
        "ZeniMax Online Studios",
        "2K Boston",
        "The Astronauts",
        "Guerrilla Games",
        "Triumph Studios",
        "Grimlore Games",
        "Bloober Team",
        "EA Tiburon",
        "Remedy Entertainment",
        "IO Interactive",
        "BioWare",
        "Insomniac Games",
        "Attention To Detail",
        "Maxis",
        "Ubisoft Massive",

    ],
}

DEVELOPER_RE = "|".join([re.escape(dev) for dev in LEXICON['developer']])
NAME_RE = "|".join([re.escape(name) for name in LEXICON['name']])


def delexicalize(text, release_year=None, exp_release_date=None,
                 specifier=None):

    text = re.sub(DEVELOPER_RE, "DEVELOPER", text, flags=re.I)
    text = re.sub(NAME_RE, "NAME", text, flags=re.I)

    if exp_release_date and exp_release_date != '':
        text = re.sub(re.escape(exp_release_date), "EXP_RELEASE_DATE", text,
                      flags=re.I)
    if release_year and release_year != '':
        text = re.sub(re.escape(release_year), "RELEASE_YEAR", text,
                      flags=re.I)

    if specifier and specifier != '':
        specifier_feats = get_specifier_feats(specifier)
        specifier_re = re.escape(specifier.replace('_', ' ').replace('-', ' '))
        text = re.sub(specifier_re, specifier_feats, text, flags=re.I)

    if exp_release_date == '' or release_year == '':
        print(text)
        print("!")

    return text

