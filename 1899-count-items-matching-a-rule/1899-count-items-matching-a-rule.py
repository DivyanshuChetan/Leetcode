class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        matches=0
        for Type,colour,name in items:
            if ruleKey=="type" and Type==ruleValue:
                matches+=1
            elif ruleKey=="color" and colour==ruleValue:
                matches+=1
            elif ruleKey=="name" and name==ruleValue:
                matches+=1
        return matches