# v-2 二分法
import java.util.ArrayList;
public class Solution {
    public int minNumberInRotateArray(int [] array) {
        if (array==null || array.length==0){
            return 0;
        }
        int p = 0;
        int q = array.length-1;
        if (array[p] < array[q]){
            return array[p];
        }
        
        if (array[p]==array[q]){
            return minNumberArray_equal(array, p, q);
        }
        return minNumberArray(array, p, q);
    }
    
    public int minNumberArray(int [] array, int p, int q){
        // 正常情况，前后两个递增数组
        // 结束条件
        if (q-p==1){
            return array[q];
        }
        
        int mid = (p+q)/2;
        if (array[p]<=array[mid]){
            return minNumberArray(array, mid, q);
        }
        else{
            return minNumberArray(array, p, mid);
        }
    }
    
    public int minNumberArray_equal(int [] array, int p, int q){
        // 特殊情况，array[p]==array[q]
        // 结束条件
        if (array[p]==array[q]){
            if (array[p+1]<array[p]){
                return array[p+1];
            }
            else{
                return minNumberArray_equal(array, p+1, q);
            }
        }
        else{
            return minNumberArray(array, p, q);
        }
    }
}


# v-2 二分法 优化了一些代码和边界条件

import java.util.ArrayList;
public class Solution {
    public int minNumberInRotateArray(int [] array) {
        if (array==null || array.length==0){
            return 0;
        }
        int p = 0;
        int q = array.length-1;
        // 特殊情况，没有发生旋转或者只有一个元素
        if (array[p] < array[q]||p==q){
            return array[p];
        }
        
        return minNumberArray_equal(array, p, q);
    }
    
    public int minNumberArray(int [] array, int p, int q){
        // 正常情况，前后两个递增数组
        // 结束条件
        if (q-p==1){
            return array[q];
        }
        
        int mid = (p+q)/2;
        if (array[p]<=array[mid]){
            return minNumberArray(array, mid, q);
        }
        else{
            return minNumberArray(array, p, mid);
        }
    }
    
    public int minNumberArray_equal(int [] array, int p, int q){
        // 特殊情况，array[p]==array[q]
        // 结束条件
        int mid = (p+q)/2;
        if (array[p]==array[q] && array[p]==array[mid]){
            if (array[p+1]<array[p]){
                return array[p+1];
            }
            else{
                return minNumberArray_equal(array, p+1, q);
            }
        }
        else{
            return minNumberArray(array, p, q);
        }
    }
}
