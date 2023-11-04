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
    public partial class FormMain : Form
    {
        bool isDragging = false;
        Point offset;

        public FormMain()
        {
            InitializeComponent();
        }

        private void FormMain_Load(object sender, EventArgs e)
        {
            pnlMain.BackColor = Color.Tomato;
            lblPos.Text = "Panel: (0, 0)\nArea: None";
        }

        private void pnlMain_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isDragging = true;
                offset = new Point(e.X, e.Y);
            }
        }

        private void pnlMain_MouseMove(object sender, MouseEventArgs e)
        {
            if (isDragging)
            {
                int panelX = pnlMain.Left;
                int panelY = pnlMain.Top;

                int newX = panelX + e.X - offset.X;
                int newY = panelY + e.Y - offset.Y;

                pnlMain.Left = newX;
                pnlMain.Top = newY;

                string area = "None";
                if (newX < this.Width / 2 && newY < this.Height / 2)
                    area = "Top-Left";
                else if (newX >= this.Width / 2 && newY < this.Height / 2)
                    area = "Top-Right";
                else if (newX < this.Width / 2 && newY >= this.Height / 2)
                    area = "Bottom-Left";
                else if (newX >= this.Width / 2 && newY >= this.Height / 2)
                    area = "Bottom-Right";

                lblPos.Text = $"Panel: ({newX}, {newY})\nArea: {area}";
            }
        }

        private void pnlMain_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isDragging = false;

                int clientHeight = this.Height - SystemInformation.CaptionHeight - 2 * SystemInformation.BorderSize.Height;

                // Snap the panel to the appropriate side
                if (pnlMain.Left < this.Width / 2 && pnlMain.Top < this.Height / 2)
                    pnlMain.Location = new Point(0, 0);
                else if (pnlMain.Left >= this.Width / 2 && pnlMain.Top < this.Height / 2)
                    pnlMain.Location = new Point(this.Width - pnlMain.Width, 0);
                else if (pnlMain.Left < this.Width / 2 && pnlMain.Top >= this.Height / 2)
                    pnlMain.Location = new Point(0, clientHeight - pnlMain.Height);
                else if (pnlMain.Left >= this.Width / 2 && pnlMain.Top >= this.Height / 2)
                    pnlMain.Location = new Point(this.Width - pnlMain.Width, clientHeight - pnlMain.Height);
            }
        }
    }
}


