using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace dev
{
    public partial class FormMain : Form
    {
        private string message;

        public FormMain()
        {
            InitializeComponent();
        }

        private void buttonSetAlarm_Click(object sender, EventArgs e)
        {
            DateTime alarmTime = dateTimePickerAlarm.Value;
            string dayOfWeek = comboBoxDayOfWeek.SelectedItem.ToString();
            this.message = textBoxMessage.Text;

            timerAlarm.Interval = (int)(alarmTime - DateTime.Now).TotalMilliseconds;
            timerAlarm.Start();

            using (StreamWriter writer = new StreamWriter("alarm.txt", true))
            {
                writer.WriteLine($"Alarm time: {alarmTime} - Day of week: {dayOfWeek} - Message: {message}");
            }

            MessageBox.Show($"Alarm set for {dayOfWeek} at {alarmTime}", "Alamr Set", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void timerAlarm_Tick(object sender, EventArgs e)
        {
            MessageBox.Show($"Alarm!\n{this.message}");
            timerAlarm.Stop();
        }
    }
}
