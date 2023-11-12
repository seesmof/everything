using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace dev
{
    public partial class FormMain : Form
    {
        public FormMain()
        {
            InitializeComponent();
        }

        private void btnCreate_Click(object sender, EventArgs e)
        {
            DateTime alarmTime = dateTimePickerTime.Value;
            DayOfWeek alarmDay = (DayOfWeek)Enum.Parse(typeof(DayOfWeek), comboBoxDayOfWeek.SelectedItem.ToString());
            string message = textBoxMessage.Text;
            AlarmClock alarmClock = new AlarmClock(alarmTime, alarmDay);
            alarmClock.Alarm += () =>
            {
                MessageBox.Show(message, "Alarm");
                lblStatus.Text = "Status: Not Set";
            };
            lblStatus.Text = $"Status: Set to {alarmTime} on {alarmDay}";
        }
    }
}
