import csv

def sign_up(account,password):
	csv_file=csv.reader(open('account.csv','a'))
	#csv_file.close()
	csv_file=csv.reader(open('account.csv','r'))
	for stu in csv_file:
		print(stu[0])
		if account==stu[0]:
			#print('wrong!')
			return 0  #账号已存在
	#csv_file.close()	
	sign_stu=[account,password]
	if account == '':
		return 3
	elif password == '':
		return 2

	out = open('account.csv','a', newline='')
	csv_write = csv.writer(out,dialect='excel')
	csv_write.writerow(sign_stu)
	#print('successful!')
	return 1  #注册成功



def log_in(account,password):
	csv_file=csv.reader(open('account.csv','a'))
	csv_file=csv.reader(open('account.csv','r'))
	for stu in csv_file:
		if account==stu[0]:
			if password==stu[1]:
				#print('Login Successful!')
				return 0      #登录成功
			else:
				#print('Wrong Password!')
				return 1      #密码错误
	#print('Account Do Not Exist!')
	return 2        #账号不存在
#log_in('why','123344')