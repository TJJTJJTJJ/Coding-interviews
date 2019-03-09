// v-3.0
public class Solution {
    public int NumberOf1(int n) {
        int count = 0;
        int i = 1;
        while(i != 0){
            if( (n&i)!=0 ){
                ++count;
            }
            i <<= 1;
        }
        return count;
    }
}
// 注意,(n&i)!=0不能写成(n&i)==1，因为如果当前位为1，那么就等于2的m次方，如果当前为0，那么久等于0.
// v-4.0
public class Solution {
    public int NumberOf1(int n) {
        int count = 0;
        while( n !=0 ){
            count ++;
            n = n&(n-1);
        }
        return count;
    }
}