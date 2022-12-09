import  maya.cmds as cmds



def ChangeColor(color):
   selectionPoly = cmds.ls(sl=True) # important for final script to get selections and to renane #
   for sel in selectionPoly: #sel = selection just saying for the selected objects#
       shapes = cmds.listRelatives(sel, children=True, shapes=True) #selectes the children as well#
       for shape in shapes:
           cmds.setAttr('%s.overrideEnabled' % (shape), True) #OverrideEnabled changes the attr to be able to be overrided#
           cmds.setAttr('%s.overrideColor' % (shape), color) #changes the Attribute of color#

   return #always needed for functions#
ChangeColor(3)