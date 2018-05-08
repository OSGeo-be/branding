# OSGeo-be branding materials

## Logo

Current logo propositions:

<img src="logo/osgeo-be-small.svg" height="186" width="186"/><br><br>

<img src="logo/osgeo-be.svg" height="200" width="760"/>

See <a href="logo/comparison.md">comparison to other logos</a>.

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
