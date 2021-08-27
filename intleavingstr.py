class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return len(s1) + len(s2) == len(s3) and (f := cache(lambda i, j: i < len(s1) and s1[i] == s3[i+j] and f(i+1, j) or j < len(s2) and s2[j] == s3[i+j] and f(i, j+1) or i+j == len(s3)))(0, 0)

    
    
    
    
   ###optional add: print( "s3 is an interleaving of s1 and s2")
