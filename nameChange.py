import maya.cmds as cmds

#Partition is used to create, query or add/remove sets to a partition (Partition is a list for lists?)
#Rpartition method takes the last occurence of a specified string and splits into tuples conatining three elements
#   @1 elem contains  the part before the string,@2 contains the specified string,@3 the part after
#Enumerate allows you too keep count of iterations and counts it and returns it in a form of enumerationg object

def NamingFunction(string):
    selectionPoly = cmds.ls(sl=True)  # important for final script to get selections and to renane #
    string.partition("##")
    for count, object in enumerate(selectionPoly):
        cmds.rename(object,string.partition('#')[0]+ str(count + 1).zfill(string.count('#'))+ string.rpartition('#')[2])





NamingFunction("Leg_##_jnt")