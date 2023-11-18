// Task C - Main
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace dev
{
    public partial class FormMain : Form
    {
        public FormMain()
        {
            InitializeComponent();

            this.KeyPreview = true;
        }

        private void FormMain_KeyPress(object sender, KeyPressEventArgs e)
        {
            int keyCode = (int)e.KeyChar;
            labelKeyCode.Text = $"Key Code: {keyCode}\nKey Name: {e.KeyChar}";

            using (StreamWriter writer = new StreamWriter("log.txt", true))
            {
                writer.WriteLine($"Key Code: {keyCode} - Key Name: {e.KeyChar}");
            }
        }
    }
}
