using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Windows.Forms;

namespace dev
{
    public class Result
    {
        // Properties
        public string Name { get; set; } // The name of the user
        public int Score { get; set; } // The score of the user
        public string Difficulty { get; set; } // The difficulty level of the game

        // Constructor
        public Result(string name, int score, string difficulty)
        {
            // Initialize the properties with the parameters
            Name = name;
            Score = score;
            Difficulty = difficulty;
        }

        // A method to return a string representation of the result
        public override string ToString()
        {
            // Return the name, score, and difficulty level separated by commas
            return Name + "," + Score + "," + Difficulty;
        }
    }
}
