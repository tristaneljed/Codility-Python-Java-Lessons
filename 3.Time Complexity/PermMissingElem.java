 import java.util.*;

// 100/100
class Solution {
    public int solution(int[] A) {
        if (A.length == 0) {
            return 1;
        }
        Arrays.sort(A);
        for (int i = 0; i < A.length; i++) {
            if (A[i] != i + 1) {
                return i + 1;
            }
        }
        return A.length + 1;
    }
}