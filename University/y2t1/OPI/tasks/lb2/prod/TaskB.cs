// Завдання 2

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

        private void btnMoveRight_Click(object sender, EventArgs e)
        {
            if (leftList.Items.Count > 0)
            {
                ListViewItem item = leftList.Items[leftList.Items.Count - 1];
                leftList.Items.RemoveAt(leftList.Items.Count - 1);
                rightList.Items.Add(item);
            }
        }

        private void btnMoveLeft_Click(object sender, EventArgs e)
        {
            if (rightList.Items.Count > 0)
            {
                ListViewItem item = rightList.Items[rightList.Items.Count - 1];
                rightList.Items.RemoveAt(rightList.Items.Count - 1);
                leftList.Items.Add(item);
            }
        }

        private void btnAddL_Click(object sender, EventArgs e)
        {
            leftList.Items.Add($"Item {leftList.Items.Count}");
        }

        private void btnAddR_Click(object sender, EventArgs e)
        {
            rightList.Items.Add($"Item {rightList.Items.Count}");
        }

        private void btnRemoveL_Click(object sender, EventArgs e)
        {
            if (leftList.Items.Count > 0)
            {
                leftList.Items.RemoveAt(leftList.Items.Count - 1);
            }
        }

        private void btnRemoveR_Click(object sender, EventArgs e)
        {
            if (rightList.Items.Count > 0)
            {
                rightList.Items.RemoveAt(rightList.Items.Count - 1);
            }
        }
    }
}