from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
import random
import re
from warnings import warn

from mrt.e2e.meta import (
    NAME_RE, NEAR_RE, NAMES_TOKENIZED, NEARS_TOKENIZED, LEXICON,
)


def correct_utterance(text):

    if text.endswith("'"):
        if text[-2] not in ['.', '?', '!']:
            text = text[:-1] + ".'"
    elif text.endswith('"'):
        if text[-2] not in ['.', '?', '!']:
            text = text[:-1] + '."'
    elif text[-1] not in ['.', '?', '!']:
        text = text + '.'

    text = re.sub(r'One family friendly venue is The Wrestlers.  It is averagely rated.  Near Café Rouge is a Japanese,  family friendly place called The Golden Curry.', 'One family friendly venue is the Wrestlers. It is averagely rated. Near Café Rouge is a Japanese, family friendly place called the Wrestlers.', text)
    text = re.sub(r'The Wrestlers is an average, family friendly venue.  Near Café Rouge is a Japanese,  family friendly place called The Golden Curry.', 'The Wrestlers is an average, family friendly venue.  Near Café Rouge is a Japanese,  family friendly place called The Wrestlers.', text)
    text = re.sub(r"Sicilia,It", r"Sicilia. It", text)
    text = re.sub(r"Punter Is", r"Punter is", text)
    text = re.sub(r" Yes ", r" yes ", text)
    text = re.sub(r" Is ", r" is ", text)
    text = re.sub(r" In ", r" in ", text)
    text = re.sub(r" i ", r" I ", text)
    text = re.sub(r"euro", r"Euro", text)
    text = re.sub(r"a price ranch of", r"a price range of", text)
    text = re.sub(r"family , We", r"family. We", text)

    text = re.sub(r"ONE STAR", r"one star", text)
    text = re.sub(r"Travellers Rest Beefeaters", r"Travellers Rest Beefeater", text)
    text = re.sub(r"WIld", r"Wild", text)
    text = re.sub(r" Area", r" area", text)
    text = re.sub(r"food. IT", r"food. It", text)
    text = re.sub(r" IT ", r" it ", text)
    text = re.sub(r" Entertainment", r" entertainment", text)
    text = re.sub(r"Wrestlers Is", r"Wrestlers is", text)
    text = re.sub(r"shop-The Punter-is", r"shop - The Punter - is", text)
    text = re.sub(r"\s+", r" ", text)
    text = re.sub(r"in the city centre\. Golden Palace", r"in the city centre. The Golden Palace", text)
    text = re.sub(r"but It has", r"but it has", text)
    text = re.sub(r"Star, Inexpensive", r"star, inexpensive", text)
    text = re.sub(r"Join Us", r"Join us", text)
    text = re.sub(r"Punter In which", r"Punter in which", text)
    text = re.sub(r", In riverside, Yes", r", in riverside, yes", text)
    text = re.sub(r"HIGH", r"high", text)
    text = re.sub(r" Poor", r" poor", text)
    text = re.sub(r" North", r" north", text)

    text = re.sub(r" South", r" south", text)
    text = re.sub(r"range, It", r"range. It", text)
    text = re.sub(r"Eagle That", r"Eagle that", text)
    text = re.sub(r"King, It", r"King. It", text)
    text = re.sub(r"pricing, It", r"pricing. It", text)
    text = re.sub(r"near burger king", r"near Burger King", text)
    text = re.sub(r"King, It's", r"King. It's", text)
    text = re.sub(r"; (\w)", lambda x: "; " + x.groups(0)[0].lower(), text)
    text = re.sub(r"city ,It's", r"city. It's", text)
    text = re.sub(r'near\. The Por', r'near the Por', text)
    text = re.sub(r'5and ', r'5 and ', text)
    text = re.sub(r'a Café Brazil is 5out', r'a Café Brazil is 5 out', text)
    text = re.sub(r'food, It has', r'food. It has', text)
    text = re.sub(r' Family', r' family', text)
    text = re.sub(r' Ambient', r' ambient', text)
    text = re.sub(r'is located in the city centre It is family',
                  r'is located in the city centre. It is family', text)
    text = re.sub(r"food Ina", r"food in a", text)
    text = re.sub(r"30 euro", r"30 Euro", text)
    text = re.sub(r"food .price", r"food. Price", text)
    text = re.sub(r" 5\. Cricketers", r" 5. The Cricketers", text)
    text = re.sub(r"Aromis", r"Aromi", text)
    text = re.sub(r"-Friendly", r"-friendly", text)
    text = re.sub(r"shop- with", r"shop - with", text)
    text = re.sub(r" Fast", r" fast", text)
    text = re.sub(r" You", r" you", text)
    text = re.sub(r" Welcome", r" welcome", text)
    text = re.sub(r"average - rated", r"average-rated", text)
    text = re.sub(r"an Average", r"an average", text)
    text = re.sub(r"with a high customer rating It ", 
                  r"with a high customer rating. It ", text)
    text = re.sub("([^.!?]) The", r"\1 the", text)
    text = re.sub(r"Crown Plaza Hotel", r"Crowne Plaza Hotel", text)
    text = re.sub(r"Cocum Café", r"Cocum café", text)
    text = re.sub(r"friendly Café", r"friendly café", text)
    text = re.sub(r" a Café", r" a café", text)
    text = re.sub(r" the Café", r" the café", text)
    text = re.sub(r" the café Sicilia", r" the Café Sicilia", text)
    text = re.sub(r" the café Brazil", r" the Café Brazil", text)
    text = re.sub(r" a café Brazil", r" a Café Brazil", text)
    text = re.sub(r"is not family friendly, It",
                  r"is not family friendly. It", text)
    text = re.sub(r"English food, Its high",
                  r"English food. Its high", text)
    text = re.sub(r"Brown Cambridge", r"Browns Cambridge", text)
    text = re.sub(r"English food\. it", r"English food. It", text)
    text = re.sub(r"English food It", r"English food. It", text)
    text = re.sub(r"Aromi Is a ", r"Aromi is a ", text)
    text = re.sub(r" Food", r" food", text)
    text = re.sub(r" River", r" river", text)
    text = re.sub(r"This Café", r"This café", text)
    text = re.sub(r"good Café", r"good café", text)
    text = re.sub(r" Kid", r" kid", text)
    text = re.sub(r" Shop", r" shop", text)
    text = re.sub(r" High", r" high", text)
    text = re.sub(r" Range", r" range", text)
    text = re.sub(r" Located", r" located", text)
    text = re.sub(r" Cheap", r" cheap", text)
    text = re.sub(r" Rate", r" rate", text)
    text = re.sub(r" City", r" city", text)
    text = re.sub(r" Centre", r" centre", text)
    text = re.sub(r" Center", r" center", text)
    text = re.sub(r"([^.]) Customer", r"\1 customer", text)
    text = re.sub(r" Rating", r" rating", text)
    text = re.sub(r" Friendly", r" friendly", text)

    text = re.sub(r"Chines ", r"Chinese ", text)
    text = re.sub(r"AVERAGE", r"average", text)
    text = re.sub(r"Riverside", r"riverside", text)
    text = re.sub(r"City center", r"city center", text)
    text = re.sub(r"shop providing Chinese food It is", 
                  r"shop providing Chinese food. It is", text)

    text = re.sub(r"5 out of 5\. city center", 
                  r"5 out of 5. City center", text)
    text = re.sub(r"kids Friendly", r"kids friendly", text)
    text = re.sub(r"In Riverside", r"In riverside", text)
    text = re.sub(r"in Riverside", r"in riverside", text)
    text = re.sub(r"\.,", r",", text)
    text = re.sub(r", \.", r",", text)
    text = re.sub(r"center\. of", r"center of", text)
    text = re.sub(r"5of5", r"5 of 5", text)
    text = re.sub(r"Rouge\.6", r"Rouge.", text)
    text = re.sub(r"25\.Yes", r"25. Yes", text)
    text = re.sub(r"of5", r"of 5", text)
    text = re.sub(r"\. ,", r",", text)
    text = re.sub(r"\.\.$", r".", text)
    text = re.sub(r"\. \.$", r".", text)
    text = re.sub(r"30\.£", r"30£", text)
    text = re.sub(r"L20", r"£20", text)
    text = re.sub(r'5star', '5 star', text)
    text = re.sub(r'1out', '1 out', text)
    text = re.sub(r'3out', '3 out', text)
    text = re.sub(r'3o', '30', text)
    text = re.sub(r",([^ ])", r", \1", text)
    text = re.sub(r" \. ", r". ", text)
    text = re.sub(r" \.$", r".", text)
    text = re.sub(r" , ", r", ", text)
    text = re.sub(r" -([^ ])", r"-\1", text)
    text = re.sub(r";([^ ])", r"; \1", text)
    text = re.sub(r"Inn. 's", r"Inn's", text)
    text = re.sub(r"£ ", r"£", text)
    text = re.sub(r"£20- £", r"£20-£", text)
    text = re.sub("([^ ])- a ", r"\1 - a ", text)
    text = re.sub("(\d) - (\d)", r"\1-\2", text)
    text = re.sub("(\d)- (\d)", r"\1-\2", text)
    text = re.sub("(\d) - £", r"\1-£", text)
    text = re.sub("([a-z])£", r"\1 £", text)
    text = re.sub(" - only", r"-only", text)
    text = re.sub("children- ", r"children-", text)
    text = re.sub("highly- ", r"highly-", text)
    text = re.sub("take- ", r"take-", text)
    text = re.sub("high- ", r"high-", text)
    text = re.sub(r" \.average", r". Average", text)
    text = re.sub(r" \.Price", r". Price", text)
    text = re.sub(r" \.children", r". Children", text)
    text = re.sub(r" \.The", r". The", text)
    text = re.sub(" :", r":", text)
    text = re.sub("NON - ", r"NON-", text)
    text = re.sub("non- ", r"non-", text)
    text = re.sub(" ,", r",", text)
    text = re.sub("area-", r"area -", text)
    text = re.sub("fun-", r"fun -", text)
    text = re.sub("over- expensive", r"over-expensive", text)
    text = re.sub("adult- ", r"adult-", text)
    text = re.sub("Family- ", r"Family-", text)
    text = re.sub("family- ", r"family-", text)
    text = re.sub("price - order", r"price-order", text)
    text = re.sub("Boat-", r"Boat -", text)
    text = re.sub("eatery- ", r"eatery - ", text)
    text = re.sub(" .Nice", r". Nice", text)
    text = re.sub(" .No", r". No", text)
    text = re.sub(" .customer", r". Customer", text)
    text = re.sub("average- rated", r"average-rated", text)
    text = re.sub("moderate- rated", r"moderate-rated", text)
    text = re.sub("moderate- priced", r"moderate-priced", text)
    text = re.sub(" ; ", r"; ", text)
    text = re.sub(r"\s*--\s*", " -- ", text)
    text = re.sub("-located near Café Sicilia-",
                  " - located near Café Sicilia - ", text)
    text = re.sub(r", The", ", the", text)
    text = re.sub(r"ranges, It", "ranges. It", text)
    text = re.sub(r" Child", " child", text)

    text = re.sub(r"\. (\w)", lambda x: ". " + x.groups(0)[0].upper(), text)
    text = re.sub(r"ratings...b", r"ratings... b", text)
    text = text[0].upper() + text[1:]

    return text

