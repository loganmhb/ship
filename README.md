# ship

Toy shell written in Python.

All it does is run the command you give it, splitting on spaces.

Example:

```
[master*] lbuckley @ ~/Development/ship
 $ ./ship.py
  %  cat ship.py
  #!/usr/bin/env python
  
  import os
  
  
  def prompt():
      print " % ",
      
      
  def main():
      while True:
          prompt()
          cmd = raw_input().split(' ')
          if cmd[0] == 'exit':
              break
          else                                                    
              os.spawnvp(os.P_WAIT, cmd[0], cmd)


  if __name__ == "__main__":
      main()
 % 
```

