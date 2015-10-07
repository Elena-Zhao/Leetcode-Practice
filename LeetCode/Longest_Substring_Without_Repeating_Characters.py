__author__ = 'Elena'

#
"""
Problem Description:

Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Handle the special case: empty string
        if len(s) == 0: return 0

        lastAppPos = {s[0]:0}               # Last appear position of alphabet
        longestEndingHere = [1] * len(s)    # Longest substring ending here

        for index in xrange(1, len(s)):
            lastPos = lastAppPos.get(s[index], -1)
            if lastPos < index - longestEndingHere[index-1]:
                # The substring, ending in the previous position, could be
                # extended WITHOUT chop.
                longestEndingHere[index] = longestEndingHere[index-1] + 1
            else:
                # The substring, ending in the previous position, have to
                # be chopped and THEN extended.
                longestEndingHere[index] = index - lastPos
            lastAppPos[s[index]] = index    # Update the last appear position

        return max(longestEndingHere)

s = Solution()
print s.lengthOfLongestSubstring('abcabcbb')