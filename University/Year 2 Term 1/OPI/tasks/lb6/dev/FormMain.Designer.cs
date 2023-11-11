namespace dev
{
    partial class FormMain
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
            this.components = new System.ComponentModel.Container();
            this.dateTimePickerAlarm = new System.Windows.Forms.DateTimePicker();
            this.comboBoxDayOfWeek = new System.Windows.Forms.ComboBox();
            this.textBoxMessage = new System.Windows.Forms.TextBox();
            this.lblTime = new System.Windows.Forms.Label();
            this.lblDayOfWeek = new System.Windows.Forms.Label();
            this.lblMessage = new System.Windows.Forms.Label();
            this.buttonSetAlarm = new System.Windows.Forms.Button();
            this.lblStatus = new System.Windows.Forms.Label();
            this.timerAlarm = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // dateTimePickerAlarm
            // 
            this.dateTimePickerAlarm.Format = System.Windows.Forms.DateTimePickerFormat.Time;
            this.dateTimePickerAlarm.Location = new System.Drawing.Point(12, 38);
            this.dateTimePickerAlarm.Name = "dateTimePickerAlarm";
            this.dateTimePickerAlarm.Size = new System.Drawing.Size(75, 22);
            this.dateTimePickerAlarm.TabIndex = 0;
            // 
            // comboBoxDayOfWeek
            // 
            this.comboBoxDayOfWeek.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBoxDayOfWeek.FormattingEnabled = true;
            this.comboBoxDayOfWeek.Items.AddRange(new object[] {
            "Понеділок",
            "Вівторок",
            "Середа",
            "Четвер",
            "П\'ятниця",
            "Субота",
            "Неділя"});
            this.comboBoxDayOfWeek.Location = new System.Drawing.Point(93, 38);
            this.comboBoxDayOfWeek.Name = "comboBoxDayOfWeek";
            this.comboBoxDayOfWeek.Size = new System.Drawing.Size(162, 24);
            this.comboBoxDayOfWeek.TabIndex = 1;
            // 
            // textBoxMessage
            // 
            this.textBoxMessage.Location = new System.Drawing.Point(261, 40);
            this.textBoxMessage.Name = "textBoxMessage";
            this.textBoxMessage.Size = new System.Drawing.Size(195, 22);
            this.textBoxMessage.TabIndex = 2;
            // 
            // lblTime
            // 
            this.lblTime.AutoSize = true;
            this.lblTime.Location = new System.Drawing.Point(12, 19);
            this.lblTime.Name = "lblTime";
            this.lblTime.Size = new System.Drawing.Size(38, 16);
            this.lblTime.TabIndex = 3;
            this.lblTime.Text = "Time";
            // 
            // lblDayOfWeek
            // 
            this.lblDayOfWeek.AutoSize = true;
            this.lblDayOfWeek.Location = new System.Drawing.Point(90, 19);
            this.lblDayOfWeek.Name = "lblDayOfWeek";
            this.lblDayOfWeek.Size = new System.Drawing.Size(106, 16);
            this.lblDayOfWeek.TabIndex = 3;
            this.lblDayOfWeek.Text = "Day of the Week";
            // 
            // lblMessage
            // 
            this.lblMessage.AutoSize = true;
            this.lblMessage.Location = new System.Drawing.Point(258, 19);
            this.lblMessage.Name = "lblMessage";
            this.lblMessage.Size = new System.Drawing.Size(64, 16);
            this.lblMessage.TabIndex = 3;
            this.lblMessage.Text = "Message";
            // 
            // buttonSetAlarm
            // 
            this.buttonSetAlarm.BackColor = System.Drawing.Color.YellowGreen;
            this.buttonSetAlarm.FlatAppearance.BorderSize = 0;
            this.buttonSetAlarm.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonSetAlarm.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonSetAlarm.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.buttonSetAlarm.Location = new System.Drawing.Point(462, 39);
            this.buttonSetAlarm.Name = "buttonSetAlarm";
            this.buttonSetAlarm.Size = new System.Drawing.Size(112, 23);
            this.buttonSetAlarm.TabIndex = 4;
            this.buttonSetAlarm.Text = "Set Alarm";
            this.buttonSetAlarm.UseVisualStyleBackColor = false;
            this.buttonSetAlarm.Click += new System.EventHandler(this.buttonSetAlarm_Click);
            // 
            // lblStatus
            // 
            this.lblStatus.AutoSize = true;
            this.lblStatus.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblStatus.Location = new System.Drawing.Point(12, 76);
            this.lblStatus.Name = "lblStatus";
            this.lblStatus.Size = new System.Drawing.Size(76, 20);
            this.lblStatus.TabIndex = 3;
            this.lblStatus.Text = "Status: ...";
            // 
            // timerAlarm
            // 
            this.timerAlarm.Tick += new System.EventHandler(this.timerAlarm_Tick);
            // 
            // FormMain
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.ClientSize = new System.Drawing.Size(584, 361);
            this.Controls.Add(this.buttonSetAlarm);
            this.Controls.Add(this.lblMessage);
            this.Controls.Add(this.lblStatus);
            this.Controls.Add(this.lblDayOfWeek);
            this.Controls.Add(this.lblTime);
            this.Controls.Add(this.textBoxMessage);
            this.Controls.Add(this.comboBoxDayOfWeek);
            this.Controls.Add(this.dateTimePickerAlarm);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.MaximumSize = new System.Drawing.Size(600, 400);
            this.MinimumSize = new System.Drawing.Size(600, 400);
            this.Name = "FormMain";
            this.Text = "Робота з клавіатурою - ОПІ Лабораторна 6";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DateTimePicker dateTimePickerAlarm;
        private System.Windows.Forms.ComboBox comboBoxDayOfWeek;
        private System.Windows.Forms.TextBox textBoxMessage;
        private System.Windows.Forms.Label lblTime;
        private System.Windows.Forms.Label lblDayOfWeek;
        private System.Windows.Forms.Label lblMessage;
        private System.Windows.Forms.Button buttonSetAlarm;
        private System.Windows.Forms.Label lblStatus;
        private System.Windows.Forms.Timer timerAlarm;
    }
}

