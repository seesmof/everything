## Лаб1. Знаймоство з Visual Studio CS

### Завдання

#### 1

Текст - створити новий проєкт з двома елементами TextBox та одним Button. Зробити так, щоб при натисканні кнопки Button дані, що вводяться в одному з елементів TextBox, повторювалися в іншому

Рішення

```cs
// Task1.cs

namespace windowsFormsGettingHangOf
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            textBox1.Focus();
            textBox2.Text = "Waiting for input...";
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void duplicateText(string text)
        {
            if (text.Length > 0 && text != null && text != "Input stuff here...")
            {
                textBox2.Text = text;
            }
            else
            {
                textBox1.Text = "Input stuff here...";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                string inputText = textBox1.Text;
                duplicateText(inputText);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Something went wrong...", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                duplicateText(textBox1.Text);
            }
        }

        private void textBox2_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                textBox2.Text = "This one is for output...";
            }
        }
    }
}
```

```cs
// Task1.Designer.cs

namespace windowsFormsGettingHangOf
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            textBox1 = new TextBox();
            textBox2 = new TextBox();
            button1 = new Button();
            label1 = new Label();
            label2 = new Label();
            SuspendLayout();
            //
            // textBox1
            //
            textBox1.Location = new Point(12, 37);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(510, 31);
            textBox1.TabIndex = 0;
            textBox1.TextChanged += textBox1_TextChanged;
            textBox1.KeyDown += textBox1_KeyDown;
            //
            // textBox2
            //
            textBox2.Location = new Point(528, 37);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(510, 31);
            textBox2.TabIndex = 1;
            textBox2.TextChanged += textBox2_TextChanged;
            textBox2.KeyDown += textBox2_KeyDown;
            //
            // button1
            //
            button1.Location = new Point(1044, 35);
            button1.Name = "button1";
            button1.Size = new Size(112, 34);
            button1.TabIndex = 1;
            button1.Text = "Duplicate";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            //
            // label1
            //
            label1.AutoSize = true;
            label1.Location = new Point(12, 9);
            label1.Name = "label1";
            label1.Size = new Size(88, 25);
            label1.TabIndex = 2;
            label1.Text = "Input Box";
            //
            // label2
            //
            label2.AutoSize = true;
            label2.Location = new Point(528, 9);
            label2.Name = "label2";
            label2.Size = new Size(103, 25);
            label2.TabIndex = 2;
            label2.Text = "Output Box";
            //
            // MainForm
            //
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            ClientSize = new Size(1168, 87);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(button1);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            MinimumSize = new Size(1190, 143);
            Name = "MainForm";
            Text = "Text Duplication";
            Load += MainForm_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox textBox1;
        private TextBox textBox2;
        private Button button1;
        private Label label1;
        private Label label2;
    }
}
```

#### 2

Текст - створити новий проєкт з двома елементами TextBox. Зробити так, щоб дані, що вводяться в одному з них, повторювалися в іншому у реальному часі

Рішення

```cs
// Task2.cs

namespace windowsFormsGettingHangOf
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void closeOnEscape(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)
            {
                Close();
            }
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            textBox1.Focus();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            textBox2.Text = textBox1.Text;
        }

        private void MainForm_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
        }

        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
        }

        private void textBox2_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
            textBox2.Text = "This one is for output...";
        }
    }
}
```

```cs
// Task2.Designer.cs

namespace windowsFormsGettingHangOf
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            textBox1 = new TextBox();
            textBox2 = new TextBox();
            label1 = new Label();
            label2 = new Label();
            SuspendLayout();
            //
            // textBox1
            //
            textBox1.Location = new Point(12, 37);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(510, 31);
            textBox1.TabIndex = 0;
            textBox1.TextChanged += textBox1_TextChanged;
            textBox1.KeyDown += textBox1_KeyDown;
            //
            // textBox2
            //
            textBox2.Location = new Point(528, 37);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(510, 31);
            textBox2.TabIndex = 1;
            textBox2.KeyDown += textBox2_KeyDown;
            //
            // label1
            //
            label1.AutoSize = true;
            label1.Location = new Point(12, 9);
            label1.Name = "label1";
            label1.Size = new Size(88, 25);
            label1.TabIndex = 2;
            label1.Text = "Input Box";
            //
            // label2
            //
            label2.AutoSize = true;
            label2.Location = new Point(528, 9);
            label2.Name = "label2";
            label2.Size = new Size(103, 25);
            label2.TabIndex = 2;
            label2.Text = "Output Box";
            //
            // MainForm
            //
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            ClientSize = new Size(1055, 87);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            MinimumSize = new Size(1077, 143);
            Name = "MainForm";
            Text = "Real-Time Text Visualizer";
            Load += MainForm_Load;
            KeyDown += MainForm_KeyDown;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox textBox1;
        private TextBox textBox2;
        private Label label1;
        private Label label2;
    }
}
```

