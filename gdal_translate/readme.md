# gdal_translate 

## WMS commands

extract image from a xml file

         ./gdal_translate -of JPEG -outsize 1500 1000 Swisstopo_wms.xml onearth_global_mosaic.jpg

create a service description file (see : https://courses.spatialthoughts.com/gdal-tools.html#listing-wms-layers)

In order to work, the projection must be EPSG:3857 (WGS 84)

        gdal_translate -of WMS "WMS:https://wms.geo.admin.ch/?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=ch.swisstopo.pixelkarte-farbe&STYLES=default&CRS=EPSG:3857" swisstopo_pixelkarte.xml

         