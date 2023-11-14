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
        // Global variables
        char character; // The current character to be entered by the user
        int time; // The remaining time for entering the character
        int score; // The current score of the user
        int maxTime; // The maximum time for entering the character based on the difficulty level
        int minChars; // The minimum number of characters to be entered based on the difficulty level
        int maxChars; // The maximum number of characters to be entered based on the difficulty level
        int minWords; // The minimum number of words to be entered based on the difficulty level
        int maxWords; // The maximum number of words to be entered based on the difficulty level
        Random random; // A random number generator object
        BestResults bestResults; // A best results object


        public FormMain()
        {
            InitializeComponent();
            tmrGame.Interval = 1000;

            // Load the best results from the file
            bestResults = new BestResults("bestresults.txt");
            bestResults.Load();
            // Set the default difficulty level to Easy
            cmbDifficulty.SelectedIndex = 0;
            // Reset the game variables and controls
            ResetGame();
        }

        // A method to reset the game variables and controls
        private void ResetGame()
        {
            // Set the character to null
            character = '\0';
            // Set the time to 0
            time = 0;
            // Set the score to 0
            score = 0;
            // Set the maxTime, minChars, maxChars, minWords, and maxWords variables according to the difficulty level
            switch (cmbDifficulty.SelectedIndex)
            {
                case 0: // Easy
                    maxTime = 10;
                    minChars = 1;
                    maxChars = 1;
                    minWords = 1;
                    maxWords = 1;
                    break;
                case 1: // Medium
                    maxTime = 8;
                    minChars = 1;
                    maxChars = 2;
                    minWords = 1;
                    maxWords = 2;
                    break;
                case 2: // Hard
                    maxTime = 6;
                    minChars = 1;
                    maxChars = 3;
                    minWords = 1;
                    maxWords = 3;
                    break;
                case 3: // Expert
                    maxTime = 4;
                    minChars = 2;
                    maxChars = 4;
                    minWords = 2;
                    maxWords = 4;
                    break;
                case 4: // Master
                    maxTime = 2;
                    minChars = 3;
                    maxChars = 5;
                    minWords = 3;
                    maxWords = 5;
                    break;
            }
            // Set the character label to "Press Start to begin"
            lblCharacter.Text = "Press Start to begin";
            // Set the input text box to empty
            txtInput.Text = "";
            // Set the timer label to "Time: 0"
            lblTimer.Text = "Time: 0";
            // Set the score label to "Score: 0"
            lblScore.Text = "Score: 0";
            // Enable the start button
            btnStart.Enabled = true;
            // Disable the stop button
            btnStop.Enabled = false;
            // Disable the input text box
            txtInput.Enabled = false;
            // Enable the difficulty combo box
            cmbDifficulty.Enabled = true;
        }

        // A method to generate a new character to be entered by the user
        private void GenerateCharacter()
        {
            // Get a random number of characters between minChars and maxChars
            int chars = random.Next(minChars, maxChars + 1);
            // Get a random number of words between minWords and maxWords
            int words = random.Next(minWords, maxWords + 1);
            // Initialize an empty string
            string str = "";
            // Loop for each word
            for (int i = 1; i <= words; i++)
            {
                // Loop for each character
                for (int j = 1; j <= chars; j++)
                {
                    // Get a random character between 'a' and 'z'
                    char c = (char)random.Next('a', 'z' + 1);
                    // Append the character to the string
                    str += c;
                }
                // If the current word is not the last word, append a space to the string
                if (i < words)
                {
                    str += ' ';
                }
            }
            // Set the character variable to the string
            character = str;
            // Set the character label to the character
            lblCharacter.Text = character.ToString();
        }

        // A method to start the game
        private void StartGame()
        {
            // Disable the start button
            btnStart.Enabled = false;
            // Enable the stop button
            btnStop.Enabled = true;
            // Enable the input text box
            txtInput.Enabled = true;
            // Disable the difficulty combo box
            cmbDifficulty.Enabled = false;
            // Set the input text box to empty
            txtInput.Text = "";
            // Set the focus to the input text box
            txtInput.Focus();
            // Generate a new character to be entered by the user
            GenerateCharacter();
            // Set the time variable to maxTime
            time = maxTime;
            // Set the timer label to "Time: " + time
            lblTimer.Text = "Time: " + time;
            // Enable the game timer
            tmrGame.Enabled = true;
        }

        // A method to stop the game
        private void StopGame()
        {
            // Disable the game timer
            tmrGame.Enabled = false;
            // Disable the start button
            btnStart.Enabled = true;
            // Disable the stop button
            btnStop.Enabled = false;
            // Disable the input text box
            txtInput.Enabled = false;
            // Enable the difficulty combo box
            cmbDifficulty.Enabled = true;
            // Create a new result object with the user's name, score, and difficulty level
            Result result = new Result(InputBox("Enter your name", "Name"), score, cmbDifficulty.SelectedItem.ToString());
            // Add the result to the best results list
            bestResults.Add(result);
            // Save the best results to the file
            bestResults.Save();
            // Reset the game variables and controls
            ResetGame();
        }
    }
