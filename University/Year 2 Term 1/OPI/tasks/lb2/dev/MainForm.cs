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
            tableList.Items.Clear();
            progressOutput.Value = 0;

            int maxMultiplier = (int)inputMultiplier.Value;

            progressOutput.Maximum = maxMultiplier;

            for (int i = 1; i <= maxMultiplier; i++)
            {
                ListViewItem item = new ListViewItem(i.ToString());

                for (int j = 1; j <= maxMultiplier; j++)
                {
                    item.SubItems.Add((i * j).ToString());
                }

                tableList.Items.Add(item);
                progressOutput.Value = i;
            }
        }
    }
}