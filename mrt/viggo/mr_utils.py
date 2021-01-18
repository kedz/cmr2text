from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
import random
import re
from warnings import warn

from mrt.viggo.meta import (
    CATEGORICAL_SLOTS, LIST_SLOTS, LEXICON, DEVELOPER_TOKENS, SRT_NAME_TOKENS,
    MONTHS,
)


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

def delexicalize_tokens(tokens, specifier=None, no_dates=False, **kwargs):
    tokens = list(tokens)

    for _, patt in DEVELOPER_TOKENS:
        tokens = _delex_tokens(tokens, patt, 'DEVELOPER')
    tokens = _delex_tokens(tokens, ['spectrum', 'holobyte', ',', 'inc.'], 
                           'DEVELOPER')
    tokens = _delex_tokens(tokens, ['spectrum', 'holobyte', ',', 'inc'], 
                           'DEVELOPER')
    tokens = _delex_tokens(tokens, ['blizzard'], 
                           'DEVELOPER')
    
    for _, patt in SRT_NAME_TOKENS:
        tokens = _delex_tokens(tokens, patt, 'NAME')
    tokens = _delex_tokens(tokens, ['half', '-', 'life', '2'], 'NAME')
    tokens = _delex_tokens(tokens, ['spider', '-', 'man'], 'NAME')

    if not no_dates:
        i = 0
        while i < len(tokens):
            if re.match('\d\d\d\d', tokens[i]) and tokens[i-1] == ',' \
                    and re.match('\d\d?', tokens[i-2]) \
                    and re.match(MONTHS, tokens[i-3], flags=re.I):
                tokens = tokens[:i-3] + ["EXP_RELEASE_DATE"] + tokens[i+1:]
                i = i - 3

            if tokens[i] == '2019':
                tokens[i] = 'EXP_RELEASE_DATE'

            if re.match('\d\d\d\d', tokens[i]) and tokens[i] != '2019':
                tokens[i] = 'RELEASE_YEAR'

            if re.match("'0\d", tokens[i]):
                tokens[i] = 'RELEASE_YEAR'

            i += 1
            
    if specifier:
        feats = get_specifier_feats(specifier)
        stoks = word_tokenize(specifier.replace("-", " - ").replace('_', ' '))
        for i, t in enumerate(tokens):
            s = max(i - len(stoks) + 1, 0)
            if tokens[s:i+1] == stoks:
                tokens = tokens[:s] + [feats] + tokens[i+1:]
                i = s + 1

    return tokens   

def lexicalize_string(text, name=None, developer=None, release_year=None,
                      exp_release_date=None, specifier=None, **kwargs):
    
    if name:
        text = re.sub(r'NAME', name, text)

    if developer:
        text = re.sub(r'DEVELOPER', developer, text)
        
    if release_year:
        text = re.sub(r'RELEASE_YEAR', release_year, text)

    if exp_release_date:
        text = re.sub(r'EXP_RELEASE_DATE', exp_release_date, text)

    if specifier:
        feats = get_specifier_feats(specifier)
        text = re.sub(feats, specifier.replace("_", " "), text)

    return text

def linearize_mr(mr, delex=False, order='random', return_header=True,
                 freq_info=None):
    da = mr['da']
    rating = f"rating={mr['slots'].get('rating', 'N/A')}"
    slot_fillers = []
    for slot, filler in mr['slots'].items():
        if slot == 'rating':
            continue
        if slot in LIST_SLOTS:
            for item in filler:
                slot_fillers.append(f'{slot}={item}')
