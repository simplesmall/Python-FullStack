def salary(perhour,hour):
    all = 0
    # should_all = perhour * should
    # other_all = perhour * 1.5 * other
    # all = should_all + other_all
    #Though there is some way to short needed diagram,lessen flexiable at the same time
    should = 20
    all=perhour*hour+perhour*1.5*(hour-should)
    return all
ret = salary(10, 200)
print(ret)
