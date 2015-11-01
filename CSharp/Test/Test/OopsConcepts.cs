using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace abstractClass
{
    abstract class Shape
    {
        public double Area()
        {
            return 0.0;
        }

        public abstract double Area2();
        
    }

    class Rectangle : Shape
    {

        private double width, height;

        public double Width { set; get; }

        public double Height { set; get; }

        /*
          shadowing the Area from abstract class

        */
        public new double Area()
        {
            return Width * Height;

        }

        /*
            implementing the Area2 abstract mehtod from abstract class
        */

        public override double Area2()
        {
            throw new NotImplementedException();
        }


    }
    
}



namespace interfaceExp

{
    interface Vechicle
    {
        bool EngineStart();
        bool EngineStop();
        bool LeftTurn(double degree);
        bool RightTurn(double degree);
        
    }


    class BasicCar: Vechicle
    {
        /*
        interface implementations has to be public
        */

        public bool EngineStart()
        {
            return true;
        }

        public bool EngineStop()
        {
            return true;
        }

        public bool LeftTurn(double degree)
        {
            return true;
        }

        public bool RightTurn(double degree)
        {
            return true;
        }
        
    }

}


