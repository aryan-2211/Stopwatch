# template for "Stopwatch: The Game"
import simplegui
# define global variables
run_status = False
chances_count, success, total_chances = 0,0,0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D, t = t % 10, t / 10
    C, t = t % 10, t / 10
    B, A = t % 6, t / 6
    return str(A) + ":" + str(B) + ":" + str(C) + "." + str(D)

def result() :
    return str(success) + "/" + str(total_chances)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start() :
    global run_status
    timer.start()
    run_status = True
    
def stop():
    global run_status, success, total_chances
    timer.stop()
    if run_status:
        total_chances += 1
        if chances_count % 10 == 0:
            success += 1
    
    run_status = False
    
def reset():
    global run_status, success, total_chances, chances_count
    timer.stop()
    run_status = False
    chances_count, success, total_chances = 0, 0, 0

# define event handler for timer with 0.1 sec interval
def tick():
    global chances_count
    chances_count += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(chances_count),[55,80], 30, "white")
    canvas.draw_text(result(), [150, 30], 25, "Red")

# create frame
frame = simplegui.create_frame("Stopwath", 200, 200)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
