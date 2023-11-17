// Завдання 3

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
            this.tableList = new System.Windows.Forms.ListView();
            this.inputMultiplier = new System.Windows.Forms.NumericUpDown();
            this.btnRun = new System.Windows.Forms.Button();
            this.lblMultiplier = new System.Windows.Forms.Label();
            this.progressOutput = new System.Windows.Forms.ProgressBar();
            ((System.ComponentModel.ISupportInitialize)(this.inputMultiplier)).BeginInit();
            this.SuspendLayout();
            // 
            // tableList
            // 
            this.tableList.HideSelection = false;
            this.tableList.Location = new System.Drawing.Point(12, 90);
            this.tableList.Name = "tableList";
            this.tableList.Size = new System.Drawing.Size(560, 259);
            this.tableList.TabIndex = 0;
            this.tableList.TileSize = new System.Drawing.Size(60, 30);
            this.tableList.UseCompatibleStateImageBehavior = false;
            // 
            // inputMultiplier
            // 
            this.inputMultiplier.Location = new System.Drawing.Point(12, 25);
            this.inputMultiplier.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.inputMultiplier.Name = "inputMultiplier";
            this.inputMultiplier.Size = new System.Drawing.Size(479, 20);
            this.inputMultiplier.TabIndex = 1;
            this.inputMultiplier.Value = new decimal(new int[] {
            9,
            0,
            0,
            0});
            // 
            // btnRun
            // 
            this.btnRun.Location = new System.Drawing.Point(497, 25);
            this.btnRun.Name = "btnRun";
            this.btnRun.Size = new System.Drawing.Size(75, 20);
            this.btnRun.TabIndex = 2;
            this.btnRun.Text = "Run";
            this.btnRun.UseVisualStyleBackColor = true;
            this.btnRun.Click += new System.EventHandler(this.btnRun_Click);
            // 
            // lblMultiplier
            // 
            this.lblMultiplier.AutoSize = true;
            this.lblMultiplier.Location = new System.Drawing.Point(9, 9);
            this.lblMultiplier.Name = "lblMultiplier";
            this.lblMultiplier.Size = new System.Drawing.Size(78, 13);
            this.lblMultiplier.TabIndex = 3;
            this.lblMultiplier.Text = "Multiplier Value";
            // 
            // progressOutput
            // 
            this.progressOutput.Location = new System.Drawing.Point(12, 61);
            this.progressOutput.Name = "progressOutput";
            this.progressOutput.Size = new System.Drawing.Size(560, 23);
            this.progressOutput.TabIndex = 4;
            // 
            // MainForm
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.ClientSize = new System.Drawing.Size(584, 361);
            this.Controls.Add(this.progressOutput);
            this.Controls.Add(this.lblMultiplier);
            this.Controls.Add(this.btnRun);
            this.Controls.Add(this.inputMultiplier);
            this.Controls.Add(this.tableList);
            this.MaximumSize = new System.Drawing.Size(600, 400);
            this.MinimumSize = new System.Drawing.Size(600, 400);
            this.Name = "MainForm";
            this.Text = "Task A";
            ((System.ComponentModel.ISupportInitialize)(this.inputMultiplier)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListView tableList;
        private System.Windows.Forms.NumericUpDown inputMultiplier;
        private System.Windows.Forms.Button btnRun;
        private System.Windows.Forms.Label lblMultiplier;
        private System.Windows.Forms.ProgressBar progressOutput;
    }
}

