# References
https://www.youtube.com/watch?v=3Zv-s9UUrFM&pp=ygUMYXJyYXkgc3BpcmFs

```
import java.util.*;
public class Solution {
     public static int[] spiralMatrix(int [][]MATRIX) {
        int rows = MATRIX.length;
	    int cols = MATRIX[0].length;
	    int top = 0;
	    int bottom = rows -1;
	    int left = 0;
	    int right = cols -1;
        List<Integer> ans = new ArrayList<>();
        while(top<=bottom && left<=right) {
            // go left to right
            for(int i=left;i<=right;i++) 
                ans.add(MATRIX[top][i]);
            top++;

            // go right to bottom
            for(int i=top;i<=bottom;i++) 
                ans.add(MATRIX[i][right]);
            right--;

            if(top<=bottom) {	
                // go bottom to left
                for(int i=right;i>=left;i--) 
                    ans.add(MATRIX[bottom][i]);
                bottom--;
            }

            if(left <= right) {
                // go left to top
                for(int i=bottom;i>=top;i--) 
                    ans.add(MATRIX[i][left]);
                left++;
            }
        }
        return ans.stream().mapToInt(i->i).toArray();
    }	

}
```
