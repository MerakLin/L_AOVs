# Shuffle_AOVs
#在.nuke文件中的menu.py加入以下字段：
import L_AOVs
menuBar = nuke.menu('Nuke')
menuBar.addCommand('L_AOVs/L_AOVs', 'L_AOVs.L_AOVs(nuke.selectedNode())' , 'alt+a' )
