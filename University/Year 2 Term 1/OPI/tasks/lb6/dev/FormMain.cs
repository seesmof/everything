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
            AlarmClock alarmClock = new AlarmClock(alarmTime, alarmDay);
            alarmClock.Alarm += () =>
            {
                MessageBox.Show(alarmText, "Alarm");
                lblStatus.Text = "Status: Not Set";
            }
            lblStatus.Text = $"Status: Set to {alarmTime} on {alarmDay}";
        }

        private void btnCreate_Click(object sender, EventArgs e)
        {
            alarmTime = dateTimePickerTime.Value;
            alarmDay = (DayOfWeek)Enum.Parse(typeof(DayOfWeek), comboBoxDayOfWeek.SelectedItem.ToString());
            alarmText = textBoxMessage.Text;

            CreateAlarm();
        }

        private void FormMain_FormClosing(object sender, FormClosingEventArgs e)
        {
            using (StreamWriter sw = new StreamWriter("alarm.txt"))
            {
                sw.WriteLine(alarmTime);
                sw.WriteLine(alarmDay);
                sw.WriteLine(alarmText);
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

                    alarmTime = DateTime.Parse(alarmTimeString);
                    alarmDay = (DayOfWeek)Enum.Parse(typeof(DayOfWeek), alarmDayString);

                    CreateAlarm();
                }
            }
        }
    }
}
