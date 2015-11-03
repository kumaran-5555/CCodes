using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}

class Program
{
    static void Main(string[] args)
    {
        Solution sol = new Solution();
        string s = "catsanddog";
        HashSet<string> dict = new HashSet<string>{ "cat", "cats", "and", "sand", "dog" };

        //Console.Write(sol.GenerateTrees(2));

        Console.ReadKey();



    }
}

