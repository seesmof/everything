// Paint - Main 

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
        Point currentPoint;
        Graphics g;
        string currentText = "";
        Color currentColor = Color.Black;
        float currentThickness = 1.0f;

        public FormMain()
        {
            InitializeComponent();
        }

        private void unselectAllTools()
        {
            foreach (ToolStripButton button in this.toolStrip.Items)
            {
                button.Checked = false;
            }
        }

        private void selectTool(object sender, EventArgs e)
        {
            ToolStripButton button = (ToolStripButton)sender;
            currentTool = button.Tag.ToString();

            unselectAllTools();
            button.Checked = true;

            if (currentTool == "Text")
            {
                currentText = "";
                showInputDialog();
            }
        }

        private void showInputDialog()
        {
            try
            {
                InputDialog dialog = new InputDialog();
                dialog.ShowDialog();
                currentText = dialog.InputText;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void drawingCanvas_MouseDown(object sender, MouseEventArgs e)
        {
            if (currentTool == "Line")
            {
                g = drawingCanvas.CreateGraphics();
                startPoint = e.Location;
            }
            else if (currentTool == "Ellipse")
            {
                g = drawingCanvas.CreateGraphics();
                startPoint = e.Location;
            }
            else if (currentTool == "Pencil")
            {
                g = drawingCanvas.CreateGraphics();
                currentPoint = e.Location;
            }
            else if (currentTool == "Rectangle")
            {
                g = drawingCanvas.CreateGraphics();
                startPoint = e.Location;
            }
            else if (currentTool == "Text")
            {
                g = drawingCanvas.CreateGraphics();
                g.DrawString(currentText, new Font("Arial", 12), Brushes.Black, e.Location);
            }
        }

        private void drawingCanvas_MouseMove(object sender, MouseEventArgs e)
        {
            try
            {
                if (currentTool == "Line" && g != null)
                {
                    endPoint = e.Location;
                }
                else if (currentTool == "Ellipse" && g != null)
                {
                    endPoint = e.Location;
                }
                else if (currentTool == "Pencil" && g != null)
                {
                    g.DrawLine(Pens.Black, currentPoint, e.Location);
                    currentPoint = e.Location;
                }
                else if (currentTool == "Rectangle" && g != null)
                {
                    endPoint = e.Location;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
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
            else if (currentTool == "Ellipse" && g != null)
            {
                int width = Math.Abs(endPoint.X - startPoint.X);
                int height = Math.Abs(endPoint.Y - startPoint.Y);

                g.DrawEllipse(Pens.Black, Math.Min(startPoint.X, endPoint.X), Math.Min(startPoint.Y, endPoint.Y), width, height);

                g.Dispose();
                g = null;
            }
            else if (currentTool == "Pencil" && g != null)
            {
                g.Dispose();
                g = null;
            }
            else if (currentTool == "Rectangle" && g != null)
            {
                int width = Math.Abs(endPoint.X - startPoint.X);
                int height = Math.Abs(endPoint.Y - startPoint.Y);

                g.DrawRectangle(Pens.Black, Math.Min(startPoint.X, endPoint.X), Math.Min(startPoint.Y, endPoint.Y), width, height);

                g.Dispose();
                g = null;
            }
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
    }
}