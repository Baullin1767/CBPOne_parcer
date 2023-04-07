# CBPOne_parcer

Скрипт находит окна для пересечения мексиканско-американской границы.

Как он это делает:
  1. Листает все существующие ворота
  2. Фиксирует код страницы
  3. Если понимает, что код страницы отличается от кода страницы без свободных дат делает скриншот
  4. Сохраняет все скриншоты в отдельные папки для каждых ворот.
  
Что использует:
  1. Framework AndroidViewClient
  2. adb
Нужно для корректной работы:
  1. Эмулятор BlueStacks
  2. adb (желательно в папке вместе со скриптом
  3. Аккаунт в CBPOnе.(Нужно ввести все данные добраться до выбора даты посещения и только потом включить скрипт)

Скрипт выполняется около 10 минут после чего останавливается. Обычно этого достаточно чтобы поймать хотя бы одно свободное время.
