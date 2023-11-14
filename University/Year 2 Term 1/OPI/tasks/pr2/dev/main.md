# Дослідження командного середовища Microsoft Windows

## Мета роботи

Дослідити основні команди консолі Microsoft Windows, створити пакетний файл, який повинен виконувати функції автоматизації деяких процесів у командному середовищі операційної системи Microsoft Windows.

## Завдання до роботи

- Використовуючи методичні вказівки до виконання практичних робіт і глобальну мережу Інтернет, вивчити основні команди консолі. Детально описати характеристики та призначення восьми команд за вибором зі списку:
  - CLS
  - COPY
  - DIR
  - ECHO
  - GOTO
  - EXIT
  - IF
  - MD
- Власноруч створити пакетний командний файл `*.bat`, який має цікаве та корисне призначення. Відобразити результати виконання цього файлу

## Результати виконання роботи

### Опис команд

- CLS: This command is used to clear the screen of the console. It doesn't take any arguments and simply clears all the text from the console window.
- COPY: This command is used to copy files from one location to another. It takes two arguments: the source file and the destination location.
- DIR: This command is used to display a list of files and subdirectories in a directory. It can take various switches to modify its output, such as /w for wide listing format or /p to pause after each screenful of output.
- ECHO: This command is used to display a message on the screen or to turn on or off the echoing of commands in a batch file. For example, ECHO Hello, World! would display "Hello, World!" on the console.
- GOTO: This command is used in batch files to direct the command processor to a labelled line in the script. For example, GOTO END would jump to a line labelled :END.
- EXIT: This command is used to end a command processor session, or to close a script or batch file.
- IF: This command is used to perform conditional processing in batch files. For example, IF EXIST filename (DEL filename) would delete the specified file if it exists.
- MD: This command is used to create a directory. For example, MD new_directory would create a new directory named "new_directory".

### Розробка пакетного файлу

## Висновки

Таким чином, ми дослідили основні команди консолі Microsoft Windows, а також створили пакетний файл, який виконав функції автоматизації деяких процесів у командному середовищі операційної системи Microsoft Windows.

### Контрольні питання

#### Яке призначення мають консольні команди?

Консольні команди, також відомі як інструкції командного рядка, в основному використовуються для взаємодії з операційною системою комп'ютера. Вони дають змогу користувачам безпосередньо вказувати комп'ютеру виконувати певні завдання, наприклад, керувати файлами та каталогами, запускати програми або отримувати доступ до мережевих ресурсів. Консольні команди часто потужніші та гнучкіші, ніж графічні інтерфейси користувача, що дозволяє виконувати складні операції та писати сценарії.

#### У яких випадках застосовуються команди консолі?

Консольні команди використовуються в різних ситуаціях. Системні адміністратори часто використовують їх для таких завдань, як обслуговування системи, автоматизація повторюваних завдань та усунення несправностей. Розробники використовують консольні команди для виконання завдань програмування, таких як компіляція та запуск програм, керування системами контролю версій та взаємодія з базами даних. Консольні команди також використовуються, коли графічний інтерфейс користувача недоступний, наприклад, на віддаленому сервері або при мінімальній інсталяції операційної системи.

#### Яким чином створюється пакетний командний файл?

Пакетний командний файл, також відомий як пакетний скрипт, - це текстовий файл, який містить серію консольних команд. Щоб створити пакетний командний файл, спочатку відкрийте текстовий редактор, а потім напишіть команди, які ви хочете виконати, кожну з нового рядка. Після того, як ви напишете всі команди, ви зберігаєте файл з розширенням .bat (у Windows). Коли цей файл запускається, команди виконуються в тому порядку, в якому вони з'являються у файлі. Це особливо корисно для автоматизації завдань, що повторюються.
