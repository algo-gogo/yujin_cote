'''
또 지대 짱나는 카카오 문제
노래 가사에 특정 키워드가 몇 개 포함되어 있는지 검색하는 프로그램.
와일드카드;;; 아놔 ㅋㅋ 역시고만고만하게내지않죠?

예를 들어 "fro??"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는 매치되지 않습니다.

가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때,
각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해 주세요.

단어 자체의 중복은 없는걸로 가정함.
'''

class Node(object):
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.children = {}

    def count_string(self, index):
        next_child = [self]

        for i in range(index):
            for child in next_child:
                next_child.append(child)

        count = 0
        for child in next_child:
            if child.value != None:
                count += 1

        return count




class Trie(object):
    def __init__(self):
        self.root = Node()

    def print_all(self, next_nodes):
        if(len(next_nodes) == 0 ):
            return

        for node in next_nodes:
            current = node
            if current.value: print( current.value )

            next_nodes = []

            for child in current.children:
                next_nodes.append(current.children[child])

            self.print_all(next_nodes)


    def insert(self, string):
        current = self.root

        for char in string:
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]
        current.value = string

    def search(self, string, index=0, candidates=[], prefix=0, suffix=0 ):
        # current = self.root

        # print( index )

        if index < prefix:
            if(len(candidates)>0):
                next_node = []
                for node in candidates:
                    current = node
                    for child in current.children:
                        next_node.append(current.children[child])

                return self.search(string, index+1, next_node, prefix, suffix)

        found = 0

        for current in candidates:
            node = current
            for char_index in range(index, len(string)-suffix):
                if string[char_index] in node.children:
                    node = node.children[string[char_index]]
                else:
                    break

            if suffix > 0:
                found += node.count_string(suffix)
            elif node.value == None:
                continue
            else:
                found += 1
            print(node.value)
        return found

    # def search_count(self, string):
    #     current = self.root

    #     for char in string:
    #         if char in current.children:
    #             current = current.children[char]
    #         else:
    #             return None

    #     if current.value == None:
    #         return None
    #     return current.count

    

def find_wildcard_start(word, start, end, last=-1):
    if(word[len(word)-1]) != "?":
        return 0
    mid = (start + end) // 2

    if( start>end ):
        return last
    elif( word[mid] == "?" ):
        last = mid
        return find_wildcard_start(word, start, mid-1, last)
    else:
        return find_wildcard_start(word, mid+1, end, last)

def find_wildcard_end(word, start, end, last=-1):
    if(word[0]) != "?":
        return 0

    mid = (start + end) // 2

    if( start>end ):
        return last
    elif( word[mid] == "?" ):
        last = mid
        return find_wildcard_end(word, mid+1, end, last)
    else:
        return find_wildcard_end(word, start, mid-1, last)

def check(word, query, start=0):
    # print( query, index )
    if len(word) != len(query):
        return False

    for i in range(start,len(word)):
        if query[i] == "?":
            return True
        elif query[i] != word[i]:
            return False

    return True

def solution(words, queries):
    answer = []
    trie = Trie()

    for word in words:
        trie.insert(word)
        
        # print(query)
        # count = 0
        # index = 0

        # if( query[0] == "?" ):
        #     index = find_wildcard_end(query, 0, len(query)-1) + 1

        # for word in words:
        #     if (check(word, query, index)):
        #         count += 1

        # answer.append(count)

    trie.print_all([trie.root])
    print(find_wildcard_end("?????", 0, len("?????")-1))
    trie.search("?????", 0, [trie.root], find_wildcard_end("?????", 0, len("?????")-1)+1, 0)
    trie.search("frodo", 0, [trie.root], 0, 4)
    # print(Trie)

    return answer

print( solution(
    ["frodo", "front", "frost"],
    # ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]
    )
)