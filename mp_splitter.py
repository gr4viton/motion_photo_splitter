from dataclasses import dataclass
import click

from mmap import mmap


@dataclass
class Splitter:

    marker: str = "MotionPhoto_Data"

    quiet: bool = False

    pic_suffix: str = ".jpg"
    vid_suffix: str = ".mp4"

    _megabyte = 1024 ** 2

    def split(self, fname):
        self.print(f"{fname} :: ", end="")
        try:
            pic, vid = self._open_and_split(fname)
        except FileNotFoundError:
            self.print("file not found")

        self.print("exporting ", end="")
        self.save_file(fname, self.pic_suffix, pic)
        self.print(" && ", end="")
        self.save_file(fname, self.vid_suffix, vid)
        self.print()

    def _open_and_split(self, fname):
        with open(fname, "rb+") as fil:
            file_map = mmap(fil.fileno(), 0)

            edge = self.get_edge(file_map)
            if edge < 0:
                return

            pic, vid = self.get_split_file_bytes(edge, file_map)
        return pic, vid

    def get_edge(self, file_map):
        edge = file_map.find(self.marker_len)
        if edge == -1:
            self.print(f"does not contain the marker `{self.marker}`")
        if edge + len(self.marker_len) == file_map.size():
            edge = -2
            self.print(f"contains no data after the `{self.marker}`")

        return edge

    @property
    def marker_len(self):
        return bytes(self.marker, "utf-8")

    def get_split_file_bytes(self, edge, file_map):
        pic = self.read_bytes(file_map, 0, edge + 2)
        vid = self.read_bytes(file_map, edge + len(self.marker_len), file_map.size())
        return pic, vid

    def read_bytes(self, file_map, start, up_to_num_bytes):
        file_map.seek(start)
        fbytes = file_map.read(up_to_num_bytes)
        return fbytes

    def save_file(self, fname_orig, suffix, fbytes):
        fname = f"{fname_orig}{suffix}"
        with open(fname, "wb") as fil:
            fil.write(fbytes)
            fsiz = len(fbytes) / self._megabyte
            self.print(f"{fname} [{fsiz:.2f} MB]", end="")

    def print(self, msg="", end=None):
        if not self.quiet:
            print(msg, end=end)


@click.command()
@click.option("-q", "--quiet", "quiet", is_flag=True, help="supress all output")
@click.option(
    "-m",
    "--marker",
    "marker",
    default="MotionPhoto_Data",
    show_default=True,
    help="The utf-8 encoded edge marker text. Default is for samsung motion photos",
)
@click.option(
    "--pic-suffix", "pic_suffix", default=".jpg", show_default=True, help="Suffix of the splitted picture file."
)
@click.option(
    "--vid-suffix", "vid_suffix", default=".mp4", show_default=True, help="Suffix of the splitted video file."
)
@click.argument("filenames", nargs=-1)
def split_the_motion_files(filenames, **kwargs):
    """Take list of filenames containing joined photo and video and split them in two separate files.

    Works for samsung motion photos by default - they contain "MotionPhoto_data" edge marker - but any other marker text can be passed.

    CARE: If you set empty string as the file suffix, the original file gets overwritten!
    """
    spl = Splitter(**kwargs)
    for fname in filenames:
        spl.split(fname)


if __name__ == "__main__":
    split_the_motion_files()  # noqa
