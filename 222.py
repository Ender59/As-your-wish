import random
p1 = 0
b=0
s=int(input("choose your job : 1.assassin 2.worrior 3.tank : "))
boss=0
a = 0
set=int(input("1. shop 2.fight 3.exit : "))


while b==0 :
	while set == 2 :
		if s == 1:
			print ("hello assassin")
			p1 = 240
			boss=500
			a = int(input("1.attack 2.defence 3.escape : "))
			if a==1:
				x = int(input("enter 1 to attack"))
				while x==1 :
					atk = random.randint(50,200)
					boss -= atk
					if boss <= 0:
						print("victory")
						break
					else:
						p1 -= random.randint(30,100)
						print("Boss HP :",boss,"Your own HP",p1)
					if p1 <= 0:
						print("Your are done.")
						break
				else:
					print("enter again")
			elif a == 2 :
				x = int(input("enter 2 to defence: "))
				while x==2 :
					atk = random.randint(50,200)
					boss -= atk
					if boss <= 0:
						print("victory")
						break
					else:
						boss_atk = random.randint(30,50)
						p1 -= 0.4*boss_atk
						print("Boss HP : ",boss,"Your own HP: ",p1)
					if p1 <= 0:
						print("Your are done.")
						break
				else:
					print("enter again")
			else:
				break
	set = int(input("1. shop 2.fight 3.exit: "))
	if set == 1:
		print("not yet ")
		set = int(input("1. shop 2.fight 3.exit: "))
	elif set == 3:
		break
print("thanks for playing")

	
	
	
	
	
	
	
'''
		elif s==2 :
		print ("hello worrior")
		p1 = 310
		boss=700
		a=int(input(1.attack 2.defence 3.escape))
		while a==1:
			x = int(input("enter 1 to attack"))
			if x==1 :
				atk = random.randint(100,300)
				boss -= atk
				if boss <= 0:
					print("victory")
					break
				else:
					p1 -= random.randint(30,50)
					print("Boss HP :",boss,"Your own HP",p1)
				if p1 <= 0:
					print("Your are done.")
					break
			else:
				print("enter again")
'''





