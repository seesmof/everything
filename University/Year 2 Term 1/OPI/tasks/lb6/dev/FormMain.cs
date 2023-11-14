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
        private BestResults bestResults = new BestResults("bestresults.txt");
        private char character;
        private int time;
        private int score;
        private int maxTime;
        private int minChars;
        private int maxChars;
        private int minWords;
        private int maxWords;
        private Random random;


        public FormMain()
        {
            InitializeComponent();

            tmrGame.Interval = 1000;
            cmbDifficulty.SelectedIndex = 0;

            bestResults.Load();
            ResetGame();
        }

        private void ResetGame()
        {
            character = '\0';
            time = 0;
            score = 0;
            switch (cmbDifficulty.SelectedIndex)
            {
                case 0:
                    maxTime = 10;
                    minChars = 1;
                    maxChars = 1;
                    minWords = 1;
                    maxWords = 1;
                    break;
                case 1:
                    maxTime = 10;
                    minChars = 3;
                    maxChars = 5;
                    minWords = 1;
                    maxWords = 3;
                    break;
                case 2:
                    maxTime = 8;
                    minChars = 5;
                    maxChars = 10;
                    minWords = 3;
                    maxWords = 5;
                    break;
                case 3:
                    maxTime = 6;
                    minChars = 10;
                    maxChars = 15;
                    minWords = 5;
                    maxWords = 10;
                    break;
                case 4:
                    maxTime = 4;
                    minChars = 15;
                    maxChars = 20;
                    minWords = 10;
                    maxWords = 15;
                    break;
            }
            lblCharacter.Text = "Press Start to begin...";
            txtInput.Text = "";
            lblTimer.Text = "Time: 0";
            lblScore.Text = "Score: 0";
            btnStart.Enabled = true;
            btnStop.Enabled = false;
            txtInput.Enabled = false;
            cmbDifficulty.Enabled = true;
        }

        private void GenerateCharacter()
        {
            int chars = random.Next(minChars, maxChars + 1);
            int words = random.Next(minWords, maxWords + 1);
            string str = "";
            for (int i = 1; i <= words; i++)
            {
                for (int j = 1; j <= chars; j++)
                {
                    char c = (char)random.Next('a', 'z' + 1);
                    str += c;
                }
                if (i < words)
                {
                    str += " ";
                }
                else
                {
                    str += ".";
                }
            }
            character = str;
            lblCharacter.Text = character;
        }

        private void StartGame()
        {
            btnStart.Enabled = false;
            btnStop.Enabled = true;
            txtInput.Enabled = true;
            cmbDifficulty.Enabled = false;
            txtInput.Text = "";
            txtInput.Focus();
            GenerateCharacter();
            time = maxTime;
            lblTimer.Text = "Time: " + time;
            tmrGame.Enabled = true;
        }

        private void StopGame()
        {
            tmrGame.Enabled = false;
            btnStart.Enabled = true;
            btnStop.Enabled = false;
            txtInput.Enabled = false;
            cmbDifficulty.Enabled = true;

            Result result = new Result()
        }
    }
}
