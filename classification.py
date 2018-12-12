import re
import mmap
class TrieNode: 
      
    # Trie node class 
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self): 
      
        # Returns new trie node (initialized to NULLs) 
        return TrieNode() 
  
    def _charToIndex(self,ch): 
          
        # private helper function 
        # Converts key current character into index 
        # use only 'a' through 'z' and lower case 
          
        return ord(ch)-ord('a') 
  
  
    def insert(self,key): 
          
        # If not present, inserts key into trie 
        # If the key is prefix of trie node,  
        # just marks leaf node 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
  
            # if current character is not present 
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 
  
        # mark last node as leaf 
        pCrawl.isEndOfWord = True
  
    def search(self, key): 
          
        # Search key in the trie 
        # Returns true if key presents  
        # in trie, else false 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                return False
            pCrawl = pCrawl.children[index] 
  
        return pCrawl != None and pCrawl.isEndOfWord 
  
# driver function 
def main(): 
  
    mylist1 = []
    with open('C:\\Users\\siddh\\Desktop\\codegrind2.0\\airport_cities.txt', 'r') as f:
         mylist1 = list(map(str.strip,f))
    final1 = [x.lower() for x in mylist1]

    # Trie object 
    cities = Trie()
  
    # Construct trie 
    for key in final1:
        key = re.sub('[^a-z]+','',key)
        cities.insert(key)
    
    mylist2 = []
    final2 = []
    with open('C:\\Users\\siddh\\Desktop\\codegrind2.0\\airport_codes.txt', 'r') as f2:
         mylist2 = list(map(str.strip,f2))

    for x in mylist2:
    	start = x.find('(')
    	end = x.find(')')
    	final2.append(x[start:end].lower())

    codes = Trie()

    # Construct trie 
    for key in final2:
        key = re.sub('[^a-z]+','',key)
        codes.insert(key)

    file = open('D:\\test\\Output.txt', 'r')
    lines = [line.lower() for line in file]
    with open('D:\\test\\lower.txt', 'w') as out:
        out.writelines(lines)

    with open('D:\\test\\lower.txt', 'r') as file:
        if 'flight' in file.read():
            category = 'airfare'
        else:
            category = 'nf'
            
    return category
if __name__ == '__main__': 
    main()
