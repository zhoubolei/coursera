import sys
import json

def getsentimentdict(f):
	with open(f) as afinnfile:
		scores = {}
		for line in afinnfile:
			term, score = line.split("\t")
			scores[term] = int(score)
	#print scores.items()
	return scores

def gettwitterdata(f):
	twitterSet = []	
	with open(f) as twitterfile:
		for line in twitterfile:
			twitterSet.append(json.loads(line))
	return twitterSet

def main():
	sent_file = sys.argv[1]
	tweet_file = sys.argv[2]
	sentimentDict = getsentimentdict(sent_file)
	twitterSet = gettwitterdata(tweet_file)
	sentimentDict_new = iterDict(twitterSet, sentimentDict)
	for key in sentimentDict_new:
		print key, sentimentDict_new[key]

def iterDict(twitterSet, sentimentDict):
	sentimentDict_new = {}
	for j in range(1,50):
		for i in range(len(twitterSet)):
			sentimentscore = 0	
			sentimentword_num = 0
			if "text" in twitterSet[i]:		
				words = twitterSet[i]["text"].encode('utf-8').split()	
				for word in words:
					word.lower()
					if word in sentimentDict:
						sentimentword_num += 1
						sentimentscore += sentimentDict[word]
					elif word in sentimentDict_new:
						sentimentword_num += 1
						sentimentscore += sentimentDict_new[word]
				if sentimentword_num > 0:
					average_sentimentscore = sentimentscore / sentimentword_num
					for word in words:
						word.lower()
						sentimentDict_new[word] = average_sentimentscore
	return sentimentDict_new
if __name__ == '__main__':
    main()
