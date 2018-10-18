#! /usr/bin/env python3
import os
import rasterio
import numpy


class Ndvi():
    """Processamento de imagens .tif calculando NDVI
    """
    def __init__(self):
        pass
    
    def processSceneToNDVI(src):
        source = os.listdir(src)
        for i, v in enumerate(source):
            
            nf = str(newPath + "NDVI_" + v)
            
            with rasterio.open(path+source[i]) as img:
                band_red = img.read(3)
                band_nir = img.read(4)

                numpy.seterr(divide='ignore', invalid='ignore')
                ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)
                kwargs = img.meta
                kwargs.update(
                    dtype=rasterio.float32,
                    count = 1)
                
                with rasterio.open(nf, 'w', **kwargs) as dst:
                    dst.write_band(1, ndvi.astype(rasterio.float32))

