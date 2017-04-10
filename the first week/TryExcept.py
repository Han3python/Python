# TempConvert.py
try:
    val = input("请输入带温度表示符号的温度值(例如: 32C): ")
    if val[-1] in ['C', 'c']:
        f = 1.8 * eval(val[0:-1]) + 32
        print("转换后的温度为: %.2fF" % f)
    elif val[-1] in ['F', 'f']:
        c = (eval(val[0:-1]) - 32) / 1.8
        print("转换后的温度为: %.2fC" % c)
    else:
        print("输入有误")
except NameError:
    print("名称错误！")
except SyntaxError:
    print("语法错误！")
except ValueError:
    print("值错误！")
except TypeError:
    print("类型错误！")
except:
    print("其他错误！")