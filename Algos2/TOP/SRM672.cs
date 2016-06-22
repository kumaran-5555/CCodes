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

    class Tdetectived2
    {
        /// <summary>
        /// dfs solution, recursively try
        /// 
        /// </summary>
        /// <param name="s"></param>
        /// <returns></returns>
        /// 


        public int[] ans;
        public string[] s;
        public int n;
        public bool[] visisted;
   

        private void _Reveal(int persionId, int[] sl, int depth)
        {


            this.ans[persionId] = Math.Min(this.ans[persionId], depth);

            this.visisted[persionId] = true;
            
            int[] nsl = new int[this.n];
            Array.Copy(sl, nsl, this.n);

            int max = -1;
            // update suspicious level
            for(int i=0; i< this.n; i++)
            {
                nsl[i] = Math.Max(nsl[i], int.Parse(this.s[persionId][i].ToString()));
                if(this.visisted[i] == false)
                    max = Math.Max(max, nsl[i]);
                                
            }


            if(max == -1)
            {
                // all of them are interviewed
                this.visisted[persionId] = false;
                return;

            }

            // recurisve call 
            for(int i=0; i <this.n; i++)
            {
                if(this.visisted[i] == false && max == nsl[i])
                {
                    this._Reveal(i, nsl, depth+1);
                }
            }

            this.visisted[persionId] = false;


            return;






        
        }
        public int reveal(string[] s)
        {

            this.n = s[0].Length;

            this.ans = new int[n];
            this.s = s;
            this.visisted = new bool[this.n];
            int[] sl = new int[this.n];
            int rval = 0;
            

            for (int i = 0; i < this.n; i++)
            {
                visisted[i] = false;
                sl[i] = 0;
                ans[i] = n;
            }


            this._Reveal(0, sl, 0);


            for(int i=1; i<this.n; i++)
            {
                rval += (this.ans[i] * i);
            }


            return rval;


        }
    }
}



