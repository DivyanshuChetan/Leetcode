class Solution(object):
    def defangIPaddr(self, address):
        # return address.replace(".","[.]")
        addr=""
        for i in address:
            if i==".":
                addr+="[.]"
            else:
                addr+=i
        return addr


