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
        string currentTool = null;
        Point startPoint;
        Point endPoint;
        Graphics g;

        public FormMain()
        {
            InitializeComponent();
        }

        private void selectTool(object sender, EventArgs e)
        {
            ToolStripButton button = (ToolStripButton)sender;
            currentTool = button.Tag.ToString();
        }

        private void toolStripButtonLine_Click(object sender, EventArgs e)
        {
            selectTool(sender, e);
        }

        private void toolStripButtonEllipse_Click(object sender, EventArgs e)
        {
            selectTool(sender, e);
        }

        private void toolStripButtonPencil_Click(object sender, EventArgs e)
        {
            selectTool(sender, e);
        }

        private void toolStripButtonRectangle_Click(object sender, EventArgs e)
        {
            selectTool(sender, e);
        }

        private void toolStripButtonText_Click(object sender, EventArgs e)
        {
            selectTool(sender, e);
        }

        private void drawingCanvas_MouseDown(object sender, MouseEventArgs e)
        {
            if (currentTool == "Line")
            {
                g = drawingCanvas.CreateGraphics();
                startPoint = e.Location;
            }
        }

        private void drawingCanvas_MouseMove(object sender, MouseEventArgs e)
        {
            if (currentTool == "Line" && g != null)
            {
                endPoint = e.Location;
            }
        }

        private void drawingCanvas_MouseUp(object sender, MouseEventArgs e)
        {
            if (currentTool == "Line" && g != null)
            {
                g.DrawLine(Pens.Black, startPoint, endPoint);
                g.Dispose();
                g = null;
            }
        }
    }
}
