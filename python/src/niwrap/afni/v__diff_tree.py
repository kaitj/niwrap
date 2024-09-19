# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__DIFF_TREE_METADATA = Metadata(
    id="3dbe2eca541263b5786d164d13244368f1041377.boutiques",
    name="@diff.tree",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VDiffTreeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__diff_tree(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__diff_tree(
    new_dir: str,
    old_dir: str,
    diff_opts: str | None = None,
    ignore_append: str | None = None,
    ia: str | None = None,
    ignore_list: str | None = None,
    il: str | None = None,
    ignore_missing: bool = False,
    no_diffs: bool = False,
    quiet: bool = False,
    save: bool = False,
    show: bool = False,
    show_list_comp: bool = False,
    skip_data: bool = False,
    verb: str | None = None,
    diff_prog: str | None = None,
    xxdiff: bool = False,
    x_option: bool = False,
    runner: Runner | None = None,
) -> VDiffTreeOutputs:
    """
    Show file differences between 2 directories.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@diff.tree.html
    
    Args:
        new_dir: New directory to compare.
        old_dir: Old directory to compare.
        diff_opts: Apply OPTS as options in diff commands.
        ignore_append: Append to ignore_list (list in quotes).
        ia: Short for -ignore_append.
        ignore_list: Create new ignore_list (list in quotes).
        il: Short for -ignore_list.
        ignore_missing: Only compare overlapping files, if different files,\
            fail.
        no_diffs: Only compare existence of files.
        quiet: Only list files with diffs.
        save: Save actual file differences (txt and pdf).
        show: Show actual file differences.
        show_list_comp: Show any pairwise differences in file lists (terminate\
            after showing comparison).
        skip_data: Skip binary diff of select data files (.BRIK, .dcm,\
            .BRIK.gz).
        verb: Set verbosity level (0,1,2) (default 1).
        diff_prog: Use PROG to show diffs (e.g. xxdiff, meld).
        xxdiff: Use xxdiff to show diffs.
        x_option: Implies -xxdiff -ignore_missing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDiffTreeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DIFF_TREE_METADATA)
    cargs = []
    cargs.append("@diff.tree")
    cargs.append(new_dir)
    cargs.append(old_dir)
    if diff_opts is not None:
        cargs.extend([
            "-diff_opts",
            diff_opts
        ])
    if ignore_append is not None:
        cargs.extend([
            "-ignore_append",
            ignore_append
        ])
    if ia is not None:
        cargs.extend([
            "-ia",
            ia
        ])
    if ignore_list is not None:
        cargs.extend([
            "-ignore_list",
            ignore_list
        ])
    if il is not None:
        cargs.extend([
            "-il",
            il
        ])
    if ignore_missing:
        cargs.append("-ignore_missing")
    if no_diffs:
        cargs.append("-no_diffs")
    if quiet:
        cargs.append("-quiet")
    if save:
        cargs.append("-save")
    if show:
        cargs.append("-show")
    if show_list_comp:
        cargs.append("-show_list_comp")
    if skip_data:
        cargs.append("-skip_data")
    if verb is not None:
        cargs.extend([
            "-verb",
            verb
        ])
    if diff_prog is not None:
        cargs.extend([
            "-diff_prog",
            diff_prog
        ])
    if xxdiff:
        cargs.append("-xxdiff")
    if x_option:
        cargs.append("-X")
    ret = VDiffTreeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VDiffTreeOutputs",
    "V__DIFF_TREE_METADATA",
    "v__diff_tree",
]
