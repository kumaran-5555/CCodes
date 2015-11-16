using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class PointDistance
{
    private double distance(int x1, int y1, int x2, int y2)
    {
        return Math.Sqrt(Math.Pow((x1 - x2), 2) + Math.Pow((y1 - y2), 2));
    }


    public int[] findPoint(int x1, int y1, int x2, int y2)
    {

        Random rand = new Random();

        while (true)
        {

            int x3 = rand.Next(-100, 100);
            int y3 = rand.Next(-100, 100);

            if (this.distance(x1, y1, x3, y3) > this.distance(x2, y2, x3, y3))
                return new int[] { x3, y3 };

        }



    }
}

class OrderOfOperationsDiv2
{
    /// <summary>
    /// n^3 idea, from the partial order, find the next element
    /// which differs in min number of ones and add that to the partial
    /// order
    /// </summary>
    /// <param name="s"></param>
    /// <returns></returns>
    public int minTime(string[] s)
    {

        int partialOrder = 0;
        int width = s[0].Length;
        int cost = 0;
        int n = s.Length;

        int i, j, k;
        bool[] used = new bool[n];

        for(i=0;i< n;i++)
        {
            used[i] = false;

        }

        // iterate n times
        for(i=0;i< n;i++)
        {
            // find the minimal differing entry and add
            int minDiff = width+1;
            int minIdx = -1;
            for (j = 0; j< n;j ++)
            {
                if (used[j] == true)
                    continue;

                // compute bit difference/cost
                int difference = 0;

                for (k = 0; k < width; k++)
                {
                    if ((partialOrder & (1 << k)) == 0 && s[j][k] == '1')
                        difference += 1;
                }


                if(difference < minDiff)
                {
                    minDiff = difference;
                    minIdx = j;
                    
                }

            }

            used[minIdx] = true;
            // gaurantee that minimum will always be found
            for(k=0;k<width;k++)
            {
                if (s[minIdx][k] == '1')
                    partialOrder |= (1<< k);
            }

            cost += (minDiff* minDiff);

            //  if all bits are set, return
            if (partialOrder == (1 << (width + 1)) - 1)
                return cost;
            

        }


        return cost;


    }

}


class ShopPositions
{
    public int maxProfit(int buildings, int floors, int[] profit)
    {



        /// dp[i,j] = holds the profit realized till i-1 building assuming middle and right building floors as j
        /// right[i] = holds number buildings assumed from right building, for corresponding dp[,j] 
        int[][,] dp = new int[buildings+1][,];
        int i, j, k, m;
        for (i = 0; i < buildings+1; i++)
            dp[i] = new int[floors + 1, floors + 1];



        ///dp[i][j,k] = holds profit realized till build i-1 with j shops from building i-1 and k shops from building i
        /// dp[i+1][k,m] = max(profit[i][j+k+m] * k  + dp[i][j,k]) for m=0-floors


        for (i = 1; i < buildings+1; i++)
        {
            /// for all combinations of building i-1,
            /// try combinations
            for (m = 0; m < floors+1; m++)
            {
                for (k = 0; k < floors+1; k++)
                {
                    for (j = 0; j < (i == 1 ? 1 : floors+1); j++)
                    {
                        if (k + m + j == 0)
                            continue;

                        //Console.WriteLine(string.Format("{0} {1} {2} {3} {4}", i, j, k, m, dp[i][k, m]));
                        dp[i][k, m] = Math.Max(dp[i][k, m], profit[(i - 1) * (3 * floors) + j + k + m - 1] * (k) + dp[i - 1][j, k]);
                        //Console.WriteLine(string.Format("{0} {1} {2} {3} {4} {5}", i, j, k, m, dp[i][k, m], (i - 1) * (3 * floors) + j + k + m - 1));
                    }
                }

            }
        }

        int rval = 0;

        for(i=0;i<floors+1;i++)
        {
            rval = Math.Max(rval, dp[buildings][i, 0]);

        }


        





        return rval;
    }

}

