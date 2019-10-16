# Normalized Burn Ratio(NBR)
import xarray as xr
import numpy as np
print("Indice de estimación de severidad de fuegos")
	
period_green = xarr0["nir"].values
period_nir = xarr0["swir1"].values
mask_nan=np.logical_or(np.isnan(period_nir), np.isnan(period_swir1))
period_nbr = (period_nir-period_swir1 )/(period_nir+period_swir1 ) 
period_nbr[mask_nan]=np.nan
#Hace un clip para evitar valores extremos.
period_nbr[period_nbr>1]=np.nan
period_nbr[period_nbr<-1]=np.nan

ncoords=[]
xdims =[]
xcords={}
for x in xarr0.coords:
    if(x!='time'):
        ncoords.append( ( x, xarr0.coords[x]) )
        xdims.append(x)
        xcords[x]=xarr0.coords[x]
variables ={"nbr": xr.DataArray(period_nbr, dims=xdims,coords=ncoords)}
output=xr.Dataset(variables, attrs={'crs':xarr0.crs})
for x in output.coords:
    output.coords[x].attrs["units"]=xarr0.coords[x].units