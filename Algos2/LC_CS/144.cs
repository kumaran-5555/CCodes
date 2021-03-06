﻿using System;
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


public class Solution144
{
    public IList<int> PreorderTraversal(TreeNode root)
    {

        List<int> rval = new List<int>();

        Stack<TreeNode> stack = new Stack<TreeNode>();

        if (root == null)
        {
            return rval;
        }
        stack.Push(root);
        

        while (stack.Count > 0)
        {
            var node = stack.Pop();
            rval.Add(node.val);

            if(node.right!=  null)
            {
                stack.Push(node.right);

            }

            if(node.left != null)
            {
                stack.Push(node.left);

            }
            
        }

        return rval;




    }
}