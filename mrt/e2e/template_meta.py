from mrt.e2e.meta import LEXICON, SLOTS


slot_lexical_items = {

    "area=riverside": {
        "NP": ['the riverside area', 'the riverside'],
        "ADJP": ['a riverside area', 'a riverside'],
        "ADJP\\ADJP": ['riverside area', 'riverside'],
        "IN": ['in the riverside area',],
    },

    "area=city centre": {
        "NP": ['the city centre'],
        "ADJP": ['a city centre'],
        "ADJP\\ADJP": ['city centre'],
        "IN": ['in the city centre'],
    },



    'customer_rating=high': {
        'NP': ['a high rating', 'a high customer rating', 'high ratings', 
               'high customer ratings'],
        'NP+': ['a high rating', 'a high customer rating', 'high ratings', 
                'high customer ratings'],
        'ADJP': ['a highly rated'],
    },
    'customer_rating=low': {
        'NP': ['a low rating', 'a low customer rating', 'low ratings', 
               'low customer ratings'],
        'NP-': ['a low rating', 'a low customer rating', 'low ratings', 
                'low customer ratings'],
        'ADJP': ['a low rated'],
    },

    'customer_rating=1 out of 5': {
        'NP': ['a 1 out of 5 star rating', 'a 1 star rating'],
        'NP-': ['a 1 out of 5 star rating', 'a 1 star rating'],
        "ADJP": ['a 1 out of 5 star rated', 'a 1 star', 'a 1 star rated'],
        "ADJP-": ['a 1 out of 5 star rated', 'a 1 star', 'a 1 star rated'],
    },
    'customer_rating=3 out of 5': {
        'NP': ['a 3 out of 5 star rating', 'a 3 star rating'],
        'ADJP': ['a 3 out of 5 star rated', 'a 3 star', 'a 3 star rated'],
    },
    'customer_rating=5 out of 5': {
        'NP': ['a 5 out of 5 star rating', 'a 5 star rating'],
        'NP+': ['a 5 out of 5 star rating', 'a 5 star rating'],
        "ADJP": ['a 5 out of 5 star rated', 'a 5 star', 'a 5 star rated'],
        "ADJP+": ['a 5 out of 5 star rated', 'a 5 star', 'a 5 star rated'],
    },

    'customer_rating=average': {
        'NP': ['an average rating', 'an average customer rating', 'average ratings', 'average customer ratings'],
        'ADJP': ['an average rated', 'an average'],
    },


    "eat_type=coffee shop": {
        "ADJP\\NP": ["coffee shop"],
        "NP": ['a coffee shop'],
        "NP_OTHERREST": ['a coffee shop'],
         
    },
   "eat_type=pub": {
        "ADJP\\NP": ["pub"],
        "NP": ['a pub'],
        "NP_OTHERREST": ['a pub'],
    },
   "eat_type=restaurant": {
        "ADJP\\NP": ["restaurant"],
        "NP": ['a restaurant'],
        "NP_REST": ['restaurant'],
    },

    "family_friendly=no": {
        "VP\\ADJP": ["non family friendly", 'non kid friendly'],
        "VP\\ADJP-": ["non family friendly", 'non kid friendly'],
        "ADJP\\ADJP": ['non family friendly'],
        "ADJP\\ADJP-": ['non family friendly'],
        "ADJP": ['a non family friendly', 'a non kid friendly'],
    },
    "family_friendly=yes": {
        "VP\\ADJP": ["family friendly", 'kid friendly'],
        "VP\\ADJP+": ["family friendly", 'kid friendly'],
        "ADJP\\ADJP": ["family friendly", 'kid friendly'],
        "ADJP\\ADJP+": ["family friendly", 'kid friendly'],
        "ADJP": ["a family friendly", 'a kid friendly'],
    },
    
    "food=Chinese": {
        "NP": ["chinese food"],
    },
    "food=English": {
        "NP": ["english food"],
    },
    "food=Fast food": {
        "NP": ["fast food"],
    },
    "food=French": {
        "NP": ["french food"],
    },

    "food=Indian": {
        "NP": ["indian food"],
    },

    "food=Italian": {
        "NP": ["italian food"],
    },

    "food=Japanese": {
        "NP": ["japanese food"],
    },

    "name=Alimentum": {
        "NP": ["alimentum"],
    },
    "name=Aromi": {
        "NP": ["aromi"],
    },
    "name=Bibimbap House": {
        "NP": ["bibimbap house"],
    },
    "name=Blue Spice": {
        "NP": ["blue spice"],
    },

    'price_range=cheap': {
        'NP': ['cheap prices', 'a cheap price range'], 
        'ADJP': ['a cheap', 'a low priced'],
        'ADJ': ['cheap', 'low priced'],
    },
    'price_range=high': {
        'NP': ['high prices', 'a high price range'], 
        'ADJP': ['an expensive', 'a high priced'],
        'ADJ': ['expensive', 'high priced'],
    },
    'price_range=less than £20': {
        "IN": ['in the less than £ 20 price range',
               'in the under £ 20 price range'], 
        "ADJP_REST": ['an under £ 20',]
    },
    'price_range=moderate': {
        'NP': ['moderate prices', 'a moderate price range'], 
        'ADJP': ['a moderately priced'],
        'ADJ': ['moderately priced'],
    },
    'price_range=more than £30': {

        "IN": ['in the more than £ 30 price range',
               'in the over £ 30 price range'], 
        "ADJP_REST": ['an over £ 30',]
    },
    'price_range=£20-25': {
        "IN": ['in the £ 20 - 25 price range',],
               #'in the between £ 20 - 25 price range'],
        "ADJP_REST": ['a £ 20 - 25',]
    },

}

