# Shuffle_AOVs

安装方法：
1.将L_AOVs.py文件放入
2.在.nuke文件中的menu.py加入以下字段：
import L_AOVs
menuBar = nuke.menu('Nuke')
menuBar.addCommand('L_AOVs/L_AOVs', 'L_AOVs.L_AOVs(nuke.selectedNode())' , 'alt+a' )
