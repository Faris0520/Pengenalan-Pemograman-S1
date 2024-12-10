def take_stop(n):
    if n == 1:
        return "Easy"
    else:
        this_step =  "step(" + str(n) + ")"
        previous_steps = take_step(n-1)
        return this_step + " + " + previous_steps