// 100/100
class Solution {
    public int solution(int[] A) {
         int r = 0;
        //xor each value.. odd one will be left
        for(int i=0;i<A.length;i++)
            r ^=A[i];
 
    return r;
    }
}