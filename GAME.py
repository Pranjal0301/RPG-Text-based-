from tkinter import *  # import everything from the tkinter library
from PIL import ImageTk, Image  # used to import image
from tkinter import messagebox  # used to create popup messages.

root = Tk()  # used to create an tkinter window named root
root.attributes('-fullscreen', TRUE)  # to create a full screened tkinter window
root.title('Text adventure game!')  # to set the title of the window

####################################################################################DEFINATIONS#############################################################################################################################################################

weapon = 0  # global variable showing if we have a weapon or not.


def run():
    def forest():
        def left():
            Label(page2, text='''
            You decide to take the left road, and surely it was the right choice.
            After walking about an hour or so, you start to see a stream of smoke rising in the distance. You quickly dash towards it and find your classmates sitting around an campfire!
            You Won congratulations !
            ''', font=('Times new roman', 12, 'bold')).grid(row=6, column=0)
            Button(page2, text='Quit Game',
                   command=lambda: [messagebox.showinfo("Lucky", "Survived without any adventure? Lucky..."),
                                    root.destroy()], font=('Times new roman', 13, 'bold'), relief=RAISED,
                   fg='red').grid(row=7, column=0, ipadx=50, ipady=20)

        def right():
            global weapon
            Label(page2, text='''
                        You decide to take the right turn as right is always right...Right ? Wrong as it turns out it was an dead end and there is nowhere for you to go anymore. Also the roar is
                        closer than ever before. The lion slowly emerges from behind the thickets of shrubs and you can see in it’s eyes that it is hungry.

                        ''', font=('Times new roman', 12, 'bold')).grid(row=5, column=0)
            if weapon == 0:
                Label(page2, text='''
                    Well, you die. You stood no chance in front of a hungry lion and that too without a weapon.
                    The lion easily pounces on you and sinks it’s fangs in your neck and everything turns black. 
                    YOU LOOSE.
                    ''', font=('Times new roman', 12, 'bold')).grid(row=6, column=0)
                Button(page2, text='Quit Game',
                       command=lambda: [messagebox.showerror("Ouch", "Fighting without a weapon? Bad idea."),
                                        root.destroy()], font=('Times new roman', 13, 'bold'), relief=RAISED,
                       fg='red').grid(row=8, column=0, ipadx=50, ipady=20)
            else:
                Label(page2, text='''
                     You ready your spear, even though you have never used a spear before in your life but you do have some experience with dueling canes and your mom sent you to fighting lessons when you
                     were younger. You grip the shaft of the spear tightly and rather than waiting for the lion to attack you muster every bit of courage inside of you and charge! The lion was not expecting
                     this bravery or foolishness ? Whatever the case the lion is surprised and you get a clean hit on the side of it’s belly before it could get out of the way. The lion charges you but you 
                     side step.. just as you were taught in the fighting classes. The lion is loosing a lot of blood from the abdominal wound and is more ferocious than ever. You make a plan, you will try to 
                     let the lion attack and try to land a fatal blow when it gets near to you. The lion pounces , you raise your spear and side step simultaneously and strike with all your might!
                     The lion’s paw grazes your right thigh as you were not able to get away in time but your plan worked. The spear passed right through the lion’s neck and it collapses to the ground.

                     You actually beat the lion! But got yourself wounded in the process. You are loosing a lot of blood and loosing it very quickly. You tear off your shirt sleeve and tie it around your leg. 
                     You sense some commotion behind you in the thickets. You become tense and wait for whatever it is to reveal itself. It is your friend!
                     Turns out your friends were nearby and came to search for you as soon as they heard all the commotion of the fight between you and the lion.

                     You Won Congratulations!
                                   ''', font=('Times new roman', 12, 'bold')).grid(row=6, column=0)
                Button(page2, text='Quit Game',
                       command=lambda: [messagebox.showinfo("Wow", "What a battle! You Survived!! Congratulations!!!"),
                                        root.destroy()], font=('Times new roman', 13, 'bold'), relief=RAISED,
                       fg='red').grid(row=7, column=0, ipadx=50, ipady=20)

        Label(page2, text='''
            You decide it would be better if you ventured deeper into the dense forest as it is more likely that you would find your classmates there as they had the plan to go deeper today.
            While venturing deeper , you come towards an identical crossroads. One going left and the other towards right. There is no way to distinguish them from one another.What do you do ?
                           ''', font=('Times new roman', 12, 'bold')).grid(row=3, column=0)
        Button(page2, text="Choose to go Right", relief=RAISED, command=right,
               font=('Times new roman', 10, 'bold')).grid(row=4, column=0)
        Button(page2, text="Choose to go Left", relief=RAISED, command=left, font=('Times new roman', 10, 'bold')).grid(
            row=5, column=0)

    def river():
        def die_2():
            Label(page2, text='''
                    Well , you die…and rather painfully. What did you expect jumping in a river infested with flesh eating fish? YOU LOOSE! 
                    ''', font=('Times new roman', 12, 'bold',)).grid(row=6, column=0)
            Button(page2, text='Quit Game',
                   command=lambda: [messagebox.showerror("Oh No", "Bad choices? Try Again!"), root.destroy()],
                   font=('Times new roman', 13, 'bold'), relief=RAISED, fg='red').grid(row=7, column=0, ipadx=50,
                                                                                       ipady=20)  # here lambda is used to assign 2 functions to a single button... the first function is the messagebox and the second is the simple exit button.

        def lion_fight():
            global weapon
            Label(page2, text='''
                               You decide to stand your ground. If you are going to die, you will die with courage not running away like a coward. The lion slowly emerges from behind the thickets of 
                               shrubs and you can see in it’s eyes that it is hungry.
                                ''', font=('Times new roman', 12, 'bold')).grid(row=6, column=0)

            if weapon == 0:
                Label(page2, text='''
                    Well, you die. You stood no chance , none whatsoever in front of a hungry lion and that too without a weapon.
                    The lion easily pounces on you and sinks it’s fangs in your neck and everything turns black. 
                    YOU LOOSE.
                    ''', font=('Times new roman', 12, 'bold')).grid(row=7, column=0)
                Button(page2, text='Quit Game',
                       command=lambda: [messagebox.showerror("Ouch", "Fighting without a weapon? Bad idea."),
                                        root.destroy()], font=('Times new roman', 13, 'bold'), relief=RAISED,
                       fg='red').grid(row=8, column=0, ipadx=50, ipady=20)
            else:
                Label(page2, text='''
                     You ready your spear, even though you have never used a spear before in your life but you do have some experience with dueling canes and your mom sent you to fighting lessons when you
                     were younger. You grip the shaft of the spear tightly and rather than waiting for the lion to attack you muster every bit of courage inside of you and charge! The lion was not expecting
                     this bravery or foolishness ? Whatever the case the lion is surprised and you get a clean hit on the side of it’s belly before it could get out of the way. The lion charges you but you 
                     side step.. just as you were taught in the fighting classes. The lion is loosing a lot of blood from the abdominal wound and is more ferocious than ever. You make a plan, you will try to 
                     let the lion attack and try to land a fatal blow when it gets near to you. The lion pounces , you raise your spear and side step simultaneously and strike with all your might!
                     The lion’s paw grazes your right thigh as you were not able to get away in time but your plan worked. The spear passed right through the lion’s neck and it collapses to the ground.

                     You actually beat the lion! But got yourself wounded in the process. You are loosing a lot of blood and loosing it very quickly. You tear off your shirt sleeve and tie it around your leg. 
                     You sense some commotion behind you in the thickets. You become tense and wait for whatever it is to reveal itself. It is your friend!
                     Turns out your friends were nearby and came to search for you as soon as they heard all the commotion of the fight between you and the lion.

                     You Won Congratulations!


                                   ''', font=('Times new roman', 12, 'bold')).grid(row=7, column=0)
                Button(page2, text='Quit Game',
                       command=lambda: [messagebox.showinfo("Wow", "What a battle! You Survived!! Congratulations!!!"),
                                        root.destroy()], font=('Times new roman', 13, 'bold'), relief=RAISED,
                       fg='red').grid(row=8, column=0, ipadx=50, ipady=20)

        Label(page2, text='''
        ROARRRRRRR! You think that going towards the river would be wiser and bolt towards the water. But to your despair find out that the river is infested with flesh eating Piranhas! And the roar is 
        closer than ever. You can either try and face the lion head on like a brave man or try to test your swimming skills by trying to outswim the piranhas.Whatever you do, do it quick!
        ''', font=('Times new roman', 12, 'bold')).grid(row=3, column=0)
        Button(page2, text="Try to swim in the dangerous lake!", relief=RAISED, font=('Times new roman', 10, 'bold'),
               command=die_2).grid(row=4, column=0)
        Button(page2, text="Try to stand your ground against the lion!", relief=RAISED,
               font=('Times new roman', 10, 'bold'), command=lion_fight).grid(row=5, column=0)

    page2 = Toplevel()  # page 2 is the name of the second window.
    page2.title('Page2')
    page2.attributes('-fullscreen', TRUE)
    Label(page2, text='''
    You dash in the opposite direction of that roar as fast as you can. After running for a while you come on a crossroads, you can either choose to go towards the river OR venture deeper in the forests. 
    This is an important decision so choose wisely!
'''
          , font=('Times new roman', 11, 'bold')).grid(row=0, column=0)
    Button(page2, text="Choose to go towards the river", relief=RAISED, command=river,
           font=('Times new roman', 10, 'bold')).grid(row=1, column=0)
    Button(page2, text='Choose to go deeper into the forest', relief=RAISED, font=('Times new roman', 10, 'bold'),
           command=forest).grid(row=2, column=0)


