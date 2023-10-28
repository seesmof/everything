// Завдання 1

namespace dev
{
    partial class MainForm
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
            this.btnReset = new System.Windows.Forms.Button();
            this.btnRun = new System.Windows.Forms.Button();
            this.baseInput = new System.Windows.Forms.NumericUpDown();
            this.lblBaseInput = new System.Windows.Forms.Label();
            this.expInput = new System.Windows.Forms.NumericUpDown();
            this.lblExpInput = new System.Windows.Forms.Label();
            this.progressOutput = new System.Windows.Forms.ProgressBar();
            this.lblOutput = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.baseInput)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.expInput)).BeginInit();
            this.SuspendLayout();
            // 
            // btnReset
            // 
            this.btnReset.Location = new System.Drawing.Point(497, 35);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(75, 20);
            this.btnReset.TabIndex = 0;
            this.btnReset.Text = "Reset";
            this.btnReset.UseVisualStyleBackColor = true;
            this.btnReset.Click += new System.EventHandler(this.btnReset_Click);
            // 
            // btnRun
            // 
            this.btnRun.Location = new System.Drawing.Point(416, 35);
            this.btnRun.Name = "btnRun";
            this.btnRun.Size = new System.Drawing.Size(75, 20);
            this.btnRun.TabIndex = 0;
            this.btnRun.Text = "Run";
            this.btnRun.UseVisualStyleBackColor = true;
            this.btnRun.Click += new System.EventHandler(this.btnRun_Click);
            // 
            // baseInput
            // 
            this.baseInput.Location = new System.Drawing.Point(12, 35);
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
            // lblBaseInput
            // 
            this.lblBaseInput.AutoSize = true;
            this.lblBaseInput.Location = new System.Drawing.Point(9, 19);
            this.lblBaseInput.Name = "lblBaseInput";
            this.lblBaseInput.Size = new System.Drawing.Size(71, 13);
            this.lblBaseInput.TabIndex = 2;
            this.lblBaseInput.Text = "Base Number";
            // 
            // expInput
            // 
            this.expInput.Location = new System.Drawing.Point(230, 35);
            this.expInput.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.expInput.Name = "expInput";
            this.expInput.Size = new System.Drawing.Size(180, 20);
            this.expInput.TabIndex = 1;
            this.expInput.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // lblExpInput
            // 
            this.lblExpInput.AutoSize = true;
            this.lblExpInput.Location = new System.Drawing.Point(227, 19);
            this.lblExpInput.Name = "lblExpInput";
            this.lblExpInput.Size = new System.Drawing.Size(71, 13);
            this.lblExpInput.TabIndex = 2;
            this.lblExpInput.Text = "Base Number";
            // 
            // progressOutput
            // 
            this.progressOutput.Location = new System.Drawing.Point(12, 71);
            this.progressOutput.Name = "progressOutput";
            this.progressOutput.Size = new System.Drawing.Size(560, 23);
            this.progressOutput.TabIndex = 3;
            // 
            // lblOutput
            // 
            this.lblOutput.AutoSize = true;
            this.lblOutput.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblOutput.Location = new System.Drawing.Point(9, 171);
            this.lblOutput.Name = "lblOutput";
            this.lblOutput.Size = new System.Drawing.Size(166, 25);
            this.lblOutput.TabIndex = 4;
            this.lblOutput.Text = "Results here...";
            // 
            // MainForm
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.ClientSize = new System.Drawing.Size(584, 361);
            this.Controls.Add(this.lblOutput);
            this.Controls.Add(this.progressOutput);
            this.Controls.Add(this.lblExpInput);
            this.Controls.Add(this.lblBaseInput);
            this.Controls.Add(this.expInput);
            this.Controls.Add(this.baseInput);
            this.Controls.Add(this.btnRun);
            this.Controls.Add(this.btnReset);
            this.MaximumSize = new System.Drawing.Size(600, 400);
            this.MinimumSize = new System.Drawing.Size(600, 400);
            this.Name = "MainForm";
            this.Text = "Task A";
            ((System.ComponentModel.ISupportInitialize)(this.baseInput)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.expInput)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnReset;
        private System.Windows.Forms.Button btnRun;
        private System.Windows.Forms.NumericUpDown baseInput;
        private System.Windows.Forms.Label lblBaseInput;
        private System.Windows.Forms.NumericUpDown expInput;
        private System.Windows.Forms.Label lblExpInput;
        private System.Windows.Forms.ProgressBar progressOutput;
        private System.Windows.Forms.Label lblOutput;
    }
}

