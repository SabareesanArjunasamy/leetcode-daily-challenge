def bagOfTokensScore(tokens: list[int], power: int) -> int:
        tokens.sort()
        if not tokens or tokens[0] > power:
            return 0
        up, down = 0, len(tokens) - 1
		
        maxScore, curScore = 0, 0
        
        while up <= down:
            if tokens[up] <= power:
                power -= tokens[up]
                curScore += 1
                up += 1
            else:
                power += tokens[down]
                curScore -= 1
                down -= 1
            maxScore = max(maxScore, curScore)
        
        return maxScore
    
tokens, power = [100], 50
print(bagOfTokensScore(tokens, power))
tokens,power = [100,200],150
print(bagOfTokensScore(tokens, power))
tokens, power = [100,200,300,400], 200
print(bagOfTokensScore(tokens, power))
