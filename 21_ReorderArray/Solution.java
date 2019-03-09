//解法1：不保序
public class Solution {
    public void reOrderArray(int [] array) {
        if (array==null||array.length==0){
            return;
        }
        int pStart = 0;
        int pEnd = array.length-1;
        while(pStart<pEnd){
            while(pStart<pEnd&&(array[pStart]&1)!=0){
                pStart++;
            }
            while(pStart<pEnd&&(array[pEnd]&1)==0){
                pEnd--;
            }
            if(pStart<pEnd){
                int tmp = array[pStart];
                array[pStart] = array[pEnd];
                array[pEnd] = tmp;
            }
        }
        
    }
}
// 解法3：
import java.util.Arrays;
public class Solution {
    public void reOrderArray(int [] array) {
        if (array==null||array.length==0){
            return;
        }
        
        int numOfOdd = 0;
        int[] bak = Arrays.copyOf(array, array.length);
        int p1 = 0, p3 = 0;
        int p2 = array.length-1;
        int p4 = p2;
        for(int i=0;i<array.length;i++){
            if((bak[p1]&1)==1){
                array[p3] = bak[p1];
                p3++;
            }
            p1++;
            if((bak[p2]&1)==0){
                array[p4] = bak[p2];
                p4--;
            }
            p2--;
        }
    }
}

// 解法2留给python