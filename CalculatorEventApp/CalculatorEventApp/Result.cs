using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CalculatorEventApp
{
    public partial class Result : Form
    {
        
        public Result()
        {
            InitializeComponent();
        }
        private void btnHitung_Click(object sender, EventArgs e)
        {
            Calculator getCalculator = new Calculator();
            getCalculator.OnProses += new Calculator.Ali1999(this.Callback);
            float num = (float)getCalculator.ShowDialog();
        }

        private void Callback(string name, string symbol, float a, float b, float hasil)
        {
            listResult.Items.Add("Hasil " + name + " " + a + " " + symbol + " " + b + " = " + hasil);
        }
    }
}