def extract_mr(mr_string):
    da = 'inform'
    da_args = mr_string
        
    mr = {"da": da, "slots": {}}
    for slot, vals in re.findall(r'([\w_ ]+)\[(.*?)\]', da_args):
        slot = re.sub(r'([a-z])([A-Z])', r'\1 \2', slot).lower().strip()
        slot = slot.replace(' ', '_')
        if slot in mr['slots']:
            mr["slots"][slot] += "|" + vals
        else:
            mr["slots"][slot] = vals

    for slot, val in mr['slots'].items():
        if "|" in val:
            mr['slots'][slot] = "|".join(sorted(set(val.split("|"))))
    return mr

def tokenize(text):
    tokens = []
    text = re.sub(r"5\. ", r"5 . ", text)
    text = re.sub(r"'(\d) out of 5'", r"` \1 out of 5 '", text) 
    text = re.sub(r"5located", r"5 located", text)
    text = re.sub(r"rating of 1\.", r"rating of 1 .", text)
    text = re.sub(r"10\. ", r"10 . ", text)
    text = re.sub(r"40\. ", r"40 . ", text)
    text = re.sub(r"1 out of 5\. ", r"1 out of 5 . ", text)
    text = re.sub(r"5 out of 5\. ", r"5 out of 5 . ", text)
    text = re.sub(r"3 out of 5\. ", r"3 out of 5 . ", text)
    text = re.sub(r"25\. ", r"25 . ", text)
    text = re.sub(r"30\. ", r"30 . ", text)
    text = re.sub(r"e30", r"e 30", text)
    text = re.sub(r"20£\.", r"20 £ .", text)
    text = re.sub(r"30£", r"30 £", text)
    text = re.sub(r"25£", r"25 £", text)
    text = re.sub(r"20£", r"20 £", text)
    text = re.sub(r"20\.", r"20 .", text)
    text = re.sub(r" e20", r" e 20", text)
    text = re.sub(r"-e25", r"-e 25", text)
    text = re.sub(r"25lb", r"25 lb", text)
    text = re.sub(r"20lb", r"20 lb", text)
    text = re.sub(r"(\w)\.\. ", r"\1 . . ", text)

    sentences = sent_tokenize(text)

    for i, sentence in enumerate(sentences, 1):
        sentence = re.sub(r'([^ ])-([^ ])', r'\1 - \2', sentence)
        sentence = re.sub(r' -([^ ])', r' - \1', sentence)
        sentence = re.sub(r'([^ ])- ', r'\1 - ', sentence)
        sentence = re.sub(r'£(\w)', r'£ \1', sentence)
        sentence = re.sub(r"'(\w+)'", r"` \1 '", sentence)
        sentence = re.sub(r"'(\w+ \w+)'", r"` \1 '", sentence)
        sentence = re.sub(r"'(\w+ \w+ \w+)'", r"` \1 '", sentence)
        sentence = re.sub("'(" + NAME_RE + ")'", r"` \1 '", sentence, flags=re.I)
        sentence = re.sub("'(" + NEAR_RE + ")'", r"` \1 '", sentence, flags=re.I)
        text = re.sub("'(\w+)'", r"` \1 '", text)
        tokens.extend(word_tokenize(sentence))
        if i < len(sentences):
            tokens.append('<sent>')
    return tokens

