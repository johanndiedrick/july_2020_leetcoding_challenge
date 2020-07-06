class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_list = [str(x) for x in digits]
        integer = int("".join(string_list))
        integer += 1
        string_integer = str(integer)
        return [x for x in string_integer]
