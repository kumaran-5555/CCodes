using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class CombiningSlimes
{
    public int maxMascots(int[] a)
    {
        Array.Sort(a);

        int rval = 0;
        for(int i=0; i<a.Length-1; i++)
        {
            rval += (a[i] * a[i + 1]);
            a[i + 1] += a[i];


        }

        return rval;
    }
}