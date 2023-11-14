using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dev
{
    public class BestResults
    {
        public List<Result> Results { get; set; }
        public string FileName { get; set; }

        public BestResults(string fileName)
        {
            FileName = fileName;
            Results = new List<Result>();
        }

        public void Load()
        {
        }

        public void Save()
        {
        }

        public void Add(Result result)
        {
        }

        public void Show()
        {
        }
    }
}
