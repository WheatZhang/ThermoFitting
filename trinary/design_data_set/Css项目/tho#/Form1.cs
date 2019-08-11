using System;
using System.Windows.Forms;
using HYSYS;
using System.Diagnostics;
using System.IO;
using System.Collections.Generic;

namespace HYSYS_RTO
{
    public partial class Main_RTO : Form
    {
        HysysContral.HysysControlClass MyHysysControlClass = new HysysContral.HysysControlClass();
        PublicClass.ConsoleClass MyConsoleClass = new PublicClass.ConsoleClass();

        public Main_RTO()
        {
            InitializeComponent();
        
        }
        
        public void Main_RTO_Load(object sender, EventArgs e)
        {
            //Open Console
            MyConsoleClass.OpenConsole();
        }

        public void Main_RTO_FormClosed(object sender, FormClosedEventArgs e)
        {
            MyConsoleClass.CloseConsole();
        }

        private void Start_Click(object sender, EventArgs e)
        {
            //open
            PlantApplication HysysApp = MyHysysControlClass.Hysys_Connect();
            dynamic HysysSimulation = Microsoft.VisualBasic.Interaction.GetObject("C:/Users/lou/Desktop/connect/thermodynamics.hsc");
            HysysSimulation.visible = true;
            

        }

        private void run_Click(object sender, EventArgs e)
        {

            myFun_design_database();

        }

