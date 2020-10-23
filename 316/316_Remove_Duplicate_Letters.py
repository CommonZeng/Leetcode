class Solution(object):
    def removeDuplicateLetters(self, s):
        self.d = {}
        s = self.removeRepeat(s)
        res = self.removeDuplicateLettersRecursive(s, 'z')
        return res

    def removeDuplicateLettersRecursive(self, s, letter):
        # print 'processing', letter
        if letter < 'a':
            self.d[s] = s
            return s
        h, l_big = self.getHash(s, letter)
        if self.d.get(h) is not None:
            best = self.d[h]
            i = 0
            res = ''
            for char in best:
                if char != '~':
                    res += char
                else:
                    res += l_big[i]
                    i += 1
            # print s, letter, h, self.d[h], l_big, res
            return res
        l_pos = []
        for i, c in enumerate(s):
            if c == letter:
                l_pos.append(i)
        if len(l_pos) > 1:
            # print s, letter, h, l_pos
            new_s = self.removeAllButPos(s, letter, l_pos[-1])
            l_removed = [self.removeDuplicateLettersRecursive(new_s, chr(ord(letter)-1))]
            i = 0
            while i < len(l_pos)-1:
                pos = l_pos[i]
                next_pos = l_pos[i+1]
                if next_pos == pos + 1:
                    i += 1
                    continue
                new_s = self.removeAllButPos(s, letter, pos)
                l_removed.append(self.removeDuplicateLettersRecursive(new_s, chr(ord(letter)-1)))
                has_small = False
                for char in s[pos+1:next_pos]:
                    if char < letter:
                        has_small = True
                if not has_small:
                    # print s, letter, l_removed
                    break
                i += 1
            best = min(l_removed)
            self.d[h] = self.genPattern(s, letter, best, h, l_big)
            # print 's, letter, best, h, self.d[h] =', s, letter, best, h, self.d[h]
            return best
        else:
            best =  self.removeDuplicateLettersRecursive(s, chr(ord(letter)-1))
            self.d[h] = self.genPattern(s, letter, best, h, l_big)
            return best

    def removeAllButPos(self, s, letter, pos):
        new_s = ''
        for i, c in enumerate(s):
            if c != letter or i == pos:
                new_s += c
        return new_s

    def removeRepeat(self, s):
        new_s = ''
        for char in s:
            if len(new_s) == 0:
                new_s += char
            elif char != new_s[-1]:
                new_s += char
        return new_s

    def getHash(self, s, letter):
        l_big = []
        h = ''
        str_big = ''
        for char in s:
            if char <= letter:
                h += char
                if len(str_big) > 0:
                    l_big.append(str_big)
                str_big = ''
            else:
                if str_big == '':
                    h += '~'
                str_big += char
        if len(str_big) > 0:
            l_big.append(str_big)
        # print 's =', s, 'letter =', letter, 'h =', h
        # h = self.removeRepeat(h)
        return h, l_big

    def genPattern(self, s, letter, best, h, l_big):
        pattern = ''

        str_big_id = 0
        i = 0
        while i < len(best):
            char = best[i]
            if char <= letter:
                pattern += char
                i += 1
            else:
                str_big = l_big[str_big_id]
                str_big_id += 1
                i += len(str_big)
                pattern += '~'
        return pattern

        # for ease of discussion, let assume the string contains all letters a to z
        # at this stage z is fixed along with a and other one-time letter
        # now we consider y
        # the way to think about it is
        # consider we know the answer for all other letters (by removing all duplicates of them)
        # and y is the only letter open for discussion 
        # then the best y determined by this thought experiment will be the best y in the solution
        # because after you eventally arrive at that solution
        # the said choise of y have already been shown to dominate all others by this thought experiment
        # consider the substring starting from the first appearance of y, it is in this general format below
        # y0 [small0] y1 [small1] z [small2] y2 [small3] y3 [small4],
        # WLOG, [small0] and [small3] are non-empty (if empty then we just merge the two adjacent y's)
        # when [small1] is non-empty, we should choose the rightmost y(y3)
        # the reason being
        #   y0 [small0,1] z [small2,3,4]
        # > [small0] y1 [small1] z [small2,3,4]
        # > [small0,1] z [small2] y2 small[3,4] 
        # > [small0,1] z [small2,3] y3 small[4]
        # if [small1] is empty, then it becomes
        # y0 [small0] y1 z [small2] y2 [small3] y3 [small4],
        # we can verify in similar way that y1 is best.
        # so the choice is different depending on whether [small1] is empty
        # if at this stage we know whether its emtpy or not (by having no choice), then we are done (for y)
        # if not then we still have two candidates y1 and y3
        # note that y0, y2 are dominated in either case and can thus be removed from the general form of the substr
        # [small0] y1 [small1] z [small2,3] y3 [small4]
        # also, whatever is before y0 in the whole solution string can be merged into [small0]
        # so the above format represents the entire solution string
        # now for each letter between y1 and z, we need to decide if it is retained in the [small1] in the final solution

