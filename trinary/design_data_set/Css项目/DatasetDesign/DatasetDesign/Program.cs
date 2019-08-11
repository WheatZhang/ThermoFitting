using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Data;


namespace DatasetDesign
{
    class Program
    {
        static void Main(string[] args)
        {
            CreateDataset();
        }

        static void CreateDataset()
        {
            DataTable rawData = CSVFileHelper.OpenCSV("trinary_xiata_data.csv", '\t');
            foreach (DataRow dr in rawData.Rows)
            {
                string name  = dr["Place"] as string; 
                systemData.Add(name, new SimulationVariable(Double.Parse((string)dr["initValue"]), Double.Parse((string)dr["max"]),
                    Double.Parse((string)dr["min"]), Double.Parse((string)dr["baseValue"])));
            }
        }
    }
}
