
slot_lexical_items = {
    "release_year=PLACEHOLDER": {
        "DATE": ["RELEASE_YEAR"],
    },

    "genres=MMORPG": {
        "GENRE_CONS_NOUN_GAME": ["mmorpg"],
        "GENRE_CONS_ADJ_GAME": ["massively multiplayer online role playing"],
    },
    "genres=action": {
        "GENRE_VOW_ADJ_GAME": ["action"],
#        "GENRE_VOW_NOUN_GAME": ["action game"],
    },    
	"genres=action-adventure": {
        "GENRE_VOW_ADJ_GAME": ["action-adventure"],
   #     "GENRE_VOW_NOUN_GAME": ["action-adventure game", 
#								"action and adventure game"],
	},
    "genres=adventure": {
        "GENRE_VOW_ADJ_GAME": ["adventure"],
    },  
    "genres=arcade": {
        "GENRE_VOW_ADJ_GAME": ["arcade"],
    }, 
    "genres=driving/racing": {
        "GENRE_CONS_ADJ_GAME": ["driving/racing", "driving", "racing"],
        "GENRE_CONS_NOUN_GAME": ["driver/racer", "driver", "racer"]
    },
    "genres=fighting": {
        "GENRE_CONS_ADJ_GAME": ["fighting"],
        "GENRE_CONS_NOUN_GAME": ["fighter"],
    },
    "genres=hack-and-slash": {
        "GENRE_CONS_ADJ_GAME": ["hack-and-slash"],
    },
    "genres=indie": {
        "GENRE_VOW_ADJ_GAME": ["indie"],
    },
    "genres=music": {
        "GENRE_CONS_ADJ_GAME": ["music"],
    },
    "genres=pinball": {
        "GENRE_CONS_ADJ_GAME": ["pinball"],
    },
    "genres=platformer": {
        "GENRE_CONS_ADJ_GAME": ["platform", "platforming"],
        "GENRE_CONS_NOUN_GAME": ["platformer"],
    },
    "genres=point-and-click": {
        "GENRE_CONS_ADJ_GAME": ["point-and-click"],
    },
    "genres=puzzle": {
        "GENRE_CONS_ADJ_GAME": ["puzzle"],
        "GENRE_CONS_NOUN_GAME": ["puzzler"],
    },
    "genres=real-time strategy": {
        "GENRE_CONS_ADJ_GAME": ["real-time strategy"],
    },
    "genres=role-playing": {
        "GENRE_CONS_ADJ_GAME": ["role-playing"],
    },
    "genres=shooter": {
        "GENRE_CONS_ADJ_GAME": ["shooter"],
        "GENRE_CONS_NOUN_GAME": ["shooter"],
    },
    "genres=simulation": {
        "GENRE_CONS_ADJ_GAME": ["simulation"],
        "GENRE_CONS_NOUN_GAME": ["simulator", "sim"],
    },
    "genres=sport": {
        "GENRE_CONS_ADJ_GAME": ["sports"],
    },
    "genres=strategy": {
        "GENRE_CONS_ADJ_GAME": ["strategy"],
    },
    "genres=tactical": {
        "GENRE_CONS_ADJ_GAME": ["tactical"],
    },
    "genres=text adventure": {
        "GENRE_CONS_ADJ_GAME": ["text adventure"],
        "GENRE_CONS_NOUN_GAME": ["text adventure"],
    },
    "genres=trivia/board game": {
        "GENRE_CONS_NOUN_GAME": ["trivia/board game"],
    },
    "genres=turn-based strategy": {
        "GENRE_CONS_ADJ_GAME": ["turn-based strategy"],
    },
    "genres=vehicular combat": {
        "GENRE_CONS_ADJ_GAME": ["vehicular combat"],
    },
    "available_on_steam=no": {
        "ADJP_GAME": ["not available on steam", ],
        "CONS_ADJ_GAME": ["non steam"],
        "VPF_GAME": ["will not be available on steam", ],
        "VPP_GAME": ["is not available on steam", ],
        "-NOUN": ["steam"],
    },
    "available_on_steam=yes": {
        "ADJP_GAME": ["available on steam", ],
        "VPF_GAME": ["will be available on steam",],
        "VPP_GAME": ["is available on steam",],
        "CONS_ADJ_GAME": ["steam"],
        "+NOUN": ["steam"],
    },
    "developer=PLACEHOLDER": {
        "VP_GAME": ["is by DEVELOPER", "is from the developer DEVELOPER"],
        "ADJP_GAME": ["by DEVELOPER", "from the developer DEVELOPER"],
        "PP_GAME": ["from DEVELOPER", "by DEVELOPER"],
        "NOUN": ["DEVELOPER"],
    },
    "esrb=E (for Everyone)": {
        "ADJ_GAME": ["rated e ( for everyone )"],
        "ADJP_GAME": ["rated e ( for everyone )"],
    },
    "esrb=E 10+ (for Everyone 10 and Older)": {
        "ADJ_GAME": ["rated e 10+ ( for everyone 10 and older )"],
        "ADJP_GAME": ["rated e 10+ ( for everyone 10 and older )"],
    },
   "esrb=M (for Mature)": {
        "ADJ_GAME": ["rated m ( for mature )"],
        "ADJP_GAME": ["rated m ( for mature )"],
    },
   "esrb=T (for Teen)": {
        "ADJ_GAME": ["rated t ( for teen )"],
        "ADJP_GAME": ["rated t ( for teen )"],
    },
    "exp_release_date=PLACEHOLDER": {
        "DATE": ["EXP_RELEASE_DATE"],

    },
    "has_linux_release=no": {
        "ADJP_GAME": ["not available on linux",],
        "VPF_GAME": ["will not be available on linux",],
        "VPP_GAME": ["is not available on linux",],
        "-NOUN": ["linux"],
    },
    "has_linux_release=yes": {
        "ADJP_GAME": ["available on linux"],
        "VPF_GAME": ["will be available on linux"],
        "VPP_GAME": ["is available on linux"],
        "+NOUN": ["linux"],
    },
    "has_mac_release=no": {
        "ADJP_GAME": ["not available on mac",],
        "VPF_GAME": ["will not be available on mac",],
        "VPP_GAME": ["is not available on mac",],
        "-NOUN": ["mac"],
    },
    "has_mac_release=yes": {
        "ADJP_GAME": ["available on mac"],
        "VPF_GAME": ["will be available on mac"],
        "VPP_GAME": ["is available on mac"],
        "+NOUN": ["mac"],
    },
    "has_multiplayer=no": {
        "ADJ_GAME": ["single-player"],
        "-ADJ_MODE": ["single-player"],
        "PP_GAME": ["with no multiplayer mode"],
        "SUBC_GAME": ["that is single-player only", "that does not have a multiplayer mode"],
    },
    "has_multiplayer=yes": {
        "ADJ_GAME": ["multiplayer"],
        "+ADJ_MODE": ["multiplayer"],
        "+PP_GAME": ["with multiplayer mode"],
        "SUBC_GAME": ["that has a multiplayer mode"],
    },
    "name=PLACEHOLDER": {
        "NP_GAME": ["NAME"],
    },
    "platforms=Nintendo": {
        "NOUN": ["nintendo"],
    },
    "platforms=Nintendo Switch": {
        "NOUN": ["nintendo switch"],
    },
    "platforms=PC": {
        "NOUN": ["pc"],
    },

    "platforms=Xbox": {
        "NOUN": ["xbox"],
    },
    "platforms=PlayStation": {
        "NOUN": ["playstation"],
    },


    "player_perspective=bird view": {
        "ADJ_PERS": ["bird view"], 
    },

    "player_perspective=first person": {
        "ADJ_PERS": ["first person"],
    },
    "player_perspective=third person": {
        "ADJ_PERS": ["third person"],
    },
    "player_perspective=side view": {
        "ADJ_PERS": ["side view"],
    },

}

