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
        int clicks = 0;
        Timer timer;
        Color[] colors = new Color[]
        {
            Color.Orange,
            Color.YellowGreen,
            Color.ForestGreen,
            Color.DimGray,
            Color.IndianRed,
            Color.Brown,
            Color.Firebrick,
            Color.Maroon,
            Color.DarkRed,
            Color.Chocolate,
            Color.LightSalmon,
            Color.LightSeaGreen,
            Color.LightSkyBlue,
            Color.LightSlateGray,
            Color.Lime,
            Color.LimeGreen
        };

        public FormMain()
        {
            InitializeComponent();
        }

        private void FormMain_Load(object sender, EventArgs e)
        {
            timer = new Timer();
            timer.Interval = SystemInformation.DoubleClickTime;
            timer.Tick += Timer_Tick;
            btnMain.BackColor = Color.YellowGreen;
            btnMain.ForeColor = ControlPaint.LightLight(btnMain.BackColor);
            lblInfo.Text = $"Clicks: {clicks}\nColor: {btnMain.BackColor.Name}";
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            timer.Stop();
            clicks = 0;
        }

        private void btnMain_Click(object sender, EventArgs e)
        {
            clicks++;

            lblInfo.Text = $"Clicks: {clicks}\nColor: {btnMain.BackColor.Name}";

            if (clicks == 3)
            {
                timer.Stop();
                clicks = 0;

                TripleClickAction();

                lblInfo.Text = $"Clicks: {clicks}\nColor: {btnMain.BackColor.Name}";
            }
            else
            {
                timer.Start();
            }
        }

        private void TripleClickAction()
        {
            Random random = new Random();

            int newX = random.Next(20, this.Width - btnMain.Width - 20);
            int newY = random.Next(20, this.Height - btnMain.Height - 20);

            btnMain.Left = newX;
            btnMain.Top = newY;

            int index = random.Next(0, colors.Length);
            btnMain.BackColor = colors[index];
            btnMain.ForeColor = ControlPaint.LightLight(btnMain.BackColor);
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            btnMain.Location = new Point(199, 147);
        }
    }
}


