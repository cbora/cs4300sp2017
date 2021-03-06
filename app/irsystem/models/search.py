import numpy as np
import json
import os
import requests
from StringIO import StringIO
# Load some data into memory
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
print os.getcwd()

data_file_name = 'data/data.json'
with open(data_file_name) as data_file:
    data = json.load(data_file)

url = "https://s3.amazonaws.com/cs4300/sims_array.npy"
r = requests.get(url)
#scores = np.load('data/sims_array.npy')
#scores = np.load(StringIO(r.content))
#scores = np.load('data/hash_all_sims_array.npy')
#scores = np.load('data/hash_all_sims_array_new.npy')
scores = np.load('data/hash_top20_sims_array_final.npy')

results_file_name = 'data/result.json'
with open(results_file_name) as d:
    more_data = json.load(d)
    
# character_id to index mapping
character_to_index_map = {}
for i, v in enumerate(data):
    character_to_index_map[v['character_id']] = i


# Load characters in memory
character_file_name = 'data/characters.json'
with open(character_file_name) as ch:
    chars = json.load(ch)

# used for auto fill on the frontend
auto_fill = []
auto_fill_id_map = {}
for x in chars:
    auto_fill.append(x['display'])
    auto_fill_id_map[x['display']] = x['id']

def query_info(query):
    tmp = auto_fill_id_map[query]
    index = character_to_index_map[tmp]
    d = data[index]
    cid = d['character_id']
    try:
        d['poster'] = more_data[cid]['poster']
        d['plot'] = more_data[cid]['plot']
    except:
        d['poster'] = 'http://images.clipartpanda.com/movie-night-clipart-9cp4q9xcE.jpeg'
        d['plot'] = 'N/A'
    return d

'''computes best fuzzy match to query paramter & return'''
def getFuzzyMatch(query):
    # make score dictionary 
    xToScores = {x['display'].lower():[-1,-1] for x in chars}
    # conversion from usable comparison back to formal storage
    lowerToUpper = {x['display'].lower():x for x in chars}
    lQ = query.lower()
    # compute scores for each movie on ratio and token_set_ratio
    for x in lowerToUpper.keys(): 
        xToScores[x][0] = fuzz.ratio(x,lQ)
        xToScores[x][1] = fuzz.token_set_ratio(x.lower(),lQ)
    # sort by specific ratio
    byRatio = sorted(xToScores.iteritems(), key=lambda i:i[1][0],reverse=True)
    byToken = sorted(xToScores.iteritems(), key=lambda i:i[1][1],reverse=True)
    # pull out character name
    byRatio = [n[0] for n in byRatio]
    byToken = [n[0] for n in byToken]
    # get top 3 for each one to choose from 
    possibles = byRatio[:3] + byToken[:3]
    # choose (black box implementation by fuzzywuzzy)
    finalAnswer = process.extractOne(query, possibles)[0]
    # convert back to original display name
    return lowerToUpper[finalAnswer]['display']

def queryExists(query):
    return auto_fill_id_map.get(query,None) != None

def process_query(query):
    """
     Function to process query and assumes query is the character id


    tmp= auto_fill_id_map[query]

    index = character_to_index_map[tmp]
    row = scores[index]

    t = []
    for i, v in enumerate(row):
        if v < 0:
            # do not add it this score (either from same movie or same character)
            continue
        t.append((v, i))

    t = sorted(t)
    indexes = [x[1] for x in t]
    results = []
    for i in reversed(indexes):
        results.append(data[i])

    # return results in sorted order
    return results[:20]
    """

    tmp = auto_fill_id_map[query]
    print "TMP: ", tmp
    index = character_to_index_map[tmp]
    print "INDEX: ", index
    row = scores[index]

    results = []
    i = 0
    for k in range(0, len(row)/5):
        #print i
        # e = index of similar characters
        e = int(row[i])
        

        d = data[e]
        cid = d['character_id']
        d['character_name'] = d['character_name'].lower()
        #print more_data[cid]
        i = i + 1
        d['sentiment'] = int(round(row[i] * 100))
        i = i + 1
        d['tfidf'] = int(round(row[i] * 100))
        i = i + 1
        d['movie'] = int(round(row[i] * 100))
        i = i + 1
        d['charac_score'] = int(round(row[i] * 100))
        i = i + 1    

        try:
            d['poster'] = more_data[cid]['poster']
            d['plot'] = more_data[cid]['plot']
        except:
            d['poster'] = 'N/A'
            d['plot'] = 'N/A'
        #d['character_id'] = 
        #results[-1]['character_name'] = results[-1]['character_name'].lower()
        results.append(d)
    return results

def process_query_first_version(query):
    """
     Process query of first function
    
     Function to process query and assumes query is the character id

    """
    tmp= auto_fill_id_map[query]

    index = character_to_index_map[tmp]
    row = scores[index]

    t = []
    for i, v in enumerate(row):
        if v < 0:
            # do not add it this score (either from same movie or same character)
            continue
        t.append((v, i))

    t = sorted(t)
    indexes = [x[1] for x in t]
    results = []
    for i in reversed(indexes):
        results.append(data[i])

    # return results in sorted order
    return results[:20]
