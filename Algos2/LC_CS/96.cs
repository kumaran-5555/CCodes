using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Solution96
{
    /// <summary>
    ///  dp solution
    /// dp[i] = holds number of BST that can be createed using i sorted numbers
    /// dp[i] = sum(dp[l] * dp[r]) for (j in  0...i) { l = j-1; r=i-j }
    /// </summary>
    /// <param name="n"></param>
    /// <returns></returns>
    public int NumTrees(int n)
    {
        int[] dp = new int[n+1];

        dp[0] = 0;
        dp[1] = 1;

        for (int i = 2; i <= n; i++)
        {
            int total = 0;
            // j tracks the root
            for(int j=1; j<=i; j++)
            {
                total += (dp[j - 1] * dp[i - j]);
            }

            dp[i] = total;
            
        }

        return dp[n];

    }
}