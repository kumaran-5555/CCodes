using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */



public class Solution95
{
    /// <summary>
    /// dp[i] - holds list of binary that are possible to get using 1-i numbers
    /// dp[i] - 
    ///         for (j in 1...n)
    ///             j.left = dp[j-1]
    ///             j.right = clone(dp[i-j],j+1)
    /// </summary>
    /// <param name="n"></param>
    /// <returns></returns>
    /// 

    private TreeNode CloneTree(TreeNode node, int offset)
    {
        if (node == null)
            return null;

        TreeNode newNode = new TreeNode(node.val + offset);
        newNode.left = CloneTree(node.left, offset);
        newNode.right = CloneTree(node.right, offset);

        return newNode;


    }
    public IList<TreeNode> GenerateTrees(int n)
    {
        Dictionary<int, List<TreeNode>> dp = new Dictionary<int, List<TreeNode>>();

        
        dp.Add(0, new List<TreeNode> { null });

        TreeNode node = new TreeNode(1);

        dp.Add(1, new List<TreeNode> { node });
        var righTrees = new List<TreeNode>();
        var leftTrees = new List<TreeNode>();

        for (int i = 2; i <= n; i++)
        {

            List<TreeNode> l = new List<TreeNode>();

            // j tracks the root
            for (int j = 1; j <= i; j++)
            {
                // cross all left tree and right trees

                dp.TryGetValue(j - 1, out leftTrees);
                dp.TryGetValue(i - j, out righTrees);
                // iterate leftTrees
                foreach (TreeNode left in leftTrees)
                {
                    // iterate through rightTrees

                    foreach (TreeNode _right in righTrees)
                    {
                        var right = this.CloneTree(_right, j);
                        TreeNode newNode = new TreeNode(j);
                        newNode.left = left;
                        newNode.right = right;

                        l.Add(newNode);

                    }
                }




            }
            dp.Add(i, l);

        }



        
        return dp[n];








    }
}