        public void myFun1()
        {
            PlantApplication HysysApp = MyHysysControlClass.Hysys_Connect();
            dynamic HysysSimulationCase = HysysApp.ActiveDocument;
            dynamic FEED = HysysSimulationCase.Flowsheet.MaterialStreams.Item("FEED");
            dynamic top = HysysSimulationCase.Flowsheet.MaterialStreams.Item("top");
            dynamic bottom = HysysSimulationCase.Flowsheet.MaterialStreams.Item("bottom");
            HysysSimulationCase.solver.CanSolve = true;
            string result1 = @"C:\Users\lou\Desktop\connect\density_result.txt";//结果保存到F:\result1.txt
            FileStream fs = new FileStream(result1, FileMode.Create);
            StreamWriter wr = null;
            wr = new StreamWriter(fs);
            //update

            double[] pressureRange = new double[] { 100, 600 };
            int n_sample = 200;
            double pressure;
            for (int i = 0; i <= n_sample; i++)
            {
                pressure = pressureRange[0] + i * (pressureRange[1] - pressureRange[0]) / n_sample;
                FEED.PressureValue = pressure;
                wr.WriteLine(FEED.TemperatureValue + "\n");
            }

            List<double> oxygen_boiling_temp = new List<double>();
            List<double> nitrogen_boiling_temp = new List<double>();
            StreamReader file = new StreamReader(@"C:\Users\lou\Desktop\connect\oxygen_pressure.txt");
            string line;
            while ((line = file.ReadLine()) != null)
            {
                oxygen_boiling_temp.Add(double.Parse(line));
            }
            file.Close();
            file = new StreamReader(@"C:\Users\lou\Desktop\connect\nitrogen_pressure.txt");
            while ((line = file.ReadLine()) != null)
            {
                nitrogen_boiling_temp.Add(double.Parse(line));
            }
            file.Close();

            //double[] pressureRange = new double[] { 100, 600 };
            //double[] temperatureRange = new double[2];
            //int n_sample = 200;
            //double pressure;
            //double temperature;
            //double vaporO2Frac;
            //double vaporN2Frac;
            //double liquidO2Frac;
            //double liquidN2Frac;
            //double vaporEnthalpy;
            //double liquidEnthalpy;
            //double[] feedComposition=new double[2];
            //for (int i = 0; i <= n_sample; i++)
            //{
            //    pressure = pressureRange[0] + i * (pressureRange[1] - pressureRange[0]) / n_sample;
            //    temperatureRange[0] = nitrogen_boiling_temp[i];
            //    temperatureRange[1] = oxygen_boiling_temp[i];
            //    for (int j = 0; j <= n_sample; j++)
            //    {
            //        temperature = temperatureRange[0] + j * (temperatureRange[1] - temperatureRange[0]) / n_sample;
            //        FEED.PressureValue = pressure;
            //        FEED.TemperatureValue = temperature;
            //        feedComposition[0] = 1.0 - 1.0 / n_sample * j;
            //        feedComposition[1] = 1.0 - feedComposition[0];
            //        FEED.ComponentMolarFractionValue = feedComposition;
            //        wr.Write(Convert.ToString(pressure));
            //        wr.Write(",");
            //        wr.Write(Convert.ToString(temperature));
            //        wr.Write(",");
            //        vaporO2Frac = top.ComponentMolarFractionValue[1];
            //        wr.Write(Convert.ToString(vaporO2Frac));
            //        wr.Write(",");
            //        vaporN2Frac = top.ComponentMolarFractionValue[0];
            //        wr.Write(Convert.ToString(vaporN2Frac));
            //        wr.Write(",");
            //        liquidO2Frac = bottom.ComponentMolarFractionValue[1];
            //        wr.Write(Convert.ToString(liquidO2Frac));
            //        wr.Write(",");
            //        liquidN2Frac = bottom.ComponentMolarFractionValue[0];
            //        wr.Write(Convert.ToString(liquidN2Frac));
            //        wr.Write(",");
            //        vaporEnthalpy = top.MolarEnthalpyValue;
            //        wr.Write(Convert.ToString(vaporEnthalpy));
            //        wr.Write(",");
            //        liquidEnthalpy = bottom.MolarEnthalpyValue;
            //        wr.Write(Convert.ToString(liquidEnthalpy));
            //        wr.Write("\n");
            //    }
            //}
            //wr.Close();

            //double[] pressureRange = new double[] { 100, 600 };
            double[] temperatureRange = new double[2];
            //int n_sample = 200;
            //double pressure;
            double temperature;
            double vaporDensity;
            double liquidDensity;
            double[] feedComposition = new double[2];
            for (int i = 0; i <= n_sample; i++)
            {
                pressure = pressureRange[0] + i * (pressureRange[1] - pressureRange[0]) / n_sample;
                temperatureRange[0] = nitrogen_boiling_temp[i];
                temperatureRange[1] = oxygen_boiling_temp[i];
                for (int j = 0; j <= n_sample; j++)
                {
                    temperature = temperatureRange[0] + j * (temperatureRange[1] - temperatureRange[0]) / n_sample;
                    FEED.PressureValue = pressure;
                    FEED.TemperatureValue = temperature;
                    feedComposition[0] = 1.0 - 1.0 / n_sample * j;
                    feedComposition[1] = 1.0 - feedComposition[0];
                    FEED.ComponentMolarFractionValue = feedComposition;
                    wr.Write(Convert.ToString(pressure));
                    wr.Write(",");
                    wr.Write(Convert.ToString(temperature));
                    wr.Write(",");
                    vaporDensity = top.MolarDensityValue;
                    wr.Write(Convert.ToString(vaporDensity));
                    wr.Write(",");
                    liquidDensity = bottom.MolarDensityValue;
                    wr.Write(Convert.ToString(liquidDensity));
                    wr.Write("\n");
                }
            }
            wr.Close();


            //double[] pressureRange = new double[] { 100, 600 };
            //double[] temperatureRange = new double[] { -200, -160 };
            //double[] compositionRange = new double[] { 0, 1 };
            //int n_sample = 40;
            //double pressure;
            //double temperature;
            //double vaporFraction;
            //double nitrogenFrac;
            //double oxygenFrac;
            //double enthalpy;

            //for (int i = 0; i <= n_sample; i++)
            //{
            //    pressure = pressureRange[0] + i * (pressureRange[1] - pressureRange[0]) / n_sample;
            //    FEED.pressureValue = pressure;
            //    for (int j = 0; j <= n_sample; j++)
            //    {
            //        temperature = temperatureRange[0] + j * (temperatureRange[1] - temperatureRange[0]) / n_sample;
            //        FEED.temperatureValue = temperature;
            //        for (int k = 0; k <= n_sample; k++)
            //        {
            //            nitrogenFrac = compositionRange[0] + k * (compositionRange[1] - compositionRange[0]) / n_sample;
            //            oxygenFrac = 1 - nitrogenFrac;
            //            FEED.ComponentMolarFractionValue = new double[] { nitrogenFrac, oxygenFrac };
            //            wr.Write(Convert.ToString(pressure));
            //            wr.Write(",");
            //            wr.Write(Convert.ToString(temperature));
            //            wr.Write(",");
            //            wr.Write(Convert.ToString(nitrogenFrac));
            //            wr.Write(",");
            //            wr.Write(Convert.ToString(oxygenFrac));
            //            wr.Write(",");
            //            vaporFraction = FEED.VapourFractionValue;
            //            wr.Write(Convert.ToString(vaporFraction));
            //            wr.Write(",");
            //            enthalpy = FEED.MolarEnthalpyValue;
            //            wr.Write(Convert.ToString(enthalpy));
            //            wr.Write("\n");
            //        }
            //    }
            //}
            //wr.Close();
        }

