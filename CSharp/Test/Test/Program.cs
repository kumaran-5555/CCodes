using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    interface Bike
    {
        void start(int key, int key2);


    }

    interface Bike2
    {
        int start(int key);
    }


    class BikeImplementation : Bike, Bike2
    {

        public void start(int key, int key2)
        {
            return;
        }


        public int start(int key)
        {
            return key;
        }

    }

    abstract class A
    {

        

        public void methodA()
        {
            Console.WriteLine("From class A method A");
        }

        protected void methodB()
        {
            Console.WriteLine("From class A method B");
        }
        public abstract void methodC(int a, int b);

    }



    class AImplementation : A, Bike, IDisposable
    {

        protected int x;

        public void start(int key, int key2)
        {
            this.methodB();
            return;
        }
        public override void methodC(int a, int b)
        {
            throw new NotImplementedException();
        }



        public AImplementation()
        {
            Console.WriteLine("In Constructor");
        }
        

        ~AImplementation()
        {
            Console.WriteLine("In Finalizer");
        }

        public void Dispose()
        {
            Console.Write("In Disposer");
            GC.SuppressFinalize(this);
        }
    }







    class Program
    {

        static void method1(A b)
        {
            Console.Write("");
        }
        static void Main(string[] args)
        {

            using (AImplementation a = new AImplementation())
            {
                a.methodB();
                a.x = 10;


                Console.WriteLine("Object Created");
            }


            GC.Collect();

            Console.ReadKey();






        }
    }
}