def start():
    def die_1():
        Label(root, text='''
        Well, you die. You stood no chance ,none whatsoever in front of a hungry lion and that too without a weapon. The lion easily pounces on you and sinks it’s fangs in your neck and everything 
        turns black.

        YOU LOOSE.
        ''', font=('Times new roman', 12, 'bold')).grid(row=8, column=1, ipadx=20)
        Button(root, text='Quit Game',
               command=lambda: [messagebox.showerror("-_-", "Brave...or Foolish?"), root.destroy()],
               font=('Times new roman', 13, 'bold'), relief=RAISED, fg='red').grid(row=9, column=1, ipadx=30, ipady=10)

    def lfw_2():
        Label(root, text='''
                       You keep on searching franticly, and finally you stumble upon a walking stick. But it is not a walking stick! You remember you friend was using a spear for  walking stick.
                       You quickly pick it up and flee for your life.
                       ''', font=('Times new roman', 12, 'bold')).grid(row=11, column=1)
        global weapon  # we have a weapon now!
        weapon = 1
        Button(root, text="Next page", relief=RAISED, command=run, font=('Times new roman', 13, 'bold'), width=17,
               height=2, fg='blue').grid(row=9, column=1, rowspan=2)

    def lfw_1():  # look for weapon for the first time
        Label(root, text='''
               You take your chances and try to look for a weapon.”ROARRRRR” The roar sounded much closer this time.You do not find anything … you start to panic.What do you do??
               ''', font=('Times new roman', 12, 'bold')).grid(row=8, column=1)
        Button(root, text="Keep on looking for a weapon...", relief=RAISED, command=lfw_2,
               font=('Times new roman', 10, 'bold')).grid(row=9, column=1)
        Button(root, text="Flee for your life", relief=RAISED, command=run, font=('Times new roman', 10, 'bold')).grid(
            row=10, column=1)

    label_1 = Label(root, text='''
So long story short, you were out on a camping trip with your class and everything was going fine until you were left behind. Now you need to survive on your own and find your way back to your 
classmates somehow.
You hear a roar, you are frightened and do not know what to do. You are sure that is a lion and you do not stand a chance against it. You have three options, You can either try to face the lion,
try to look for a weapon (it could take some time and the lion could attack you before you can find any weapon!)  ,or just flee! What will you do !?
'''
                    , font=('Times new roman', 12, 'bold')).grid(row=4, column=1, ipadx=20, ipady=5)
    Button(root, text="You decide to stay and confront the lion like a brave man!", relief=RAISED, command=die_1,
           font=('Times new roman', 10, 'bold')).grid(row=5, column=1)
    Button(root, text="Run away like a coward.", command=run, relief=RAISED, font=('Times new roman', 10, 'bold')).grid(
        row=6, column=1)
    Button(root, text="Wager on finding a weapon nearby.", relief=RAISED, command=lfw_1,
           font=('Times new roman', 10, 'bold')).grid(row=7, column=1)


####################################################################################Definations End####################################################################################################################################################################################################################################


label_header = Label(root, text='Welcome to a simple text based adventure game\n\n Escape The Jungle',
                     font=('Algerian', 18, 'bold')).grid(row=1, column=1, ipadx=350, ipady=10, sticky="NSEW")

label_info = Label(root,
                   text='      Members                      Rollno\n1.Anirudh Sharma           34\n2.Pranjal Sarode              35\n3.Harshawardhan Patil    25\n4.Snehal Kumkar             26\n5.Shrushti                         22',
                   font=('Times new roman', 12, 'bold')).grid(row=2, column=1, ipadx=0, ipady=20, sticky="NSEW")

start_button = Button(root, text='start the story', command=start, bd=8, relief=RAISED,
                      font=('Times new roman', 18, 'bold')).grid(row=3, column=1, ipadx=10, ipady=20)

mainloop()