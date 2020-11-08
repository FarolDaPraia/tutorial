# Tutorial
path of python learning

* 49_YAML
* 50_openpyxl
* 51_MVC
* 52_built_in

## Projects
* hangman
* blackjack
* CodeWars
  + 5kyu string increments


## notes:
* difference between is and ==  
```python
teste
```

* global variables  
when you create a variable inside a function, that variable is local,
and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
```python
>> x = 'variable'  
>> def myfunc():  
>>    global x
```

* rstrip()  
The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing
character to remove.
```python
>> strng = 'XfZ{*=Qz6223277273011185565679023644880826440000000008733985'  
>> head = strng.rstrip('0123456789')
head = '6223277273011185565679023644880826440000000008733985'
```
