import gen
def printout(line_obj):
    print("嗨！",line_obj[0])
    print("您的身分證字號："+line_obj[1])
    print("您的性別："+gen.gen(line_obj[2]))
    print("您的身高："+line_obj[3]+"公分")
    print("您的體重："+line_obj[4]+"公斤")
    print("您的年齡："+line_obj[5]+"歲")