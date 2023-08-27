data=read.table("C:\\Users\\adity\\Downloads\\probit.txt",head=T)
dose=data$dose
dead=data$dead
size=data$size
x=qnorm(dead/size)
plot(dose,x,type='o')
