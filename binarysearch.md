# Lowerbound
https://www.codingninjas.com/studio/problems/lower-bound_8165382?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries

```
public class Solution {
    public static int lowerBound(int []arr, int n, int val) {
        int low = 0;
        int high = arr.length-1;
        int resultIndex = -1;
        while(low<=high) {
            int mid = low + (high-low)/2;
            if(arr[mid]>=val) {
                // interim set and keep searching
                resultIndex = mid;
                high = mid-1;		
            }
            else
                low = mid+1;
        }
        return resultIndex;
    }
}
```
