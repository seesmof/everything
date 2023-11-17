// Завдання 3

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dev
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a string: ");
            string input = Console.ReadLine();
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
        }
    }
}