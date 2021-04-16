for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s' %(i,j,i*j),end=' ')  # end=' '表示不换行，只是加个空格
    print() # 单纯换行