#        elif slot == 'specifier':
#            feats = get_specifier_feats(filler)
#            slot_fillers.append(f'{slot}={feats}')
        else:
            for item in filler.split("|"):
                slot_fillers.append(f'{slot}={item}')

    if delex:
        for i, t in enumerate(slot_fillers):
            if t.startswith('name') and not t.endswith('='):
                slot_fillers[i] = 'name=PLACEHOLDER'
            if t.startswith('developer') and not t.endswith('='):
                slot_fillers[i] = 'developer=PLACEHOLDER'
            if t.startswith('release_year') and not t.endswith('='):
                slot_fillers[i] = 'release_year=PLACEHOLDER'
            if t.startswith('exp_release_date') and not t.endswith('='):
                slot_fillers[i] = 'exp_release_date=PLACEHOLDER'
            if t.startswith('specifier'):
                feats = get_specifier_feats(t.split('=')[1])
                slot_fillers[i] = f'specifier={feats}'

    if order == 'random':
        random.shuffle(slot_fillers)

    if order == 'inc_freq':
        genres = [x for x in slot_fillers if x.startswith('genres')]
        genres = sorted(
            genres, 
            key=lambda x: freq_info['delex_slot_filler_counts'][x])
        platforms = [x for x in slot_fillers if x.startswith('platforms')]
        platforms = sorted(
            platforms, 
            key=lambda x: freq_info['delex_slot_filler_counts'][x])
        player_perspective = [x for x in slot_fillers 
                              if x.startswith('player_perspective')]
        player_perspective = sorted(
            player_perspective, 
            key=lambda x: freq_info['delex_slot_filler_counts'][x])

        nonlist = [x for x in slot_fillers 
            if x not in genres + platforms + player_perspective]

        slot_fillers = sorted(
            nonlist + genres + platforms + player_perspective,
            key=lambda x: freq_info['slot_counts'][x.split("=")[0]])

    if order == 'dec_freq':
        genres = [x for x in slot_fillers if x.startswith('genres')]
        genres = sorted(
            genres, 
            key=lambda x: freq_info['delex_slot_filler_counts'][x],
            reverse=True)
        platforms = [x for x in slot_fillers if x.startswith('platforms')]
        platforms = sorted(
            platforms, 
            key=lambda x: freq_info['delex_slot_filler_counts'][x],
            reverse=True)
        player_perspective = [x for x in slot_fillers 
                              if x.startswith('player_perspective')]
        player_perspective = sorted(
            player_perspective, 
            key=lambda x: freq_info['delex_slot_filler_counts'][x],
            reverse=True)

        nonlist = [x for x in slot_fillers 
            if x not in genres + platforms + player_perspective]

        slot_fillers = sorted(
            nonlist + genres + platforms + player_perspective,
            key=lambda x: freq_info['slot_counts'][x.split("=")[0]],
            reverse=True)
    if order == 'inc_freq_fixed':
        fixed_slot_fillers = []
        for slot, _ in sorted(freq_info['slot_counts'].items(),
                              key=lambda x: x[1]):
            if slot in LIST_SLOTS:

                fillers = [f'{slot}={x}' for x in mr['slots'].get(slot, [])]
                fillers = sorted(
                    fillers,
                    key=lambda x: freq_info['delex_slot_filler_counts'][x])
                r = freq_info["list_slot_max_lengths"][slot]
                fixed_slot_fillers.extend(fillers)
                if len(fillers) < r:
                    fixed_slot_fillers.extend(
                        [f'{slot}=N/A'] * (r - len(fillers)))
            else:
                if delex and slot in ['name', 'developer', 'release_year',
                                      'exp_release_date'] \
                         and mr['slots'].get(slot, 'N/A') not in ('N/A', ''):
                    sf = f'{slot}=PLACEHOLDER'
                elif delex and slot == 'specifier' \
                        and mr['slots'].get(slot, 'N/A') not in ('N/A', ''):
                    feats = get_specifier_feats(mr['slots']['specifier'])
                    sf = f'{slot}={feats}'
                else:
                    f = mr['slots'].get(slot, 'NA')
                    if "|" in f:
                        fs = [f'{slot}={x}' for x in f.split("|")]

                        fs.sort(key=lambda x: freq_info['delex_slot_filler_counts'][x])
                        sf = fs[-1]                        

                    else:
                        sf = f"{slot}={mr['slots'].get(slot, 'N/A')}"
                
                fixed_slot_fillers.append(sf)

        slot_fillers = fixed_slot_fillers

    if order == 'dec_freq_fixed':
        fixed_slot_fillers = []
        for slot, _ in sorted(freq_info['slot_counts'].items(),
                              key=lambda x: x[1], reverse=True):
            if slot in LIST_SLOTS:

                fillers = [f'{slot}={x}' for x in mr['slots'].get(slot, [])]
                fillers = sorted(
                    fillers,
                    key=lambda x: freq_info['delex_slot_filler_counts'][x],
                    reverse=True)
                r = freq_info["list_slot_max_lengths"][slot]
                fixed_slot_fillers.extend(fillers)
                if len(fillers) < r:
                    fixed_slot_fillers.extend(
                        [f'{slot}=N/A'] * (r - len(fillers)))
            else:
                if delex and slot in ['name', 'developer', 'release_year',
                                      'exp_release_date'] \
                         and mr['slots'].get(slot, 'N/A') not in ('N/A', ''):
                    sf = f'{slot}=PLACEHOLDER'
                elif delex and slot == 'specifier' \
                        and mr['slots'].get(slot, 'N/A') not in ('N/A', ''):
                    feats = get_specifier_feats(mr['slots']['specifier'])
                    sf = f'{slot}={feats}'
                else:
                    f = mr['slots'].get(slot, 'NA')
                    if "|" in f:
                        fs = [f'{slot}={x}' for x in f.split("|")]

                        fs.sort(key=lambda x: freq_info['delex_slot_filler_counts'][x])
                        sf = fs[-1]                        

                    else:
                        sf = f"{slot}={mr['slots'].get(slot, 'N/A')}"
                
                fixed_slot_fillers.append(sf)

        slot_fillers = fixed_slot_fillers


    if return_header:
        return [da, rating] + slot_fillers
    else:
        return slot_fillers


