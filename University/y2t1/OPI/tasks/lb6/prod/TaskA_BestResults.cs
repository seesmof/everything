// Task A - Best Results
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Windows.Forms;

namespace dev
{
    public class BestResults
    {
        // Properties
        public List<Result> Results { get; set; } // The list of best results
        public string FileName { get; set; } // The name of the file where the best results are saved

        // Constructor
        public BestResults(string fileName)
        {
            // Initialize the list of best results as an empty list
            Results = new List<Result>();
            // Initialize the file name with the parameter
            FileName = fileName;
        }

        // A method to load the best results from the file
        public void Load()
        {
            // Try to open the file for reading
            try
            {
                // Create a stream reader object with the file name
                using (StreamReader sr = new StreamReader(FileName))
                {
                    // Read the file line by line until the end of the file
                    while (!sr.EndOfStream)
                    {
                        // Read a line from the file
                        string line = sr.ReadLine();
                        // Split the line by commas
                        string[] parts = line.Split(',');
                        // Create a new result object with the parts
                        Result result = new Result(parts[0], int.Parse(parts[1]), parts[2]);
                        // Add the result to the list of best results
                        Results.Add(result);
                    }
                }
            }
            // Catch any exception that may occur
            catch (Exception e)
            {
                // Show a message box with the exception message
                MessageBox.Show(e.Message, "Error");
            }
        }

        // A method to save the best results to the file
        public void Save()
        {
            // Try to open the file for writing
            try
            {
                // Create a stream writer object with the file name
                using (StreamWriter sw = new StreamWriter(FileName))
                {
                    // Loop through each result in the list of best results
                    foreach (Result result in Results)
                    {
                        // Write the result to the file
                        sw.WriteLine(result.ToString());
                    }
                }
            }
            // Catch any exception that may occur
            catch (Exception e)
            {
                // Show a message box with the exception message
                MessageBox.Show(e.Message, "Error");
            }
        }

        // A method to add a new result to the list of best results
        public void Add(Result result)
        {
            // Add the result to the list of best results
            Results.Add(result);
            // Sort the list of best results by score and difficulty level
            Results = Results.OrderByDescending(r => r.Score).ThenBy(r => r.Difficulty).ToList();
        }

        // A method to show the best results in a message box
        public void Show()
        {
            // Initialize an empty string
            string message = "";
            // Loop through each result in the list of best results
            foreach (Result result in Results)
            {
                // Append the result to the message with a new line
                message += result.Name + " - " + result.Score + " - " + result.Difficulty + "\n";
            }
            // Show a message box with the message and the title "Best Results"
            MessageBox.Show(message, "Best Results");
        }
    }
}
