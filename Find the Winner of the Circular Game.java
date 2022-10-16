class Solution {
    public int findTheWinner(int n, int k) {
        
        if(k == 1)
            return n;
        
        if(n==1)
            return 0;
        
        
        return winner(n, k) + 1;
        
    }
    
    public int winner(int n, int k)
    {
        if(n == 1)
            return 0;
        else
        {
            //winner for n == winner for n-1 with offset k, and if result is greater than current n, it will start again at 0 (result % n)
            //works for when n = 0, so final result is for n starting from 0, which means add 1 to the final result
            int result = (winner(n-1, k) + k)%n; 
            return result;
        }
    }
}