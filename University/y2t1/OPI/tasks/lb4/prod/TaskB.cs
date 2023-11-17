// Завдання 2

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dev
{
    internal class Program
    {
        private const string SessionFile = "session.txt";

        static void Main(string[] args)
        {
            string input;

            if (File.Exists(SessionFile))
            {
                input = File.ReadAllLines(SessionFile).Last();
            }
            else
            {
                Console.Write("Enter an expression: ");
                input = Console.ReadLine();
            }

            double result = Calculate(input);
            Console.WriteLine($"Result: {result}");

            File.AppendAllLines(SessionFile, new[] { input });
        }

        private static double Calculate(string input)
        {
            string[] parts = input.Split(' ');
            double num1 = double.Parse(parts[0]);
            string operation = parts[1];
            double num2 = double.Parse(parts[2]);

            switch (operation)
            {
                case "+":
                case "plus":
                    return num1 + num2;
                case "-":
                case "minus":
                    return num1 - num2;
                case "*":
                case "multiply":
                case "times":
                    return num1 * num2;
                case "/":
                case "divide":
                case "by":
                    return num1 / num2;
                default:
                    throw new Exception("Invalid operation");
            }
        }
    }
}