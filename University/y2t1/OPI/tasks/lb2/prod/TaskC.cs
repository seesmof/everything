// Завдання 3

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
        }

        private void btnRun_Click(object sender, EventArgs e)
        {
            var maxMultiplier = (int)inputMultiplier.Value;
            tableList.Items.Clear();

            progressOutput.Maximum = 0;
            progressOutput.Maximum = maxMultiplier;

            for (var i = 1; i <= maxMultiplier; i++)
            {
                for (var j = 1; j <= maxMultiplier; j++)
                {
                    tableList.Items.Add($"{i} * {j} = {i * j}");
                }
                progressOutput.Value = i;
                tableList.Items.Add("");
            }
        }
    }
}