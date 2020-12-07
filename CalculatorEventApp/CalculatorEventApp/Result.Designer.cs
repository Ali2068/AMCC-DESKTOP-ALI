namespace CalculatorEventApp
{
    partial class Result
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.HasilBox = new System.Windows.Forms.GroupBox();
            this.btnHitung = new System.Windows.Forms.Button();
            this.listResult = new System.Windows.Forms.ListBox();
            this.HasilBox.SuspendLayout();
            this.SuspendLayout();
            // 
            // HasilBox
            // 
            this.HasilBox.Controls.Add(this.listResult);
            this.HasilBox.Location = new System.Drawing.Point(11, 11);
            this.HasilBox.Name = "HasilBox";
            this.HasilBox.Size = new System.Drawing.Size(356, 362);
            this.HasilBox.TabIndex = 0;
            this.HasilBox.TabStop = false;
            this.HasilBox.Text = "[ Hasil ]";
            // 
            // btnHitung
            // 
            this.btnHitung.Location = new System.Drawing.Point(12, 388);
            this.btnHitung.Name = "btnHitung";
            this.btnHitung.Size = new System.Drawing.Size(355, 33);
            this.btnHitung.TabIndex = 1;
            this.btnHitung.Text = "Hitung";
            this.btnHitung.UseVisualStyleBackColor = true;
            this.btnHitung.Click += new System.EventHandler(this.btnHitung_Click);
            // 
            // listResult
            // 
            this.listResult.FormattingEnabled = true;
            this.listResult.ItemHeight = 16;
            this.listResult.Location = new System.Drawing.Point(6, 29);
            this.listResult.Name = "listResult";
            this.listResult.Size = new System.Drawing.Size(344, 324);
            this.listResult.TabIndex = 0;
            // 
            // Result
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(376, 435);
            this.Controls.Add(this.btnHitung);
            this.Controls.Add(this.HasilBox);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "Result";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Hasil Perhitungan";
            this.HasilBox.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox HasilBox;
        private System.Windows.Forms.Button btnHitung;
        private System.Windows.Forms.ListBox listResult;
    }
}

