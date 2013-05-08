import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

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

	for i in range(len(twitterSet)):
		sentimentscore = 0	
		if "text" in twitterSet[i]:		
			words = twitterSet[i]["text"].split()	
			for word in words:
				if word in sentimentDict:
					sentimentscore += sentimentDict[word]
			print sentimentscore
#	for i in range(10):
#		print twitterSet[i]["text"]
	

if __name__ == '__main__':   
	main()
	#my = getsentimentdict()





