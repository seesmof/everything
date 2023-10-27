namespace dev
{
    partial class FormA
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
            this.expInput = new System.Windows.Forms.NumericUpDown();
            this.baseInput = new System.Windows.Forms.NumericUpDown();
            this.lblExpInput = new System.Windows.Forms.Label();
            this.lblBaseInput = new System.Windows.Forms.Label();
            this.btnRun = new System.Windows.Forms.Button();
            this.btnReset = new System.Windows.Forms.Button();
            this.progressOutput = new System.Windows.Forms.ProgressBar();
            this.lblOutput = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.expInput)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.baseInput)).BeginInit();
            this.SuspendLayout();
            // 
            // expInput
            // 
            this.expInput.Location = new System.Drawing.Point(230, 44);
            this.expInput.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.expInput.Name = "expInput";
            this.expInput.Size = new System.Drawing.Size(180, 20);
            this.expInput.TabIndex = 0;
            this.expInput.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // baseInput
            // 
            this.baseInput.Location = new System.Drawing.Point(12, 44);
            this.baseInput.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.baseInput.Name = "baseInput";
            this.baseInput.Size = new System.Drawing.Size(212, 20);
            this.baseInput.TabIndex = 1;
            this.baseInput.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // lblExpInput
            // 
            this.lblExpInput.AutoSize = true;
            this.lblExpInput.Location = new System.Drawing.Point(227, 28);
            this.lblExpInput.Name = "lblExpInput";
            this.lblExpInput.Size = new System.Drawing.Size(92, 13);
            this.lblExpInput.TabIndex = 2;
            this.lblExpInput.Text = "Exponent Number";
            // 
            // lblBaseInput
            // 
            this.lblBaseInput.AutoSize = true;
            this.lblBaseInput.Location = new System.Drawing.Point(12, 28);
            this.lblBaseInput.Name = "lblBaseInput";
            this.lblBaseInput.Size = new System.Drawing.Size(71, 13);
            this.lblBaseInput.TabIndex = 2;
            this.lblBaseInput.Text = "Base Number";
            // 
            // btnRun
            // 
            this.btnRun.Location = new System.Drawing.Point(416, 44);
            this.btnRun.Name = "btnRun";
            this.btnRun.Size = new System.Drawing.Size(75, 20);
            this.btnRun.TabIndex = 3;
            this.btnRun.Text = "Run";
            this.btnRun.UseVisualStyleBackColor = true;
            this.btnRun.Click += new System.EventHandler(this.btnRun_Click);
            // 
            // btnReset
            // 
            this.btnReset.Location = new System.Drawing.Point(497, 44);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(75, 20);
            this.btnReset.TabIndex = 3;
            this.btnReset.Text = "Reset";
            this.btnReset.UseVisualStyleBackColor = true;
            this.btnReset.Click += new System.EventHandler(this.btnReset_Click);
            // 
            // progressOutput
            // 
            this.progressOutput.Location = new System.Drawing.Point(15, 81);
            this.progressOutput.Name = "progressOutput";
            this.progressOutput.Size = new System.Drawing.Size(557, 23);
            this.progressOutput.TabIndex = 4;
            // 
            // lblOutput
            // 
            this.lblOutput.AutoSize = true;
            this.lblOutput.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblOutput.Location = new System.Drawing.Point(12, 142);
            this.lblOutput.Name = "lblOutput";
            this.lblOutput.Size = new System.Drawing.Size(166, 25);
            this.lblOutput.TabIndex = 5;
            this.lblOutput.Text = "Results here...";
            // 
            // FormA
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(584, 361);
            this.Controls.Add(this.lblOutput);
            this.Controls.Add(this.progressOutput);
            this.Controls.Add(this.btnReset);
            this.Controls.Add(this.btnRun);
            this.Controls.Add(this.lblBaseInput);
            this.Controls.Add(this.lblExpInput);
            this.Controls.Add(this.baseInput);
            this.Controls.Add(this.expInput);
            this.MaximumSize = new System.Drawing.Size(600, 400);
            this.MinimumSize = new System.Drawing.Size(600, 400);
            this.Name = "FormA";
            this.Text = "Task A";
            ((System.ComponentModel.ISupportInitialize)(this.expInput)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.baseInput)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.NumericUpDown expInput;
        private System.Windows.Forms.NumericUpDown baseInput;
        private System.Windows.Forms.Label lblExpInput;
        private System.Windows.Forms.Label lblBaseInput;
        private System.Windows.Forms.Button btnRun;
        private System.Windows.Forms.Button btnReset;
        private System.Windows.Forms.ProgressBar progressOutput;
        private System.Windows.Forms.Label lblOutput;
    }
}

