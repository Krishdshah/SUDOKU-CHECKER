dict1={}

def checkrow(d):
  l2=[1,2,3,4,5,6,7,8,9]
  for i in range(1,10):
    if sorted(d['l'+str(i)])==l2:
      k=True
    else:
      k=False
      break
  return k

def checkcol(d):
  l2=[1,2,3,4,5,6,7,8,9]
  z=True
  for j in range(9):
    comp=[]
    for i in range(1,10):
      comp.append(d['l'+str(i)][j])
    if sorted(comp)==l2:
      z=True
    else:
      z=False
      break
  return z

def checkbox(d):
  y=True
  l2=[1,2,3,4,5,6,7,8,9]
  for i in [0,3,6]:
    if y==True:
      for a in range(0,3):
        if y==True:
          for j in range(1,10,3):
            lbox=[]
            lbox=dict1['l'+str(j)][i:i+3]+dict1['l'+str(j+1)][i:i+3]+dict1['l'+str(j+2)][i:i+3]
            if sorted(lbox)==l2:
              y=True
            else:
              y=False
              break
        else:
          break
  else:
    return y
      

      
    


print('Enter Row wise and click enter after supplying every row:')
for i in range(1,10):
  l='l'+str(i)
  list1=list(eval(input('Enter:')))
  dict1[l]=list1

row=checkrow(dict1)
col=checkcol(dict1)
box=checkbox(dict1)
if row==col==box==True:
  print('Correct sudoku entered')
else:
  print('Sudoku not correct')


  
  
