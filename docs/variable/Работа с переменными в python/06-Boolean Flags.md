[[variable (Переменные)]]
---
Теги: #python #variable #bool

## Логические флаги

Логические флаги помогают управлять потоком выполнения и принятием решений в ваших программах. Как следует из названия, эти переменные могут быть либо пустыми, `True`либо пустыми `False`. Вы можете использовать их в условных операторах , `while`циклах и логических выражениях.

Предположим, вам нужно поочередно выполнять два разных действия в цикле. В этом случае вы можете использовать переменную-флаг для переключения действий в каждой итерации:

```python
>>> toggle = True

>>> for _ in range(4):
...     if toggle:
...         print(f"✅ toggle is {toggle}")
...         print("Do something...")
...     else:
...         print(f"❌ toggle is {toggle}")
...         print("Do something else...")
...     toggle = not toggle
...
✅ toggle is True
Do something...
❌ toggle is False
Do something else...
✅ toggle is True
Do something...
❌ toggle is False
Do something else...
```

При каждом выполнении этого цикла условное выражение проверяет значение параметра, `toggle`чтобы определить, какое действие следует предпринять. В конце цикла значение параметра изменяется `toggle`с помощью `not` оператора. В следующей итерации будет выполнено альтернативное действие.

Флаги также используются в качестве аргументов функций. Рассмотрим следующий простой пример:

```python
>>> def greet(name, verbose=False):
...     if verbose:
...         print(f"Hello, {name}! It's great to see you!")
...     else:
...         print(f"Hello, {name}!")
...

>>> greet("Pythonista")
Hello, Pythonista!

>>> greet("Pythonista", verbose=True)
Hello, Pythonista! It's great to see you!
```

В этом примере `verbose`аргументом является логическая переменная, которая позволяет выбрать, какое приветственное сообщение отображать.