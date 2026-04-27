from matplotlib import colors

FOCUS_REGION = {
    "x0": 2.5,  # longitude start
    "x1": 9.5,  # longitude end
    "wx": 7,    # longitude width
    "y0": 48,   # latitude start
    "y1": 53,   # latitude end
    "wy": 5     # latitude width
}

FOCUS_REGION_L = {
    "x0": 2,  # longitude start
    "x1": 12,  # longitude end
    "wx": 10,    # longitude width
    "y0": 47,   # latitude start
    "y1": 54,   # latitude end
    "wy": 7     # latitude width
}

PASSIVE_REGION = {
    "x0": -10,  # longitude start
    "x1": 40,   # longitude end
    "wx": 50,   # longitude width
    "y0": 30,   # latitude start
    "y1": 75,   # latitude end
    "wy": 45    # latitude width  
}

PRUDENCE_REGIONS = {"BI": {"name": "British Isles", "lon": slice(-10, 2), "lat": slice(50, 59)},
                    "IP": {"name": "Iberian Peninsula", "lon": slice(-10, 3), "lat": slice(36, 44)},
                    "FR": {"name": "France", "lon": slice(-5, 5), "lat": slice(44, 50)},
                    "ME": {"name": "Mid-Europe", "lon": slice(2, 16), "lat": slice(48, 55)},
                    "SC": {"name": "Scandinavia", "lon": slice(5, 30), "lat": slice(55, 70)},
                    "AL": {"name": "Alps", "lon": slice(5, 15), "lat": slice(44, 48)},
                    "MD": {"name": "Mediterranean", "lon": slice(3, 25), "lat": slice(36, 44)},
                    "EA": {"name": "Eastern Europe", "lon": slice(16, 30), "lat": slice(44, 55)}}

# Plotting setups:
SUM_LVL = [0, 0.1, 1 , 2, 5, 10, 15, 20, 30, 50, 75, 100, 125, 150, 200]    #precipitation sums
SUM_NORM = colors.BoundaryNorm(SUM_LVL, 256)

DIV_LVL = [-160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160] #precipitation diffs
DIV_NORM = colors.TwoSlopeNorm(vmin=-160, vcenter=0, vmax=160)

W2L_LVL = [0, 0.1, 0.5, 1., 1.5, 2., 3., 4., 6.] #large:W2L_LVL = [0, 0.1, 0.5, 1., 1.5,  3., 5., 9.]
W2L_NORM = colors.BoundaryNorm(W2L_LVL, 256)

PLOT_WINDOW = [-5, 25, 37, 62]      #Bounds: West, East, South, North


# Colors:
c_ctl = "tab:blue"
c_dry = "tab:orange"
c_wet = "tab:green"
c_rea = "black"