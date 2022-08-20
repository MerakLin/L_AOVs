from ast import Return
from random import shuffle
from select import select
import nuke
###传参问题不使用的函数###
# def Shuffle_Temp_Save(shuffle_temp,dot):
#     shuffle_temp=dot
#     return shuffle_temp

# def CreateDotShuffle(node,shuffle_temp,layers,b):
#     dot=nuke.nodes.Dot()
#     if shuffle_temp!=0:
#         dot.setInput(0,shuffle_temp)
#     else:
#         dot.setInput(0,node)
#     shuffle=nuke.nodes.Shuffle2(postage_stamp=True,name=layers[b])
#     shuffle['in1'].setValue('Shuffle_'+layers[b])
#     shuffle.setInput(0,dot)
#     shuffle_temp=Shuffle_Temp_Save(shuffle_temp,dot)
#     unpremult=nuke.nodes.Unpremult()
#     unpremult.setInput(0,shuffle)
#遇到bug问题联系微信：lolea144，虽然我可能也不会修bug哈哈哈，代码菜鸡瞎写的


###GUI选择Layers###
def SelectLayers(node):
    layers=['0'for c in range(0,100)]
    channels=node.channels()
    ##GUI选择Layers##
    for c in channels:
        all_layers=list(set([c.split('.')[0] for c in channels]))
        all_layers.sort()
        p=nuke.Panel('Select Shuffle AOVs')
        all_layers_count=0
        for c in all_layers:
            p.addBooleanCheckBox(all_layers[all_layers_count], False)
            all_layers_count=all_layers_count+1
     ##如果不选择返回0##
    if not p.show():
        return 0
     ##计数选择的Layers##   
    all_layers_count=0
    layers_count=0
    temp=len(all_layers)
    for c in range(temp):
        print(p.value(all_layers[c]))
        if p.value(all_layers[all_layers_count]):
            layers[layers_count]=all_layers[all_layers_count]
            layers_count=layers_count+1
        all_layers_count=all_layers_count+1
     ##清除列表中非Layers元素##       
    for c in range(100-layers_count):
        layers.remove('0')
    return layers

###主函数###
def L_AOVs(node):
    s=node
    b=0
    shuffle_temp=0
    selectlayer_sult=SelectLayers(s)
    if selectlayer_sult==0:
        Return
    else:
         for a in range(len(selectlayer_sult)):
            dot=nuke.nodes.Dot()
            if shuffle_temp!=0:
                dot.setInput(0,shuffle_temp)
            else:
                dot.setInput(0,node)
            shuffle=nuke.nodes.Shuffle2(postage_stamp=True,name='Shuffle_'+selectlayer_sult[b])
            shuffle['in1'].setValue(selectlayer_sult[b])
            shuffle.setInput(0,dot)
            shuffle_temp=dot
            unpremult=nuke.nodes.Unpremult()
            unpremult.setInput(0,shuffle)         
            b=b+1
