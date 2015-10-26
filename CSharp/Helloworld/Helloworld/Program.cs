using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;


namespace Heap
{

    class IntComparer : IComparer<int>
    {
        public int Compare(int x, int y)
        {
            return x-y;
        }       
    }

    public class MinHeap<TKey, TValue>
    {

        private List<KeyValuePair<TKey, TValue>> list;
        public int count
        {
            get; private set;
        }
        

        private IComparer<TKey> comp;

        
        
        public MinHeap(IComparer<TKey> comp)
        {
            this.count = 0;
            this.comp = comp;
            this.list = new List<KeyValuePair<TKey, TValue>>();
        }
        
        ~MinHeap()
        {
            ;
        }

        public void Add(TKey key, TValue value)
        {

            list.Add(new KeyValuePair<TKey, TValue>(key, value));
            count++;

            HeapifyEndToStart();

            

        }

        public KeyValuePair<TKey, TValue> PeekMin()
        {
            if(count > 0)
            {
                return list[0];
            }

            return default(KeyValuePair<TKey, TValue>);

        }

        public KeyValuePair<TKey,TValue> PopMin()
        {
            if (count == 0)
                return default(KeyValuePair<TKey, TValue>);

            var rVal = list[0];
            
            if(count == 1)
            {
                list.RemoveAt(0);
                count--;
                return rVal;
            }

            var temp = list.Last();
            list.RemoveAt(list.Count - 1);
            list[0] = temp;
            count--;
            HeapifyStartToEnd();
            

            return rVal;
        }

        public KeyValuePair<TKey,TValue> PopMinWithReplace(TKey key, TValue value)
        {
            if (count == 0)
                return default(KeyValuePair<TKey, TValue>);

            var rVal = list[0];


            list[0] = new KeyValuePair<TKey, TValue>(key, value);
            HeapifyStartToEnd();

            return rVal;
        }


        private void HeapifyEndToStart()
        {
            for(int i=(list.Count-2)/2; i >=0; i--)
            {
   

                var parentIdx = i;
                if((2*i+1) < list.Count && comp.Compare(list[parentIdx].Key, list[2*i+1].Key) > 0)
                {
                    parentIdx = 2 * i + 1;
                }

                if ((2*i+2) < list.Count && comp.Compare(list[parentIdx].Key, list[2*i+2].Key) > 0)
                {
                    parentIdx = 2 * i + 2;
                }

                if (parentIdx != i)
                {
                    var temp = list[parentIdx];
                    list[parentIdx] = list[i];
                    list[i] = temp;
                }

            }

        }

        private void HeapifyStartToEnd()
        {
            // we assume heap property is maintained expcept for the 
            // first element

            for(int i=0; (2*i+1)<list.Count; i++)
            {
                
                var smallestIdx = i;
                if(2*i+1 < list.Count && comp.Compare(list[smallestIdx].Key, list[2*i+1].Key) > 0)
                {
                    smallestIdx = 2 * i + 1;
                }

                if(2*i+2< list.Count && comp.Compare(list[smallestIdx].Key, list[2*i+2].Key) > 0)
                {
                    smallestIdx = 2 * i + 2;
                }

                if(smallestIdx != i)
                {
                    var temp = list[i];
                    list[i] = list[smallestIdx];
                    list[smallestIdx] = temp;
                }
            }



        }


        

        

    }
    class HeapTest
    {
        static void Main()
        {
            var heap = new MinHeap<int, int>(new IntComparer());

            for (int i = 100; i > 0; i--)
            {
                heap.Add(i, i);
            }

            while (heap.count > 50)
            {
                Console.Write(string.Format("Value {0}\n", heap.PopMin().Key));
            }

            for(int i=200; i>100;i--)
            {
                heap.Add(i, i);
            }

            while (heap.count > 0)
            {
                Console.Write(string.Format("Value {0}\n", heap.PopMin().Key));
            }


            Console.ReadKey();
        }
    }
}
