using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class IsItASquare
{
    public string isSquare(int[] x, int[] y)
    {

        int[] idx = new int[] { 0, 1, 2, 3 };



        return "";



    }
}

class AnArray
{

    private int[] A;


    private Dictionary<int, int>[,] dp;


    private int gcd(int a, int b)
    {
        int min = Math.Min(a, b);
        int max = Math.Max(a, b);

        while (max % min != 0)
        {
            var temp = max % min;

            max = min;
            min = temp;
        }

        return min;
        
    }

    private int f(int pos, int k, int num)
    {


        if (dp[pos, num] == null)
            dp[pos, num] = new Dictionary<int, int>();

        if(dp[pos,num].ContainsKey(k))
            return dp[pos,num][k];
        
        if (num == 0)
        {
            // we have got all numberrs, return 1 only if k == 1
            if (k == 1)
            {
                dp[pos,num][k] = 1;
                return 1;
            }
            else
            {
                dp[pos,num][k] = 0;
                return 0;
            }

        }

        if(pos == 0)
        {
            // we don't have any number to use
            dp[pos,num][k] = 0;
            return 0;
        }


        //consider this
        var total = this.f(pos-1, k/this.gcd(this.A[pos-1], k), num-1);

        // skipping
        total += this.f(pos-1, k, num);

        dp[pos,num][k] = total;

        
        return total;


    }

    public int solveProblem(int[] A, int K)
    {
        this.A = A;
        this.dp = new Dictionary<int, int>[2001, 4];

        var rval = this.f(A.Length, K, 3);
        return rval;



    }


}
