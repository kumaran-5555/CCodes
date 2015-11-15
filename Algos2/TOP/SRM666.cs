using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class GoodString
{
    public string isGood(string s)
    {
        int aCount = 0, bCount = 0;

        for (int i = 0; i < s.Length; i++)
        {
            if(s[i] == 'a')
            {
                aCount += 1;
            }
            else
            {
                if (aCount <= 0)
                    return "Bad";
                else
                    aCount -= 1;

            }
            

        }

        if (aCount == 0)
            return "Good";

        return "Bad";

    }
}
