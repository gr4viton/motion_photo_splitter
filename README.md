# Motion photo splitter

Take list of filenames containing joined photo and video and split them in two separate files.

Usefull eg for [samsung motion photo files](https://www.samsung.com/global/galaxy/what-is/motion-photo/)

## Install

The [package is ready to be installed from PYPI](https://pypi.org/project/motion-photo-splitter/), python3.5+ needed.

```bash
pip3 install motion-photo-splitter
```

## Usage

```bash
Usage: motion_photo_splitter [OPTIONS] [FILENAMES]...

  Take list of filenames containing joined photo and video and split them in
  two separate files.

  Works for samsung motion photos by default - they contain
  "MotionPhoto_data" edge marker - but any other marker text can be passed.

  NOTE: how the output file names are constructed:

  `{path_prefix}{fname_orig}{pic_suffix}` - for picture files
  `{path_prefix}{fname_orig}{vid_suffix}` - for video files

  WARNING: If you set empty string as the file suffix, the original file
  gets overwritten! WARNING: If using the `path-prefix`, you should create
  the folders yourself.

Options:
  -q, --quiet         supress all output
  -m, --marker TEXT   The utf-8 encoded edge marker text. Default is for
                      samsung motion photos  [default: MotionPhoto_Data]

  --pic-suffix TEXT   Suffix of the splitted picture file.  [default: .jpg]
  --vid-suffix TEXT   Suffix of the splitted video file.  [default: .mp4]
  --path-prefix TEXT  Prefix of the splitted files path - eg to put them in
                      subfolder `out/`.  [default: ]

  --help              Show this message and exit.
```

## Examples

### One file
```bash
> motion_photo_splitter images/pic.jpg
image/pic.jpg :: exporting image/pic.jpg.jpg [3.69 MB] && image/pic.jpg.mp4 [1.13 MB]
```

### Multiple files with different suffixes
```bash
> motion_photo_splitter --pic-suffix=.jpeg --vid-suffix=.mpeg4 images/pic1.jpg images/pic2.jpg
image/pic1.jpg :: exporting image/pic1.jpg.jpeg [3.69 MB] && image/pic1.jpg.mpeg4 [1.13 MB]
image/pic2.jpg :: exporting image/pic2.jpg.jpeg [3.69 MB] && image/pic2.jpg.mpeg4 [1.13 MB]
```

### Prefix folder
```bash
> mkdir out
> motion_photo_splitter pic.jpg --path-prefix="out/"
pic.jpg :: exporting out/pic.jpg.jpg [3.69 MB] && out/pic.jpg.mp4 [1.13 MB]
```

## Links

Wrote from scratch.

Other projects with the similar goal:
- https://github.com/cliveontoast/GoMoPho
- https://github.com/joemck/ExtractMotionPhotos
- https://forum.xda-developers.com/android/general/tool-to-extract-samsung-motion-photos-t3568899