#### 3

Текст - створити новий проєкт з потрібними елементами. Зробити так, щоб обраний елемент випадаючого списку автоматично вписувався до текстового блоку, але тільки при натисканні на кнопку. При цьому, передбачити можливість дозволяти вивід чи ні

Рішення

```cs
// Task3.cs

namespace windowsFormsGettingHangOf
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void closeOnEscape(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)
            {
                Close();
            }
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            label2.Visible = false;
            checkBox1.Checked = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                if (comboBox1.SelectedItem != null)
                {
                    label2.Visible = true;
                    textBox1.Text = comboBox1.SelectedItem.ToString();
                    string sportNameToLowercase = textBox1.Text!.ToLower();
                    label2.Text = "Your favorite sport is " + sportNameToLowercase + "!";
                }
                else
                {
                    MessageBox.Show("Please select your favorite sport", "ERROR: Sport not selected", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else
            {
                MessageBox.Show("Please tick the checkbox to see your favorite sport", "ERROR: Checkbox not ticked", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
        }

        private void MainForm_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
        }

        private void comboBox1_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
        }

        private void button1_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
        }
    }
}
```

```cs
// Task3.Designer.cs

namespace windowsFormsGettingHangOf
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            comboBox1 = new ComboBox();
            label1 = new Label();
            button1 = new Button();
            checkBox1 = new CheckBox();
            textBox1 = new TextBox();
            label2 = new Label();
            SuspendLayout();
            //
            // comboBox1
            //
            comboBox1.FormattingEnabled = true;
            comboBox1.Items.AddRange(new object[] { "Football", "Basketball", "Baseball", "Soccer", "Cricket", "American Football" });
            comboBox1.Location = new Point(12, 37);
            comboBox1.Name = "comboBox1";
            comboBox1.Size = new Size(325, 33);
            comboBox1.TabIndex = 0;
            comboBox1.KeyDown += comboBox1_KeyDown;
            //
            // label1
            //
            label1.AutoSize = true;
            label1.Location = new Point(12, 9);
            label1.Name = "label1";
            label1.Size = new Size(225, 25);
            label1.TabIndex = 1;
            label1.Text = "Choose your favorite sport";
            //
            // button1
            //
            button1.Location = new Point(653, 35);
            button1.Name = "button1";
            button1.Size = new Size(112, 34);
            button1.TabIndex = 2;
            button1.Text = "Reveal";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            button1.KeyDown += button1_KeyDown;
            //
            // checkBox1
            //
            checkBox1.AutoSize = true;
            checkBox1.Location = new Point(12, 76);
            checkBox1.Name = "checkBox1";
            checkBox1.Size = new Size(183, 29);
            checkBox1.TabIndex = 3;
            checkBox1.Text = "Allow text output?";
            checkBox1.UseVisualStyleBackColor = true;
            //
            // textBox1
            //
            textBox1.Location = new Point(343, 39);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(304, 31);
            textBox1.TabIndex = 4;
            textBox1.KeyDown += textBox1_KeyDown;
            //
            // label2
            //
            label2.AutoSize = true;
            label2.Location = new Point(343, 9);
            label2.Name = "label2";
            label2.Size = new Size(103, 25);
            label2.TabIndex = 1;
            label2.Text = "Output Box";
            //
            // MainForm
            //
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            ClientSize = new Size(780, 124);
            Controls.Add(textBox1);
            Controls.Add(checkBox1);
            Controls.Add(button1);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(comboBox1);
            MinimumSize = new Size(802, 180);
            Name = "MainForm";
            Text = "Favorite Sport Form";
            Load += MainForm_Load;
            KeyDown += MainForm_KeyDown;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private ComboBox comboBox1;
        private Label label1;
        private Button button1;
        private CheckBox checkBox1;
        private TextBox textBox1;
        private Label label2;
    }
}
```

## Пра1. Операційні системи

### Завдання

