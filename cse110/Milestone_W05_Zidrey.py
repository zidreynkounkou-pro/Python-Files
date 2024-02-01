# Variables
user_name = input("Enter your full name here, please: ").title()
print()
print("We welcome you here", user_name + "!", "We have prepared a wonderful game for you. We hope you are going to enjoy it!")
print()

right = "on the right"
eat_it = "picking up the mango and eat it"
assume_punish = "assuming the punishment"
accpt_his_offer = "accepting his offer"



step_one = input("Imagine you go in search of gold called Perfect Gold, because of its power, you name it, in an area that you do not control. You walk for around a hour, then get in between two pathways. You see that the pathway on the left brigths, there is no hole. Everything is cool there. However, the pathway on the right has thorns at the beginning, holes, but very clear and radiating very far ahead. You see a man from the left pathway telling you to go there if you want really getting your Perfet Gold and he will provide you some help, show you where to find it. 'Do not go on the right', he says. However, you see a wise old man telling you to go on the right, over there, are what you need in abondance. 'I will provide you some help a long the way so you can support those thorns and everything that may come in your way.', he says. In a such crucial situation, in what direction would you like to go? ON THE RIGHT or LEFT? ")

 # Conditions
if step_one.lower() == right:
     on_the_right = input("You chose going on the right direction. By the time you go on the right, the wise old man keeps his promise, so helps you to walk over thorns and holes. 'Welcome in my world son, you are going to find what you expect but, you need to follow step by step my instruction. I want you not eating every fruit that you may see as long as many days you are going to stay here seeking for your Perfect Gold. I am going to find something to eat for you.', he says. As you are so hungry, you accept waiting for him bringing you someting to eat. Three hours have passed, the wise man has not been back yet. By chance, you see a very attractive mango falling from the tree. What will you do? PICKING UP THE MANGO AND EAT IT or KEEPING THE INSTRUCTION GIVEN BY AND CONTUNUING TO WAIT FOR THE WISE OLD MAN? ")
     if on_the_right.lower() == eat_it:
        picking_up = input("You chose to eat the mango. The time you finish eating the mango the wise man comes back holding the Perfect Gold on his hands. You look at him and start trumbling. 'Why are you trumbling, did you eat a fruit?', he says. You assume that you have eaten a mango, because you were very hungry. 'Because you have not followed my law, this means you are not prepared enough to have this Perfect Gold. I would like to observe you for one year and see if you will be able not eating a fruit anymore.' Says the wise old man. What will you do? GOING BACK HOME or ASSUMING THE PUNISHMENT? ")
        if picking_up.lower() == assume_punish:
             print("Congradulation! You have shown us that you are a finisher. We appreciate that you are that kind of person!")
             
        else:
             print("We are sorry that you decided to go back home. When you start a journey in something I would like to have for the behalf of whoever may be, it is import keep the cap until you get what you need to have if there there always a possibility.")
     else:
      keep_instruct = input("As you have been faithful in my instruction, you won the first step, you still have the second step. 'As you are fat, I want you to run a distance of ten kilometers then come back right here. What will you do? RUNNING or DESOBEIT?")
else:
    on_the_left = input("You chose going on the left. You take the left and you see that man laughing in strange way saying: ' You are the welcome in my community! I know where you can fing what you are looking for, but before I show you the way I need you to work for me, so you are going to be my disciple. What will be your reaction here? ACCEPTING HIS OFFER or DECLINING HIS OFFER?")
                 
     










