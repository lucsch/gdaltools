# GDAL TOOLS

Porting of some gdals tools using conan

## gdal_addo

Create pyramids / overviews

        gdal_addo file.tif 2 4 8 16 (internal pyramids)
        gdal_addo -ro file.tif 2 4 8 16 (external pyramids)

## gdal_translate

Convert between file formats

        gdal_translate file_in.jpg -of GTiff fileout.tif

