

'''

Nisarg Patel
31469102
CS341

'''
import math

class ParseError(Exception): pass



#==============================================================
# FRONT END PARSER
#==============================================================

i = 0 # keeps track of what character we are currently reading.
err = None
variable={}


 # 0     <statement> → table | show <exp>{,<exp>} | <id> = <exp>

def statement():
  global i, err
  
 
  if w[i] == 'table':
    
    
    print("Symbol Table: \n")
    print("================\n")
    
    for var in variable:
      print( str(var) + "  =  " + str(variable[var]) )
    
    value = 'Done'
    
  
  elif w[i] == 'show':
    i += 1
    while True:
      try:
        if w[i] != '$':
          value = exp()
          i+=1
          print('value: ' + str(value))
      except IndexError:
        break

     
    value = 'done'
    
  else:
    
    temp = w[i]
    i+=1
    if w[i] == '=':
      i += 1
      value = exp()
      variable[temp] = value
    else:
      print("missing '=' ")
    
    #print(variable)
    value = 'Done'
  

  
  


  return value

# 1     <exp> → <term>{+<term> | -<term>}
def exp():
    global i, err

    value = term()
  
    while True:
        if w[i] == '+':
            i += 1
            value = binary_op('+', value, term())
        elif w[i] == '-':
            i += 1
            value = binary_op('-', value, term())
        else:
            break

    return value
  
#2     <term> → <factor>{*<factor> | /<factor>}
  
def term():
    global i, err

    value = factor()
    while True:
        if w[i] == '*':
            i += 1
            value = binary_op('*', value, factor())
        elif w[i] == '/':
            i += 1
            value = binary_op('/', value, factor())
        else:
            break

    return value

#<factor> → (<exp>) | pi | <func>(<exp>) | <atomic>

def factor():
    global i, err
    
    usernput = w[i]
    flag = isinstance(usernput,str)
    
    value = None
    if w[i] == '(':
      i += 1          # read the next character
      value = exp()
      if w[i] == ')':
        i += 1
        return value
      else:
        print('missing )')
        raise ParseError
    
        
    elif w[i] == 'pi':
      i += 1
      return math.pi
    
    elif w[i] == 'sin':
      i +=1  
      if w[i] == '(':

        i += 1
        value = exp()
        math_func = func(value, 'sin')
        if w[i] == ')':
          i+= 1
          #print(math_func)
          return math_func
        else:
          print('missing )')
          raise ParseError

    elif w[i] == 'cos':
      i +=1
      if w[i] == '(':
        i += 1
        value = exp()
        math_func = func(value, 'cos')
        if w[i] == ')':
          i+= 1
          
          #print (math_func)
          return math_func
        else:
          print('missing )')
          raise ParseError
            
    elif w[i] == 'tan':
      i +=1
      if w[i] == '(':
        i += 1
        value = exp()
        math_func = func(value, 'tan')
        if w[i] == ')':
          i+= 1
          #print (math_func)
          return math_func
        else:
          print('missing )')
          raise ParseError

    elif w[i] == 'sqrt':
      i +=1 
      if w[i] == '(':
          i += 1
          value = exp()
          math_func = func(value, 'sqrt')
          if w[i] == ')':
            i+= 1            
            #print(math_func)
            return math_func
          else:
              print('missing )')
              raise ParseError
   
    
    
      

    else:
      try:
        value = atomic(w[i])
        i += 1          # read the next character
      except ValueError as err:
        #print('number expected')
        value = variable[w[i]]
        i += 1
    
    
    #print('factor returning', value)
    
    if value == None: raise ParseError
    return value


# <func> → sin | cos | tan | sqrt
def func(value,mathfun):
    global i, err
  
    #print(mathfun)
   

    
    if mathfun == 'sin':
      value = math.sin(value)
      return value
    
    elif mathfun == 'cos':
      value = math.cos(value)
      return value
    
    elif mathfun == 'tan':
      value = math.tan(value)
      return value
    
    elif mathfun == 'sqrt':
      value = math.sqrt(value)
      return value
    
    else:
      print('missing math function')
      value = None
      return value
    
#==============================================================
# BACK END PARSER (ACTION RULES)
#==============================================================

def binary_op(op, lhs, rhs):
    if op == '+': return lhs + rhs
    elif op == '-': return lhs - rhs
    elif op == '*': return lhs * rhs
    elif op == '/': return lhs / rhs
    else: return None

def atomic(x):
    return float(x)


w = input('\nEnter expression: ')
while w != '':
    #------------------------------
    # Split string into token list.
    #
    for c in '()+-*/':
        w = w.replace(c, ' '+c+' ')
    w = w.split()
    w.append('$') # EOF marker

    print('\nToken Stream:     ', end = '')
    for t in w: print(t, end = '  ')
    print('\n')
    i = 0
    try:
        print( statement())
         # call the parser
    except:
        print('parse error')
    print()
    
    print()
    w = input('\n\nEnter expression: ')
#print(w[:i], '|', w[i:])


