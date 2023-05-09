import gen
def printout(line_obj):
    print("嗨！",line_obj[2])
    print("您的身分證字號："+line_obj[1])
    print("您的性別："+gen.gen(str(line_obj[3])))
    print("您的身高："+str(line_obj[5])+"公分")
    print("您的體重："+str(line_obj[4])+"公斤")
    print("您的年齡："+str(line_obj[6])+"歲")
    return "嗨！"+line_obj[1]+'\n'+"您的身分證字號："+line_obj[2]+'\n'+"您的性別："+gen.gen(str(line_obj[3]))+'\n'+"您的身高："+str(line_obj[5])+"公分"+'\n'+"您的體重："+str(line_obj[4])+"公斤"+"\n"+"您的年齡："+str(line_obj[6])+"歲"+"\n"
    