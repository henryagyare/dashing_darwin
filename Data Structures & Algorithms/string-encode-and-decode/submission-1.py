class Solution:

    def encode(self, strs: List[str]) -> str:
        return_string = ""
        for word in strs:
            return_string += "("
            curr = "("
            for char in word:
                char_ascii = ord(char)
                curr += str(ord(char)) + "|"
                return_string += str(ord(char)) + "|"
            return_string += "|)" if curr == "(" else ")"
        print("Encoded String: ", return_string)
        return return_string

    def decode(self, s: str) -> List[str]:
        # print("s: ", s)
        if s == "()":
            return [""]
        ret = []
        # word = ""
        # for char in s:
        #     if char == "(":
        #         word = ""
        #         continue
        #     word += char()
        #     if char == ")":
        #         ret.append(word)
        words = s.split("|)")[:-1]
        for wordcode in words:
            w = wordcode[1:].split("|")
            print("w: ", w)
            word = "".join([chr(int(c)) if c else "" for c in w])
            print("word: ", word)
            ret.append(word)
        return ret



