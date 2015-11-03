using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using srm1076;

namespace TOP
{
    class Program
    {
        static void Main()
        {
            SRM1076 s = new SRM1076();
            string rval = s.decrypt("THEQUICKBROWNFOXJUMPSOVERTHELAZYHOG", "UIFRVJDLCSPXOGPYKVNQTPWFSUIFMBAZIPH", "DIDYOUNOTICESKIPPEDLETTER");

            Console.Write(rval);
        }
    }
}
