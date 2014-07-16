'''
Created on Jul 15, 2014

Feature extractor

@author: rsingh
'''

import re

def _loadFeatureFile(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    
    resp = []
    for line in lines:
        resp.append(line.strip())
    
    return resp

unigramFeatures = _loadFeatureFile('features/unigram')
bigramFeatures = _loadFeatureFile('features/bigram')
smileyFeatures = _loadFeatureFile('features/smiley')

def preProcess(tweet):
    # process the tweets
    
    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)    
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet

def getFeatureVector(tweet):
    tweet = preProcess(tweet)
    txtLow = tweet.lower()

    # result storage
    fvec = {}

    # search for each feature
    for key in unigramFeatures:
        fvec[key] = False
        fvec[key] = fvec[key] or (txtLow.find(key) != -1)

    for key in bigramFeatures:
        fvec[key] = False
        fvec[key] = fvec[key] or (txtLow.find(key) != -1)
        
    for key in smileyFeatures:
        s = 'endswith_%s' % key
        
        fvec[s] = False
        fvec[s] = fvec[s] or txtLow.endswith(key) 
        
    return fvec


if __name__ == '__main__':
    t = '@bkad5161 than apologize to @apple ;)'
    features = getFeatureVector(t)
    for k,v in features.iteritems():
        if v:
            print k
