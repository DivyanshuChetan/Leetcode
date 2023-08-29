class Solution(object):
    def checkIfPangram(self, sentence):
        map={}
        for i in sentence:
            if i not in map:
                map[i]=1
        if len(map)>25:
            return True
        return False