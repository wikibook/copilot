import shutil
import filecmp
import os


def get_good_filename(fname):
    """
    fname is the name of a png file.

    While the file fname exists, add an _ character
    right before the .png part of the filename;
    e.g. 9595.png becomes 9595_.png.

    Return the resulting filename.
    """
    while os.path.exists(fname):
        fname = fname.replace(".png", "_.png")
    return fname


def make_copy(fname, target_dir):
    """
    fname is a filename like pictures1/1262.png.
    target_dir is the name of a directory.

    Compare the file fname to all files in target_dir.
    If fname is not identical to any file in target_dir, copy it to target_dir
    """
    for target_fname in os.listdir(target_dir):
        if filecmp.cmp(fname, os.path.join(target_dir, target_fname)):
            return
    shutil.copy(
        fname, get_good_filename(os.path.join(target_dir, os.path.basename(fname)))
    )


def make_copies(dirs, target_dir):
    """
    dirs is a list of directory names.
    target_dir is the name of a directory.

    Check each file in the directories and compare it to all files in target_dir.
    If a file is not identical to any file in target_dir, copy it to target_dir
    """
    for dir in dirs:
        for fname in os.listdir(dir):
            make_copy(os.path.join(dir, fname), target_dir)


make_copies(["pictures1", "pictures2"], "pictures_combined")