test = Solution()
# print test.removeDuplicateLetters("bcabc") # "abc"
# print test.removeDuplicateLetters("cbacdcbc") # "acdb"
# print test.removeDuplicateLetters("fabhfaecfadgeg") # "abhcfdeg"
# print test.removeDuplicateLetters("fabhfaecfadgegh") # "abcfdegh"
# print test.removeDuplicateLetters("dwzbwczdwzaydw") # "bcdwzay"
# print test.removeDuplicateLetters("mitnlruhznjfyzmtmfnstsxwktxlboxutbic") # "ilrhjfyzmnstwkboxuc"
# print test.removeDuplicateLetters("leetcode") # "letcod"
# print test.removeDuplicateLetters("stsxwktxboxutbc") # "stwkboxuc"
# print test.removeDuplicateLetters("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws") # "bfegkuyjorndiqszpcaw"
print test.removeDuplicateLetters("yioccqiorhtoslwlvfgzycahonecugtatbyphpuunwvaalcpndabyldkdtzfjlgwqk") # "ciorhsaebpunvdyktzfjlgwq"
# print test.removeDuplicateLetters("laepnvlpndl") # "aenvlpd"
# print test.removeDuplicateLetters(
#     "wmxkuuoordmnpnebikzzujdpscpedcrsjphcaykjsmobturjjxxpoxvvrynmapegvtlasmyuddgxygkaztmbpkrnukbxityz"
# ) # "wbcdhajmoegvlskprnuxityz"
# print test.removeDuplicateLetters(
#     "peymrzknlxtrutjiybqemquchgvtmmtpjvunvekszrkatctcirxwuqknrycpdtcuadblzkkleduezgspoxhhssoipbmdgrqggpfdsanolzczpaggwxrlaleaqtnzxclmxwjucnujsptnbmmjzzjhypnlsoxjveywsufegzlfnyvkcnfevkshbckfropoydkdlblppllgefagjgpajsplvxknvtlgtjyhmnwxcpjjzcizihycvsnhnnmqohivekitxzuo"
# ) # "abcefghkrdjlmnwpiysqovtxzu"
# print test.removeDuplicateLetters(
#     "cruaebrnuzdmpfivugqejkspqvxxgnjixjtoboexjwcywzwptiahdbxkmhccsdnlmrmldwoxnurnlaiyzshimpzbmunvwhfkcvbeeorioxoxommgkjablxuibuxbuhhclgjwsgecuhvqscwutbownyjckhqlhjrdmtkozdwuewsxpupwhjeywznccjdeiisirvkvfroiyhhwuynmhwsdzmwauezxbssaxefktyufjnysvcmxrqxunoipqrbjxnxdwmeebpgucfxvvaansdpfetpipqynomtwkloczuepklwmhawfgovewnvxeqyghndlyoqxvoxwozfzprqwvcewvzjykyohfmywymudenrxwcoxrbsgctenzjxhqwtghlpnhkrjkxualiarouhscitxpmgabllajoqipvslibzxioocvvpdlwxvbvspezufenplebnajqsyixar"
# ) # "abcdefghjkiostmlpvwxzunqyr"
# print test.removeDuplicateLetters(
#     "yiklorymxepctlnomfmymitulgfuudxturmemjxxlloevwyfriazwyckgbfogfrppnsomjfhoobirytzzksemgrcbcegbbhaurrrlyxquuoivdcykcpnntgrktwtmgstjrvsvajfukhxwgvsvgzwoatnnzszksxstzkojmyuriyriyqkaqghoxilykyxepnsjeybgxxwyyornzxzttsylsoqlumzwlsdxvzgjfpwwoejsieeyoremvqfyekmxdsabogijmqxdruiydlkrvobwqmlmahmfpwbopbdxhinowqavdasnkeagpjvznzfmlllydgosztljnkrkpjhsqtjxjumzasfitacjqenwcskkkifgzatcevfwererjjabmmmdsnuacxzrgjyytbmxccagjbemkmemjpaqwpjdsunvmfuromfhmumhlzycbhptfjuodlgjxuxcggtotaxjlqbccghyplvtgrwwlhmriwnecdhjmbpzdaqgpyhinawvmxjyiptiroxtuwybcjjkqcirscdqbakpwdiabgirknpvlwmvspufpdqchvbqbspyznfuscidqcbtcvwsqgjjdfpnuhgpxkgikvagtbhnssycxpefsqxbcgtubdmtcojbzpcjvfoslunoiixxdakfczg"
# ) # "abcdefghijklmnoprqstvwuxyz"
