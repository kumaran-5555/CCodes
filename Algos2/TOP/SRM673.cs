using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class BearSong
{
    public static int countRareNotes(int[] notes)
    {
        HashSet<int> unseen = new HashSet<int>();

        foreach (int i in notes)
        {
            if (unseen.Contains(i))
            {
                unseen.Remove(i);
            }
            else
            {
                unseen.Add(i);
            }
        }

        return unseen.Count();

    }
}


class BearSlowlySorts
{
    public static int minMoves(int[] w)
    {
        int min = w[0];
        int max = w[0];

        bool sorted = true;
        int n = w.Length;

        // is it sorted
        for (int i = 1; i < w.Length; i++)
        {
            if (w[i] < min)
                min = w[i];
            if (w[i] > max)
                max = w[i];
        }
        for(int i=1; i< n; i++)
        { 
            if (w[i - 1] > w[i])
            {
                sorted = false;
                break;
            }
        }
        if (sorted)
            return 0;

        if (w[0] == min || w[n - 1] == max)
            return 1;

        if (w[0] == max && w[n - 1] == min)
            return 3;

        return 2;


    }

    
}


