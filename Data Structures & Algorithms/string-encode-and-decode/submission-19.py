class Solution:

    def encode(self, strs: List[str]) -> str:
        builder = ""
        for string in strs:
            builder += "|"
            builder += string
            
        return builder

    def decode(self, s: str) -> List[str]:
        ret = []
        index = -1
        for char in s:
            if char == "|":
                ret.append("")

                index += 1
                continue
            if index < len(ret):
                ret[index] += char
        return ret

        
       
        
