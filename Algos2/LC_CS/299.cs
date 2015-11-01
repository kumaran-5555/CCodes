using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Solution299
{
    public string GetHint(string secret, string guess)
    {

        int cows = 0;
        int bulls = 0;
        Dictionary<char, int> count = new Dictionary<char, int>();

        for(int i=0; i < secret.Length; i++)
        {
            if (secret[i] == guess[i])
            {
                bulls += 1;

            }
            else
            {
                if (count.ContainsKey(secret[i]))
                {
                    count[secret[i]] += 1;
                }
                else
                {
                    count.Add(secret[i], 1);
                }

            }

        }

        for (int i = 0; i < secret.Length; i++)
        {
            if(guess[i] != secret[i] && count.ContainsKey(guess[i]) && count[guess[i]] > 0)
            {
                count[guess[i]] -= 1;
                cows += 1;
            }
        }


        return string.Format("{0}A{1}B", bulls, cows);

    }
}