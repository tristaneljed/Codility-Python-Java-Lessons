//100%
class Solution {
    public int solution(int[] A) {
        int[] store = new int[A.length];
        store[0] = A[0];
        for (int i = 1; i < A.length; i++) {
            store[i] = store[i-1];
            for (int minus = 2; minus <= 6; minus++) {
                if (i >= minus) {
                    store[i] = Math.max(store[i], store[i - minus]);
                } else {
                    break;
                }
            }
            store[i] += A[i];
        }
        return store[A.length - 1];
    }
}