// Завдання 3

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace dev
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string stateFilePath = "state.txt";
            string input = "";

            if (File.Exists(stateFilePath))
            {
                string[] previousState = File.ReadAllLines(stateFilePath);
                if (previousState.Length > 0)
                    input = previousState[previousState.Length - 1];
            }

            if (string.IsNullOrEmpty(input))
            {
                Console.Write("Enter a string: ");
                input = Console.ReadLine();
            }

            Console.WriteLine("Original string: " + input);

            // Chars
            Console.WriteLine("Chars:");
            for (int i = 0; i < input.Length; i++)
            {
                Console.WriteLine("Char at index " + i + ": " + input[i]);
            }

            // Remove
            string removed = input.Remove(input.Length - 1, 1);
            Console.WriteLine("String after removing last character: " + removed);

            // Insert
            string inserted = input.Insert(input.Length - 1, " there");
            Console.WriteLine("String after inserting ' there' before last character: " + inserted);

            File.AppendAllText(stateFilePath, input + Environment.NewLine);
        }
    }
}