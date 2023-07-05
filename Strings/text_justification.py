class Solution:
    def fullJustify (self, words: List[str], maxWidth: int) -> List[str]:
        i, used_places, res = 0, 0, []
        while (i < len(words)):
            start_i, used_places = i, 0
            while ((i < len(words)) and ((used_places + len(words[i])) <= maxWidth)):
                used_places += len(words[i]) + 1
                i += 1
            num_of_words_in_curr_line = i - start_i
            num_of_spaces_in_curr_line = maxWidth - used_places + num_of_words_in_curr_line
            line = []
            if (num_of_words_in_curr_line == 1):
                for j in range(start_i, i):
                    for ch in words[j]: line.append(ch)
                while (num_of_spaces_in_curr_line > 0):
                    line.append(' ')
                    num_of_spaces_in_curr_line -= 1
            elif (i == len(words)):
                for j in range(start_i, i):
                    for ch in words[j]: line.append(ch)
                    if (num_of_spaces_in_curr_line > 0):
                        line.append(' ')
                        num_of_spaces_in_curr_line -= 1
                while (num_of_spaces_in_curr_line > 0):
                    line.append(' ')
                    num_of_spaces_in_curr_line -= 1
            else:
                num_of_space_places = num_of_words_in_curr_line - 1
                common_spaces_per_word, extra_spaces_per_word = divmod(num_of_spaces_in_curr_line, num_of_space_places)
                for j in range(start_i, i):
                    for ch in words[j]: line.append(ch)
                    if ((j + 1) != i):
                        tot_spc = common_spaces_per_word + (1 if (extra_spaces_per_word > 0) else 0)
                        while (tot_spc > 0):
                            line.append(' ')
                            tot_spc -= 1
                        if (extra_spaces_per_word > 0): extra_spaces_per_word -= 1
            res.append("".join(line))
        return res