def tokenize(text):

    text = re.sub(r'(\d)\.', r'\1 .', text)
    text = re.sub(r'inc\. it', r'inc . it', text)
    text = re.sub(r'ltd\. it', r'ltd . it', text)
    text = re.sub(r'ltd\. the', r'ltd . the', text)
    text = re.sub(r'ltd\. you', r'ltd . you', text)
    texr = re.sub(r'Ltd\. The', 'Ltd . The', text)
    text = re.sub(r' (V)\. ', r' \1 . ', text, flags=re.I)
    text = re.sub(r' M\. ', r' m . ', text, flags=re.I)
    text = re.sub(r' t\. ', r' t . ', text, flags=re.I)
    text = re.sub(r' ok\. ', r' ok . ', text, flags=re.I)
    text = re.sub(r' e\.', r' e .', text, flags=re.I)
    text = re.sub(r"ions'", r"ions '", text, flags=re.I)
    text = re.sub(r'twisted metal', 'Twisted Metal', text)
    tokens = []
    sentences = sent_tokenize(text)

    for i, sentence in enumerate(sentences, 1):
        sentence = re.sub(r"fps\.", r"fp__ __s.", sentence)
        sentence = re.sub(r"fps", r"fp__ __s", sentence)
        sentence = re.sub(r"FPS\.", r"FP__ __S.", sentence)
        sentence = re.sub(r"FPS", r"FP__ __S", sentence)
        sentence = re.sub(r"(\w)/(\w)", r"\1 / \2", sentence)
        sentence = re.sub(r"(\w)-(\w)", r"\1 - \2", sentence)
        sentence = re.sub(r'(\w)-(\w)', r'\1 - \2', sentence)
        sentence = re.sub(r' -(\w)', r' - \1', sentence)
        sentence = re.sub(r'\)-(\w)', r') - \1', sentence)
        sentence = re.sub(r'(\w)- ', r'\1 -', sentence)

        tokens.extend(word_tokenize(sentence))
        if i < len(sentences):
            tokens.append('<sent>')
    return tokens

