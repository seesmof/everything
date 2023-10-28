Виконати наступні загальні завдання:

- Возведення числа у регульовану ступінь за допомогою `NumericUpDown`. При цьому за допомогою `ProgressBar` продемонструвати ступінь виконання операції (возведення у ступінь доцільно виконувати за допомогою операції множення з використанням операторів циклу). Результат вивести на екран. Зробити оформлення інтерфейсу програми (за необхідності використовувати додаткові візуальні елементи з відповідними властивостями)
- Створити програму для керування двома списками `ListView`. Надавати можливість видаляти елементи списку, додавати та переміщувати з першого до другого та навпаки. Зробити оформлення інтерфейсу

Виконати наступне індивідуальне завдання

- Реалізувати програму для створення таблиці множення з керуванням максимального множника та з виводом у елемент `ListView`. Візуалізувати процес роботи програми елементом `ProgressBar`. Зробити оформлення інтерфейс програми.

---

- Raise a number to a power using NumericUpDown. Use ProgressBar to show the progress of the operation. The operation should be done using multiplication in a loop. Display the result on the screen. Design the program interface, using additional visual elements if necessary.
- Create a program to manage two ListView lists. The program should allow you to delete list items, add and move items from one list to another and vice versa. Design the program interface.
- Implement a program to create a multiplication table, controlling the maximum multiplier and displaying it in a ListView element. Visualize the program's operation with a ProgressBar. Design the program interface.

---

### Контрольні питання

#### Як здійснюється додавання елементу у ListView?

Додавання елементу в ListView в C# WinForms можна здійснити декількома способами. Один з них - це використання методу Add колекції Items контролу ListView. Наприклад, можна створити новий елемент ListViewItem і додати його в ListView таким чином: listView1.Items.Add(item);. Також можна додати підпункти до елементу ListView, використовуючи колекцію SubItems елементу ListViewItem. Наприклад, item1.SubItems.Add("SubItem1a");.

#### Як здійснюється додавання вузлів у TreeView?

Вузли в TreeView додаються за допомогою колекції Nodes контролу TreeView або окремого вузла TreeNode. Наприклад, можна додати вузол в TreeView таким чином: treeView1.Nodes.Add(new TreeNode());. Щоб додати вузол як дочірній до існуючого вузла, використовується колекція Nodes батьківського вузла. Наприклад, parentNode.Nodes.Add(new TreeNode());.

#### Як здійснюється пошук елементів у ListView?

Пошук елементів у ListView можна здійснити за допомогою методу FindItemWithText, який приймає рядок пошуку як аргумент і повертає перший елемент, що відповідає цьому рядку. Наприклад, ListViewItem item = listView1.FindItemWithText("text"); знайде і поверне перший елемент ListView, текст якого відповідає "text".
