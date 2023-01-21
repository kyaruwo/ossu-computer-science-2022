# tower of pain

def printMove(fr, to):
    print(f"move from {fr} to {to}")


def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)

        Towers(1, fr, to, spare)

        Towers(n-1, spare, to, fr)


Towers(4, "b", "a", "c")

# https://pythontutor.com/visualize.html#code=def%20printMove%28fr,%20to%29%3A%0A%20%20%20%20print%28f%22move%20from%20%7Bfr%7D%20to%20%7Bto%7D%22%29%0A%0A%0Adef%20Towers%28n,%20fr,%20to,%20spare%29%3A%0A%20%20%20%20if%20n%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20printMove%28fr,%20to%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20Towers%28n-1,%20fr,%20spare,%20to%29%0A%0A%20%20%20%20%20%20%20%20Towers%281,%20fr,%20to,%20spare%29%0A%0A%20%20%20%20%20%20%20%20Towers%28n-1,%20spare,%20to,%20fr%29%0A%0A%0ATowers%284,%20%22b%22,%20%22a%22,%20%22c%22%29%0A%0A%23%20link%0A&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
# https://www.youtube.com/watch?v=WPSeyjX1-4s @ 20:12
