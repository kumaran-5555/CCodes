using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Solution140
{
    private int n;
    private string s;
    private ISet<string> wordDict;
    // dp[i] = holds the list of word broken strings
    private Dictionary<int, IList<string>> dp;


    /// <summary>
    /// returns word broken list 
    /// </summary>
    /// <param name="pos"> position in the target string </param>
    /// <returns> list of workbroken list for the string of end to till pos</returns>
    private IList<string> _Wordbreak(int pos)
    {
        
        IList<string> rval = new List<string>();
        if (this.dp.ContainsKey(pos))
        {

            this.dp.TryGetValue(pos, out rval);
            return rval;
        }



        // should not be called with

        for (int i = pos; i < this.n; i++)
        {
            var substr = this.s.Substring(pos, i - pos + 1);
            if (!this.wordDict.Contains(substr))
            {
                // can't break at i
                continue;
            }

            if (i == this.n - 1)
            {
                // recusion bottoms up
                rval.Add(substr);
                continue;
            }
            else
            {
                foreach (string s in this._Wordbreak(i + 1))
                {
                    rval.Add(substr + " " + s);
                }

            }

        }

        this.dp.Add(pos, rval);

        return rval;
    }

    public IList<string> WordBreak(string s, ISet<string> wordDict)
    {

        this.n = s.Length;
        this.s = s;
        this.wordDict = wordDict;
        this.dp = new Dictionary<int, IList<string>>();

        var rval = this._Wordbreak(0);


        return rval;

    }


}

