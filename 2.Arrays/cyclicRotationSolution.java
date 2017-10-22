    private static int[] cyclicRotationSolution(int[] A, int K) {
        int[] rotated = new int[A.length];
        for (int i = 0; i < A.length; i++) {
            int newPos = (i + K) % A.length;
            rotated[newPos] = A[i];
        }
        return rotated;
    }