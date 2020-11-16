############# For Loop ##################################
# for each in [3,4,56,7,8]:
# 	print(each)
# 	if each==56:
# 		break
# print("after loop")


############### break in if condition #####################
# paths=['/usr/bin','/usr/bin/httpd','/home/users/xyz/weblogic/config.xml']
# for each_path in paths:
# 	print("now working on: ",each_path)
# 	if 'httpd' in each_path:
# 		print(each_path)
# 		break
# print("outside of for loop")


############## break in while condition ####################
# cnt=1
# while True:
# 	print(cnt)
# 	if cnt==100:
# 		break # break keyword will break the loop and it wont't go to the next iteration
# 	cnt=cnt+1


################  continue in if condition ###################
for each in range(1,11):
	if each ==7:
		continue  # Continue will break only this if condition and it will go for next iteration
		print("this is the line inside of your if condition after continue keyword")
	print(each)


################# pass  in if condition ####################
# if True:
# 	pass


################### pass in for loop #########################
# for each in range(3):
# 	pass