        public void myFun2()
        {
            PlantApplication HysysApp = MyHysysControlClass.Hysys_Connect();
            dynamic HysysSimulationCase = HysysApp.ActiveDocument;
            dynamic FEED = HysysSimulationCase.Flowsheet.MaterialStreams.Item("FEED");
            dynamic top = HysysSimulationCase.Flowsheet.MaterialStreams.Item("vapour");
            dynamic bottom = HysysSimulationCase.Flowsheet.MaterialStreams.Item("liquid");
            HysysSimulationCase.solver.CanSolve = true;
            string result1 = @"C:\Users\lou\Desktop\connect\trinaryThermo.txt";//结果保存到F:\result1.txt
            FileStream fs = new FileStream(result1, FileMode.Create);
            StreamWriter wr = null;
            wr = new StreamWriter(fs);
            //update

            double[] pressureRange = new double[] { 500, 600 };
            double[] nitrogenCompRange = new double[] { 0, 1 };
            double[] argonCompRange = new double[] { 0, 0.02 };
            double[] temperatureRange = new double[2];
            double[] feedComposition = new double[3];
            int n_sample1 = 20;
            int n_sample2 = 20;
            int n_sample3 = 80;
            int n_sample4 = 8;
            double temperature;
            double pressure;
            double nitrogenComp;
            double oxygenComp;
            double argonComp;
            double[] vaporComp;
            double[] liquidComp;
            double vaporDensity;
            double liquidDensity;
            double vaporMolarEnthalpy;
            double liquidMolarEnthalpy;
            double vaporMolarFlow;
            double liquidMolarFlow;
            wr.Write("P,T,N2,O2,Ar,y_N2,y_O2,y_Ar,x_N2,x_O2,x_Ar,vap_rho,liq_rho,vap_etlp,liq_etlp,vap_F,liq_F\n");
            try
            {
                for (int i = 0; i <= n_sample1; i++)
                {
                    pressure = pressureRange[0] + i * (pressureRange[1] - pressureRange[0]) / n_sample1;
                    temperatureRange[0] = 0.0379 * pressure - 190.23 - 5;
                    temperatureRange[0] = 0.0379 * pressure - 190.23 + 5;
                    for (int j = 0; j <= n_sample2; j++)
                    {
                        temperature = temperatureRange[0] + j * (temperatureRange[1] - temperatureRange[0]) / n_sample2;
                        for (int x = 0; x <= n_sample3; x++)
                        {
                            nitrogenComp = nitrogenCompRange[0] + x * (nitrogenCompRange[1] - nitrogenCompRange[0]) / n_sample3;
                            for (int y = 0; y <= n_sample4; y++)
                            {
                                argonComp = argonCompRange[0] + y * (argonCompRange[1] - argonCompRange[0]) / n_sample4;
                                oxygenComp = 1 - nitrogenComp - argonComp;
                                if (oxygenComp < 0)
                                {
                                    break;
                                }
                                FEED.PressureValue = pressure;
                                FEED.TemperatureValue = temperature;
                                feedComposition[0] = nitrogenComp;
                                feedComposition[1] = oxygenComp;
                                feedComposition[2] = argonComp;
                                FEED.ComponentMolarFractionValue = feedComposition;
                                vaporComp = top.ComponentMolarFractionValue;
                                liquidComp = bottom.ComponentMolarFractionValue;
                                vaporDensity = top.MolarDensityValue;
                                liquidDensity = bottom.MolarDensityValue;
                                vaporMolarEnthalpy = top.MolarEnthalpyValue;
                                liquidMolarEnthalpy = bottom.MolarEnthalpyValue;
                                vaporMolarFlow = top.MolarFlowValue;
                                liquidMolarFlow = bottom.MolarFlowValue;

                                wr.Write(Convert.ToString(pressure));
                                wr.Write(",");
                                wr.Write(Convert.ToString(temperature));
                                wr.Write(",");
                                wr.Write(Convert.ToString(nitrogenComp));
                                wr.Write(",");
                                wr.Write(Convert.ToString(oxygenComp));
                                wr.Write(",");
                                wr.Write(Convert.ToString(argonComp));
                                wr.Write(",");
                                wr.Write(Convert.ToString(vaporComp[0]));
                                wr.Write(",");
                                wr.Write(Convert.ToString(vaporComp[1]));
                                wr.Write(",");
                                wr.Write(Convert.ToString(vaporComp[2]));
                                wr.Write(",");
                                wr.Write(Convert.ToString(liquidComp[0]));
                                wr.Write(",");
                                wr.Write(Convert.ToString(liquidComp[1]));
                                wr.Write(",");
                                wr.Write(Convert.ToString(liquidComp[2]));
                                wr.Write(",");
                                wr.Write(Convert.ToString(vaporDensity));
                                wr.Write(",");
                                wr.Write(Convert.ToString(liquidDensity));
                                wr.Write(",");
                                wr.Write(Convert.ToString(vaporMolarEnthalpy));
                                wr.Write(",");
                                wr.Write(Convert.ToString(liquidMolarEnthalpy));
                                wr.Write(",");
                                wr.Write(Convert.ToString(vaporMolarFlow));
                                wr.Write(",");
                                wr.Write(Convert.ToString(liquidMolarFlow));
                                wr.Write("\n");
                            }
                        }

                    }
                }
            }
            catch(Exception e)
            {
                wr.Close();
            }
            wr.Close();
        }
		public void myFun_design_database()
        {
            PlantApplication HysysApp = MyHysysControlClass.Hysys_Connect();
            dynamic HysysSimulationCase = HysysApp.ActiveDocument;
            dynamic FEED = HysysSimulationCase.Flowsheet.MaterialStreams.Item("FEED");
            dynamic top = HysysSimulationCase.Flowsheet.MaterialStreams.Item("vapour");
            dynamic bottom = HysysSimulationCase.Flowsheet.MaterialStreams.Item("liquid");
            HysysSimulationCase.solver.CanSolve = true;
            
            //update

            double[] pressureRange = new double[] { 500, 600 };
            double[] nitrogenCompRange = new double[] { 0, 1 };
            double[] oxygenCompRange = new double[] { 0, 0.02 };
            double[] temperatureRange = new double[2];
            double[] feedComposition = new double[3];
            int n_sample1 = 4;
            int n_sample2 = 4;
            int n_sample3 = 4;
            int n_sample4 = 4;
            double temperature;
            double pressure;
            double nitrogenComp;
            double oxygenComp;
            double argonComp;
            double[] vaporComp;
            double[] liquidComp;
            double vaporDensity;
            double liquidDensity;
            double vaporMolarEnthalpy;
            double liquidMolarEnthalpy;
            double vaporMolarFlow;
            double liquidMolarFlow;
            
            try
            {
				foreach (DataRow dr in rawData.Rows)
				{
					string name  = dr["Place"] as string; 
					string result1 = @"C:\Users\lou\Desktop\connect\dataset_design\"+name+".csv";//结果保存到F:\result1.txt
					FileStream fs = new FileStream(result1, FileMode.Create);
					StreamWriter wr = null;
					wr = new StreamWriter(fs);
					wr.Write("P,T,N2,O2,Ar,y_N2,y_O2,y_Ar,x_N2,x_O2,x_Ar,vap_rho,liq_rho,vap_etlp,liq_etlp,vap_F,liq_F\n");
					pressureRange[0] = dr["P_min"] as double; 
					pressureRange[1] = dr["P_max"] as double; 
					temperatureRange[0] = dr["T_min"] as double; 
					temperatureRange[1] = dr["T_max"] as double; 
					nitrogenCompRange[0] = dr["x_N2_min"] as double; 
					nitrogenCompRange[1] = dr["x_N2_max"] as double; 
					oxygenCompRange[0] = dr["x_O2_min"] as double; 
					oxygenCompRange[1] = dr["x_O2_max"] as double; 

					for (int i = 0; i <= n_sample1; i++)
					{
						pressure = pressureRange[0] + i * (pressureRange[1] - pressureRange[0]) / n_sample1;
						for (int j = 0; j <= n_sample2; j++)
						{
							temperature = temperatureRange[0] + j * (temperatureRange[1] - temperatureRange[0]) / n_sample2;
							for (int x = 0; x <= n_sample3; x++)
							{
								nitrogenComp = nitrogenCompRange[0] + x * (nitrogenCompRange[1] - nitrogenCompRange[0]) / n_sample3;
								for (int y = 0; y <= n_sample4; y++)
								{
									oxygenComp = oxygenCompRange[0] + y * (oxygenCompRange[1] - oxygenCompRange[0]) / n_sample4;
									argonComp = 1 - nitrogenComp - oxygenComp;
									if (argonComp < 0)
									{
										break;
									}
									FEED.PressureValue = pressure;
									FEED.TemperatureValue = temperature;
									feedComposition[0] = nitrogenComp;
									feedComposition[1] = oxygenComp;
									feedComposition[2] = argonComp;
									FEED.ComponentMolarFractionValue = feedComposition;
									vaporComp = top.ComponentMolarFractionValue;
									liquidComp = bottom.ComponentMolarFractionValue;
									vaporDensity = top.MolarDensityValue;
									liquidDensity = bottom.MolarDensityValue;
									vaporMolarEnthalpy = top.MolarEnthalpyValue;
									liquidMolarEnthalpy = bottom.MolarEnthalpyValue;
									vaporMolarFlow = top.MolarFlowValue;
									liquidMolarFlow = bottom.MolarFlowValue;
									if(vaporMolarFlow<=1e-10)
									{
										continue
									}
									if(liquidMolarFlow<=1e-10)
									{
										continue
									}
									wr.Write(Convert.ToString(pressure));
									wr.Write(",");
									wr.Write(Convert.ToString(temperature));
									wr.Write(",");
									wr.Write(Convert.ToString(nitrogenComp));
									wr.Write(",");
									wr.Write(Convert.ToString(oxygenComp));
									wr.Write(",");
									wr.Write(Convert.ToString(argonComp));
									wr.Write(",");
									wr.Write(Convert.ToString(vaporComp[0]));
									wr.Write(",");
									wr.Write(Convert.ToString(vaporComp[1]));
									wr.Write(",");
									wr.Write(Convert.ToString(vaporComp[2]));
									wr.Write(",");
									wr.Write(Convert.ToString(liquidComp[0]));
									wr.Write(",");
									wr.Write(Convert.ToString(liquidComp[1]));
									wr.Write(",");
									wr.Write(Convert.ToString(liquidComp[2]));
									wr.Write(",");
									wr.Write(Convert.ToString(vaporDensity));
									wr.Write(",");
									wr.Write(Convert.ToString(liquidDensity));
									wr.Write(",");
									wr.Write(Convert.ToString(vaporMolarEnthalpy));
									wr.Write(",");
									wr.Write(Convert.ToString(liquidMolarEnthalpy));
									wr.Write(",");
									wr.Write(Convert.ToString(vaporMolarFlow));
									wr.Write(",");
									wr.Write(Convert.ToString(liquidMolarFlow));
									wr.Write("\n");
								}
							}

						}
					}
					wr.Close();
				}
            }
            catch(Exception e)
            {
                wr.Close();
            }
            
        }
        private void Close_Click(object sender, EventArgs e)
        {
            //close
            
            Process[] P = Process.GetProcessesByName("AspenHysys");
            P[0].Kill();
        }
    }
}
