using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class BearDartsDiv2
{
    /// <summary>
    /// same solution works for div1 :)
    /// </summary>
    /// <param name="w"></param>
    /// <returns></returns>
    public long count(int[] w)
    {

        long rval = 0;

        Dictionary<int, Dictionary<int, int>> multiplicationCount = new Dictionary<int, Dictionary<int, int>>();
        Dictionary<int, Dictionary<int, int>> divisionCount = new Dictionary<int, Dictionary<int, int>>();


        long limit = 10000000;

        int n = w.Length;

        int i, j;

        for (i = 1; i < n-2; i++)
        {
            multiplicationCount.Add(i, new Dictionary<int, int>());
            for (j = 0; j < i; j++)
            {
                var prod = w[j] * w[i];

                if (prod > limit)
                    continue;

                if (multiplicationCount[i].ContainsKey(prod))
                    multiplicationCount[i][prod] += 1;
                else
                    multiplicationCount[i][prod] = 1;

                

            }

        }


        for(i=n-2; i>1; i--)
        {

            divisionCount.Add(i, new Dictionary<int, int>());
            for(j=n-1; j > i; j--)
            {
                if (w[j] % w[i] != 0)
                    continue;
                var div = w[j] / w[i];

                if (divisionCount[i].ContainsKey(div))
                    divisionCount[i][div] += 1;
                else
                    divisionCount[i][div] = 1;
                

            }
        }


        for (i = 1; i < n - 2; i++)
        {
            var prod = multiplicationCount[i];
            for(j=i+1; j < n-1; j++)
            {
                var div = divisionCount[j];

                foreach(var key in prod.Keys.Intersect(div.Keys))
                {
                    rval += (prod[key] * div[key]);

                }


            }
        }



        return rval;

    }
}


class TreeCutCount
{
    private Dictionary<int, long>[,] dp;
    private int h;
    private int w;
    private int mod;

    /// <summary>
    /// Dictionary<int,int> dp[i][mask] - maps treeCount, numOfWays after height i and next rows state is mask
    /// mask - a bit is set if it has cut tree on top of it
    /// each recursion, create mask for the new level using this rows mask and recurse
    /// find out all next stages and proceed to next heigh
    /// </summary>
    /// <param name="H"></param>
    /// <param name="W"></param>
    /// <param name="mask"></param>
    /// <returns></returns>
    private void f(int i)
    {
        if (i >= this.h)
            return;

        for (int config = 0; config < (1 << this.w); config++)
        {
            for (int m = 0; m < (1 << this.w); m++)
            {
                if (dp[i, m] == null)
                    // this state is not achievable
                    continue;


                int mask = 0;

                // update mask
                // config is the pattern in the current row
                // 1 - means try right
                // 0 - means try left
                // mask, 1 - tree already covered, 0 - empty

                int count = 0;
                int b = 0;
                while (b < this.w)
                {
                    int bit = 1 << b;

                    if ((m & bit) > 0)
                    {
                        // current position is alredy covered
                        b += 1;
                        continue;
                    }

                    if (b < this.w - 1 && (m & (1 << (b + 1))) == 0)
                    {
                        // right is posible
                        if ((config & bit) > 0)
                        {
                            // right is prefered
                            count += 1;
                            b += 2;
                            continue;

                        }
                        else
                        {
                            // down is prefered
                            if (i == h - 1)
                            {
                                // down is not possible
                                // do right
                                count += 1;
                                b += 2;
                                continue;

                            }
                            else
                            {
                                mask |= bit;
                                count += 1;

                            }
                        }

                    }
                    else
                    {
                        // right is not possible
                        if ((config & bit) > 0)
                        {
                            // right prefered but right is not possible                            
                            if (i == h - 1)
                            {
                                // down is also not possible
                                ;
                            }
                            else
                            {
                                // down
                                mask |= bit;
                                count += 1;

                            }
                        }
                        else
                        {
                            // down is prefered
                            if (i == h - 1)
                            {
                                // down is not possible
                                ;

                            }
                            else
                            {
                                mask |= bit;
                                count += 1;

                            }
                        }



                    }
                    b += 1;

                }




                if (dp[i + 1, mask] == null)
                    dp[i + 1, mask] = new Dictionary<int, long>();

                foreach (int k in dp[i, m].Keys)
                {

                    // update tree count
                    if (dp[i + 1, mask].ContainsKey(count + k))
                        dp[i + 1, mask][count + k] = (dp[i + 1, mask][count + k] + dp[i, m][k]) % this.mod;
                    else
                        dp[i + 1, mask][count + k] = dp[i, m][k];


                }

            }

        }

        f(i + 1);

    }

    public long TreeCut(int W, int H, int Mod)
    {
        this.dp = new Dictionary<int, long>[H + 1, 1 << W];
        this.h = H;
        this.w = W;
        this.mod = Mod;

        dp[0, 0] = new Dictionary<int, long> { { 0, 1 } };

        this.f(0);

        long rval = 0;

        foreach (int t in dp[this.h, 0].Keys)
        {
            rval = (rval + ((dp[this.h, 0][t] * t) % this.mod)) % this.mod;

        }


        return rval;

    }

}
