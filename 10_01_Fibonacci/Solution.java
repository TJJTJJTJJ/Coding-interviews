public class Solution {
    public int Fibonacci(int n) {
        if(n==0){
            return 0;
        }
        if(n==1){
            return 1;
        }
        
        int f1 = 0;
        int f2 = 1;
        int f3 = 0;
        for(int i=2;i<=n;i++){
            f3 = f1 + f2;
            f1 = f2;
            f2 = f3;
        }
        return f3;

    }
}