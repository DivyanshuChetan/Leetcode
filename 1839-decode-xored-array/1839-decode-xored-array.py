class Solution(object):
    def decode(self, encoded, first):
        n=len(encoded)
        arr=[0]*(n+1)
        arr[0] = first
        for i in range(n):
            arr[i+1] = encoded[i] ^ arr[i]
        return arr
            