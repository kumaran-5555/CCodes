using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;

namespace srm1076
{
    class SRM1076
    {

        public string decrypt(string a, string b, string y)
        {
            Dictionary<char, char> map = new Dictionary<char, char>();
            BitArray aMap = new BitArray(26);
            BitArray bMap = new BitArray(26);

            for (int i = 0; i < b.Length; i++)
            {
                if (map.ContainsKey(b[i]))
                    continue;

                map.Add(b[i], a[i]);
                aMap.Set((int)(a[i] - 'A'), true);
                bMap.Set((int)(b[i] - 'A'), true);

            }

            if(map.Count == 25)
            {
                char aMiss = ' ';
                char bMiss = ' ';
                for(int i=0;i <26; i++)
                {
                    if (!aMap[i])
                        aMiss = (char)(i + 'A');

                    if (!bMap[i])
                        bMiss = (char)(i + 'A');


                      
                }

                map.Add(bMiss, aMiss);

            }

            string output = "";

            for(int i=0; i < y.Length; i++)
            {
                if (!map.ContainsKey(y[i]))
                    return "";

                output = string.Concat(output, map[y[i]]);

            }

            return output;

        }



    }
}



