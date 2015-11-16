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

        for(int i=0; i<s.Length; i++)
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
