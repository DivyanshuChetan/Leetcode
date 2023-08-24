class Solution(object):
    def decodeMessage(self, key, message):
        mapping={" ":" "}
        i=0
        decoded_msg=""
        alphabet="abcdefghijklmnopqrstuvwxyz"
        
        for char in key:
            if char not in mapping:
                mapping[char]=alphabet[i]
                i+=1
        
        for char in message:
            decoded_msg+=mapping[char]
        
        return decoded_msg           