// Завдання 2

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
            Console.Write("Enter an expression: ");
            string input = Console.ReadLine();
            double result = Calculate(input);
            Console.WriteLine($"Result: {result}");
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
