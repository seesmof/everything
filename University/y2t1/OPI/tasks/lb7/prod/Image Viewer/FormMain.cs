// Image Viewer - Main

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
        private List<Image> images = new List<Image>();
        private int currentImageIndex = -1;

        public FormMain()
        {
            InitializeComponent();

            lblEmpty.Visible = true;
        }

        private void button_Click(object sender, EventArgs e)
        {
            OpenFileDialog dialog = new OpenFileDialog();
            dialog.Filter = "Image Files(*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF";
            if (dialog.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    Image image = Image.FromFile(dialog.FileName);
                    images.Add(image);
                    currentImageIndex = images.Count - 1;
                    pictureBox.Image = image;
                    lblEmpty.Visible = false;
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }

        private void previousButton_Click(object sender, EventArgs e)
        {
            if (currentImageIndex > 0)
            {
                currentImageIndex--;
                Image image = images[currentImageIndex];
                pictureBox.Image = image;
            }
        }

        private void nextButton_Click(object sender, EventArgs e)
        {
            if (currentImageIndex < images.Count - 1)
            {
                currentImageIndex++;
                Image image = images[currentImageIndex];
                pictureBox.Image = image;
            }
        }

        private void btnZoom_Click(object sender, EventArgs e)
        {
            if (pictureBox.SizeMode == PictureBoxSizeMode.Zoom)
            {
                pictureBox.SizeMode = PictureBoxSizeMode.CenterImage;
                btnZoom.Text = "Center";
            }
            else
            {
                pictureBox.SizeMode = PictureBoxSizeMode.Zoom;
                btnZoom.Text = "Zoom";
            }
        }
    }
}