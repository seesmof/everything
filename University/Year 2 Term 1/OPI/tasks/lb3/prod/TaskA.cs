// Завдання 1

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
            string compressed = Compress(input);
            Console.WriteLine($"Compressed: {compressed}");
            string decompressed = Decompress(compressed);
            Console.WriteLine($"Decompressed: {decompressed}");
        }

        private static string Compress(string input)
        {
            StringBuilder sb = new StringBuilder();
            int count = 1;
            for (int i = 1; i < input.Length; i++)
            {
                if (input[i] == input[i - 1] && !Char.IsWhiteSpace(input[i]))
                {
                    count++;
                }
                else
                {
                    if (count > 1)
                    {
                        sb.Append(input[i - 1].ToString() + count);
                    }
                    else
                    {
                        sb.Append(input[i - 1]);
                    }
                    count = 1;
                }
            }
            if (count > 1)
            {
                sb.Append(input[input.Length - 1].ToString() + count);
            }
            else
            {
                sb.Append(input[input.Length - 1]);
            }
            return sb.ToString();
        }

        private static string Decompress(string input)
        {
            StringBuilder sb = new StringBuilder();
            int count = 0;
            for (int i = 0; i < input.Length; i++)
            {
                if (Char.IsDigit(input[i]))
                {
                    count = int.Parse(input[i].ToString());
                    while (count > 1)
                    {
                        sb.Append(input[i - 1]);
                        count--;
                    }
                }
                else
                {
                    sb.Append(input[i]);
                }
            }
            return sb.ToString();
        }
    }
}
