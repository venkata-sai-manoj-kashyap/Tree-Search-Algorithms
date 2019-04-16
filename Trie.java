class TrieNode{
    TrieNode[] children = new TrieNode[26];
    boolean isEndOfWord = false;
}

public class Trie {
    TrieNode root = new TrieNode();

    static int convertToIndex(char s){
        return (int) s - (int) 'a';
    }

    static char convertToChar(int x){
        return (char)(x + (int) 'a');
    }

    int insertString(String s){
        try{
            s = s.replace(" ", "");
            char[] str = s.toCharArray();
            TrieNode current = root;
            for(char x: str){
                int index = convertToIndex(x);
                if(current.children[index] == null)
                    current.children[index] = new TrieNode();
                current = current.children[index];
            }

            current.isEndOfWord = true;
            return 0;
        }

        catch (Exception e){
            e.printStackTrace();
            return -1;
        }
    }

    public boolean stringSearch(String s){
        try{
            TrieNode current = root;
            char[] str = s.toCharArray();
            for(char x: str){
                int index = convertToIndex(x);
                if(current.children[index] == null)
                    return false;

                current = current.children[index];
            }

            return current.isEndOfWord;
        }
        catch (Exception e){
            e.printStackTrace();
            return false;
        }
    }
}
