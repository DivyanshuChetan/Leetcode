class Solution(object):
    def restoreString(self, s, indices):
        answer=[""]*len(s)
     
        for i in range(len(s)):
            target_index=indices[i]
            answer[target_index]=s[i]
        return "".join(answer)

# class Solution:
#     def restoreString(self, s, indices):
        # Create a list to hold the shuffled characters
        # answer = [''] * len(s)

        # # Loop through each character in the original string
        # for i in xrange(len(s)):
        #     # Get the index where the current character should go based on indices
        #     target_index = indices[i]

        #     # Place the current character at the target index in the answer list
        #     answer[target_index] = s[i]
        
        # # Convert the list to a string and return the shuffled string
        # return ''.join(answer)