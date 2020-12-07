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
    public partial class Calculator : Form
    {
        public delegate void Ali1999(string name, string symbol, float a, float b, float hasil);

        public event Ali1999 OnProses;
        public Calculator()
        {
            InitializeComponent();
        }
        private void btnSubmit_Click(object sender, EventArgs e)
        {
            string name = this.cmbOperasi.Text.ToLower();
            string symbol = null;
            float hasil = 0;
            float NilaiA = float.Parse(txtNilaiA.Text);
            float NilaiB = float.Parse(txtNilaiB.Text);
            switch (this.cmbOperasi.SelectedIndex)
            {
                case 0:
                    hasil = NilaiA + NilaiB;
                    symbol = "+";
                    break;
                case 1:
                    hasil = NilaiA - NilaiB;
                    symbol = "-";
                    break;
                case 2:
                    hasil = NilaiA * NilaiB;
                    symbol = "*";
                    break;
                case 3:
                    hasil = NilaiA / NilaiB;
                    symbol = "/";
                    break;
            }
            this.OnProses(name, symbol, NilaiA, NilaiB, hasil);
        }
    }
}
