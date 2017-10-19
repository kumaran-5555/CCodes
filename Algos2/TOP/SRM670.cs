using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Drbalance
{

    private int numOfNegatives(StringBuilder s)
    {
        int plus = 0;
        int minus = 0;
        int rval = 0;

        for (int i = 0; i < s.Length; i++)

        {
            if (s[i] == '+')
                plus++;
            else if (s[i] == '-')
                minus++;

            if (plus - minus < 0)
                rval++;

        }

        return rval;


    }
    public int lesscng(string s, int k)
    {
        StringBuilder str = new StringBuilder(s);

        int rval = this.numOfNegatives(str);

        bool addMinus = false;

        if (rval == k)
            return 0;

        if (rval < k)
            addMinus = true;

        rval = 0;
        for(int i=0; i<str.Length; i++)
        {
            if (this.numOfNegatives(str) == k)
                break;
            if(addMinus && str[i] == '+')
            {
                str[i] = '-';
                rval += 1;
                if (this.numOfNegatives(str) > k)
                {
                    str[i] = '+';
                    rval -= 1;
                }
                
            }
            else if(str[i] == '-')
            {
                str[i] = '+';
                rval += 1;
                if(this.numOfNegatives(str)<k)
                {
                    str[i] = '-';
                    rval -= 1;
                }

            }



        }

        return rval;

    }
}


class Cdgame
{
    public int rescount(int[] a, int[] b)
    {

        HashSet<int> outcomes = new HashSet<int>();



        int n = a.Length;

        int sumA = 0, sumB = 0;
        int i, j;
        for (i=0; i< n; i++)
        {
            sumA += a[i];
            sumB += b[i];
        }

        for (i = 0; i < n; i++)
        {
            for (j = 0; j < n; j++)
            { 
                var newA = sumA - a[i] + b[j];
                var newB = sumB - b[j] + a[i];
                outcomes.Add(newA * newB);

            }

        }

        return outcomes.Count;

    }
}