templates = {
    ("name", 'available_on_steam'): [
        (("NP_GAME", "-NOUN"),
         "NP_GAME_1 is not available on -NOUN_2 ."), 
        (("NP_GAME", "+NOUN"),
         "NP_GAME_1 is available on +NOUN_2 ."), 
    ],
    ('available_on_steam', 'name'): [
        (("-NOUN", "NP_GAME"),
         "there is a game that is not available on -NOUN_1 called NP_GAME_2 ."),
        (("+NOUN", "NP_GAME"),
         "there is a game that is available on +NOUN_1 called NP_GAME_2 ."), 
    ],

    ("name", 'developer'): [
        (("NP_GAME", "VP_GAME"),
         "NP_GAME_1 VP_GAME_2 ."), 
    ],
    ('developer', 'name'): [
        (("PP_GAME", "NP_GAME"),
         "there is a game PP_GAME_1 called NP_GAME_2 ."), 
    ],

    ("name", 'player_perspective'): [
        (("NP_GAME", "ADJ_PERS"),
         "NP_GAME_1 has a ADJ_PERS_2 perspective ."), 
    ],
    ('player_perspective', 'name'): [
        (("ADJ_PERS", 'NP_GAME'),
         "there is a game with a ADJ_PERS_1 perspective called NP_GAME_2 ."), 
    ],

    ("name", 'esrb'): [
        (("NP_GAME", "ADJ_GAME"),
         "NP_GAME_1 is ADJ_GAME_2 ."), 
    ],
    ('esrb', 'name'): [
        (("ADJ_GAME", "NP_GAME"),
         "for a game that is ADJ_GAME_1 try NP_GAME_2 ."), 
    ],

    ("name", 'exp_release_date'): [
        (("NP_GAME", "DATE"),
         "NP_GAME_1 is expected to be released on DATE_2 ."), 
    ],
    ('exp_release_date', 'name'): [
        (("DATE", "NP_GAME"),
         "there is a game with an expected release date of DATE_1 called NP_GAME_2 ."), 
    ],

    ("name", 'release_year'): [
        (("NP_GAME", "DATE"),
         "NP_GAME_1 was released in DATE_2 ."), 
    ],
    ('release_year', 'name'): [
        (("DATE", "NP_GAME"),
         "there is a DATE_1 game called NP_GAME_2 ."), 
    ],





    ("name", 'genres'): [
        (("NP_GAME", "GENRE_CONS_ADJ_GAME"),
         "NP_GAME_1 is a GENRE_CONS_ADJ_GAME_2 game ."), 
        (("NP_GAME", "GENRE_VOW_ADJ_GAME"),
         "NP_GAME_1 is an GENRE_VOW_ADJ_GAME_2 game ."), 
        (("NP_GAME", "GENRE_CONS_NOUN_GAME"),
         "NP_GAME_1 is a GENRE_CONS_NOUN_GAME_2 ."), 
        (("NP_GAME", "GENRE_VOW_NOUN_GAME"),
         "NP_GAME_1 is an GENRE_VOW_NOUN_GAME_2 ."), 
    ],

    ('genres', 'name'): [
        (("GENRE_CONS_ADJ_GAME", "NP_GAME"),
         "there is a GENRE_CONS_ADJ_GAME_1 game called NP_GAME_2 ."), 
        (("GENRE_VOW_ADJ_GAME", "NP_GAME"),
         "there is an GENRE_VOW_ADJ_GAME_1 game called NP_GAME_2 ."), 
        (("GENRE_CONS_NOUN_GAME", "NP_GAME"),
         "there is a GENRE_CONS_NOUN_GAME_1 called NP_GAME_2 ."), 
        (("GENRE_VOW_NOUN_GAME", "NP_GAME"),
         "there is an GENRE_VOW_NOUN_GAME_1 called NP_GAME_2 ."), 
    ],

    ("name", 'has_linux_release'): [
        (("NP_GAME", "-NOUN"),
         "NP_GAME_1 is not available on -NOUN_2 ."), 
        (("NP_GAME", "+NOUN"),
         "NP_GAME_1 is available on +NOUN_2 ."), 
    ],
    ('has_linux_release', 'name'): [
        (("-NOUN", 'NP_GAME'),
         "there is a game that is not available on -NOUN_1 called NP_GAME_2 ."), 
        (("+NOUN", 'NP_GAME'),
         "there is a game that is available on +NOUN_1 called NP_GAME_2 ."), 
    ],
    ("name", 'has_mac_release'): [
        (("NP_GAME", "-NOUN"),
         "NP_GAME_1 is not available on -NOUN_2 ."), 
        (("NP_GAME", "+NOUN"),
         "NP_GAME_1 is available on +NOUN_2 ."), 
    ],
    ('has_mac_release', 'name'): [
        (("-NOUN", 'NP_GAME'),
         "there is a game that is not available on -NOUN_1 called NP_GAME_2 ."), 
        (("+NOUN", 'NP_GAME'),
         "there is a game that is available on +NOUN_1 called NP_GAME_2 ."), 
    ],
    ("name", 'has_multiplayer'): [
        (("NP_GAME", "-ADJ_MODE"),
         "NP_GAME_1 only has a -ADJ_MODE_2 mode ."), 
        (("NP_GAME", "+ADJ_MODE"),
         "NP_GAME_1 has a +ADJ_MODE_2 mode ."), 
    ],

    ('has_multiplayer', 'name'): [
        (("-ADJ_MODE", 'NP_GAME'),
         "there is a game that only has a -ADJ_MODE_1 mode called NP_GAME_2 ."), 
        (("+ADJ_MODE", 'NP_GAME'),
         "there is a game that has a +ADJ_MODE_1 mode called NP_GAME_2 ."), 
    ],

 
    ("name", 'platforms'): [
        (("NP_GAME", "NOUN"),
         "NP_GAME_1 is available on NOUN_2 ."), 
    ],

    ('platforms', 'name'): [
        (('NOUN', "NP_GAME"),
         "there is a NOUN_1 game called NP_GAME_2 ."), 
    ],



    ('available_on_steam', 'player_perspective'): [
        (("-NOUN", "ADJ_PERS"),
         "it is not available on -NOUN_1 . it has a ADJ_PERS_2 perspective ."), 
        (("+NOUN", "ADJ_PERS"),
         "it is available on +NOUN_1 . it has a ADJ_PERS_2 perspective ."), 
    ],
    ('has_linux_release', 'player_perspective'): [
        (("-NOUN", "ADJ_PERS"),
         "it is not available on -NOUN_1 . it has a ADJ_PERS_2 perspective ."), 
        (("+NOUN", "ADJ_PERS"),
         "it is available on +NOUN_1 . it has a ADJ_PERS_2 perspective ."), 
    ],
    ('has_mac_release', 'player_perspective'): [
        (("-NOUN", "ADJ_PERS"),
         "it is not available on -NOUN_1 . it has a ADJ_PERS_2 perspective ."), 
        (("+NOUN", "ADJ_PERS"),
         "it is available on +NOUN_1 . it has a ADJ_PERS_2 perspective ."), 
    ],
    ('has_multiplayer', 'player_perspective'): [
        (("+ADJ_MODE", "ADJ_PERS"),
         "it has a +ADJ_MODE_1 mode and it has a ADJ_PERS_2 perspective ."), 
        (("-ADJ_MODE", "ADJ_PERS"),
         "it only has a -ADJ_MODE_1 mode and it has a ADJ_PERS_2 perspective ."), 
    ],
    ('player_perspective', 'player_perspective'): [
        (("ADJ_PERS", "ADJ_PERS"),
           "it has a ADJ_PERS_1 perspective . it also has a ADJ_PERS_2 perspective ."), 
    ],
    ('player_perspective', 'has_multiplayer'): [
        (("ADJ_PERS", "+ADJ_MODE"),
         "it has a ADJ_PERS_1 perspective and it has a +ADJ_MODE_2 mode ."), 
        (("ADJ_PERS", "-ADJ_MODE"),
         "it has a ADJ_PERS_1 perspective and it only has a -ADJ_MODE_2 mode ."), 
    ],



    ('player_perspective', 'available_on_steam'): [
        (("ADJ_PERS", "-NOUN"),
         "it has a ADJ_PERS_1 perspective . it is not available on -NOUN_2 ."), 
        (("ADJ_PERS", "+NOUN"),
         "it has a ADJ_PERS_1 perspective . it is available on +NOUN_2 ."), 
    ],
    ('player_perspective', 'has_linux_release'): [
        (("ADJ_PERS", "-NOUN"),
         "it has a ADJ_PERS_1 perspective . it is not available on -NOUN_2 ."), 
        (("ADJ_PERS", "+NOUN"),
         "it has a ADJ_PERS_1 perspective . it is available on +NOUN_2 ."), 
    ],
    ('player_perspective', 'has_mac_release'): [
        (("ADJ_PERS", "-NOUN"),
         "it has a ADJ_PERS_1 perspective . it is not available on -NOUN_2 ."), 
        (("ADJ_PERS", "+NOUN"),
         "it has a ADJ_PERS_1 perspective . it is available on +NOUN_2 ."), 
    ],






    ('available_on_steam', 'has_multiplayer'): [
        (("-NOUN", "+ADJ_MODE"),
         "it is not available on -NOUN_1 but it does have a +ADJ_MODE_2 mode ."), 
        (("+NOUN", "+ADJ_MODE"),
         "it is available on +NOUN_1 and it has a +ADJ_MODE_2 mode ."), 
        (("-NOUN", "-ADJ_MODE"),
         "it is not available on -NOUN_1 and it only has a -ADJ_MODE_2 mode ."), 
        (("+NOUN", "-ADJ_MODE"),
         "it is available on +NOUN_1 but it only has a -ADJ_MODE_2 mode ."), 

    ],

    ("has_multiplayer", 'available_on_steam'): [
        (("+ADJ_MODE", "-NOUN"),
         "it does have a +ADJ_MODE_1 mode but it is not available on -NOUN_2 ."), 
        (("+ADJ_MODE", "+NOUN"),
         "it has a +ADJ_MODE_1 mode and it is available on +NOUN_2 ."), 
        (("-ADJ_MODE", "-NOUN"),
         "it only has a -ADJ_MODE_1 mode and it is not available on -NOUN_2 ."), 
        (("-ADJ_MODE", "+NOUN"),
         "it only has a -ADJ_MODE_1 mode but it is available on +NOUN_2 ."), 
#
    ],
    ('developer', 'player_perspective'): [
        (("PP_GAME", "ADJ_PERS"),
         "it is a game PP_GAME_1 that has a ADJ_PERS_2 perspective .",),
    ],
    ('player_perspective', 'developer'): [
        (("ADJ_PERS", "PP_GAME"),
         "it has a ADJ_PERS_1 perspective . it is PP_GAME_2 ."), 
    ],




    ('developer', 'has_multiplayer'): [
        (("PP_GAME", "+ADJ_MODE"),
         "it is a game PP_GAME_1 that has a +ADJ_MODE_2 mode .",),
        (("PP_GAME", "-ADJ_MODE"),
         "it is a game PP_GAME_1 that only has a -ADJ_MODE_2 mode .",),
    ],

    ('developer', 'platforms'): [
        (("PP_GAME", "NOUN"),
         "it is a game PP_GAME_1 that is available on NOUN_2 .",),
    ],
    ('platforms', 'developer'): [
        (("NOUN", "PP_GAME"),
         "it is a game available on NOUN_1 PP_GAME_2 .",),
    ],
    ('platforms', 'player_perspective'): [
        (("NOUN", "ADJ_PERS"),
         "it is available on NOUN_1 and it has a ADJ_PERS_2 perspective .",),
    ],
    ('esrb', 'player_perspective'): [
        (("ADJ_GAME", "ADJ_PERS"),
         "it is a ADJ_GAME_1 game and it has a ADJ_PERS_2 perspective .",),
    ],
    ('player_perspective', 'esrb'): [
        (("ADJ_PERS", "ADJ_GAME"),
         "it is a ADJ_PERS_1 , ADJ_GAME_2 game .",),
    ],


    ('exp_release_date', 'player_perspective'): [
        (("DATE", "ADJ_PERS"),
         "it has an expected release date of DATE_1 and it has a ADJ_PERS_2 perspective .",),
    ],

    ('release_year', 'player_perspective'): [
        (("DATE", "ADJ_PERS"),
         "it was released in DATE_1 and it has a ADJ_PERS_2 perspective .",),
    ],

    ('player_perspective', "exp_release_date"): [
        (("ADJ_PERS", "DATE"),
         "it has a ADJ_PERS_1 perspective and it has an expected release date of DATE_2 .",),
    ],

    ('player_perspective', "release_year"): [
        (("ADJ_PERS", "DATE"),
         "it has a ADJ_PERS_1 perspective and it was released in DATE_2 .",),
    ],



    ('player_perspective', 'platforms'): [
        (("ADJ_PERS", "NOUN"),
         "it has a ADJ_PERS_1 perspective and is available on NOUN_2 .",),
    ],




    ('has_multiplayer', 'developer'): [
        (("+ADJ_MODE", "PP_GAME"),
         "it is a game that has a +ADJ_MODE_1 mode PP_GAME_2 .",),
        (("-ADJ_MODE", "PP_GAME"),
         "it is a game that only has a -ADJ_MODE_1 mode PP_GAME_2 .",),
    ],

    ('has_multiplayer', 'esrb'): [

        (("+ADJ_MODE", "ADJ_GAME"),
         "it is a game that has a +ADJ_MODE_1 mode that is ADJ_GAME_2 .",),
        (("-ADJ_MODE", "ADJ_GAME"),
         "it is a game that only has a -ADJ_MODE_1 mode that is ADJ_GAME_2 .",),
    ],

    ('esrb', "platforms"): [
        (("ADJ_GAME", "NOUN"), 
         "it is ADJ_GAME_1 and is available on NOUN_2 ."),
    ],

    ("platforms", "esrb"): [
        (("NOUN", "ADJ_GAME"), 
         "it is available on NOUN_1 and is ADJ_GAME_2 ."),
    ],



    ('esrb', "has_multiplayer"): [
        (("ADJ_GAME", "ADJ_GAME"), 
         "it is a ADJ_GAME_1 , ADJ_GAME_2 game ."),
    ],
    ('exp_release_date', 'platforms'): [
        (("DATE", "NOUN"),
         "it is expected to be released on DATE_1 . it will be available on NOUN_2 ."),
    ],
    ('release_year', 'platforms'): [
        (("DATE", "NOUN"),
         "it was released in DATE_1 . it is available on NOUN_2 ."),
    ],

    ('platforms', 'exp_release_date'): [
        (("NOUN", "DATE"),
         "it will be available on NOUN_1 . it is expected to be released on DATE_2 ."),
    ],
    ('platforms', 'release_year'): [
        (("NOUN", "DATE"),
         "it is available on NOUN_1 . it was released in DATE_2 ."),
    ],

    ('exp_release_date', 'has_multiplayer'): [
        (("DATE", "+ADJ_MODE"),
         "it is expected to be released on DATE_1 . it will have a +ADJ_MODE_2 mode ."),
        (("DATE", "-ADJ_MODE"),
         "it is expected to be released on DATE_1 . it will only have a -ADJ_MODE_2 mode ."),
    ],
    ('release_year', 'has_multiplayer'): [
        (("DATE", "+ADJ_MODE"),
         "it was released in DATE_1 . it has a +ADJ_MODE_2 mode ."),
        (("DATE", "-ADJ_MODE"),
         "it was released in DATE_1 . it only has a -ADJ_MODE_2 mode ."),
    ],


    ('has_multiplayer', 'exp_release_date'): [

        (("+ADJ_MODE", "DATE"),
         "it is a game that has a +ADJ_MODE_1 mode with an expected release date of DATE_2 .",),
        (("-ADJ_MODE", "DATE"),
         "it is a game that only has a -ADJ_MODE_1 mode with an expected release date of DATE_2 .",),
    ],
    ('has_multiplayer', 'release_year'): [

        (("+ADJ_MODE", "DATE"),
         "it has a +ADJ_MODE_1 mode and it was released in DATE_2 .",),
        (("-ADJ_MODE", "DATE"),
         "it only has a -ADJ_MODE_1 mode and it was released in DATE_2 .",),
    ],


    ('has_multiplayer', 'genres'): [

        (("ADJ_GAME", "GENRE_CONS_ADJ_GAME"), 
         "it is a ADJ_GAME_1 GENRE_CONS_ADJ_GAME_2 game ."),
        (("ADJ_GAME", "GENRE_VOW_ADJ_GAME"), 
         "it is a ADJ_GAME_1 GENRE_VOW_ADJ_GAME_2 game ."),
        (("ADJ_GAME", "GENRE_CONS_NOUN_GAME"), 
         "it is a ADJ_GAME_1 GENRE_CONS_NOUN_GAME_2 ."),
        (("ADJ_GAME", "GENRE_VOW_NOUN_GAME"), 
         "it is a ADJ_GAME_1 GENRE_VOW_NOUN_GAME_2 ."),
 
    ],
    ('genres', 'player_perspective'): [
        (("GENRE_CONS_ADJ_GAME", "ADJ_PERS"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game with a ADJ_PERS_2 perspective ."),
        (("GENRE_VOW_ADJ_GAME", "ADJ_PERS"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game with a ADJ_PERS_2 perspective ."),
        (("GENRE_CONS_NOUN_GAME", "ADJ_PERS"), 
         "it is a GENRE_CONS_NOUN_GAME_1 with a ADJ_PERS_2 perspective ."),
        (("GENRE_VOW_NOUN_GAME", "ADJ_PERS"), 
         "it is an GENRE_VOW_NOUN_GAME_1 with a ADJ_PERS_2 perspective ."),
    ],
    ('player_perspective', 'genres'): [
        (("ADJ_PERS", "GENRE_CONS_ADJ_GAME"), 
         "it is a ADJ_PERS_1 , GENRE_CONS_ADJ_GAME_2 game ."),
        (("ADJ_PERS", "GENRE_VOW_ADJ_GAME"), 
         "it is a ADJ_PERS_1 , GENRE_VOW_ADJ_GAME_2 game ."),
        (("ADJ_PERS", "GENRE_CONS_NOUN_GAME"), 
         "it is a ADJ_PERS_1 , GENRE_CONS_NOUN_GAME_2 ."),
        (("ADJ_PERS", "GENRE_VOW_NOUN_GAME"), 
         "it is a ADJ_PERS_1 , GENRE_VOW_NOUN_GAME_2 ."),
    ],


    ('genres', 'platforms'): [
        (("GENRE_CONS_ADJ_GAME", "NOUN"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game available on NOUN_2 ."),
        (("GENRE_VOW_ADJ_GAME", "NOUN"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game available on NOUN_2 ."),
        (("GENRE_CONS_NOUN_GAME", "NOUN"), 
         "it is a GENRE_CONS_NOUN_GAME_1 available on NOUN_2 ."),
        (("GENRE_VOW_NOUN_GAME", "NOUN"), 
         "it is an GENRE_VOW_NOUN_GAME_1 available on NOUN_2 ."),
    ],
    ('platforms', 'genres'): [
        (("NOUN", "GENRE_CONS_ADJ_GAME"), 
         "it is available on NOUN_1 . it is a GENRE_CONS_ADJ_GAME_2 game ."),
        (("NOUN", "GENRE_VOW_ADJ_GAME"), 
         "it is available on NOUN_1 . it is an GENRE_VOW_ADJ_GAME_2 game ."),
        (("NOUN", "GENRE_CONS_NOUN_GAME"), 
         "it is available on NOUN_1 . it is a GENRE_CONS_NOUN_GAME_2 ."),
        (("NOUN", "GENRE_VOW_NOUN_GAME"), 
         "it is available on NOUN_1 . it is an GENRE_VOW_NOUN_GAME_2 ."),
    ],


    ('genres', 'has_multiplayer'): [

        (("GENRE_CONS_ADJ_GAME", "+ADJ_MODE"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game with a +ADJ_MODE_2 mode ."),
        (("GENRE_CONS_ADJ_GAME", "-ADJ_MODE"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game with a -ADJ_MODE_2 mode only ."),
        (("GENRE_VOW_ADJ_GAME", "+ADJ_MODE"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game with a +ADJ_MODE_2 mode ."),
        (("GENRE_VOW_ADJ_GAME", "-ADJ_MODE"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game with a -ADJ_MODE_2 mode only ."),
        (("GENRE_CONS_NOUN_GAME", "+ADJ_MODE"), 
         "it is a GENRE_CONS_NOUN_GAME_1 with a +ADJ_MODE_2 mode ."),
        (("GENRE_CONS_NOUN_GAME", "-ADJ_MODE"), 
         "it is a GENRE_CONS_NOUN_GAME_1 with a -ADJ_MODE_2 mode only ."),
        (("GENRE_VOW_NOUN_GAME", "+ADJ_MODE"), 
         "it is an GENRE_VOW_NOUN_GAME_1 with a +ADJ_MODE_2 mode ."),
        (("GENRE_VOW_NOUN_GAME", "-ADJ_MODE"), 
         "it is an GENRE_VOW_NOUN_GAME_1 with a -ADJ_MODE_2 mode only ."),


    ],
    ("has_linux_release", "has_multiplayer"): [
        (("+NOUN", "+ADJ_MODE"),
         "it is available on +NOUN_1 and it has a +ADJ_MODE_2 mode ."),
        (("+NOUN", "-ADJ_MODE"),
         "it is available on +NOUN_1 but it only has a -ADJ_MODE_2 mode ."),
        (("-NOUN", "-ADJ_MODE"),
         "it is not available on -NOUN_1 and it only has a -ADJ_MODE_2 mode ."),
        (("-NOUN", "+ADJ_MODE"),
         "it is not available on -NOUN_1 but it does have a +ADJ_MODE_2 mode ."),
    ],
    ("has_multiplayer", "has_linux_release"): [
        (("+ADJ_MODE", "+NOUN"),
         "it has a +ADJ_MODE_1 mode and it is available on +NOUN_2 ."),
        (("-ADJ_MODE", "+NOUN"),
         "it only has a -ADJ_MODE_1 mode but it is available on +NOUN_2 ."),
        (("-ADJ_MODE", "-NOUN"),
         "it only has a -ADJ_MODE_1 mode and it is not available on -NOUN_2 ."),
        (("+ADJ_MODE", "-NOUN"),
         "it has a +ADJ_MODE_1 mode but it is not available on -NOUN_2 ."),
    ],
    ("has_multiplayer", "has_mac_release"): [
        (("+ADJ_MODE", "+NOUN"),
         "it has a +ADJ_MODE_1 mode and it is available on +NOUN_2 ."),
        (("-ADJ_MODE", "+NOUN"),
         "it only has a -ADJ_MODE_1 mode but it is available on +NOUN_2 ."),
        (("-ADJ_MODE", "-NOUN"),
         "it only has a -ADJ_MODE_1 mode and it is not available on -NOUN_2 ."),
        (("+ADJ_MODE", "-NOUN"),
         "it has a +ADJ_MODE_1 mode but it is not available on -NOUN_2 ."),
    ],
    ("has_multiplayer", "platforms"): [
        (("+ADJ_MODE", "NOUN"),
         "it has a +ADJ_MODE_1 mode and it is available on NOUN_2 ."),
        (("-ADJ_MODE", "NOUN"),
         "it only has a -ADJ_MODE_1 mode but it is available on NOUN_2 ."),
    ],
    ("platforms", "has_multiplayer"): [
        (("NOUN", "+ADJ_MODE"),
         "it is available on NOUN_1 and it has a +ADJ_MODE_2 mode ."),
        (("NOUN", "-ADJ_MODE"),
         "it is available on NOUN_1 but it only has a -ADJ_MODE_2 mode ."),
    ],





    ("has_mac_release", "has_multiplayer"): [
        (("+NOUN", "+ADJ_MODE"),
         "it is available on +NOUN_1 and it has a +ADJ_MODE_2 mode ."),
        (("+NOUN", "-ADJ_MODE"),
         "it is available on +NOUN_1 but it only has a -ADJ_MODE_2 mode ."),
        (("-NOUN", "-ADJ_MODE"),
         "it is not available on -NOUN_1 and it only has a -ADJ_MODE_2 mode ."),
        (("-NOUN", "+ADJ_MODE"),
         "it is not available on -NOUN_1 but it does have a +ADJ_MODE_2 mode ."),
    ],

 
     

    ("has_linux_release", "has_mac_release"): [
         (("+NOUN", "+NOUN"), 
         "it is available on both +NOUN_1 and +NOUN_2 .",),
         (("+NOUN", "-NOUN"), 
         "it is available on +NOUN_1 but not -NOUN_2 .",),
         (("-NOUN", "+NOUN"), 
         "while it is not available on -NOUN_1 , it is available on +NOUN_2 .",),
         (("-NOUN", "-NOUN"), 
         "it is not available on -NOUN_1 or -NOUN_2 .",),

    ],
    ("has_mac_release", "has_linux_release"): [
         (("+NOUN", "+NOUN"), 
         "it is available on both +NOUN_1 and +NOUN_2 .",),
         (("+NOUN", "-NOUN"), 
         "it is available on +NOUN_1 but not -NOUN_2 .",),
         (("-NOUN", "+NOUN"), 
         "while it is not available on -NOUN_1 , it is available on +NOUN_2 .",),
         (("-NOUN", "-NOUN"), 
         "it is not available on -NOUN_1 or -NOUN_2 .",),

    ],

 
    

    ("available_on_steam", "has_mac_release"): [
         (("+NOUN", "+NOUN"), 
         "it is available on both +NOUN_1 and +NOUN_2 .",),
         (("+NOUN", "-NOUN"), 
         "it is available on +NOUN_1 but not -NOUN_2 .",),
         (("-NOUN", "+NOUN"), 
         "while it is not available on -NOUN_1 , it is available on +NOUN_2 .",),
         (("-NOUN", "-NOUN"), 
         "it is not available on -NOUN_1 or -NOUN_2 .",),

    ],
    ("has_mac_release", "available_on_steam"): [
         (("+NOUN", "+NOUN"), 
         "it is available on both +NOUN_1 and +NOUN_2 .",),
         (("+NOUN", "-NOUN"), 
         "it is available on +NOUN_1 but not -NOUN_2 .",),
         (("-NOUN", "+NOUN"), 
         "while it is not available on -NOUN_1 , it is available on +NOUN_2 .",),
         (("-NOUN", "-NOUN"), 
         "it is not available on -NOUN_1 but not -NOUN_2 .",),

    ],

    ("exp_release_date", "has_mac_release"): [
         (("DATE", "VPF_GAME"), 
         "it is expected to be released on DATE_1 . it VPF_GAME_2 .",),

    ],
    ("has_mac_release", "exp_release_date"): [
#        (("VPF_GAME", "DATE"),
#         "it VPF_GAME_1 and it has an expected release date of DATE_2."),
        (("VPF_GAME", "DATE"),
         "it VPF_GAME_1 . it has an expected release date of DATE_2 ."),

    ],
    ("esrb", "has_mac_release"): [
          (("ADJ_GAME", "ADJP_GAME"), 
         "it is a ADJ_GAME_1 game ADJP_GAME_2 .",),
  
    ],
    ("has_mac_release", "esrb"): [
        (("ADJP_GAME", "ADJP_GAME"),
         "it is ADJP_GAME_1 . it is ADJP_GAME_2 ."),  
    ],
    ("has_mac_release", "developer"): [
        (("ADJP_GAME", "VP_GAME"),
         "it is ADJP_GAME_1 and it VP_GAME_2 .",)
    ],
    ("developer", "has_mac_release"): [
     (("VP_GAME", "ADJP_GAME"),
         "it VP_GAME_1 and ADJP_GAME_2 .",),
     (("VP_GAME", "ADJP_GAME"),
         "it VP_GAME_1 and it is ADJP_GAME_2 .",),

    ],
    ("has_mac_release", "genres"): [
        (("ADJP_GAME", "GENRE_VOW_NOUN_GAME"), 
         "it is ADJP_GAME_1 . it is an GENRE_VOW_NOUN_GAME_2 .",),
        (("ADJP_GAME", "GENRE_CONS_NOUN_GAME"), 
         "it is ADJP_GAME_1 . it is a GENRE_CONS_NOUN_GAME_2 .",),

        (("ADJP_GAME", "GENRE_VOW_ADJ_GAME"), 
         "it is ADJP_GAME_1 . it is an GENRE_VOW_ADJ_GAME_2 game .",),
        (("ADJP_GAME", "GENRE_CONS_ADJ_GAME"), 
         "it is ADJP_GAME_1 . it is a GENRE_CONS_ADJ_GAME_2 game .",),
    ],
    ("genres", "has_mac_release"): [
#        (("GENRE_CONS_ADJ_GAME", "ADJP_GAME"), 
#         "it is a GENRE_CONS_ADJ_GAME_1 game ADJP_GAME_2 .",),
#        (("GENRE_VOW_ADJ_GAME", "ADJP_GAME"), 
#         "it is an GENRE_VOW_ADJ_GAME_1 game ADJP_GAME_2 .",),
        (("GENRE_CONS_ADJ_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game . it is ADJP_GAME_2 .",),
        (("GENRE_VOW_ADJ_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game . it is ADJP_GAME_2 .",),

#        (("GENRE_CONS_NOUN_GAME", "ADJP_GAME"), 
#         "it is a GENRE_CONS_NOUN_GAME_1 ADJP_GAME_2 .",),
#        (("GENRE_VOW_NOUN_GAME", "ADJP_GAME"), 
#         "it is an GENRE_VOW_NOUN_GAME_1 ADJP_GAME_2 .",),
        (("GENRE_CONS_NOUN_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_NOUN_GAME_1 . it is ADJP_GAME_2 .",),
        (("GENRE_VOW_NOUN_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_NOUN_GAME_1 . it is ADJP_GAME_2 .",),

    ],


















    ("available_on_steam", "has_linux_release"): [
         (("+NOUN", "+NOUN"), 
         "it is available on both +NOUN_1 and +NOUN_2 .",),
         (("+NOUN", "-NOUN"), 
         "it is available on +NOUN_1 but not -NOUN_2 .",),
         (("-NOUN", "+NOUN"), 
         "while it is not available on -NOUN_1 , it is available on +NOUN_2 .",),
         (("-NOUN", "-NOUN"), 
         "it is not available on -NOUN_1 or -NOUN_2 .",),

    ],
    ("has_linux_release", "available_on_steam"): [
         (("+NOUN", "+NOUN"), 
         "it is available on both +NOUN_1 and +NOUN_2 .",),
         (("+NOUN", "-NOUN"), 
         "it is available on +NOUN_1 but not -NOUN_2 .",),
         (("-NOUN", "+NOUN"), 
         "while it is not available on -NOUN_1 , it is available on +NOUN_2 .",),
         (("-NOUN", "-NOUN"), 
         "it is not available on -NOUN_1 but not -NOUN_2 .",),

    ],
    ("release_year", "has_linux_release"): [
         (("DATE", "VPP_GAME"), 
         "it is was released in DATE_1 . it VPP_GAME_2 .",),

    ],
    ("release_year", "has_mac_release"): [
         (("DATE", "VPP_GAME"), 
         "it is was released in DATE_1 . it VPP_GAME_2 .",),

    ],


    ("exp_release_date", "has_linux_release"): [
         (("DATE", "VPF_GAME"), 
         "it is expected to be released on DATE_1 . it VPF_GAME_2 .",),

    ],
    ("has_linux_release", "exp_release_date"): [
#        (("VPF_GAME", "DATE"),
#         "it VPF_GAME_1 and it has an expected release date of DATE_2."),
        (("VPF_GAME", "DATE"),
         "it VPF_GAME_1 . it has an expected release date of DATE_2 ."),

    ],
    ("has_linux_release", "release_year"): [
#        (("VPF_GAME", "DATE"),
#         "it VPF_GAME_1 and it has an expected release date of DATE_2."),
        (("VPP_GAME", "DATE"),
         "it VPP_GAME_1 . it was released in DATE_2 ."),

    ],
    ("has_mac_release", "release_year"): [
#        (("VPF_GAME", "DATE"),
#         "it VPF_GAME_1 and it has an expected release date of DATE_2."),
        (("VPP_GAME", "DATE"),
         "it VPP_GAME_1 . it was released in DATE_2 ."),

    ],


    ("esrb", "has_linux_release"): [
          (("ADJ_GAME", "ADJP_GAME"), 
         "it is a ADJ_GAME_1 game ADJP_GAME_2 .",),
  
    ],
    ("has_linux_release", "esrb"): [
        (("ADJP_GAME", "ADJP_GAME"),
         "it is ADJP_GAME_1 . it is ADJP_GAME_2 ."),  
    ],
    ("has_linux_release", "developer"): [
        (("ADJP_GAME", "VP_GAME"),
         "it is ADJP_GAME_1 and it VP_GAME_2 .",)
    ],
    ("developer", "has_linux_release"): [
     (("VP_GAME", "ADJP_GAME"),
         "it VP_GAME_1 and ADJP_GAME_2 .",),
     (("VP_GAME", "ADJP_GAME"),
         "it VP_GAME_1 and it is ADJP_GAME_2 .",),

    ],
    ("has_linux_release", "genres"): [
        (("ADJP_GAME", "GENRE_VOW_NOUN_GAME"), 
         "it is ADJP_GAME_1 . it is an GENRE_VOW_NOUN_GAME_2 .",),
        (("ADJP_GAME", "GENRE_CONS_NOUN_GAME"), 
         "it is ADJP_GAME_1 . it is a GENRE_CONS_NOUN_GAME_2 .",),

        (("ADJP_GAME", "GENRE_VOW_ADJ_GAME"), 
         "it is ADJP_GAME_1 . it is an GENRE_VOW_ADJ_GAME_2 game .",),
        (("ADJP_GAME", "GENRE_CONS_ADJ_GAME"), 
         "it is ADJP_GAME_1 . it is a GENRE_CONS_ADJ_GAME_2 game .",),
    ],
    ("genres", "has_linux_release"): [
#        (("GENRE_CONS_ADJ_GAME", "ADJP_GAME"), 
#         "it is a GENRE_CONS_ADJ_GAME_1 game ADJP_GAME_2 .",),
#        (("GENRE_VOW_ADJ_GAME", "ADJP_GAME"), 
#         "it is an GENRE_VOW_ADJ_GAME_1 game ADJP_GAME_2 .",),
        (("GENRE_CONS_ADJ_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game . it is ADJP_GAME_2 .",),
        (("GENRE_VOW_ADJ_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game . it is ADJP_GAME_2 .",),

#        (("GENRE_CONS_NOUN_GAME", "ADJP_GAME"), 
#         "it is a GENRE_CONS_NOUN_GAME_1 ADJP_GAME_2 .",),
#        (("GENRE_VOW_NOUN_GAME", "ADJP_GAME"), 
#         "it is an GENRE_VOW_NOUN_GAME_1 ADJP_GAME_2 .",),
        (("GENRE_CONS_NOUN_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_NOUN_GAME_1 . it is ADJP_GAME_2 .",),
        (("GENRE_VOW_NOUN_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_NOUN_GAME_1 . it is ADJP_GAME_2 .",),

    ],






    ("exp_release_date", "developer"): [
         (("DATE", "VP_GAME"), 
         "it is expected to be released on DATE_1 . it VP_GAME_2 .",),
         (("DATE", "VP_GAME"), 
         "it is expected to be released on DATE_1 and it VP_GAME_2 .",),

    ],
    ("release_year", "developer"): [
         (("DATE", "NOUN"), 
         "it was released in DATE_1 by NOUN_2 .",),

    ],

    ("exp_release_date", "available_on_steam"): [
         (("DATE", "VPF_GAME"), 
         "it is expected to be released on DATE_1 . it VPF_GAME_2 .",),

    ],
    ("release_year", "available_on_steam"): [
         (("DATE", "VPP_GAME"), 
         "it was released in DATE_1 . it VPP_GAME_2 .",),
    ],

    ("exp_release_date", "genres"): [
         (("DATE", "GENRE_CONS_ADJ_GAME"), 
         "it is expected to be released on DATE_1 . it is a GENRE_CONS_ADJ_GAME_2 game .",),
        (("DATE", "GENRE_VOW_ADJ_GAME"), 
         "it is expected to be released on DATE_1 . it is an GENRE_VOW_ADJ_GAME_2 game .",),

         (("DATE", "GENRE_CONS_NOUN_GAME"), 
          "it is expected to be released on DATE_1 . it is a GENRE_CONS_NOUN_GAME_2 .",),
        (("DATE", "GENRE_VOW_NOUN_GAME"), 
         "it is expected to be released on DATE_1 . it is an GENRE_VOW_NOUN_GAME_2 game .",),


    ],

    ("release_year", "genres"): [
         (("DATE", "GENRE_CONS_ADJ_GAME"), 
         "it was released in DATE_1 . it is a GENRE_CONS_ADJ_GAME_2 game .",),
        (("DATE", "GENRE_VOW_ADJ_GAME"), 
         "it was released in DATE_1 . it is an GENRE_VOW_ADJ_GAME_2 game .",),

         (("DATE", "GENRE_CONS_NOUN_GAME"), 
          "it was released in DATE_1 . it is a GENRE_CONS_NOUN_GAME_2 .",),
        (("DATE", "GENRE_VOW_NOUN_GAME"), 
         "it was released in DATE_1 . it is an GENRE_VOW_NOUN_GAME_2 game .",),


    ],

    ("exp_release_date", "esrb"): [
         (("DATE", "ADJ_GAME"), 
         "it has an expected released date of DATE_1 and will be ADJ_GAME_2 .",),
         (("DATE", "ADJ_GAME"), 
         "it will be released on DATE_1 and will be ADJ_GAME_2 .",),

    ],
    ("release_year", "esrb"): [
         (("DATE", "ADJ_GAME"), 
         "it was released in DATE_1 and is ADJ_GAME_2 .",),
         (("DATE", "ADJ_GAME"), 
         "it was released in DATE_1 . it is ADJ_GAME_2 .",),


    ],

    ("developer", "exp_release_date"): [
         (("VP_GAME", "DATE"), 
         "it VP_GAME_1 . it is expected to be released on DATE_2 .",),

         (("VP_GAME", "DATE"), 
         "it VP_GAME_1 and it is expected to be released on DATE_2 .",),


    ],
    ("developer", "release_year"): [
         (("VP_GAME", "DATE"), 
         "it VP_GAME_1 . it was released in DATE_2 .",),
         (("VP_GAME", "DATE"), 
         "it VP_GAME_1 and it was released in DATE_2 .",),


    ],

    ("available_on_steam", "exp_release_date"): [
        (("VPF_GAME", "DATE"),
         "it VPF_GAME_1 and it has an expected release date of DATE_2 ."),
        (("VPF_GAME", "DATE"),
         "it VPF_GAME_1 . it has an expected release date of DATE_2 ."),

    ],
    ("available_on_steam", "release_year"): [
        (("VPP_GAME", "DATE"),
         "it VPP_GAME_1 and it was released in DATE_2 ."),
        (("VPP_GAME", "DATE"),
         "it VPP_GAME_1 . it was released in DATE_2 ."),

    ],


    ("genres", "release_year"): [
         (("GENRE_CONS_ADJ_GAME", "DATE"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game that was released in DATE_2 .",),
        (("GENRE_VOW_ADJ_GAME", "DATE"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game that was released in DATE_2 .",),
        (("GENRE_CONS_ADJ_GAME", "DATE"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game . it was released in DATE_2 .",),
        (("GENRE_VOW_ADJ_GAME", "DATE"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game . it was released in DATE_2 .",),

         (("GENRE_CONS_NOUN_GAME", "DATE"), 
         "it is a GENRE_CONS_NOUN_GAME_1 that was released in DATE_2 .",),
        (("GENRE_VOW_NOUN_GAME", "DATE"), 
         "it is an GENRE_VOW_NOUN_GAME_1 that was released in DATE_2 .",),
        (("GENRE_CONS_NOUN_GAME", "DATE"), 
         "it is a GENRE_CONS_NOUN_GAME_1 . it was released in DATE_2 .",),
        (("GENRE_VOW_NOUN_GAME", "DATE"), 
         "it is an GENRE_VOW_NOUN_GAME_1 . it was released in DATE_2 .",),





    ],

    ("genres", "exp_release_date"): [
         (("GENRE_CONS_ADJ_GAME", "DATE"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game that has an expected release date of DATE_2 .",),
        (("GENRE_VOW_ADJ_GAME", "DATE"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game that has an expected release date of DATE_2 .",),
        (("GENRE_CONS_ADJ_GAME", "DATE"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game . it is expected to be released on DATE_2 .",),
        (("GENRE_VOW_ADJ_GAME", "DATE"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game . it is expected to be released on DATE_2 .",),

         (("GENRE_CONS_NOUN_GAME", "DATE"), 
         "it is a GENRE_CONS_NOUN_GAME_1 that has an expected release date of DATE_2 .",),
        (("GENRE_VOW_NOUN_GAME", "DATE"), 
         "it is an GENRE_VOW_NOUN_GAME_1 that has an expected release date of DATE_2 .",),
        (("GENRE_CONS_NOUN_GAME", "DATE"), 
         "it is a GENRE_CONS_NOUN_GAME_1 . it is expected to be released on DATE_2 .",),
        (("GENRE_VOW_NOUN_GAME", "DATE"), 
         "it is an GENRE_VOW_NOUN_GAME_1 . it is expected to be released on DATE_2 .",),





    ],
    ("esrb", "exp_release_date"): [
         (("ADJ_GAME", "DATE"), 
         "it is a ADJ_GAME_1 game that is expected to be released on DATE_2 .",),
         (("ADJ_GAME", "DATE"), 
         "it is a ADJ_GAME_1 game with an expected release date of DATE_2 .",),

    ],
    ("esrb", "release_year"): [
         (("ADJ_GAME", "DATE"), 
         "it is a ADJ_GAME_1 game that was released in DATE_2 .",),
         (("ADJ_GAME", "DATE"), 
         "it is a ADJ_GAME_1 game from DATE_2 .",),

    ],




    ("esrb", "developer"): [
         (("ADJ_GAME", "ADJP_GAME"), 
         "it is a ADJ_GAME_1 game ADJP_GAME_2 .",),
 
    ],
    ("esrb", "available_on_steam"): [
          (("ADJ_GAME", "ADJP_GAME"), 
         "it is a ADJ_GAME_1 game ADJP_GAME_2 .",),
  
    ],
    ("esrb", "genres"): [
        (("ADJ_GAME", "GENRE_VOW_NOUN_GAME"), 
         "it is a ADJ_GAME_1 GENRE_VOW_NOUN_GAME_2 .",),
        (("ADJ_GAME", "GENRE_CONS_NOUN_GAME"), 
         "it is a ADJ_GAME_1 GENRE_CONS_NOUN_GAME_2 .",),

        (("ADJ_GAME", "GENRE_VOW_ADJ_GAME"), 
         "it is a ADJ_GAME_1 GENRE_VOW_ADJ_GAME_2 game .",),
        (("ADJ_GAME", "GENRE_CONS_ADJ_GAME"), 
         "it is a ADJ_GAME_1 GENRE_CONS_ADJ_GAME_2 game .",),


    ],
    ("developer", "esrb"): [
         (("ADJP_GAME", "ADJP_GAME"),
         "it is ADJP_GAME_1 and ADJP_GAME_2 ."),

 
    ],
    ("available_on_steam", "esrb"): [
        (("ADJP_GAME", "ADJP_GAME"),
         "it is ADJP_GAME_1 and ADJP_GAME_2 ."),

    
  
    ],
    ("genres", "esrb"): [
         (("GENRE_CONS_ADJ_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game ADJP_GAME_2 .",),
        (("GENRE_VOW_ADJ_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game ADJP_GAME_2 .",),
        (("GENRE_CONS_ADJ_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game . it is ADJP_GAME_2 .",),
        (("GENRE_VOW_ADJ_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game . it is ADJP_GAME_2 .",),

        (("GENRE_CONS_NOUN_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_NOUN_GAME_1 ADJP_GAME_2 .",),
        (("GENRE_VOW_NOUN_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_NOUN_GAME_1 ADJP_GAME_2 .",),
        (("GENRE_CONS_NOUN_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_NOUN_GAME_1 . it is ADJP_GAME_2 .",),
        (("GENRE_VOW_NOUN_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_NOUN_GAME_1 . it is ADJP_GAME_2 .",),

    ],


    ("genres", "developer"): [
         (("GENRE_CONS_ADJ_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game ADJP_GAME_2 .",),
        (("GENRE_VOW_ADJ_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game ADJP_GAME_2 .",),
        (("GENRE_CONS_ADJ_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game . it is ADJP_GAME_2 .",),
        (("GENRE_VOW_ADJ_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game . it is ADJP_GAME_2 .",),

        (("GENRE_CONS_NOUN_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_NOUN_GAME_1 ADJP_GAME_2 .",),
        (("GENRE_VOW_NOUN_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_NOUN_GAME_1 ADJP_GAME_2 .",),
        (("GENRE_CONS_NOUN_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_NOUN_GAME_1 . it is ADJP_GAME_2 .",),
        (("GENRE_VOW_NOUN_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_NOUN_GAME_1 . it is ADJP_GAME_2 .",),
    ],
    ("available_on_steam", "developer"): [
        (("ADJP_GAME", "VP_GAME"),
         "it is ADJP_GAME_1 and it VP_GAME_2 .",)
    ], 
    ("developer", "genres"): [
        (("ADJP_GAME", "GENRE_VOW_NOUN_GAME"), 
         "it is ADJP_GAME_1 and it is an GENRE_VOW_NOUN_GAME_2 .",),
        (("ADJP_GAME", "GENRE_CONS_NOUN_GAME"), 
         "it is ADJP_GAME_1 and it is a GENRE_CONS_NOUN_GAME_2 .",),

        (("ADJP_GAME", "GENRE_VOW_ADJ_GAME"), 
         "it is ADJP_GAME_1 and it is an GENRE_VOW_ADJ_GAME_2 game .",),
        (("ADJP_GAME", "GENRE_CONS_ADJ_GAME"), 
         "it is ADJP_GAME_1 and it is a GENRE_CONS_ADJ_GAME_2 game .",),

    ],
    ("developer", "available_on_steam"): [
     (("VP_GAME", "ADJP_GAME"),
         "it VP_GAME_1 and ADJP_GAME_2 .",),
     (("VP_GAME", "ADJP_GAME"),
         "it VP_GAME_1 and it is ADJP_GAME_2 .",),

    ],

    ("available_on_steam", "platforms"): [

        (("+NOUN", "NOUN"), 
         "it is available on +NOUN_1 and NOUN_2 .",),
        (("-NOUN", "NOUN"), 
         "it is not available on -NOUN_1 but it is on NOUN_2 .",),

    ],

    ("platforms", "available_on_steam"): [

        (("NOUN", "+NOUN"), 
         "it is available on NOUN_1 and +NOUN_2 .",),
        (("NOUN", "-NOUN"), 
         "it is available on NOUN_1 but it is not on -NOUN_2 .",),

    ],


    ("has_linux_release", "platforms"): [
        (("+NOUN", "NOUN"), 
         "it is available on +NOUN_1 and NOUN_2 .",),
        (("-NOUN", "NOUN"), 
         "it is not available on -NOUN_1 but it is on NOUN_2 .",),
    ],

    ("platforms", "has_linux_release"): [
        (("NOUN", "+NOUN"), 
         "it is available on NOUN_1 and +NOUN_2 .",),
        (("NOUN", "-NOUN"), 
         "it is available on NOUN_1 but it is not on -NOUN_2 .",),
    ],
    ("platforms", "has_mac_release"): [
        (("NOUN", "+NOUN"), 
         "it is available on NOUN_1 and +NOUN_2 .",),
        (("NOUN", "-NOUN"), 
         "it is available on NOUN_1 but it is not on -NOUN_2 .",),
    ],
    ("platforms", "platforms"): [
        (("NOUN", "NOUN"), 
         "it is available on NOUN_1 and NOUN_2 .",),
    ],




    ("has_mac_release", "platforms"): [
        (("+NOUN", "NOUN"), 
         "it is available on +NOUN_1 and NOUN_2 .",),
        (("-NOUN", "NOUN"), 
         "it is not available on -NOUN_1 but it is on NOUN_2 .",),
    ],




    ("available_on_steam", "genres"): [
        (("ADJP_GAME", "GENRE_VOW_NOUN_GAME"), 
         "it is ADJP_GAME_1 and it is an GENRE_VOW_NOUN_GAME_2 .",),
        (("ADJP_GAME", "GENRE_CONS_NOUN_GAME"), 
         "it is ADJP_GAME_1 and it is a GENRE_CONS_NOUN_GAME_2 .",),

        (("ADJP_GAME", "GENRE_VOW_ADJ_GAME"), 
         "it is ADJP_GAME_1 and it is an GENRE_VOW_ADJ_GAME_2 game .",),
        (("ADJP_GAME", "GENRE_CONS_ADJ_GAME"), 
         "it is ADJP_GAME_1 and it is a GENRE_CONS_ADJ_GAME_2 game .",),
    ],
    ("genres", "available_on_steam"): [
        (("GENRE_CONS_ADJ_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game ADJP_GAME_2 .",),
        (("GENRE_VOW_ADJ_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game ADJP_GAME_2 .",),
        (("GENRE_CONS_ADJ_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 game . it is ADJP_GAME_2 .",),
        (("GENRE_VOW_ADJ_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 game . it is ADJP_GAME_2 .",),

        (("GENRE_CONS_NOUN_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_NOUN_GAME_1 ADJP_GAME_2 .",),
        (("GENRE_VOW_NOUN_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_NOUN_GAME_1 ADJP_GAME_2 .",),
        (("GENRE_CONS_NOUN_GAME", "ADJP_GAME"), 
         "it is a GENRE_CONS_NOUN_GAME_1 . it is ADJP_GAME_2 .",),
        (("GENRE_VOW_NOUN_GAME", "ADJP_GAME"), 
         "it is an GENRE_VOW_NOUN_GAME_1 . it is ADJP_GAME_2 .",),

    ],
    ("available_on_steam", "available_on_steam"): [

    ],
    ("genres", "genres"): [
        (("GENRE_CONS_ADJ_GAME", "GENRE_CONS_NOUN_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 GENRE_CONS_NOUN_GAME_2 .",),
        (("GENRE_VOW_ADJ_GAME", "GENRE_CONS_NOUN_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 GENRE_CONS_NOUN_GAME_2 .",),
        (("GENRE_VOW_ADJ_GAME", "GENRE_VOW_NOUN_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 GENRE_VOW_NOUN_GAME_2 .",),
        (("GENRE_CONS_ADJ_GAME", "GENRE_VOW_NOUN_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 GENRE_VOW_NOUN_GAME_2 .",),
#
#
#
#
        (("GENRE_CONS_ADJ_GAME", "GENRE_CONS_ADJ_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 and GENRE_CONS_ADJ_GAME_2 game .",),
        (("GENRE_CONS_ADJ_GAME", "GENRE_VOW_ADJ_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 and GENRE_VOW_ADJ_GAME_2 game .",),
        (("GENRE_VOW_ADJ_GAME", "GENRE_CONS_ADJ_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 and GENRE_CONS_ADJ_GAME_2 game .",),
        (("GENRE_VOW_ADJ_GAME", "GENRE_VOW_ADJ_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 and GENRE_VOW_ADJ_GAME_2 game .",),

        (("GENRE_CONS_ADJ_GAME", "GENRE_CONS_ADJ_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 GENRE_CONS_ADJ_GAME_2 game .",),
        (("GENRE_CONS_ADJ_GAME", "GENRE_VOW_ADJ_GAME"), 
         "it is a GENRE_CONS_ADJ_GAME_1 GENRE_VOW_ADJ_GAME_2 game .",),
        (("GENRE_VOW_ADJ_GAME", "GENRE_CONS_ADJ_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 GENRE_CONS_ADJ_GAME_2 game .",),
        (("GENRE_VOW_ADJ_GAME", "GENRE_VOW_ADJ_GAME"), 
         "it is an GENRE_VOW_ADJ_GAME_1 GENRE_VOW_ADJ_GAME_2 game .",),
 
         
        (("GENRE_CONS_NOUN_GAME", "GENRE_CONS_NOUN_GAME"), 
         "it is a GENRE_CONS_NOUN_GAME_1 as well as a GENRE_CONS_NOUN_GAME_2 .",),
        (("GENRE_VOW_NOUN_GAME", "GENRE_CONS_NOUN_GAME"), 
         "it is an GENRE_VOW_NOUN_GAME_1 as well as a GENRE_CONS_NOUN_GAME_2 .",),
        (("GENRE_VOW_NOUN_GAME", "GENRE_VOW_NOUN_GAME"), 
         "it is an GENRE_VOW_NOUN_GAME_1 as well as an GENRE_VOW_NOUN_GAME_2 .",),
        (("GENRE_CONS_NOUN_GAME", "GENRE_VOW_NOUN_GAME"), 
         "it is a GENRE_CONS_NOUN_GAME_1 as well as an GENRE_VOW_NOUN_GAME_2 .",),

        (("GENRE_CONS_NOUN_GAME", "GENRE_CONS_ADJ_GAME"), 
         "it is a GENRE_CONS_NOUN_GAME_1 as well as a GENRE_CONS_ADJ_GAME_2 game .",),
        (("GENRE_VOW_NOUN_GAME", "GENRE_CONS_ADJ_GAME"), 
         "it is an GENRE_VOW_NOUN_GAME_1 as well as a GENRE_CONS_ADJ_GAME_2 game .",),
        (("GENRE_VOW_NOUN_GAME", "GENRE_VOW_ADJ_GAME"), 
         "it is an GENRE_VOW_NOUN_GAME_1 as well as an GENRE_VOW_ADJ_GAME_2 game .",),
        (("GENRE_CONS_NOUN_GAME", "GENRE_VOW_ADJ_GAME"), 
         "it is a GENRE_CONS_NOUN_GAME_1 as well as an GENRE_VOW_ADJ_GAME_2 game .",),

    ],
}

invalid_transitions = set([
    ('exp_release_date', 'release_year'),
    ('release_year', 'exp_release_date'),
    ("esrb", "esrb"),
    ("has_linux_release", "has_linux_release"),
    ("has_mac_release", "has_mac_release"),
    ("available_on_steam", "available_on_steam"),
    ("has_multiplayer", "has_multiplayer"),
])

