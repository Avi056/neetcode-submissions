class Solution:

    def encode(self, strs: List[str]) -> str:
        toRet = ""
        for string in strs:
            toRet+=f"{len(string)}#{string}"
        return toRet

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            curr_len = int(s[i:j])
            j+=1
            decoded.append(s[j:j+curr_len])
            i = j + curr_len

        return decoded

