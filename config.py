from matplotlib import colors

FOCUS_REGION = {
    "x0": 2.5,  # longitude start
    "x1": 9.5,  # longitude end
    "wx": 7,    # longitude width
    "y0": 48,   # latitude start
    "y1": 53,   # latitude end
    "wy": 5     # latitude width
}

PASSIVE_REGION = {
    "x0": -15,  # longitude start
    "x1": 40,   # longitude end
    "wx": 55,   # longitude width
    "y0": 35,   # latitude start
    "y1": 75,   # latitude end
    "wy": 40    # latitude width  
}

# Plotting setups:
SUM_LVL = [0, 0.1, 1 , 2, 5, 10, 15, 20, 30, 50, 75, 100, 125, 150, 200]    #precipitation sums
SUM_NORM = colors.BoundaryNorm(SUM_LVL, 256)

DIV_LVL = [-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160] #precipitation diffs
DIV_NORM = colors.TwoSlopeNorm(vmin=-100, vcenter=0, vmax=160)

W2L_LVL = [0, 0.1, 0.5, 1., 1.5, 2., 3., 4.]
W2L_NORM = colors.BoundaryNorm(W2L_LVL, 256)

PLOT_WINDOW = [-5, 25, 37, 62]      #Bounds: West, East, South, North

