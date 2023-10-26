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
    public partial class TaskA : Form
    {
        public TaskA()
        {
            InitializeComponent();

            lblResults.Text = "";
        }

        private void btnCalculate_Click(object sender, EventArgs e)
        {
            var baseNum = (int)inputBase.Value;
            var exponent = (int)inputExponent.Value;
            var result = 1;

            progressOutput.Maximum = exponent;
            progressOutput.Value = 0;

            for (var i = 0; i < exponent; i++)
            {
                result *= baseNum;
                progressOutput.Value++;
            }

            lblResults.Text = $"{baseNum}**{exponent} = {result}";
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            inputBase.Value = 1;
            inputExponent.Value = 1;
        }
    }
}
