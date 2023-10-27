виконати наступні загальні завдання:

- возведення числа у регульовану ступінь за допомогою `NumericUpDown`. при цьому за допомогою `ProgressBar` продемонструвати ступінь виконання операції (возведення у ступінь доцільно виконувати за допомогою операції множення з використанням операторів циклу). результат вивести на екран. зробити оформлення інтерфейсу програми (за необхідності використовувати додаткові візуальні елементи з відповідними властивостями)
- створити програму для керування двома списками `ListView`. надавати можливість видаляти елементи списку, додавати та переміщувати з першого до другого та навпаки. зробити оформлення інтерфейсу

виконати наступне індивідуальне завдання

- реалізувати програму для створення таблиці множення з керуванням максимального множника та з виводом у елемент `ListView`. візуалізувати процес роботи програми елементом `ProgressBar`. зробити оформлення інтерфейс програми.

---

- Raise a number to a power using NumericUpDown. Use ProgressBar to show the progress of the operation. The operation should be done using multiplication in a loop. Display the result on the screen. Design the program interface, using additional visual elements if necessary.
- Create a program to manage two ListView lists. The program should allow you to delete list items, add and move items from one list to another and vice versa. Design the program interface.
- Implement a program to create a multiplication table, controlling the maximum multiplier and displaying it in a ListView element. Visualize the program's operation with a ProgressBar. Design the program interface.

---

Sure, Here are the step-by-step guides for the 3 tasks you mentioned:

## Task 1: Raise a number to a power

1. First, create a new Windows Forms Application in Visual Studio.
1. Add a NumericUpDown control, two Button controls, a ProgressBar control, and a Label control to your form. You can place them according to your needs.
1. Double click on the button you want to use to start the operation. It should take you to the button click event handler.
1. In the button click event handler, add the following code:

```
double baseNumber = (double)numericUpDown1.Value;
double power = (double)numericUpDown2.Value;
double result = 1;

progressBar1.Minimum = 0;
progressBar1.Maximum = (int)power;

for (int i = 0; i < power; i++)
{
  result *= baseNumber;
  progressBar1.Value = i + 1;
}

label1.Text = $"Result: {result}";
```

## Task 2: Manage two ListView lists

1. Create a new Windows Forms Application in Visual Studio.
1. Add two ListView controls and four Button controls to your form. These buttons will be used for adding, deleting, and moving items.
1. For adding items, double click on the add button and use the Items.Add() method of ListView.

```
listView1.Items.Add("New Item");
```

1. For deleting items, use the Items.RemoveAt() or Items.Remove() method.

```
if (listView1.SelectedItems.Count > 0)
{
  listView1.Items.Remove(listView1.SelectedItems[0]);
}
```

1. For moving items, get the selected item from one list, remove it, and then add it to the other list.

```
if (listView1.SelectedItems.Count > 0)
{
  var itemToMove = listView1.SelectedItems[0];
  listView1.Items.Remove(itemToMove);
  listView2.Items.Add(itemToMove);
}
```

## Task 3: Create a multiplication table

1. Create a new Windows Forms Application in Visual Studio.
1. Add a NumericUpDown control, a Button control, a ProgressBar control, and a ListView control to your form.
1. Double click on the button to create the click event handler.
1. In the button click event handler, add the following code:

```
int maxMultiplier = (int)numericUpDown1.Value;
listView1.Items.Clear();

progressBar1.Minimum = 0;
progressBar1.Maximum = maxMultiplier;

for (int i = 1; i <= maxMultiplier; i++)
{
  for (int j = 1; j <= maxMultiplier; j++)
  {
    listView1.Items.Add($"{i} _ {j} = {i _ j}");
  }
  progressBar1.Value = i;
}
```

Remember to adjust the control names (numericUpDown1, listView1, etc.) to match the names of the controls in your form.
