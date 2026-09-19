class Solution {

    public int[][] imageSmoother(int[][] img) {

        int m = img.length;
        int n = img[0].length;

        int[][] arr = new int[m][n];

        for (int i = 0; i < m; i++) {

            for (int j = 0; j < n; j++) {

                int[] result = soother(i, j, img);

                int sum = result[0];
                int count = result[1];

                arr[i][j] = sum / count;
            }
        }

        return arr;
    }


    int[] soother(int r, int c, int[][] img) {

        int m = img.length;
        int n = img[0].length;

        int sum = img[r][c];
        int count = 1;


        // LT
        if (r - 1 >= 0 && c - 1 >= 0) {
            sum = sum + img[r - 1][c - 1];
            count++;
        }


        // T
        if (r - 1 >= 0) {
            sum = sum + img[r - 1][c];
            count++;
        }


        // RT
        if (r - 1 >= 0 && c + 1 < n) {
            sum = sum + img[r - 1][c + 1];
            count++;
        }


        // R
        if (c + 1 < n) {
            sum = sum + img[r][c + 1];
            count++;
        }


        // L
        if (c - 1 >= 0) {
            sum = sum + img[r][c - 1];
            count++;
        }


        // LB
        if (r + 1 < m && c - 1 >= 0) {
            sum = sum + img[r + 1][c - 1];
            count++;
        }


        // B
        if (r + 1 < m) {
            sum = sum + img[r + 1][c];
            count++;
        }


        // RB
        if (r + 1 < m && c + 1 < n) {
            sum = sum + img[r + 1][c + 1];
            count++;
        }


        return new int[]{sum, count};
    }
}