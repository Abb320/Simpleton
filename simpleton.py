#Ermin Dzanic
#2024/01/28
#CSC2025 Computer Architecture/Assembly
#Prof. Kenneth W. Riddle


import pandas as pd


def displayCache(list):
  data = {
        0: [],
        10: [],
        20: [],
        30: [],
        40: [],
        50: [],
        60: [],
        70: [],
        80: [],
        90: [],
    }
  if len(list) != 0:
    y = 0
    x = 0
    for _ in range(len(list)):
      data[y].append(list[x])
      x += 1
      if x % 10 == 0:
        y += 10
      else:
        continue

    df = pd.DataFrame.from_dict(data, orient='index').fillna('0')
    print(df)
  else:
    for _ in range(10):
      data[0].append(0)
    df = pd.DataFrame.from_dict(data, orient='index').fillna('0').astype(int)
    print(df)

def read(memory, location, accumulator):
  return memory.insert(location,accumulator)

def readPrint(memory):
  print(memory)

def Print(dictionary, location):
  print(dictionary[location])


def load(memory, location):
  return location

def append(item, location, memory):
  return memory.insert(location, item)

def add(memory,accumulator):
  return int(memory) + int(accumulator)

def sub(memory, accumulator):
  return int(memory)  - int(accumulator)

def div(memory, accumulator):
  return int(memory)  / int(accumulator)

def mul(memory, accumulator):
  return int(memory)  * int(accumulator)

def branch(memory, accumulator):
  if accumulator > 0:
    return memory
  else:
    return False

def branchNeg(accumulator):
  if accumulator < 0:
    return True
  else:
    return False

def branchZero(memory, accumulator):
  if accumulator == 0:
    return memory
  else:
    return False
  
def halt():
  return False




commands ={
  10 : 'read',
  11 : "readPrint",
  12 : "Print",
  20 : 'load',
  21 : "append",
  30 : "add",
  31 : "sub",
  32 : "div",
  33 : "mul",
  40 : "branch",
  41 : "branchNeg",
  42 : "branchZero",
  43 : "halt"
}


def separator(list):
  command = []
  action = []
  for item in list:
    x = item[:2]
    y = item[2:]
    command.append(int(x))
    action.append(int(y))
  return command, action


def run(commands, command, action, memory):
  accumulator = []
  counter = 0;

  alpha = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  for item in command:
    current = command[counter]
    if current in commands:
      if current == 10:
        memory.insert(int(action[counter]), str(accumulator[0]))
        accumulator.clear()
        counter += 1
        continue
      elif current == 11:
        readPrint(memory[action[counter]])
        counter += 1
        continue
      elif current == 12:
        if action[counter] == 27:
          accumulator = [input(" ")]
          counter += 1
        else:
          print(alpha[int(action[counter])], end='')
          counter += 1
        continue
      elif current == 20:
        accumulator = [memory[action[counter]]]
        counter += 1
        continue
      elif current == 21:
        memory.insert(action[counter], int(accumulator[0]))
        counter += 1
      elif current == 30:
        accumulator = [add(memory[action[counter]], int(accumulator[0]))]
        counter += 1
        continue
      elif current == 31:
        accumulator = [sub(memory[action[counter]], int(accumulator[0]))]
        counter += 1
        continue
      elif current == 32:
        accumulator = [div(memory[action[counter]], int(accumulator[0]))]
        counter += 1
        continue
      elif current == 33:
        accumulator = [mul(memory[action[counter]], int(accumulator[0]))]
        counter += 1
        continue
      elif current == 40:
        counter += 1
        continue
      elif current == 41:
        if branchNeg(int(accumulator[0])):
            counter += 1
            accumulator.clear()
        else:
            counter = action[counter]
        continue
      elif current == 42:
        counter += 1
        continue
      elif current == 43:
        counter += 1
        break
      else:
        print('error')
    else:
      break


memory = []

counter = 0
while(True):
  counter += 1
  order = input(f"SMP{counter}> ")
  if order == "@run":
    command, action = separator(memory)
    run(commands, command, action, memory)
    continue
  elif order == '@dump':
    displayCache(memory)
    continue
  elif order == '@clear':
    memory = []
    continue
  elif order =='@exit':
    break
  else:
    if len(order) == 4:
      memory.append(order)
    else:
      print("input to long")
      continue
