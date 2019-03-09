// v-0
public class Solution {
    /**
    * 二维数组中的查找
    * @param target 目标值
    * @param array 二维数组
    * @param boolean
    */
    public boolean Find(int target, int [][] array) {
        // 空指针 或者 {{}} 多行0列
        if (array == null || array[0].length <= 0 ){
            return false;
        }
        int rows = array.length;
        int col = array[0].length;
        // 数组的最小最大值
        if ( array[0][0] > target || array[rows-1][col-1] < target ){
            return false;
        }
        // 递归去掉左上角和右下角区域元素
        return Find2( array, 0, 0, rows-1, col-1, target);
    }
    /*
    * 递归调用
    * @param [i1][j1] 待查找数组的左上角坐标
    * @param [i2][j2] 待查找数组的右下角坐标
    * @param array 二维数组
    * @param target 目标值
    */
    public boolean Find2(int [][] array, int i1, int j1, int i2, int j2, int target ){
        int i = i1;
        int j = j1;
        //数组的最小最大值
        if ( array[i1][j1] > target || array[i2][j2] < target ){
            return false;
        }
        
        // 找到对角线上合适的元素
        while ( i <= i2 && j <= j2 ){
            if ( array[i][j] == target ){
                return true;
            }
            if (array[i][j] < target){
                ++i;
                ++j;
            } else {
                break;
            }
        }
        // 希望得到的i,j是小于target中最大的数
        --i;
        --j;
        // 扁长并且已经遍历到最后一行
        if ( i==i2 ){
            return Find2(array, i1, j+1, i2, j2, target);
        }
        // 竖长并且已经遍历到最后一列
        if ( j==j2 ){
            return Find2(array, i+1, j1, i2, j2, target );
        }
        // 遍历到中间
        return Find2(array, i+1, j1, i2, j, target) || Find2(array, i1, j+1, i, j2, target);
        
    }
}

// v-1
public class Solution {
    /**
     * 二维数组中的查找
     * @param target 目标值
     * @param array 二维数组
     * @return boolean
     */
    public boolean find(int target, int[][] array) {
        if (array == null) {
            return false;
        }
        int rows = array.length;
        int columns = array[0].length;

        int i = rows - 1;
        int j = 0;
        while (i >= 0 && j < columns) {
            if (array[i][j] == target) {
                return true;
            }
            if (array[i][j] < target) {
                ++j;
            } else {
                --i;
            }
        }
        return false;
    }
}