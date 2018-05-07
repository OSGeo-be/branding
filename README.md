# OSGeo-be branding materials

## Logo

Current logo proposition:

<img src="logo/osgeo-be.svg" alt="low resultion banner" height="200" width="900"/>

## Banner

<img src="banner/banner-low-res.jpg" alt="low resultion banner" height="500"/>

To generate `banner.svg` (which embeds the fonts and image in the svg template)

```shell
python embed.py banner/banner.tpl.svg banner/banner.svg
```

To go from svg to png from the command line:

```shell
inkscape -z -e /full/path/to/banner/banner.png -a=0:-8034:3370:100 /full/path/to/banner/banner.svg
```
