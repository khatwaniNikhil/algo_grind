// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/description/
public static boolean isValid(String word){
        int hyphen = 0;
        for(int i=0;i<word.length();i++) {
            char ch = word.charAt(i);
            // valid char
            if((Character.isLowerCase(ch) && Character.isLetter(ch)))
                continue;
            if (ch == '-') {
                if(++hyphen<=1) {
                    //hyphen should be sorrounded by lowercase alphabets
                    boolean isSurroundedByLetters = !(i - 1 < 0 || !(Character.isLetter(word.charAt(i-1)) && Character.isLowerCase(word.charAt(i-1)) ) || i + 1 >= word.length()
                            || !(Character.isLetter(word.charAt(i+1))&& Character.isLowerCase(word.charAt(i+1))));
                    if(isSurroundedByLetters)
                        continue;
                }
            }
            // punctuation at end
            if((ch == '.' || ch == '!' || ch == ',' || ch == '?') && i == word.length() - 1)
                continue;
            return false;
        }
        return true;   //all the conditions satisfied
    }

    public static int howMany(String sentence) {
        Pattern pattern = Pattern.compile("\\s+");
        //Retrieving the matcher object
        Matcher matcher = pattern.matcher(sentence);
        //Replacing all space characters with single space
        sentence = matcher.replaceAll(" ");
        String[] arr = sentence.trim().split("\\s+");
        int ans = 0;
        for(String s: arr)
        {
            if(isValid(s))
            {
                ans++;
                System.out.println(s);
            }
        }
        return ans;
    }
