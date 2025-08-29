import turtle
import pandas

screen=turtle.Screen()
screen.title('US State Game')
image='states.gif'
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

states_data=pandas.read_csv('50_states.csv')
states=states_data.state.to_list()

score=0
guessed_states=[]
while len(guessed_states)<50:
    guess=screen.textinput(f'{len(guessed_states)}/50 States Correct','Guess a state name').title()
    if guess == 'Exit':
        missing_states=[]
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
                df=pandas.DataFrame(missing_states)
                df.to_csv('missed states.csv')
        break
    if guess in states and guess not in guessed_states:
        score+=1
        guessed_states.append(guess)
        obj=states_data[states_data.state==guess]
        new_turtle=turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(int(obj.x),int(obj.y))      
        new_turtle.write(f"{guess}")
    else:
        continue
    
# turtle.mainloop()