def detokenize(tokens):
    text = ' '.join(tokens)

    text = re.sub(r' <eos>', '', text)

    for misc in LEXICON['other']:
        text = re.sub(" " + re.escape(misc) + " ", " " + misc + " ", text, flags=re.I)

    for platforms in LEXICON['platforms']:
        text = re.sub(" " + re.escape(platforms) + " ", " " + platforms + " ", text, flags=re.I)

    text = re.sub(r'skyrim', 'Skyrim', text, flags=re.I)
    text = re.sub(r'todd', 'Todd', text, flags=re.I)
    text = re.sub(r' c ', ' C ', text, flags=re.I)
    text = re.sub(r' ds ', ' DS ', text, flags=re.I)
    text = re.sub('kevin spacey', 'Kevin Spacey', text, flags=re.I)
    text = re.sub('guitar hero', 'Guitar Hero', text, flags=re.I)
    text = re.sub(' nba', ' NBA', text, flags=re.I)
    text = re.sub('aaa', 'AAA', text, flags=re.I)
    text = re.sub(' playstations ', ' PlayStations', text, flags=re.I)
    text = re.sub('^playstation', 'PlayStation', text, flags=re.I)
    text = re.sub('^pc', 'PC', text, flags=re.I)
    text = re.sub('blizzard', 'Blizzard', text, flags=re.I)
    text = re.sub("<sent> (.)", lambda m: m.groups()[0].upper(), text)
    text = re.sub(" i ", " I ", text)
    text = re.sub(r' os', ' OS', text, flags=re.I)
    text = re.sub(" ai ", " AI ", text)
    text = re.sub(" e ", " E ", text)
    text = re.sub(" m ", " M ", text)
    text = re.sub(" t ", " T ", text)
    text = re.sub(' - ', '-', text)
    text = re.sub(r'\( ', '(', text)
    text = re.sub(r' \/ ', '/', text)
    text = re.sub(r' \)', ')', text)
    text = re.sub(' \?', '?', text)
    text = re.sub(' \!', '!', text)
    text = re.sub(' \.', '.', text)
    text = re.sub(' ,', ',', text)
    text = re.sub(" n't", "n't", text)
    text = re.sub(" 's", "'s", text)
    text = re.sub(" 'd", "'d", text)
    text = re.sub(" 'll", "'ll", text)
    text = re.sub(" 're", "'re", text)
    text = re.sub(" 'm", "'m", text)
    text = re.sub(" 've", "'ve", text)
    text = re.sub(" ;", ";", text)
    text = re.sub(" :", ":", text)
    text = re.sub("__ __", "", text)
    text = re.sub("fps", "FPS", text)
        
    text = re.sub(" can not ", " cannot ", text)
    text = re.sub("esrb rating", "ESRB Rating", text)
    text = re.sub("esrb", "ESRB", text, flags=re.I)
    text = re.sub("everyone 10 and older", "Everyone 10 and Older", text)
    text = re.sub("everyone 10", "Everyone 10", text)
    text = re.sub("for everyone", "for Everyone", text)
    text = re.sub(" e for everyone", " E for Everyone", text, flags=re.I)
    text = re.sub("entertainment and ratings board", 
                  "Entertainment and Ratings Board", text, flags=re.I)
    text = re.sub("\(for mature\)", "(for Mature)", text)
    text = re.sub("for teen", "for Teen", text)
    text = re.sub("teen rating", "Teen rating", text)
    text = re.sub("suitable for teenagers", "suitable for Teenagers", text)
    text = re.sub("teen rated", "Teen rated", text)
    text = re.sub(' rts', ' RTS', text)
    text = re.sub(r'/rts', '/RTS', text)
    text = re.sub(' rpg', ' RPG', text)
    text = re.sub('-rpg', '-RPG', text)
    text = re.sub('mmorpg', 'MMORPG', text)
    text = re.sub('-such', ' - such', text)
    text = re.sub('-have', ' - have', text)
    text = re.sub('must - have', 'must-have', text)
    text = re.sub('gaas', 'GAAS', text)
    text = re.sub(' ok ', ' OK ', text)
    text = re.sub(r' ok\.', ' OK.', text)
    text = re.sub(r' ok,', ' OK,', text)
    text = re.sub(r' o.k\.', ' O.K.', text)
    text = re.sub('bethesda studios', 'Bethesda Studios', text)
    text = re.sub('teen-rated', 'Teen-rated', text)

    text = re.sub("s ' ", "s' ", text)
    text = re.sub("R ' ", "R' ", text)
    text = re.sub("n ' ", "n' ", text)
    text = re.sub("Superhot Team", "SUPERHOT Team", text)
    text = re.sub('got ta', 'gotta', text)
    text = re.sub('gon na', 'gonna', text)
    text = re.sub(" june", " June", text)
    text = re.sub(" feb", " Feb", text)
    text = re.sub(" december", " December", text)
    text = re.sub(" november", " November", text)
    text = re.sub(" sept", " Sept", text)
    text = re.sub(" august", " August", text)
    text = re.sub(" october", " October", text)
    text = re.sub(" mature", " Mature", text)

    for developer in LEXICON['developer']:
        text = re.sub(re.escape(developer), developer, text, flags=re.I)

    for name in LEXICON['name']:
        text = re.sub(re.escape(name), name, text, flags=re.I)
    text = re.sub("Superhot Team", "SUPERHOT Team", text)

    text = text[0].upper() + text[1:]

    return text.strip()

