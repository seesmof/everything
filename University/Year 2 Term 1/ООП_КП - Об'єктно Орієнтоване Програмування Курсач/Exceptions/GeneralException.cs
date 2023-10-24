using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace code
{
    public class GeneralException : Exception
    {
        public GeneralException()
        {
        }

        public GeneralException(string message) : base(message) { }

        public GeneralException(string message, Exception inner) : base(message, inner) { }

        public void Display()
        {
            MessageBox.Show(this.Message, "Йой... Шось пішло не так", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }
}
