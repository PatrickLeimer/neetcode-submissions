class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string += string + "\n"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split("\n")
        return decoded_strs[:-1]