# references
https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014

# Notes
1. also known as digital tree, radix tree, prefix tree
2. primarily used for prefix matching string search
3. each node is comprised of value and array of references. In english words modeling -
with possible childs like 26 in english words set(TrieNode[26] each node contains char determined via array position(0 to 26 => a to z)
4. root node value part is empty.
6. each node represents prefix of word(a to z char) or end of word 
7. words can be searched/added by traversing the tree branch path.

## TrideNode Class
```
class TrieNode {
  boolean isWord;
  TrieNode[] childs = new TrieNode[26];

  TrieNode() {}

  boolean containsKey(char ch) {
        return (childs[ch - 'a'] != null); 
  }
  
  TrieNode get(char ch) {
      return childs[ch-'a']; 
  }
  
  void put(char ch) {
        childs[ch-'a'] = new TrieNode; 
  }
  
  void setIsWord() {
        isWord = true; 
  }
  
  boolean isWord() {
        return isWord; 
  }
}
```

```
class Trie {
  TrieNode root = new TrieNode();

  // traverse by char and insert if not already present. At end, mark isWord
  public void insert(String word) {
    TrieNode current =  root; 
    for(Char nextChar: word.toCharArray()) {
        if(!current.containsKey(nextChar) {
             current.put(nextChar);
        }
        current = current.get(nextChar);
    }
    current.setIsWord();
  }

//Returns if the word is in the trie
public static boolean search(String word) {
      TrieNode current = root; 
      for(char ch: word.toCharArray()) {
          if(!current.containsKey(ch) {
              return false; 
          }
          current = current.get(ch); 
      }
      if(node.isWord()) {
          return true; 
      }
      return false; 
  }

    //Returns if there is any word in the trie that starts with the given prefix
    public static boolean startsWith(String prefix) {
        Node current = root; 
        for(char ch: prefix.toCharArray()) {
            if(!current.containsKey(ch)) {
                return false; 
            }
            node = node.get(ch); 
        }
        return true; 
    }

  public static void insert(String word) {
       Trie trie = new Trie();
  }
}