def correct_utterance(text):
    text = text[0].upper() + text[1:]
    for developer in LEXICON['developer']:
        text = re.sub(re.escape(developer), developer, text, flags=re.I)
    for name in LEXICON['name']:
        text = re.sub(re.escape(name), name, text, flags=re.I)

    text = re.sub(' ok ', ' OK ', text)
    text = re.sub('any fast paced', 'any fast-paced', text)
    text = re.sub("Blizzard's launcher", "Blizzard Entertainment's launcher", 
                  text)
    text = re.sub("spectrum holobyte, inc,", "Spectrum HoloByte, Inc.,",
                  text, flags=re.I)

    text = re.sub("spectrum holobyte, inc ", "Spectrum HoloByte, Inc. ",
                  text, flags=re.I)
    text = re.sub(r"'09", "2009", text)
    text = re.sub(r'\\NBA', 'NBA', text)
    text = re.sub('simulaton', 'simulation', text)
    text = re.sub(' +', ' ', text)
    text = re.sub('in 2005, It', 'in 2005, it', text)
    text = re.sub('It\' is', 'It is', text)
    text = re.sub('Xbox Game', 'Xbox game', text)
    text = re.sub('fps\.', 'FPS.', text)
    text = re.sub('x,P', 'x, P', text)
    text = re.sub(' Text ad', ' text ad', text)

    text = re.sub('bird- and side view', 'bird and side view', text)
    text = re.sub('bird- and third', 'bird and third', text)
    text = re.sub("action- adventure", "action-adventure", text)
    text = re.sub("Network", "network", text)
    text = re.sub("Live", "live", text)
    text = re.sub("for teen", "for Teen", text)
    text = re.sub("For Teen", "for Teen", text)
    text = re.sub("Exclusive", "for Teen", text)
    text = re.sub('for Eveyone', 'for Everyone', text)
    text = re.sub('teen-rated', 'Teen-rated', text)
    text = re.sub('M- rated', 'M-rated', text)
    text = re.sub('bird- view', 'bird-view', text)
    text = re.sub('Corporation, It', 'Corporation. It', text)
    text = re.sub("Need for Speed:Payback", "Need for Speed: Payback", text)
    text = re.sub("NFS: Payback", "Need for Speed: Payback", text)
    text = re.sub("teen rating", "Teen rating", text)
    text = re.sub(r'was Developed', 'was developed', text)
    text = re.sub(r'E10\+', 'E 10+', text)
    text = re.sub(r'Tean', 'Teen', text)
    text = re.sub(r'for teens', 'for Teens', text)
    text = re.sub(r' i ', ' I ', text)
    text = re.sub(r'(\w)--(\w)', r'\1 -- \2', text)
    text = re.sub(r'\(Some', r'(some', text)
    text = re.sub("for teenagers", "for Teenagers", text)
    text = re.sub("teen rated", "Teen rated", text)
    text = re.sub(r'3, A', '3. A', text)
    text = re.sub(r'm, It', 'm. It', text)
    text = re.sub(r' \?', '?', text)
    text = re.sub("everyone 10 and older", "Everyone 10 and Older", text,
                  flags=re.I)
    text = re.sub(r'Fifa', 'FIFA', text)
    text = re.sub("suitable for teenagers", "suitable for Teenagers", text)
    text = re.sub(r'esrb rating', 'ESRB Rating', text, flags=re.I)
    text = re.sub('playstations', 'PlayStations', text, flags=re.I)
    text = re.sub('Spellforce', 'SpellForce', text)
    text = re.sub('Bioshock', 'BioShock', text)
    text = re.sub('The sims', 'The Sims', text)
    text = re.sub('for everyone', 'for Everyone', text)
    text = re.sub('Superhot Team', 'SUPERHOT Team', text)
    text = re.sub('Need For Speed', 'Need for Speed', text)
    text = re.sub('the division', 'The Division', text, flags=re.I)
    text = re.sub(r'\(for everyone\)', '(for Everyone)', text, flags=re.I)
    text = re.sub(r' mature', ' Mature', text, flags=re.I)
    text = re.sub(r'^mature', 'Mature', text, flags=re.I)
    text = re.sub(r'from Valve\.', 'from Valve Corporation.', text)
    return text.strip()

