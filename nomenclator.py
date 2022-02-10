import maya.cmds as cmds
from functools import partial
from datetime import datetime

counter = 0
def countRename():
	counter += 1
	return counter

def listSelectionByType(**kwargs):
	return cmds.ls(sl=True, **kwargs)

def listSelection():
	return cmds.ls(sl=True)

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

def setSuffix(listOfNames):
	suf = cmds.textFieldGrp('suffix', q = True, text = True)
	for cur_name in listOfNames:
		if cur_name.endswith(suf):
			result = cmds.confirmDialog(title='Warning !', message='Suffix '+ str(suf) + ' already exists for '+ cur_name +', continue?', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
			if result == 'Yes':
				cmds.rename(cur_name,cur_name + suf)
				countRename()
			elif result == 'No':
				continue
		else:
			cmds.rename(cur_name, cur_name + suf)
			countRename()

def setName(prefix, suffix):
	name = cmds.textFieldGrp('name', q = True, text = True)
	for cur_name in listOfNames:
		if cur_name.startswith(prefix):
			cmds.rename(cur_name, name)
			countRename()
		elif cur_name.endswith(suffix):
			cmds.rename(cur_name, name)		
			countRename()
					
def setDateFormat(listOfNames):
	dateF = cmds.textFieldGrp('', q = True, text = True)
	for cur_name in listOfNames:
		if cur_name.endswith(suf):
			result = cmds.confirmDialog(title='Warning !', message='Suffix '+ str(suf) + ' already exists for '+ cur_name +', continue?', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
			if result == 'Yes':
				cmds.rename(cur_name,cur_name + suf)
			elif result == 'No':
				continue
		else:
			cmds.rename(cur_name, cur_name + suf)
			
def listSelectionByType(nameType):
	return cmds.ls(type = nameType, sl = True)
	
#def renameByGrp():
	
	
#def increment():
	
def make_optmenu(optMenName, optMenLbl, menuItems):
    cmds.optionMenu(optMenName, label=optMenLbl)
    for item in menuItems:
        cmds.menuItem(item)	

cmds.window(title= 'Nomenclator')

cmds.columnLayout(adjustableColumn = True)
cmds.text(str(counter) + ' name(s) affected')

cmds.separator(height = 5)
make_optmenu('optType', 'Rename by Type:', ['all', 'mesh', 'joint', 'light', 'layer'])

cmds.separator(height = 5)
cmds.gridLayout(numberOfColumns=3, cellWidthHeight=(100, 25))

cmds.text(label='PREFIX :', bgc=[0,0.5,0])
cmds.textFieldGrp('prefix', editable=True)
cmds.button(label="APPLY", bgc=[0,0,0], command = lambda x : setPrefix(listSelection()))


cmds.text(label='NAME :')
name = cmds.textFieldGrp('name', editable=True)
cmds.button(label="APPLY", bgc=[0,0,0])


cmds.text(label='SUFFIX :', bgc=[0.5,0,0])
cmds.textFieldGrp('suffix', editable=True)
cmds.button(label="APPLY", bgc=[0,0,0], command = lambda x : setSuffix(listSelection()))


cmds.text(label='DATE FORMAT :', bgc=[1,1,1])
make_optmenu('optType', '', ['long date', 'short date', 'long date & time', 'short date & time'])
cmds.button(label='APPLY', bgc=[0,0,0])

cmds.separator( height=10, style='double' )
cmds.button(label='VALIDATE',bgc=[1,0,0])
cmds.separator( height=10, style='double' )

cmds.columnLayout(adjustableColumn = True)

cmds.showWindow()


