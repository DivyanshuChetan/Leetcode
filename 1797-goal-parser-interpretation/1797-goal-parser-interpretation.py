class Solution(object):
    def interpret(self, command):
        res=""
        
        for i in range(len(command)):
            if command[i]=="G":
                res+="G"
            elif command[i]=="(" and command[i+1]==")":
                res+="o"
            elif command[i]=="(" and command[i+1]=="a":
                res+="al"
        return res

