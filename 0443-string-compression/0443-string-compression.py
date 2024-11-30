class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        box_holder = 0
        pointer = 0

        while pointer < len(chars):
            char = chars[pointer]
            count = 0

            while pointer < len(chars) and chars[pointer] == char:
                pointer += 1
                count += 1
        
            chars[box_holder] = char
            box_holder +=1
        
            if count > 1:
                for i in str(count):
                    chars[box_holder] = i
                    box_holder += 1
        return box_holder