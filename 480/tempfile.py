
Trinh3Store = {}
def Trinh3(hist=[], score=[], query = False):
	def checkHistoryDifferences(Trinh3Store, hist):
		differences = -1
		try:
			if (len(Trinh3Store["myHistory"]) > 30):
				myLast10Moves = Trinh3Store["myHistory"][-30:]
				if len(hist) > 30:
					new_hist = hist[-30:]
					differences += 1
					for count in range(0, 30):
						if (new_hist[count] != myLast10Moves[count]):
							differences += 1
		except:
			return differences
		return differences


	def checkOppRatio(hist):
		turnsPassed = len(hist)
		numCs = 0.0

		for turn in hist:
			if turn[1].upper() == 'C': 
				numCs += 1
		return numCs/turnsPassed
	   
	if query:
		return ["Sand Gambler3", "He lost all his money in Vegas so now he's gambling with sand."]
	   
	turnsPassed = len(hist)
	if not "myHistory" in Trinh3Store:
		Trinh3Store["myHistory"] = []
	if turnsPassed >= 30:
		ratio = checkHistoryDifferences(Trinh3Store, hist) #returns higher when flip is high
		if ratio >= 0: 
			if random.random() >= (ratio/30 - (turnsPassed * .000133)): #if ratio of flip is high, hard to get the same val so choose opp
				Trinh3Store["myHistory"].append('D')
				return 'D'
			else:
				Trinh3Store["myHistory"].append('C')
				return 'C'
		else: #if this fails then whatever return D
			Trinh3Store["myHistory"].append('D')
			return 'D'
	else:
		Trinh3Store["myHistory"].append('C')
		return 'C'