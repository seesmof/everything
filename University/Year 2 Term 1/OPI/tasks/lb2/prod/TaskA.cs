// Завдання 1

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
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();

            lblOutput.Text = "";
        }

        private void btnRun_Click(object sender, EventArgs e)
        {
            var exp = (int)expInput.Value;
            var baseVal = (int)baseInput.Value;
            var result = 1;

            progressOutput.Value = 0;
            progressOutput.Maximum = exp;

            for (var i = 0; i < exp; i++)
            {
                result *= baseVal;
                progressOutput.Value++;
            }

            lblOutput.Text = $"Result: {result}";
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            expInput.Value = 1;
            baseInput.Value = 1;
        }
    }
}