- навести детальний опис термінів:
  - визначення ОС,
  - функції ОС,
  - типи ОС,
  - класифікація ОС,
  - складові ОС,
  - вимоги до обладнання ОС,
  - ядро ОС,
  - безпека ОС,
  - графічний інтерфейс ОС,
  - драйвери ОС,
  - історія ОС,
  - хронологія випускі ОС.
- відобразити список класів операційних систем визначеного типу, вказаним за варіантом:
  - для 16-розрядних персональних комп'ютерів
- для кожного з варіанту обрати один клас операційних систем зі списку, який був створений Вами за п. Б, або від конкретного виробника, описати функції обраної ОС, її загальні риси, відмінності її від інших ОС та хронологічно деталізувати їх родини в залежності від їх ядра. У якості прикладу, родини Windows, наведено на рисунку 1.5
  - описати функції обраної ОС,
  - описати загальні риси ОС,
  - описати відмінності її від інших ОС
  - хронологічно деталізувати їх родини в залежності від їх ядра

Контрольні питання

- визначення операційної системи. Завантаження ОС.
- загальні риси ОС.
- головні та додаткові функції ОС.
- типи операційних систем.
- складові ОС.

Третє завдання

Для опису функцій операційної системи DOS, загальних особливостей DOS та її відмінностей від інших операційних систем ми можемо зібрати інформацію з наданих результатів пошуку.

1. Функції DOS:

   - DOS (Disk Operating System) - це операційна система з інтерфейсом командного рядка, яка запускається з дисководу і надає користувачам спосіб взаємодії з комп'ютером.
   - DOS дозволяє користувачам керувати різними апаратними компонентами та пам'яттю комп'ютера за допомогою команд.
   - Вона надає функції керування файлами, такі як створення, редагування, видалення та впорядкування файлів і каталогів.
   - DOS може запускати програми та виконувати програми, написані сумісними з системою мовами програмування.
   - Вона забезпечує базовий рівень багатозадачності, дозволяючи користувачам запускати кілька програм одночасно, але з обмеженими ресурсами.

2. Загальні особливості DOS:

   - DOS - це символьна інтерфейсна система, в якій команди вводяться користувачами у вікні командного рядка.
   - Це неграфічна операційна система, керована командами, на відміну від сучасних систем з графічним інтерфейсом користувача (GUI).
   - DOS відома своєю компактністю, ефективністю та низькими вимогами до обслуговування.
   - Вона розроблена так, щоб бути легкою і придатною для роботи на старому обладнанні з обмеженими ресурсами.
   - DOS має ієрархічну файлову систему, яка організовує файли і каталоги у вигляді дерева.
   - Вона надає набір вбудованих команд для виконання різних завдань, таких як керування файлами, операції з дисками та конфігурація системи.

3. Відмінності між DOS та іншими операційними системами:

   - DOS відрізняється від сучасних операційних систем, таких як Windows, Linux і macOS, які мають графічний інтерфейс користувача і розширені можливості.
   - DOS не має вбудованої підтримки багатозадачності, захисту пам'яті або розширених мережевих можливостей.
   - Вона значною мірою покладається на знання користувачем команд і вимагає ручного введення для більшості завдань.
   - На відміну від сучасних операційних систем, DOS не має вбудованого графічного середовища робочого столу або віконної системи.
   - DOS має простіший і обмеженіший набір функцій порівняно з сучасними операційними системами, що робить її придатною для специфічних випадків використання або застарілих систем.

4. Хронологічні відомості про DOS та сімейство її ядер:
   Для класу операційних систем DOS (Disk Operating System), яке включає операційні системи, починаючи зі старших версій і переходячи до більш сучасних, можна деталізувати їх родини в залежності від їх ядра наступним чином:
   1. DOS 1.0-2.x:
      - Ядро: Оригінальне ядро DOS (без версії ядра)
      - Основні представники: MS-DOS 1.0, MS-DOS 2.0
   2. DOS 3.x:
      - Ядро: DOS 3.x Kernel
      - Основні представники: MS-DOS 3.0, MS-DOS 3.3
   3. DOS 4.x:
      - Ядро: DOS 4.x Kernel
      - Основні представники: MS-DOS 4.0
   4. DOS 5.x:
      - Ядро: DOS 5.x Kernel
      - Основні представники: MS-DOS 5.0, MS-DOS 5.0a
   5. DOS 6.x:
      - Ядро: DOS 6.x Kernel
      - Основні представники: MS-DOS 6.0, MS-DOS 6.22
