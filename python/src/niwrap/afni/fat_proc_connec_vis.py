# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FAT_PROC_CONNEC_VIS_METADATA = Metadata(
    id="b957960c6032ddd4be1b636c4e8b5e9afa55420b",
    name="fat_proc_connec_vis",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class FatProcConnecVisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_connec_vis(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cmd_txt: OutputPathType
    """Command text file output"""
    tcat_file: OutputPathType
    """Concatenated ROI masks multibrick file from the -output_tcat flag"""
    tstat_file: OutputPathType
    """Single brick file from 3dTstat operation on the tcat dataset, produced by the -output_tstat flag"""


def fat_proc_connec_vis(
    in_rois: str,
    prefix: str,
    prefix_file: str | None = None,
    tsmoo_kpb: float | int | None = None,
    tsmoo_niter: float | int | None = None,
    iso_opt: str | None = None,
    trackid_no_or: bool = False,
    output_tcat: bool = False,
    output_tstat: bool = False,
    wdir: str | None = None,
    no_clean: bool = False,
    runner: Runner | None = None,
) -> FatProcConnecVisOutputs:
    """
    fat_proc_connec_vis by AFNI Team.
    
    This program is for visualizing the volumetric output of tracking, mainly
    for the '-dump_rois ...' from 3dTrackID. It creates surface-ized views of
    the separate white matter connection maps (WMCs) which can be viewed
    simultaneously in 3D with SUMA.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/fat_proc_connec_vis.html
    
    Args:
        in_rois: List of separate files, each with a single ROI volume mask;\
            can include wildcards, etc. to specify the list.
        prefix: Directory to contain the output files: *cmd.txt and surface\
            files such as *.gii and *.niml.dset; the namebase of files within this\
            directory will be the default for the program, 'wmc'. The value PPP can\
            contain parts of a path in it.
        prefix_file: Prefix for the output files: *cmd.txt and surface files\
            such as *.gii and *.niml.dset; can include path steps; and can make one\
            level of a new directory. For example, if FFF were 'A/B', then the\
            program could make a new directory called 'A' if it didn't exist\
            already and populate it with individual files having the same prefix\
            'B'.
        tsmoo_kpb: 'KPB' parameter in IsoSurface program; default value is\
            0.01.
        tsmoo_niter: 'NITER' parameter in IsoSurface program; default value is\
            6.
        iso_opt: Input one of the 'iso* options' from IsoSurface program, such\
            as 'isorois+dsets', 'mergerois', etc. Quotations around the entry may\
            be needed, especially if something like the '-mergerois [LAB_OUT]'\
            route is being followed. Default: isorois+dsets.
        trackid_no_or: Use this option to have the program recognize the naming\
            convention of 3dTrackID output and to ignore the OR-logic ROIs,\
            including only the AND-logic (AKA pairwise) connections.
        output_tcat: Flag to output the multibrick file of concatenated ROI\
            masks; note that the [0]th brick will be all zeros (it is just a\
            placeholder). So, if there are N ROI maps concatenated, there will be\
            N+1 bricks in the output dataset, which has the name PPP_tcat.nii.gz.
        output_tstat: Flag to output the single brick file from the 3dTstat\
            operation on the tcat dataset. If there were N ROI maps concatenated,\
            then the largest value should be N. The output file's name will be\
            PPP_tstat.nii.gz.
        wdir: Working directory prefix. The format is '__WDIR_connec_vis_PPP',\
            where PPP is the input prefix.
        no_clean: Optional switch to NOT remove the working directory (default\
            is to remove the working directory).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcConnecVisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_CONNEC_VIS_METADATA)
    cargs = []
    cargs.append("fat_proc_connec_vis")
    cargs.append("-in_rois")
    cargs.append(in_rois)
    cargs.append("-prefix")
    cargs.append(prefix)
    cargs.append("[--prefix_file")
    cargs.append("FFF]")
    cargs.append("[--tsmoo_kpb")
    cargs.append("KPB]")
    cargs.append("[--tsmoo_niter")
    cargs.append("NITER]")
    cargs.append("[--iso_opt")
    cargs.append("ISO_OPT]")
    cargs.append("[--trackid_no_or]")
    cargs.append("[--output_tcat]")
    cargs.append("[--output_tstat]")
    cargs.append("[--wdir")
    cargs.append("WWW]")
    cargs.append("[--no_clean]")
    ret = FatProcConnecVisOutputs(
        root=execution.output_file("."),
        cmd_txt=execution.output_file(f"{prefix}_cmd.txt", optional=True),
        tcat_file=execution.output_file(f"{prefix}_tcat.nii.gz", optional=True),
        tstat_file=execution.output_file(f"{prefix}_tstat.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAT_PROC_CONNEC_VIS_METADATA",
    "FatProcConnecVisOutputs",
    "fat_proc_connec_vis",
]