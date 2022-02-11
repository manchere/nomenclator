import maya.cmds as cmds
from functools import partial
from datetime import datetime

counter = 0
suffix = ''
prefix = ''

def countRename():
	global counter
	counter += 1
	cmds.text(counting, edit=True, label = str(counter) + ' name(s) affected')
	return counter
	
def increment():
	inc = cmds.optionMenu('optIncrement', q = True, v = True)
	if inc == '1, 2, 3':
		return str(counter).zfill(1)
	elif inc == '01, 02, 03':
		return str(counter).zfill(2)
	elif inc == '001, 002, 003':
		return str(counter).zfill(3)
	else:
		return ''
		
def setObjectType():
	the_type = cmds.optionMenu('optType', q = True, v = True)	
	if the_type == 'all':
		return cmds.ls(sl = True)
	else:
		return listSelectionByType(the_type)
		
cmds.ls(sl = True, mat = True)
the_type = cmds.optionMenu('optType', q = True, v = True)
print(the_type)

	
def listSelectionByType(args):
	if args in ['joint', 'mesh', 'transform']:
		return cmds.ls(sl = True, type = args)
		print('type')
	elif args == 'camera':
		return cmds.ls(sl = True, cameras = True)
	elif args == 'texture':
		return cmds.ls(sl = True, textures = True)
	elif args == 'light':
		return cmds.ls(sl = True, lights = True)
	elif args == 'materials':
		return cmds.ls(sl = True, materials = True)
	
def setName(listOfNames):
	newName = cmds.textFieldGrp('name', q = True, text = True)
	for cur_name in listOfNames:
		if newName != '':
			cmds.rename(cur_name, newName + increment())
			countRename()
	global counter
	counter = 0
	increment()

def setPrefix(listOfNames):
	pre = cmds.textFieldGrp('prefix', q = True, text = True)
	print("text is"+pre)
	for cur_name in listOfNames:
		if cur_name.startswith(pre) and pre != '':
			result = cmds.confirmDialog(title='Warning !', message='Prefix '+ str(pre) + ' already exists for '+ cur_name +', continue?', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
			if result == 'Yes':
				cmds.rename(cur_name, pre + cur_name)
				countRename()
			elif result == 'No':
				continue
		else:
			cmds.rename(cur_name, pre + cur_name)
			countRename()
	global counter
	counter = 0				

def setSuffix(listOfNames):
	suf = cmds.textFieldGrp('suffix', q = True, text = True)
	for cur_name in listOfNames:
		if cur_name.endswith(suf) and suf != '':
			result = cmds.confirmDialog(title='Warning !', message='Suffix '+ str(suf) + ' already exists for '+ cur_name +', continue?', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
			if result == 'Yes':
				cmds.rename(cur_name,cur_name + suf)
				countRename()
			elif result == 'No':
				continue
		else:
			cmds.rename(cur_name, cur_name + suf)
			countRename()
	global counter
	counter = 0
					
def setDateFormat(listOfNames):
	now = datetime.now()
	the_type = cmds.optionMenu('optDate', q = True, v = True)
	for cur_name in listOfNames:
		if the_type == 'date':
			cmds.rename(cur_name,cur_name + now.strftime("%d_%m_%Y"))
			countRename()	
		elif the_type == 'date & time':
			cmds.rename(cur_name,cur_name + now.strftime("%d_%m_%Y_%H_%M_%S"))
			countRename()
	global counter
	counter = 0	
	
def make_optmenu(optMenName, optMenLbl, menuItems):
    cmds.optionMenu(optMenName, label=optMenLbl)
    for item in menuItems:
        cmds.menuItem(item)	

if (cmds.window('Nomenclator', exists = True)): 
    cmds.deleteUI('Nomenclator')
    
cmds.window('Nomenclator', title= 'Nomenclator')

cmds.columnLayout(adjustableColumn = True)
counting = cmds.text(str(counter) + ' name(s) affected')

cmds.separator(height = 5)
make_optmenu('optType', 'Rename by Type:', ['all', 'transform', 'mesh', 'joint', 'light', 'material', 'texture', 'camera'])

cmds.separator(height = 5)
make_optmenu('optIncrement', 'Increment Type:', ['maya default','1, 2, 3', '01, 02, 03', '001, 002, 003'])

cmds.separator(height = 5)
cmds.gridLayout(numberOfColumns=3, cellWidthHeight=(100, 25))

cmds.text(label='NAME :')
name = cmds.textFieldGrp('name', editable=True)
cmds.button(label="APPLY", bgc=[0,0,0], command = lambda x : setName(setObjectType()))

cmds.text(label='PREFIX :', bgc=[0,0.5,0])
cmds.textFieldGrp('prefix', editable=True)
cmds.button(label="APPLY", bgc=[0,0,0], command = lambda x : setPrefix(listSelection()))


cmds.text(label='SUFFIX :', bgc=[0.5,0,0])
cmds.textFieldGrp('suffix', editable=True)
cmds.button(label="APPLY", bgc=[0,0,0], command = lambda x : setSuffix(listSelection()))


cmds.text(label='DATE FORMAT :', bgc=[1,1,1])
make_optmenu('optDate', '', ['date', 'date & time'])
cmds.button(label='APPLY', bgc=[0,0,0], command = lambda x : setDateFormat(listSelection()))

cmds.separator(height=10, style='double')
cmds.button(label='VALIDATE',bgc=[1,0,0])
cmds.separator(height=10, style='double')

cmds.columnLayout(adjustableColumn = True)

cmds.showWindow()


