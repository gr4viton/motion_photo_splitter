# Motion photo splitter

Take list of filenames containing joined photo and video and split them in two separate files.

## Usage
```
Usage: mp_splitter.py [OPTIONS] [FILENAMES]...

  Take list of filenames containing joined photo and video and split them in
  two separate files.

  Works for samsung motion photos by default - they contain
  "MotionPhoto_data" edge marker - but any other marker text can be passed.

  CARE: If you set empty string as the file suffix, the original file gets
  overwritten!

Options:
  -q, --quiet        supress all output
  -m, --marker TEXT  The utf-8 encoded edge marker text. Default is for
                     samsung motion photos  [default: MotionPhoto_Data]

  --pic-suffix TEXT  Suffix of the splitted picture file.  [default: .jpg]
  --vid-suffix TEXT  Suffix of the splitted video file.  [default: .mp4]
  --help             Show this message and exit.
```

## Links

Wrote from scratch.

Other projects with the similar goal:
- https://github.com/cliveontoast/GoMoPho
- https://github.com/joemck/ExtractMotionPhotos
- https://forum.xda-developers.com/android/general/tool-to-extract-samsung-motion-photos-t3568899
