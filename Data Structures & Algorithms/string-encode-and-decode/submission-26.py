class Solution:

    def encode(self, strs: List[str]) -> str:
        #need to make it so string gets concatinated into one AND algo knows how to decode it later

        builder = ""
        for word in strs:
            builder += str(len(word))
            builder += "#"
            builder += word


        print(builder)
        return builder

    def decode(self, s: str) -> List[str]:
        index = 0
        number = ""
        word = ""

        ret = []

        while index <len(s):
        
            if s[index].isdigit():
                number += s[index]
                print(1)
            elif s[index] == "#" and number != "":
                number = int(number)
                index +=1
                word = s[index:index+number]
                index +=number-1
                print(2)
                ret.append(word)
                word = ""
                number = ""
            index+=1
        return ret

            
        #need to follow decode algo given previously 
