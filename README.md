# L_AOVs
自己瞎写的Shuffle插件
安装方法：
1.将L_AOVs.py文件放入.nuke文件夹中
2.在.nuke文件中的menu.py加入以下字段：
import L_AOVs
menuBar = nuke.menu('Nuke')
menuBar.addCommand('L_AOVs/L_AOVs', 'L_AOVs.L_AOVs(nuke.selectedNode())' , 'alt+a' )
