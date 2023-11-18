// Task A - Alarm Clock
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace dev
{
    public class AlarmClock
    {
        public Timer timer;
        public DateTime alarmTime;
        public DayOfWeek alarmDay;
        public bool hasAlarmWentOff;

        public AlarmClock(DateTime alarmTime, DayOfWeek alarmDay)
        {
            this.hasAlarmWentOff = false;
            this.alarmTime = alarmTime;
            this.alarmDay = alarmDay;
            timer = new Timer();
            timer.Interval = 1000;
            timer.Tick += Timer_Tick;
            timer.Start();
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            if (!hasAlarmWentOff && DateTime.Now.DayOfWeek == alarmDay && DateTime.Now.TimeOfDay >= alarmTime.TimeOfDay)
            {
                timer.Stop();
                OnAlarm();
                hasAlarmWentOff = true;
            }
        }

        public event Action Alarm;

        protected virtual void OnAlarm()
        {
            Alarm?.Invoke();
        }
    }
}
