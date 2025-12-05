import numpy as np
import xarray as xr
from matplotlib.tri import Triangulation

from config import FOCUS_REGION

def load_grid_data():
    """
    This function loads grid data that is commonly used in the analysis. It also computes the triangulation for plotting, cell areas
    and a cut-out to the focus region as defined in config.py.
    """
    grid_data = {}

    # Grid info for deterministic runs:
    grid_data["grid_26"] = xr.open_dataset("./invar/icon_grid_0026_R03B07_G.nc") 
    grid_data["tri_26"] = Triangulation(np.rad2deg(grid_data["grid_26"]["clon"]), np.rad2deg(grid_data["grid_26"]["clat"]))
    grid_data["area_26"] = grid_data["grid_26"]["cell_area"] #in m^2 although mislabeld as steradian

    # Reduced deterministic region:
    # to save disk space I chose to only save a part of the global output...
    _mask = ((np.rad2deg(grid_data["grid_26"]["clon"].values) >= -120) & 
             (np.rad2deg(grid_data["grid_26"]["clon"].values) <= 90) & 
             (np.rad2deg(grid_data["grid_26"]["clat"].values) >= 0))
    grid_data["grid_26_red"] = grid_data["grid_26"].sel(cell=np.arange(2949120)[_mask])
    grid_data["tri_26_red"] = Triangulation(np.rad2deg(grid_data["grid_26_red"]["clon"]), np.rad2deg(grid_data["grid_26_red"]["clat"]))
    grid_data["area_26_red"] = grid_data["grid_26_red"]["cell_area"]

    # Grid info for ensemble runs:
    grid_data["grid_28"] = xr.open_dataset("./invar/icon_grid_0028_R02B07_N02.nc")
    grid_data["tri_28"] = Triangulation(np.rad2deg(grid_data["grid_28"]["clon"]), np.rad2deg(grid_data["grid_28"]["clat"]))
    grid_data["area_28"] = grid_data["grid_28"]["cell_area"]


    # Define "focus region" for the different grids:
    x0, x1 = FOCUS_REGION["x0"], FOCUS_REGION["x1"]
    y0, y1 = FOCUS_REGION["y0"], FOCUS_REGION["y1"]

    grid_data["focus_cells_26"] = ((np.rad2deg(grid_data["grid_26"]["clon"]) >= x0) & (np.rad2deg(grid_data["grid_26"]["clon"]) <= x1) & 
                                   (np.rad2deg(grid_data["grid_26"]["clat"]) >= y0) & (np.rad2deg(grid_data["grid_26"]["clat"]) <= y1)).values

    grid_data["focus_cells_26_red"] = ((np.rad2deg(grid_data["grid_26_red"]["clon"]) >= x0) & (np.rad2deg(grid_data["grid_26_red"]["clon"]) <= x1) & 
                                       (np.rad2deg(grid_data["grid_26_red"]["clat"]) >= y0) & (np.rad2deg(grid_data["grid_26_red"]["clat"]) <= y1)).values

    grid_data["focus_cells_28"] = ((np.rad2deg(grid_data["grid_28"]["clon"]) >= x0) & (np.rad2deg(grid_data["grid_28"]["clon"]) <= x1) & 
                                   (np.rad2deg(grid_data["grid_28"]["clat"]) >= y0) & (np.rad2deg(grid_data["grid_28"]["clat"]) <= y1)).values

    return grid_data


def read_merged_var_det(var, dts, data_dir):
    """
    Reads input information from deterministic runs, i.e., only one realization per experiment.

    The merged files contain all time steps of a folder, i.e., step, step - 1h, step - 2h and step - 3h. 
    # In that case, doing diff works "out of the box" for accumulated variables, because the first timestep
    # in each assimilation cycle, i.e., step - 3h, is all zero.
    """

    fnames = [f"{data_dir}/fc_R03B07_{var}_merged.{dt.year:02}{dt.month:02}{dt.day:02}{dt.hour:02}" for dt in dts]

    datasets = []
    for fname in fnames:

        dataset = xr.open_dataset(fname, engine="cfgrib", backend_kwargs={"indexpath": ""}).rename({"values": "cell"})[var]
        dataset = dataset.diff(dim="step")
        dataset["step"] = dataset["valid_time"]
        datasets.append(dataset)

    return xr.concat(datasets, dim="step")


def read_merged_var_ens(var, dts, data_dir):
    """
    Similar to read_merged_var_det, but concatenates the ensemble members to their own dimension.
    """

    data_arrays = []
    for mem in range(1,21):

        fnames = [f"{data_dir}/fc_R02B07_N02_{var}_merged.{dt.year:02}{dt.month:02}{dt.day:02}{dt.hour:02}.{mem:03}" for dt in dts]
        infiles = []
        for fname in fnames:

            infile = xr.open_dataset(fname, engine="cfgrib", backend_kwargs={"indexpath": ""}).rename({"values": "cell"})[var]
            infile = infile.diff(dim="step")
            infile["step"] = infile["valid_time"]
            infiles.append(infile)

        data_arrays.append(xr.concat(infiles, dim="step"))
    
    return xr.concat(data_arrays, dim="mem")