def extract_mr(mr_string):
    m = re.match(r'^(.*?)\((.*)\)$', mr_string)
    da = m.group(1)
    da_args = m.group(2)
        
    mr = {"da": da, "slots": {}}
    for slot, vals in re.findall(r'([\w_ ]+)\[(.*?)\]', da_args):
        slot = re.sub(r'([a-z])([A-Z])', r'\1 \2', slot).lower().strip()
        slot = slot.replace(' ', '_')
        if slot in CATEGORICAL_SLOTS:
            mr["slots"][slot] = vals
        elif slot in LIST_SLOTS:
            mr["slots"][slot] = sorted(vals.split(", "))
        elif slot == "specifier":
            mr["slots"]["specifier"] = vals
        else:
            raise Exception(f"Bad slot: {slot}")

    return mr

def get_specifier_feats(specifier):
    sup_feat = 'S' if 'worst' in specifier or specifier[-2:] == 'st' else 'R'
    start_feat = 'V' if specifier[0] in 'aeiou' else 'C'
    return f'SPECIFIER_{start_feat}_{sup_feat}'

def linear_mr2mr(linear_mr, collapse_multi=False):
    mr = {'da': 'N/A', 'slots': {}}
    for sf in linear_mr:
        if '=' in sf:
            slot, filler = sf.split('=')
            if slot in LIST_SLOTS:
                if slot not in mr['slots']:
                    mr['slots'][slot] = []
                mr['slots'][slot].append(filler)
            else:
                if slot not in mr['slots']:
                    mr['slots'][slot] = filler
                else:
                    mr['slots'][slot] += "|" + filler
        else:
            mr['da'] = sf
    for key in mr['slots']:
        if key in LIST_SLOTS:
            mr['slots'][key] = sorted(set(mr['slots'][key]))
        else:
            mr['slots'][key] = "|".join(
                sorted(set(mr['slots'][key].split("|"))))

    if collapse_multi:
        for k, v in mr['slots'].items():
            if '|' in v:
                warn(f"unhandled multi filler: {k}={v}")

    return mr

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
            if t.startswith('developer=') and not t.endswith('='):
                mrseq[i] = 'developer=PLACEHOLDER'
            if t.startswith('release_year=') and not t.endswith('='):
                mrseq[i] = 'release_year=PLACEHOLDER'
            if t.startswith('exp_release_date=') and not t.endswith('='):
                mrseq[i] = 'exp_release_date=PLACEHOLDER'
            if t.startswith('specifier'):
                val = t.split('=')[1]
                feats = get_specifier_feats(val)
                mrseq[i] = f'specifier={feats}'

    return mrseq

def tags2mr(tags, delex=False):
    linear_mr = tags2linear_mr(tags, delex)
    return linear_mr2mr(linear_mr)

def remove_header(linear_mr):
    return linear_mr[2:]

def get_header(linear_mr):
    return linear_mr[:2]

def mr2header(mr):
    return [mr['da'], f"rating={mr['slots'].get('rating', 'N/A')}"]

def is_placeholder(token):
    if token in set(['NAME', 'DEVELOPER', 'EXP_RELEASE_DATE', 'RELEASE_YEAR']):
        return True
    else:
        return token.startswith("SPECIFIER")

def lexicalize_linear_mr(linear_mr, name=None, developer=None, 
                         release_year=None, exp_release_date=None, 
                         specifier=None, **kwargs):
    linear_mr = list(linear_mr)
    for i, t in enumerate(linear_mr):
        if t.startswith('name') and name != None:
            linear_mr[i] = 'name=' + name
        if t.startswith('developer') and developer != None:
            linear_mr[i] = 'developer=' + developer
        if t.startswith('release_year') and release_year != None:
            linear_mr[i] = 'release_year=' + release_year
        if t.startswith('exp_release_date') and exp_release_date != None:
            linear_mr[i] = 'exp_release_date=' + exp_release_date
        if t.startswith('specifier') and specifier != None:
            linear_mr[i] = 'specifier=' + specifier

    return linear_mr

def delexicalize_linear_mr(linear_mr):
    delex_lmr = []
    for t in linear_mr:
        if t.startswith('name') and not t.endswith("="):
            t = 'name=PLACEHOLDER'
        elif t.startswith('developer') and not t.endswith("="):
            t = 'developer=PLACEHOLDER'
        elif t.startswith('release_year') and not t.endswith("="):
            t = 'release_year=PLACEHOLDER'
        elif t.startswith('exp_release_date') and not t.endswith("="):
            t = 'exp_release_date=PLACEHOLDER'
        elif t.startswith('specifier') and not t.endswith("="):
            spec = t.split('=')[1]
            t = f'specifier={get_specifier_feats(spec)}'
        delex_lmr.append(t)
    return delex_lmr
