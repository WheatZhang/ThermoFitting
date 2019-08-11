using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using HYSYS;
using Microsoft.VisualBasic;
using System.Resources;
using System.Windows.Forms;
using HYSYS_RTO;
using System.IO;
using System.Drawing;
using System.Data;
using System.Drawing.Drawing2D;
using Microsoft;
using MSChart20Lib;
using MSChartLib;
using MSDATASRC;





namespace HYSYS_RTO.HysysContral
{
    class HysysControlClass
    {

        public PlantApplication Hysys_Connect()
        {
            dynamic HysysApp = Microsoft.VisualBasic.Interaction.CreateObject("HYSYS.Application");
            //dynamic HysysSimulation = Microsoft.VisualBasic.Interaction.GetObject("C:/ZY/05HYSYS/hysys_optimization_N2.hsc");

            HysysApp.visible = true;
            //HysysSimulation.visible = true;

            return HysysApp;
        }
        
    }
}
