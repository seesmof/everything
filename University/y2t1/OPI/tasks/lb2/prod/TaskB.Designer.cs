// Завдання 2

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
            this.leftList = new System.Windows.Forms.ListView();
            this.rightList = new System.Windows.Forms.ListView();
            this.btnAddL = new System.Windows.Forms.Button();
            this.btnRemoveL = new System.Windows.Forms.Button();
            this.btnMoveLeft = new System.Windows.Forms.Button();
            this.btnAddR = new System.Windows.Forms.Button();
            this.btnRemoveR = new System.Windows.Forms.Button();
            this.btnMoveRight = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // leftList
            // 
            this.leftList.HideSelection = false;
            this.leftList.Location = new System.Drawing.Point(12, 12);
            this.leftList.Name = "leftList";
            this.leftList.Size = new System.Drawing.Size(271, 246);
            this.leftList.TabIndex = 0;
            this.leftList.UseCompatibleStateImageBehavior = false;
            // 
            // rightList
            // 
            this.rightList.HideSelection = false;
            this.rightList.Location = new System.Drawing.Point(312, 12);
            this.rightList.Name = "rightList";
            this.rightList.Size = new System.Drawing.Size(260, 246);
            this.rightList.TabIndex = 0;
            this.rightList.UseCompatibleStateImageBehavior = false;
            // 
            // btnAddL
            // 
            this.btnAddL.Location = new System.Drawing.Point(12, 264);
            this.btnAddL.Name = "btnAddL";
            this.btnAddL.Size = new System.Drawing.Size(136, 33);
            this.btnAddL.TabIndex = 1;
            this.btnAddL.Text = "Add";
            this.btnAddL.UseVisualStyleBackColor = true;
            this.btnAddL.Click += new System.EventHandler(this.btnAddL_Click);
            // 
            // btnRemoveL
            // 
            this.btnRemoveL.Location = new System.Drawing.Point(154, 264);
            this.btnRemoveL.Name = "btnRemoveL";
            this.btnRemoveL.Size = new System.Drawing.Size(129, 33);
            this.btnRemoveL.TabIndex = 1;
            this.btnRemoveL.Text = "Remove";
            this.btnRemoveL.UseVisualStyleBackColor = true;
            this.btnRemoveL.Click += new System.EventHandler(this.btnRemoveL_Click);
            // 
            // btnMoveLeft
            // 
            this.btnMoveLeft.Location = new System.Drawing.Point(312, 303);
            this.btnMoveLeft.Name = "btnMoveLeft";
            this.btnMoveLeft.Size = new System.Drawing.Size(260, 33);
            this.btnMoveLeft.TabIndex = 1;
            this.btnMoveLeft.Text = "Move left";
            this.btnMoveLeft.UseVisualStyleBackColor = true;
            this.btnMoveLeft.Click += new System.EventHandler(this.btnMoveLeft_Click);
            // 
            // btnAddR
            // 
            this.btnAddR.Location = new System.Drawing.Point(312, 264);
            this.btnAddR.Name = "btnAddR";
            this.btnAddR.Size = new System.Drawing.Size(125, 33);
            this.btnAddR.TabIndex = 1;
            this.btnAddR.Text = "Add";
            this.btnAddR.UseVisualStyleBackColor = true;
            this.btnAddR.Click += new System.EventHandler(this.btnAddR_Click);
            // 
            // btnRemoveR
            // 
            this.btnRemoveR.Location = new System.Drawing.Point(443, 264);
            this.btnRemoveR.Name = "btnRemoveR";
            this.btnRemoveR.Size = new System.Drawing.Size(129, 33);
            this.btnRemoveR.TabIndex = 1;
            this.btnRemoveR.Text = "Remove";
            this.btnRemoveR.UseVisualStyleBackColor = true;
            this.btnRemoveR.Click += new System.EventHandler(this.btnRemoveR_Click);
            // 
            // btnMoveRight
            // 
            this.btnMoveRight.Location = new System.Drawing.Point(12, 303);
            this.btnMoveRight.Name = "btnMoveRight";
            this.btnMoveRight.Size = new System.Drawing.Size(271, 33);
            this.btnMoveRight.TabIndex = 1;
            this.btnMoveRight.Text = "Move right";
            this.btnMoveRight.UseVisualStyleBackColor = true;
            this.btnMoveRight.Click += new System.EventHandler(this.btnMoveRight_Click);
            // 
            // MainForm
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.ClientSize = new System.Drawing.Size(584, 361);
            this.Controls.Add(this.btnMoveRight);
            this.Controls.Add(this.btnMoveLeft);
            this.Controls.Add(this.btnRemoveR);
            this.Controls.Add(this.btnAddR);
            this.Controls.Add(this.btnRemoveL);
            this.Controls.Add(this.btnAddL);
            this.Controls.Add(this.rightList);
            this.Controls.Add(this.leftList);
            this.MaximumSize = new System.Drawing.Size(600, 400);
            this.MinimumSize = new System.Drawing.Size(600, 400);
            this.Name = "MainForm";
            this.Text = "Task A";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListView leftList;
        private System.Windows.Forms.ListView rightList;
        private System.Windows.Forms.Button btnAddL;
        private System.Windows.Forms.Button btnRemoveL;
        private System.Windows.Forms.Button btnMoveLeft;
        private System.Windows.Forms.Button btnAddR;
        private System.Windows.Forms.Button btnRemoveR;
        private System.Windows.Forms.Button btnMoveRight;
    }
}

