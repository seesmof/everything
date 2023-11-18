// Task B - Main
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace dev
{
    public partial class FormMain : Form
    {
        private DateTime alarmTime;
        private DayOfWeek alarmDay;
        private string alarmText;
        public FormMain()
        {
            InitializeComponent();
        }

        private void CreateAlarm()
        {
            AlarmClock alarmClock = new AlarmClock(this.alarmTime, this.alarmDay);
            alarmClock.Alarm += () =>
            {
                MessageBox.Show(this.alarmText, "Alarm");
                lblStatus.Text = "Status: Not Set";
            };
            lblStatus.Text = $"Status: Set to {this.alarmTime} on {this.alarmDay}";
        }

        private void btnCreate_Click(object sender, EventArgs e)
        {
            this.alarmTime = dateTimePickerTime.Value;
            this.alarmDay = (DayOfWeek)Enum.Parse(typeof(DayOfWeek), comboBoxDayOfWeek.SelectedItem.ToString());
            this.alarmText = textBoxMessage.Text;

            CreateAlarm();
        }

        private void FormMain_FormClosing(object sender, FormClosingEventArgs e)
        {
            using (StreamWriter sw = new StreamWriter("alarm.txt"))
            {
                sw.WriteLine(this.alarmTime);
                sw.WriteLine(this.alarmDay);
                sw.WriteLine(this.alarmText);
            }
        }

        private void FormMain_Load(object sender, EventArgs e)
        {
            if (File.Exists("alarm.txt"))
            {
                using (StreamReader sr = new StreamReader("alarm.txt"))
                {
                    string alarmTimeString = sr.ReadLine();
                    string alarmDayString = sr.ReadLine();
                    string message = sr.ReadLine();

                    this.alarmTime = DateTime.Parse(alarmTimeString);
                    this.alarmDay = (DayOfWeek)Enum.Parse(typeof(DayOfWeek), alarmDayString);
                    this.alarmText = message;

                    if (this.alarmTime < DateTime.Now || this.alarmDay < DateTime.Now.DayOfWeek || this.alarmText == "")
                    {
                        return;
                    }

                    CreateAlarm();
                }
            }
        }

        private void FormMain_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                CreateAlarm();
            }
        }
    }
}
