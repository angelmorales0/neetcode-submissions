class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return true if all characters are the same, return false otherwise,
        #first thought is adding all characters to a seperate array and checking if they are equal. 

        s_list = []
        t_list = [] #initalize the arrays to be compared to with string lengths 
    
        for letter in s:
            s_list.append(letter)
        for letter in t:
            t_list.append(letter)
    
        s_list.sort()
        t_list.sort()

        if len(t_list) != len(s_list):
            return False
        for index in range (len(s_list)):
            print (s_list, t_list)
            if s_list[index] != t_list[index]:
                return False
        return True