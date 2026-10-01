class Solution {
    public int[] getSumAbsoluteDifferences(int[] a) {
        int total = 0;
        int leftsum = 0; 
        int n = a.length;
        int[] ans = new int[n];
        

        for (int num : a) {
            total += num;  
        }
        
        for (int i = 0; i < n; i++) {
            
            int ls = (a[i] * i) - leftsum;
            
            
            int rs = (total - leftsum - a[i]) - ((n - i - 1) * a[i]);
            
            ans[i] = ls + rs;
            leftsum += a[i];
        }
        
        
        return ans;
    }
}