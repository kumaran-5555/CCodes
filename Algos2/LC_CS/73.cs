using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Solution
{
    public void SetZeroes(int[,] matrix)
    {

        int r, c;
        r = matrix.GetLength(0);
        c = matrix.GetLength(1);

        BitArray rowMap = new BitArray(r);
        BitArray colMap = new BitArray(c);

        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                if (matrix[i, j] == 0)
                {
                    rowMap.Set(i, true);
                    colMap.Set(j, true);
                }


            }
        }

        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                if (rowMap[i] || colMap[j])
                    matrix[i, j] = 0;


            }
        }




        return;


    }
}