for name in LEXICON['name']:
    slot_lexical_items[f'name={name}'] = {
        'NP': [name.lower()],
    }

for near in LEXICON['near']:
    slot_lexical_items[f'near={near}'] = {
        'NP': [near.lower()]
    }

templates = {
    ('area', 'customer_rating'): [
        (("NP", "NP"),
         "located in NP_1 , it has NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 establishment with NP_2 ."),
    ],

    ('area', "eat_type"): [
        (("ADJP", "ADJP\\NP"),
         "it is ADJP_1 ADJP\\NP_2 ."),
        (("ADJP", "ADJP\\NP"),
         "it is ADJP_1 located ADJP\\NP_2 ."),
    ],
    ('area', "family_friendly"): [
        (("NP", "VP\\ADJP-"),
         "it is located in NP_1 but VP\\ADJP-_2 ."),
        (("ADJP", "VP\\ADJP"),
         "it is ADJP_1 establishment that is VP\\ADJP_2 ."),

        (("NP", "VP\\ADJP+"),
         "it is located in NP_1 and is VP\\ADJP+_2 ."),
    ],

    ('area', 'food'): [
        (("NP", "NP"),
         "it is located in NP_1 and serves NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 establishment that serves NP_2 ."),
    ],

    ("area", "name"): [
        (('NP','NP'),
         "it is located in NP_1 and called NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 establishment called NP_2 ."),
    ],
    ("area", "near"): [
        (('NP','NP'),
         "it is located in NP_1 near NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 establishment near NP_2 ."),
    ],
    ('area', 'price_range'): [
        (("NP", "NP"),
         "located in NP_1 , it has NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 establishment with NP_2 ."),

        (("NP", "IN"),
         "located in NP_1 , it offers food IN_2 ."),
        (("ADJP", "IN"),
         "it is ADJP_1 establishment IN_2 ."),
    ],
    ('customer_rating', "area"): [
#        (("NP", "NP"),
#         "located in NP_1 , it has NP_2 ."),
        (("ADJP", "ADJP\\ADJP"),
         "it is ADJP_1 ADJP\\ADJP_2 establishment ."),
    ],

    ('customer_rating', "eat_type"): [
#        (("NP", "NP"),
#         "located in NP_1 , it has NP_2 ."),
        (("ADJP", "ADJP\\NP"),
         "it is ADJP_1 ADJP\\NP_2 ."),
    ],
    ('customer_rating', "family_friendly"): [
#        (("NP", "NP"),
#         "located in NP_1 , it has NP_2 ."),
        (("ADJP", "ADJP\\ADJP"),
         "it is ADJP_1 , ADJP\\ADJP_2 establishment ."),
        (("ADJP", "VP\\ADJP"),
         "it is ADJP_1 establishment that is VP\\ADJP_2 ."),
#        (("ADJP-", "ADJP\\ADJP-"),
#         "it is ADJP-_1 and ADJP\\ADJP-_2 establishment ."),
#        (("ADJP+", "ADJP\\ADJP+"),
#         "it is ADJP+_1 and ADJP\\ADJP+_2 establishment ."),
#        (("ADJP-", "ADJP\\ADJP+"),
#         "it is ADJP-_1 but ADJP\\ADJP+_2 establishment ."),
#        (("ADJP+", "ADJP\\ADJP-"),
#         "it is ADJP+_1 but ADJP\\ADJP-_2 establishment ."),
    ],

    ('customer_rating', "food"): [
        (("ADJP", "NP"),
         "it is ADJP_1 establishment serving NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 establishment that serves NP_2 ."),

    ],
    ('customer_rating', "name"): [
        (("ADJP", "NP"),
         "it is ADJP_1 establishment called NP_2 ."),

    ],
    ('customer_rating', "near"): [
        (("ADJP", "NP"),
         "it is ADJP_1 establishment near NP_2 ."),

    ],
    ('customer_rating', "price_range"): [
        (("ADJP", "NP"),
         "it is ADJP_1 establishment with NP_2 ."),

        (("ADJP", "IN"),
         "it is ADJP_1 establishment IN_2 ."),
    ],
    ("eat_type", "area"): [
        #(("ADJP", "ADJP\\NP"),
        # "it is ADJP_1 ADJP\\NP_2 ."),
        (("NP", "NP"),
         "it is NP_1 located in NP_2 ."),
    ],
    ("eat_type", "customer_rating"): [
        #(("ADJP", "ADJP\\NP"),
        # "it is ADJP_1 ADJP\\NP_2 ."),
        (("NP", "NP"),
         "it is NP_1 with NP_2 ."),
    ],

    ('eat_type', "family_friendly"): [
        (("NP", "VP\\ADJP"),
         "it is NP_1 that is VP\\ADJP_2 ."),
    ],
    ('eat_type', "food"): [
        (("NP", "NP"),
         "it is NP_1 serving NP_2 ."),
        (("NP", "NP"),
         "it is NP_1 that offers NP_2 ."),
    ],
    ("eat_type", "name"): [
        (("NP", "NP"),
         "it is NP_1 called NP_2 ."),
    ],
    ("eat_type", "near"): [
        (("NP", "NP"),
         "it is NP_1 near NP_2 ."),
    ],

    ('eat_type', "price_range"): [
        (("NP", "NP"),
         "it is NP_1 with NP_2 ."),

        (("NP", "IN"),
         "it is NP_1 IN_2 ."),
    ],
    ("family_friendly", "area"): [
        (("ADJP", "IN"),
         "it is ADJP_1 establishment IN_2 ."),
    ],
    ('family_friendly', 'customer_rating'): [
        (("ADJP", "NP"),
         "it is ADJP_1 establishment with NP_2 ."),
    ],

    ('family_friendly', "eat_type"): [
        (("ADJP", "ADJP\\NP"),
         "it is ADJP_1 ADJP\\NP_2 ."),
    ], 
    ("family_friendly", "food"): [
        (("ADJP", "NP"),
         "it is ADJP_1 establishment serving NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 establishment offering NP_2 ."),
    ],
    ("family_friendly", "name"): [
        (("ADJP", "NP"),
         "it is ADJP_1 place called NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 eatery called NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 establishment called NP_2 ."),
    ],
    ("family_friendly", "near"): [
        (("ADJP", "NP"),
         "it is ADJP_1 place near NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 eatery near NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 establishment near NP_2 ."),
    ],
    ("family_friendly", "price_range"): [
        (("ADJP", "NP"),
         "it is ADJP_1 place with NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 eatery with NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 establishment with NP_2 ."),
        (("ADJP", "IN"),
         "it is ADJP_1 place IN_2 ."),
        (("ADJP", "IN"),
         "it is ADJP_1 eatery IN_2 ."),
        (("ADJP", "IN"),
         "it is ADJP_1 establishment IN_2 ."),
    ],
    ("food", "area"): [
        (("NP", "IN"),
         "it serves NP_1 IN_2 ."),

    ],

    ("food", "customer_rating"): [
        (("NP", "NP"),
         "it serves NP_1 with NP_2 ."),
        (("NP", "NP-"),
         "it serves NP_1 but it has NP-_2 ."),
        (("NP", "NP+"),
         "it serves NP_1 and it has NP+_2 ."),
    ],

    ("food", "eat_type"): [
        (("NP", "NP_REST"),
         "it is a NP_1 NP_REST_2 ."),
        (("NP", "NP_OTHERREST"),
         "it serves NP_1 and is also NP_OTHERREST_2 ."),
    ],

    ("food", "family_friendly"): [
        (("NP", "ADJP"),
         "it serves NP_1 in ADJP_2 setting ."),
    ],

    ("food", "name"): [
        (("NP", "NP"),
         "it offers NP_1 and is called NP_2 ."),
    ],
    ("food", "near"): [
        (("NP", "NP"),
         "it offers NP_1 near NP_2 ."),
        (("NP", "NP"),
         "it serves NP_1 near NP_2 ."),
    ],


    ("food", "price_range"): [
        (("NP", "NP"),
         "it serves NP_1 with NP_2 ."),
        (("NP", "IN"),
         "it offers NP_1 IN_2 ."),
    ],


    ("name", "area"): [
        (("NP", "NP"),
         "NP_1 serves NP_2 ."),
        (("NP", "IN"),
         "NP_1 is located IN_2 ."),
    ],

    ("name", "customer_rating"): [
        (("NP", "NP"),
         "NP_1 has NP_2 ."),
    ],


    ("name", "eat_type"): [
        (("NP", "NP"),
         "NP_1 is NP_2 ."),
    ],

    ("name", "family_friendly"): [
        (("NP", "ADJP"),
         "NP_1 is ADJP_2 establishment ."),
        (("NP", "ADJP"),
         "NP_1 is ADJP_2 eatery ."),
        (("NP", "ADJP"),
         "NP_1 is ADJP_2 location ."),
    ],

    ("name", "food"): [
        (("NP", "NP"),
         "NP_1 offers NP_2 ."),
        (("NP", "NP"),
         "NP_1 serves NP_2 ."),
    ],

    ("name", "near"): [
        (("NP", "NP"),
         "NP_1 is located near NP_2 ."),
        (("NP", "NP"),
         "NP_1 is near NP_2 ."),
    ],

    ("name", "price_range"): [
        (("NP", "NP"),
         "NP_1 has NP_2 ."),
        (("NP", "IN"),
         "NP_1 is IN_2 ."),
    ],

    ("near", "area"): [
        (("NP", "NP"),
         "it is near NP_1 , serving NP_2 ."),
        (("NP", "IN"),
         "it is near NP_1 IN_2 ."),
    ],

    ("near", "customer_rating"): [
        (("NP", "NP"),
         "it is near NP_1 and has NP_2 ."),
    ],

    ("near", "eat_type"): [
        (("NP", "NP"),
         "located near NP_1 , it is NP_2 ."),
    ],

    ("near", "family_friendly"): [
        (("NP", "ADJP"),
         "located near NP_1 , it is ADJP_2 establishment ."),
        (("NP", "ADJP"),
         "located near NP_1 , it is ADJP_2 eatery ."),
        (("NP", "ADJP"),
         "located near NP_1 , it is ADJP_2 location ."),
    ],

    ("near", "food"): [
        (("NP", "NP"),
         "located near NP_1 , it offers NP_2 ."),
        (("NP", "NP"),
         "located near NP_1 , it serves NP_2 ."),
    ],

    ("near", "name"): [
        (("NP", "NP"),
         "close to NP_1 is NP_2 ."),
        (("NP", "NP"),
         "near to NP_1 is NP_2 ."),
    ],

    ("near", "price_range"): [
        (("NP", "NP"),
         "it is near NP_1 and it has NP_2 ."),
        (("NP", "IN"),
         "it is near NP_1 and it is IN_2 ."),
    ],

    ('price_range', "area"): [
        (("IN", "NP"),
         "it offers food IN_1 and it is located in NP_2 ."),
        (("NP", "NP"),
         "it has NP_1 and is located in NP_2 ."),
#        (("ADJP", "ADJP\\ADJP"),
#         "it is ADJP_1 ADJP\\ADJP_2 establishment ."),
    ],

    ('price_range', "eat_type"): [
        (("ADJP", "ADJP\\NP"),
         "it is ADJP_1 ADJP\\NP_2 ."),
        (("ADJP_REST", "ADJP\\NP"),
         "it is ADJP_REST_1 ADJP\\NP_2 ."),
       # (("NP", "NP"),
       #  "it offers food with NP_1 and is NP_2 ."),
    ],
    ('price_range', "family_friendly"): [
#        (("NP", "NP"),
#         "located in NP_1 , it has NP_2 ."),
        (("ADJP", "ADJP\\ADJP"),
         "it is ADJP_1 , ADJP\\ADJP_2 establishment ."),
        (("ADJP", "VP\\ADJP"),
         "it is ADJP_1 establishment that is VP\\ADJP_2 ."),
        (("ADJP_REST", "ADJP\\ADJP"),
         "it is ADJP_REST_1 , ADJP\\ADJP_2 establishment ."),
        (("ADJP_REST", "VP\\ADJP"),
         "it is ADJP_REST_1 establishment that is VP\\ADJP_2 ."),

    ],

    ('price_range', "food"): [
        (("ADJ", "NP"),
         "it serves ADJ_1 NP_2 ."),
        (("ADJP", "NP"),
         "it is ADJP_1 establishment that serves NP_2 ."),
        (("ADJP_REST", "NP"),
         "it is ADJP_REST_1 establishment that serves NP_2 ."),

    ],
    ('price_range', "name"): [
        (("NP", "NP"),
         "it has NP_1 and is called NP_2 ."),
        (("ADJP_REST", "NP"),
         "it is ADJP_REST_1 eatery called NP_2 ."),

    ],
    ('price_range', "near"): [
        (("NP", "NP"),
         "it has NP_1 and is near NP_2 ."),
        (("ADJP_REST", "NP"),
         "it is ADJP_REST_1 eatery near NP_2 ."),

    ],
    ('price_range', 'customer_rating'): [
        (("IN", "NP"),
         "it is IN_1 and has NP_2 ."),

        (("NP", "NP"),
         "it has NP_1 and NP_2 ."),


       # (("ADJP", "IN"),
       #  "it is ADJP_1 establishment IN_2 ."),
    ],


}

invalid_transitions = set([
    (slot, slot)
    for slot in SLOTS
])
