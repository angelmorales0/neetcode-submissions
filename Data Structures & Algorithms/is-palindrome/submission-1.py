class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first we must remove whitespace 
        string = s.replace(" ", "")
        character_array = []
        for character in string:
            if character.isalnum():# if character is alpha numeric, put it in array
                character_array.append(character)
        L_pointer = 0
        print(character_array)
        for R_pointer in range (len(character_array)-1, 0, -1):
            if character_array[R_pointer].lower() !=  character_array[L_pointer].lower():
                return False
            L_pointer += 1
        return True
                