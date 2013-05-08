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
	tweet_file = sys.argv[1]  
	twitterSet = gettwitterdata(tweet_file)
	hashtagDict = {}
	for i in range(len(twitterSet)):
		if "entities" in twitterSet[i]:		
			hashtags = twitterSet[i]["entities"]["hashtags"]	
			for hashtag in hashtags:
				curHashtag = hashtag["text"]
				# print curHashtag
				if curHashtag in hashtagDict:
					hashtagDict[curHashtag] += 1.0
				else:
					hashtagDict[curHashtag] = 1.0
				
			"""
			for word in words:
				if word[0] == "#" and word != "#RT" :
					word = word[1:]
					if word in hashtagDict:
						hashtagDict[word] += 1.0
					else:
						hashtagDict[word] = 1.0
	"""					
	#for word in hashtagDict:
	#	print word, hashtagDict[word]		
	count = 10
	for word in sorted(hashtagDict, key = hashtagDict.get, reverse = True):
		print word,hashtagDict[word]
		count -= 1
		if count == 0:
			break


if __name__ == '__main__':   
	main()
	#my = getsentimentdict()





