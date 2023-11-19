// Paint - Input Dialog Main

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace dev
{
    public partial class InputDialog : Form
    {
        public string InputText { get; set; }

        public InputDialog()
        {
            InitializeComponent();
        }

        private void btnSend_Click(object sender, EventArgs e)
        {
            InputText = txtInput.Text;
            this.Close();
        }
    }
}
