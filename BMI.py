h,w=eval(input("请输入身高/m和体重/kg（用逗号隔开）："))
bmi=w/pow(h,2)
print("bmi指数是：{:.3f}".format(bmi))
internationnal,inland='',''
if bmi<18.5:
    internationnal='偏瘦'
    inland='偏瘦'
elif bmi<24:
    internationnal='正常'
    inland='正常'
elif bmi<25:
    inland='偏胖'
    internationnal='正常'
elif bmi<28:
    internationnal='偏胖'
    inland='偏胖'
elif bmi<30:
    internationnal,inland='偏胖','肥胖'
else:
    internationnal,inland='肥胖','肥胖'
print("bmi指标为：\n国际指标:{}     国内指标：{}".format(internationnal,inland))
