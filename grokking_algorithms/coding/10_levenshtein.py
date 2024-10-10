from longest_common import lc_subsequence
import math


def remove_subsequence(s, subsequence, blank_char):
    new_s = ""
    copy_s = s
    for char in subsequence:
        char_index = copy_s.find(char)
        new_s += copy_s[0:char_index]
        new_s += blank_char
        copy_s = copy_s[(char_index + 1):]
    return (new_s + copy_s)


def levenshtein_distance(s1:str, s2:str):
    """gives levenshtein distance operation steps for
    transforming s1 to s2"""

    longest_common_subsequence = lc_subsequence(s1, s2)
    lowest_cost = math.inf
    blank_char = "_"
    result_msg = []

    for sequence in longest_common_subsequence:
        s1_left = remove_subsequence(s1, sequence, blank_char)
        s2_left = remove_subsequence(s2, sequence, blank_char)

        # equalizing the length
        s1_left = s1_left.ljust(len(s2_left), blank_char)
        s2_left = s2_left.ljust(len(s1_left), blank_char)

        # s1 --> s2
        counter = 0
        i = 0
        string_step_before = s1
        string_step_after = ""
        message = f"\nto transform *{s1}* to *{s2}*\n"

        while i < len(s1_left):

            if s1_left[i] == s2_left[i]:
                i += 1
                continue
            else:
                counter += 1
                message += f"\n///{counter}.STEP///\n"

            # add
            if s1_left[i] == blank_char and s2_left[i] != blank_char:
                message += f"add '{s2_left[i]}' at index {i} in '{string_step_before}'"
                string_step_after = string_step_before[:i] + s2_left[i] + string_step_before[i:]
                s1_left = s1_left[:i] + s2_left[i] + s1_left[i:]
                s2_left += blank_char
                i += 1
                # blank_char must be added at the end of 's2_left'
                # to keep the length of s1_left and s2_left equal
                # without changing the required operations
            
            # substitue
            elif s1_left[i] != blank_char and s2_left[i] != blank_char:
                message += f"substitue '{string_step_before[i]}' at index {i} in '{string_step_before}' "
                message += f"with '{s2_left[i]}'"
                string_step_after = string_step_before[:i] + s2_left[i] + string_step_before[(i+1):]
                s1_left = s1_left[:i] + s2_left[i] + s1_left[(i+1):]
                i += 1

            # remove
            elif s1_left[i] != blank_char and s2_left[i] == blank_char:
                message += f"remove '{string_step_before[i]}' at index {i} in '{string_step_before}'"
                string_step_after = string_step_before[:i] + string_step_before[(i+1):]
                s1_left = s1_left[:i] + s1_left[(i+1):] + blank_char
                # we must not update 'i' there
                # blank_char must be added at the end of 's1_left'
                # to keep the length of s1_left and s2_left equal
                # without changing the required operations
    
            message += f"\n   *{string_step_before}* --> *{string_step_after}*"
            string_step_before = string_step_after


        if counter == 0:
            message += "no operations are needed"

        if counter < lowest_cost:
            result_msg = [message]  # higher costs are deleted
            lowest_cost = counter

        elif counter == lowest_cost:
            result_msg.append(message)
    

    return result_msg
                
    

#print(remove_subsequence("abbbaaab", "ab"))
#print(remove_subsequence("bbbbaaab", "ab"))
#print(remove_subsequence("acbad", "abd"))
#print(remove_subsequence("acbad", "acd"))

s1 = "abcd"
s2 = "acbad"

s1 = "abbbaaab"
s2 = "ab"

s1 = "acbad"
s2 = "acd"

s1 = "kitten"
s2 = "sitting"
results = levenshtein_distance(s1, s2)

s1 = "flaw"
s2 = "lawn"

s1 = "meilenstein"
s2 = "levenshtein"

s1 = "aaaaaaaa"
s2 = "aaa"

s1 = "abcwwwbcd"
s2 = "abcd"

for result in results:
    print(result)
