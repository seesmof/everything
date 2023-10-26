namespace dev
{
    partial class TaskA
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
            this.inputBase = new System.Windows.Forms.NumericUpDown();
            this.inputExponent = new System.Windows.Forms.NumericUpDown();
            this.lblBaseInput = new System.Windows.Forms.Label();
            this.lblExponentInput = new System.Windows.Forms.Label();
            this.btnCalculate = new System.Windows.Forms.Button();
            this.progressOutput = new System.Windows.Forms.ProgressBar();
            this.lblResults = new System.Windows.Forms.Label();
            this.btnReset = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.inputBase)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputExponent)).BeginInit();
            this.SuspendLayout();
            // 
            // inputBase
            // 
            this.inputBase.Location = new System.Drawing.Point(11, 26);
            this.inputBase.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.inputBase.Maximum = new decimal(new int[] {
            999999999,
            0,
            0,
            0});
            this.inputBase.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.inputBase.Name = "inputBase";
            this.inputBase.Size = new System.Drawing.Size(203, 20);
            this.inputBase.TabIndex = 0;
            this.inputBase.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // inputExponent
            // 
            this.inputExponent.Location = new System.Drawing.Point(218, 26);
            this.inputExponent.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.inputExponent.Maximum = new decimal(new int[] {
            999999999,
            0,
            0,
            0});
            this.inputExponent.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.inputExponent.Name = "inputExponent";
            this.inputExponent.Size = new System.Drawing.Size(154, 20);
            this.inputExponent.TabIndex = 0;
            this.inputExponent.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // lblBaseInput
            // 
            this.lblBaseInput.AutoSize = true;
            this.lblBaseInput.Location = new System.Drawing.Point(12, 11);
            this.lblBaseInput.Name = "lblBaseInput";
            this.lblBaseInput.Size = new System.Drawing.Size(71, 13);
            this.lblBaseInput.TabIndex = 1;
            this.lblBaseInput.Text = "Base Number";
            // 
            // lblExponentInput
            // 
            this.lblExponentInput.AutoSize = true;
            this.lblExponentInput.Location = new System.Drawing.Point(215, 11);
            this.lblExponentInput.Name = "lblExponentInput";
            this.lblExponentInput.Size = new System.Drawing.Size(92, 13);
            this.lblExponentInput.TabIndex = 1;
            this.lblExponentInput.Text = "Exponent Number";
            // 
            // btnCalculate
            // 
            this.btnCalculate.Location = new System.Drawing.Point(377, 26);
            this.btnCalculate.Name = "btnCalculate";
            this.btnCalculate.Size = new System.Drawing.Size(66, 20);
            this.btnCalculate.TabIndex = 2;
            this.btnCalculate.Text = "Run";
            this.btnCalculate.UseVisualStyleBackColor = true;
            this.btnCalculate.Click += new System.EventHandler(this.btnCalculate_Click);
            // 
            // progressOutput
            // 
            this.progressOutput.Location = new System.Drawing.Point(11, 63);
            this.progressOutput.Name = "progressOutput";
            this.progressOutput.Size = new System.Drawing.Size(500, 23);
            this.progressOutput.TabIndex = 3;
            // 
            // lblResults
            // 
            this.lblResults.AutoSize = true;
            this.lblResults.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblResults.Location = new System.Drawing.Point(8, 121);
            this.lblResults.Name = "lblResults";
            this.lblResults.Size = new System.Drawing.Size(71, 20);
            this.lblResults.TabIndex = 1;
            this.lblResults.Text = "Result: ";
            // 
            // btnReset
            // 
            this.btnReset.Location = new System.Drawing.Point(445, 26);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(66, 20);
            this.btnReset.TabIndex = 2;
            this.btnReset.Text = "Reset";
            this.btnReset.UseVisualStyleBackColor = true;
            this.btnReset.Click += new System.EventHandler(this.btnReset_Click);
            // 
            // TaskA
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(523, 365);
            this.Controls.Add(this.progressOutput);
            this.Controls.Add(this.btnReset);
            this.Controls.Add(this.btnCalculate);
            this.Controls.Add(this.lblExponentInput);
            this.Controls.Add(this.lblResults);
            this.Controls.Add(this.lblBaseInput);
            this.Controls.Add(this.inputExponent);
            this.Controls.Add(this.inputBase);
            this.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.MaximumSize = new System.Drawing.Size(539, 404);
            this.MinimumSize = new System.Drawing.Size(539, 404);
            this.Name = "TaskA";
            this.Text = "TaskA";
            ((System.ComponentModel.ISupportInitialize)(this.inputBase)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputExponent)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.NumericUpDown inputBase;
        private System.Windows.Forms.NumericUpDown inputExponent;
        private System.Windows.Forms.Label lblBaseInput;
        private System.Windows.Forms.Label lblExponentInput;
        private System.Windows.Forms.Button btnCalculate;
        private System.Windows.Forms.ProgressBar progressOutput;
        private System.Windows.Forms.Label lblResults;
        private System.Windows.Forms.Button btnReset;
    }
}