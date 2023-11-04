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
    public partial class FormMain : Form
    {
        int speed = 10;
        Random random = new Random();

        public FormMain()
        {
            InitializeComponent();

            lblSpeed.Text = $"Speed: {speed}";
            trackBarSpeed.Minimum = 1;
            trackBarSpeed.Maximum = 20;
            trackBarSpeed.Value = 10;
            speed = trackBarSpeed.Value;
        }

        private void FormMain_Load(object sender, EventArgs e)
        {
            btnMain.Text = "Catch me if you can";
            lblMousePos.Text = "Mouse: (0, 0)";
            lblBtnPos.Text = "Button: (0, 0)";
        }

        private void FormMain_MouseMove(object sender, MouseEventArgs e)
        {
            int mouseX = e.X;
            int mouseY = e.Y;
            int buttonX = btnMain.Left + btnMain.Width / 2;
            int buttonY = btnMain.Top + btnMain.Height / 2;

            int dx = buttonX - mouseX;
            int dy = buttonY - mouseY;
            double angle = Math.Atan2(dy, dx);
            int distance = (int)Math.Sqrt(dx * dx + dy * dy);

            if (distance < 100)
            {
                int newX = buttonX + (int)(speed * Math.Cos(angle));
                int newY = buttonY + (int)(speed * Math.Sin(angle));

                if (newX < 0 || newX > this.Width)
                {
                    newX = buttonY - (int)(speed * Math.Sin(angle));
                }

                btnMain.Left = newX - btnMain.Width / 2;
                btnMain.Top = newY - btnMain.Height / 2;
            }

            lblBtnPos.Text = $"Button: ({buttonX}, {buttonY})";
            lblMousePos.Text = $"Mouse: ({mouseX}, {mouseY})";
        }

        private void btnMain_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("You caught me! Well done!\nDo you want to try again?", "Congratulations! You won!", MessageBoxButtons.YesNo, MessageBoxIcon.Question);

            if (result == DialogResult.Yes)
            {
                btnMain.Left = random.Next(this.Width - btnMain.Width);
                btnMain.Top = random.Next(this.Height - btnMain.Height);
            }
            else
            {
                this.Close();
            }
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            btnMain.Left = random.Next(this.Width - btnMain.Width);
            btnMain.Top = random.Next(this.Height - btnMain.Height);
        }

        private void trackBarSpeed_ValueChanged(object sender, EventArgs e)
        {

        }
    }
}