def _delex_tokens(tokens, pattern, placeholder):
    i = 0
    while i < len(tokens):
        s = max(i - len(pattern) + 1, 0)
        if [x.lower() for x in tokens[s:i+1]] == pattern:
            tokens = tokens[:s] + [placeholder] + tokens[i+1:]
            i = s + 1
        else:
            i += 1
    return tokens

def delexicalize_tokens(tokens, **kwargs):
    tokens = list(tokens)

    i = 0
    while i < len(tokens):
        if [x.lower() for x in tokens[i-5:i+1]] == ['indian', 'cuisine', 'by', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NAME'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-7:i+1]] == ['rainbow', 'vegetarian', 'café', 'is', 'near', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NAME'] + tokens[i+1:]
            i = i - 2

        if [x.lower() for x in tokens[i-4:i+1]] == ['served', 'in', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NAME'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-4:i+1]] == ['next', 'to', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-3:i+1]] == ['near', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-6:i+1]] == ['near', 'the', 'river', 'and', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-7:i+1]] == ['near', 'the', 'riverside', 'area', 'in', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2

        if [x.lower() for x in tokens[i-9:i+1]] == ['area', 'city', 'centre', 'for', 'kids', 'friendly', 'in', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-9:i+1]] == ['nearby', 'the', 'city', 'centre', 'and', 'the', 'restaurant', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-8:i+1]] == ['near', 'to', 'the', 'japanese', 'restaurant', ',', 'the', 'rice', 'boat',]:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-3:i+1]] == ['beside', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-4:i+1]] == ['near', 'of', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-4:i+1]] == ['near', 'to', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-3:i+1]] == ['by', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-4:i+1]] == ['close', 'to', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-5:i+1]] == ['for', 'the', 'restaurant', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2

        if [x.lower() for x in tokens[i-14:i+1]] == ['loch', 'fyne', 'is', 'english', 'food', 'customer', 'rating', '1', 'out', 'of', '5', 'in', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NEAR'] + tokens[i+1:]
            i = i - 2
        if [x.lower() for x in tokens[i-3:i+1]] == ['in', 'the', 'rice', 'boat']:
            tokens = tokens[:i-2] + ['NAME'] + tokens[i+1:]
            i = i - 2
        i += 1



    for _, patt in NAMES_TOKENIZED:
        tokens = _delex_tokens(tokens, patt, 'NAME')

    for _, patt in NEARS_TOKENIZED:
        tokens = _delex_tokens(tokens, patt, 'NEAR')


    for patt in [['travellers', 'rest', 'beefeaters',],
                 ['zizzis'],
                 ['punters'],
                 ['the', 'watermans'],
                ]:
        tokens = _delex_tokens(tokens, patt, 'NAME')

    return tokens

def detokenize(tokens):
    text = ' '.join(tokens)
    text = re.sub(r' <eos>', '', text)
    text = re.sub("<sent> (.)", lambda m: m.groups()[0].upper(), text)
    text = re.sub("20 £ .", "20£.", text)
    text = re.sub(' - ', '-', text)
    text = re.sub(' i ', ' I ', text)
    text = re.sub(' \?', '?', text)
    text = re.sub(' \!', '!', text)
    text = re.sub(' \.', '.', text)
    text = re.sub(' ,', ',', text)
    text = re.sub(" ''", '"', text)
    text = re.sub(" '", "'", text)
    text = re.sub("`` ", '"', text)
    text = re.sub("` ", "'", text)
    text = re.sub(" n't", "n't", text)
    text = re.sub(" 's", "'s", text)
    text = re.sub(" 'll", "'ll", text)
    text = re.sub(" 're", "'re", text)
    text = re.sub("£ ", "£", text)
    text = re.sub("-a ", " - a ", text)
    text = re.sub("-has ", " - has ", text)
    text = re.sub("-an ", " - an ", text)
    text = re.sub("-the ", " - the ", text)
    text = re.sub("-yes", " - yes", text)
    text = re.sub(" ;", ";", text)
    text = re.sub(" :", ":", text)
    text = re.sub("-(" + NAME_RE + ")-", r" - \1 - ", text, flags=re.I)
    text = re.sub("("+NAME_RE + ")-", r"\1 - ", text, flags=re.I)
    text = re.sub("-("+NAME_RE + ")", r" - \1", text, flags=re.I)
    text = re.sub("outlet-", "outlet - ", text)
    text = re.sub("-which", " - which", text)
    text = re.sub("-albeit", " - albeit", text)
    text = re.sub("-but", " - but", text)
    text = re.sub("-less", " - less", text)
    text = re.sub("-near", " - near", text)
    text = re.sub("range-(\w)", r"range - \1", text)
    text = re.sub("-just", " - just", text)
    text = re.sub("-with", " - with", text)
    text = re.sub("-and", " - and", text)
    text = re.sub("-if pricey-", " - if pricey - ", text)
    text = re.sub("-it", " - it", text)
    text = re.sub("eatery-", "eatery - ", text)
    text = re.sub("-not", " - not", text)
    text = re.sub("-i ", " - I ", text)
    text = re.sub("-located near", " - located near", text)
    text = re.sub("-is ", " - is ", text)
    text = re.sub("-then", " - then", text)
    text = re.sub("-there", " - there", text)
    text = re.sub("-though", " - though", text)
    text = re.sub("rating-", "rating - ", text)
    text = re.sub("rated-", "rated - ", text)
    text = re.sub("shop-high", "shop - high", text)
    text = re.sub("-typically", " - typically", text)
    text = re.sub("-- ", " -- ", text)
    text = re.sub("Rating: (\w)", lambda x: 'Rating: ' + x.groups(0)[0].upper(), text)
    text = re.sub('friday', 'Friday', text)
    text = re.sub('thai', 'Thai', text)
    text = re.sub('euro', 'Euro', text)
    text = re.sub('cambridge', 'Cambridge', text)
    text = re.sub(r"'the (.*?)'", r"'The \1'", text)
    text = re.sub(r'"the (.*?)"', r'"The \1"', text)
    text = re.sub(r"highly-(\d)", r"highly - \1", text)
    text = re.sub(r"british pounds", r"British Pounds", text)
    text = re.sub(r"meal-try", r"meal - try", text)
    text = re.sub(r"NAME-highly", r"NAME - highly", text)
    text = re.sub(r" luton", r" Luton", text)
    text = re.sub(r"-NAME", r" - NAME", text)

    text = text[0].upper() + text[1:]

    for name in LEXICON['name']:
        name = name.replace("The ", "")
        text = re.sub(name, name, text, flags=re.I)
    for near in LEXICON['near']:
        near = near.replace("The ", "")
        text = re.sub(near, near, text, flags=re.I)
    for food in ['Chinese', 'English', 'British', 'French',
                 'Indian', 'Italian', 'Japanese',]:
        text = re.sub(food, food, text, flags=re.I)

    return text

def tags2linear_mr(tags, delex=False, flip=False):
    if flip:
        mrseq = [t for i, t in enumerate(tags)
                 if tags[i-1:i] != [t]]
        mrseq = [x for x in mrseq if x != '0']
    else:
        mrseq = [x for x in tags if x != '0']
        mrseq = [t for i, t in enumerate(mrseq)
                 if mrseq[i-1:i] != [t]]

    if delex:
        for i, t in enumerate(mrseq):
            if t.startswith('name=') and not t.endswith('='):
                mrseq[i] = 'name=PLACEHOLDER'
            if t.startswith('near=') and not t.endswith('='):
                mrseq[i] = 'near=PLACEHOLDER'

    return mrseq

def tags2mr(tags, delex=False):
    linear_mr = tags2linear_mr(tags, delex)
    return linear_mr2mr(linear_mr)

def lexicalize_string(text, name=None, near=None, **kwargs):
    
    if name:
        if "|" in name:
            name = name.split("|")[0]
        text = re.sub(r'NAME', name, text)

    if near:
        if "|" in near:
            near = near.split("|")[0]
        text = re.sub(r'NEAR', near, text)

    text = text.replace("the The", "the") 
    text = text.replace("The The", "The") 
    text = text.replace("The Chinese The Eagle", "The Chinese Eagle") 

    return text

def linear_mr2mr(linear_mr, collapse_multi=False):
    mr = {'da': 'inform', 'slots': {}}
    for sf in linear_mr:
        slot, filler = sf.split('=')
        if slot not in mr['slots']:
            mr['slots'][slot] = filler
        else:
            mr['slots'][slot] += "|" + filler
    for key in mr['slots']:
        mr['slots'][key] = "|".join(
            sorted(set(mr['slots'][key].split("|"))))

    if collapse_multi:
        return _collapse_multi_mr(mr, linear_mr)
    else:
        return mr

def _collapse_multi_mr(mr, sf_seq):
    from copy import copy
    new_mr = copy(mr)
    for k, v in new_mr['slots'].items():

        if k == 'name' and '|' in v:
            names = [f'name={vi}' for vi in v.split('|')]
            if len(names) == 2:
                x1 = names[0]
                x2 = names[1]
                idx1 = sf_seq.index(x1)
                idx2 = sf_seq.index(x2)
                if idx1 < idx2:
                    new_mr['slots']['name'] = x1.split('=')[1]

                else:
                    new_mr['slots']['name'] = x2.split('=')[1]
            else:
                warn("unhandled name")
        if k == 'near' and '|' in v:

            nears = [f'near={vi}' for vi in v.split('|')]
            if len(nears) == 2:
                x1 = nears[0]
                x2 = nears[1]
                idx1 = sf_seq.index(x1)
                idx2 = sf_seq.index(x2)
                if idx1 < idx2:
                    new_mr['slots']['near'] = x1.split('=')[1]

                else:
                    new_mr['slots']['near'] = x2.split('=')[1]
            else:
                warn("unhandled near")

        if k == 'area' and '|' in v:
            new_mr['slots']['area'] = 'riverside'

        if k == 'price_range' and '|' in v:
            items = v.split("|")
            if len(items) == 2:
                if '£' in items[0] and '£' not in items[1]:
                    new_mr['slots']['price_range'] = items[0]
                elif '£' in items[1] and '£' not in items[0]:
                    new_mr['slots']['price_range'] = items[1]
                else:
                    new_mr['slots']['price_range'] = 'moderate'
            else:
                warn("unhandled price_range")

        if k == 'customer_rating' and '|' in v:
            items = v.split("|")
            if len(items) == 2:
                if '5' in items[0] and '5' not in items[1]:
                    new_mr['slots']['customer_rating'] = items[0]
                elif '5' in items[1] and '5' not in items[0]:
                    new_mr['slots']['customer_rating'] = items[1]
                else:
                    new_mr['slots']['customer_rating'] = 'average'
            else:
                warn("unhandled customer_rating")
        if k == 'eat_type' and '|' in v:
            items = v.split("|")
            if len(items) == 2:
                rest = 'restaurant'
                if rest in items[0] and rest not in items[1]:
                    new_mr['slots']['eat_type'] = items[1]
                elif rest in items[1] and rest not in items[0]:
                    new_mr['slots']['eat_type'] = items[0]
                else:
                    idx_pub = sf_seq.index('eat_type=pub')
                    idx_cs = sf_seq.index('eat_type=coffee shop')
                    if idx_pub < idx_cs:
                        new_mr['slots']['eat_type'] = 'pub'
                    else:
                        new_mr['slots']['eat_type'] = 'coffee shop'
            else:
                warn("unhandled eat_type")
        if k == 'food' and '|' in v:
            foods = [f'food={vi}' for vi in v.split('|')]
            if len(foods) == 2:
                x1 = foods[0]
                x2 = foods[1]
                idx1 = sf_seq.index(x1)
                idx2 = sf_seq.index(x2)
                if idx1 < idx2:
                    new_mr['slots']['food'] = x1.split('=')[1]
                else:
                    new_mr['slots']['food'] = x2.split('=')[1]
            else:
                warn("unhandled food")
        if k == 'family_friendly' and '|' in v:
            family_friendlys = [f'family_friendly={vi}' for vi in v.split('|')]
            if len(family_friendlys) == 2:
                x1 = family_friendlys[0]
                x2 = family_friendlys[1]
                idx1 = sf_seq.index(x1)
                idx2 = sf_seq.index(x2)
                if idx1 < idx2:
                    new_mr['slots']['family_friendly'] = x1.split('=')[1]
                else:
                    new_mr['slots']['family_friendly'] = x2.split('=')[1]
            else:
                warn("unhandled family_friendly")

    return new_mr

def linearize_mr(mr, delex=False, order='random', return_header=True,
                 freq_info=None):
    da = mr['da']
    rating = mr['slots'].get('rating', 'N/A')
    slot_fillers = []
    for slot, filler in mr['slots'].items():
        for item in filler.split("|"):
        #if '|' in filler:
        #    from warnings import warn
        #    warn("linearizing a multi mr")

            slot_fillers.append(f'{slot}={item}')

    if delex:
        for i, t in enumerate(slot_fillers):
            if t.startswith('name'):
                slot_fillers[i] = 'name=PLACEHOLDER'
            if t.startswith('near'):
                slot_fillers[i] = 'near=PLACEHOLDER'

    if order == 'random':
        random.shuffle(slot_fillers)

    if order == 'inc_freq':
        slot_fillers = sorted(
            slot_fillers, 
            key=lambda x: freq_info['slot_counts'][x.split("=")[0]])

    if order == 'dec_freq':
        slot_fillers = sorted(
            slot_fillers, 
            key=lambda x: freq_info['slot_counts'][x.split("=")[0]],
            reverse=True)

    if order == 'inc_freq_fixed':
        slot_fillers = sorted(slot_fillers, 
            key=lambda x: freq_info['delex_slot_filler_counts'].get(x, 0),
            reverse=True)
        for key in freq_info['slot_counts'].keys():
            if key not in mr['slots']:
                slot_fillers.append(f'{key}=N/A') 
        slot_fillers = sorted(
            slot_fillers, 
            key=lambda x: freq_info['slot_counts'][x.split("=")[0]])

        slot_fillers = [
            x for i,x in enumerate(slot_fillers)
            if (i == 0) or slot_fillers[i-1].split('=')[0] != x.split('=')[0]
        ]

    if order == 'dec_freq_fixed':
        slot_fillers = sorted(slot_fillers, 
            key=lambda x: freq_info['delex_slot_filler_counts'].get(x, 0),
            reverse=True)
        for key in freq_info['slot_counts'].keys():
            if key not in mr['slots']:
                slot_fillers.append(f'{key}=N/A') 
        slot_fillers = sorted(
            slot_fillers, 
            key=lambda x: freq_info['slot_counts'][x.split("=")[0]],
            reverse=True)
        slot_fillers = [
            x for i,x in enumerate(slot_fillers)
            if (i == 0) or slot_fillers[i-1].split('=')[0] != x.split('=')[0]
        ]

    return slot_fillers

def remove_header(linear_mr):
    return list(linear_mr)

def get_header(linear_mr):
    return []

def mr2header(mr):
    return []

def is_placeholder(token):
    return token in ['NAME', 'NEAR']

def lexicalize_linear_mr(linear_mr, name=None, near=None, **kwargs):
    linear_mr = list(linear_mr)
    for i, t in enumerate(linear_mr):
        if t.startswith('name') and name != None:
            linear_mr[i] = 'name=' + name
        if t.startswith('near') and near != None:
            linear_mr[i] = 'near=' + near

    return linear_mr

def delexicalize_linear_mr(linear_mr):
    delex_lmr = []
    for t in linear_mr:
        if t.startswith('name') and not t.endswith("="):
            t = 'name=PLACEHOLDER'
        elif t.startswith('near') and not t.endswith("="):
            t = 'near=PLACEHOLDER'
        delex_lmr.append(t)
    return delex_lmr
