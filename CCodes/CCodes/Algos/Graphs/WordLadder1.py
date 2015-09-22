#!/usr/bin/python3


from collections import  deque
from collections import defaultdict
import time
import string
__author__ = 'kumaran'


class Solution():
    '''
        compute all nodes at distance i from source and minLength-i+1 from destination
        intersection of this gives all notes at position i all shorest path
        use parent information to create paths

    '''
    def bfs(self, start, end, isStartToEnd):
        self.chars = string.ascii_lowercase
        if isStartToEnd:
            wordsAtLevel = self.startToEnd
        else:
            wordsAtLevel = self.endToStart

        queue = deque()
        queue.append(start)
        visistedSet = set()
        # marker for identifying which level
        nodeLength = 0
        minLength = self.numOfNodes
        visistedSet.add(start)

        while queue:
            nodeLength += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                wordsAtLevel[nodeLength].add(node)
                for i in range(self.wordLength):
                    # replace i th char with all posibiblites
                    # if the modified string is in words, add it to queue
                    for c in self.chars:
                        w = node[:i]+c+node[i+1:]
                        if w == end:
                            wordsAtLevel[nodeLength + 1].add(w)
                            if minLength > nodeLength+1:
                                minLength = nodeLength+1
                        if w in self.nodes:
                            if isStartToEnd:
                                self.children[node].add(w)

                            if w not in visistedSet:
                                visistedSet.add(w)
                                queue.append(w)



        if minLength == self.numOfNodes:
            return 0
        return minLength

    def buildPaths(self, node, position, pathSoFar):
        if position == self.minLength:
            self.output.append(pathSoFar)
            return

        #consider only children that at correct position
        children = self.children[node].intersection(self.allPaths[position+1])
        for c in children:
            self.buildPaths(c, position+1, pathSoFar+[c])




    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        self.numOfNodes = len(dict) + 2
        self.nodes = set(dict)
        self.wordLength = len(start)
        self.output = []
        self.startToEnd = defaultdict(set)
        self.endToStart = defaultdict(set)
        self.children = defaultdict(set)

        #self.paths(start, end, self.bfs(start, end), [start])

        #return self.output
        self.minLength = self.bfs(start, end, True)
        if not self.minLength:
            return []

        if self.minLength == 2:
            return [[start,end]]

        self.bfs(end, start, False)




        self.allPaths = defaultdict(set)


        for i in range(1,self.minLength+1):
            self.allPaths[i] = self.startToEnd[i].intersection(self.endToStart[self.minLength-i+1])
        '''

            print(i, self.endToStart[i])

        for i in self.startToEnd:
            print(i, self.startToEnd[i])

        for i in self.allPaths:
            print(i, self.allPaths[i])
        '''
        self.buildPaths(start, 1, [start])

        return self.output


if __name__ == '__main__':
    s = Solution()
    start = time.time()
    #print(s.findLadders("hot", "dog", ["hot","dog"]))
    #print(s.findLadders("hit","cog",["hot","dot","dog","lot","log"]))
    #print(s.findLadders("a","c",["a","b","c"]))

    print((s.findLadders("cet", "ism", ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"])))
    print(time.time()-start)