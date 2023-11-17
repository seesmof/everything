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
        private string CurrentCharacter = "";
        private int Score = 0;
        private string Difficulty = 0;
        public FormMain()
        {
            InitializeComponent();

            dropdownDifficulty.SelectedIndex = Difficulty;
        }

        private void btnStart_Click(object sender, EventArgs e)
        {

        }

        private void txtInput_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
