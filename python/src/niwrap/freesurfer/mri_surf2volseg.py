# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_SURF2VOLSEG_METADATA = Metadata(
    id="5311f8712d7d6a5ffead8a7275ff29df715e3532.boutiques",
    name="mri_surf2volseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriSurf2volsegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_surf2volseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_surf2volseg(
    input_segmentation: InputPathType | None = None,
    output_segmentation: str | None = None,
    source_segmentation: InputPathType | None = None,
    lh_white_surf: InputPathType | None = None,
    lh_pial_surf: InputPathType | None = None,
    rh_white_surf: InputPathType | None = None,
    rh_pial_surf: InputPathType | None = None,
    lh_cortex_mask: InputPathType | None = None,
    rh_cortex_mask: InputPathType | None = None,
    fix_presurf_ribbon: InputPathType | None = None,
    label_cortex: bool = False,
    label_wm: bool = False,
    label_wm_unknown: list[float] | None = None,
    lh_annotation: InputPathType | None = None,
    rh_annotation: InputPathType | None = None,
    wmparc_dmax: float | None = None,
    rip_unknown: bool = False,
    hypo_as_wm: bool = False,
    hashres: float | None = None,
    nhops: float | None = None,
    help_flag: bool = False,
    version_flag: bool = False,
    crs_test: list[float] | None = None,
    ctab_file: InputPathType | None = None,
    threads_number: float | None = None,
    runner: Runner | None = None,
) -> MriSurf2volsegOutputs:
    """
    Tool that cleans up presurf aseg cortex and WM, maps cortical labels from an
    annotation into a volume, and labels cerebral WM with closest cortical label.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_segmentation: Full path of input segmentation.
        output_segmentation: Output segmentation file.
        source_segmentation: Source subcortical volume segmentation file\
            (instead of using subcortical segs in input segmentation).
        lh_white_surf: White surface for left hemisphere.
        lh_pial_surf: Pial surface for left hemisphere.
        rh_white_surf: White surface for right hemisphere.
        rh_pial_surf: Pial surface for right hemisphere.
        lh_cortex_mask: Mask for left hemisphere cortex (usually\
            lh.cortex.label).
        rh_cortex_mask: Mask for right hemisphere cortex (usually\
            rh.cortex.label).
        fix_presurf_ribbon: Fix the cortical and WM labels in the input\
            segmentation using ribbon file.
        label_cortex: Relabel cortex in the input segmentation with surface\
            annotation.
        label_wm: Relabel cerebral WM in the input segmentation with surface\
            annotation.
        label_wm_unknown: Relabel unknown WM as lhval and rhval (default is\
            5001 and 5002).
        lh_annotation: Left hemisphere annotation for --label-cortex and\
            --label-wm.
        rh_annotation: Right hemisphere annotation for --label-cortex and\
            --label-wm.
        wmparc_dmax: Max distance (mm) from cortex to be labeled as gyral WM.
        rip_unknown: Do not label WM based on 'unknown' cortical label.
        hypo_as_wm: Label hypointensities as WM (when fixing with ribbon).
        hashres: Surface hash table resolution.
        nhops: Number of surface hops when searching for a nearby annotation.
        help_flag: Print out information on how to use this program.
        version_flag: Print out version and exit.
        crs_test: Test labeling of only the voxel given by column, row, slice\
            (debugging).
        ctab_file: Embed color table in the output.
        threads_number: Run in parallel with the specified number of threads.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSurf2volsegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SURF2VOLSEG_METADATA)
    cargs = []
    cargs.append("mri_surf2volseg")
    if input_segmentation is not None:
        cargs.extend([
            "--i",
            execution.input_file(input_segmentation)
        ])
    if output_segmentation is not None:
        cargs.extend([
            "--o",
            output_segmentation
        ])
    if source_segmentation is not None:
        cargs.extend([
            "--src",
            execution.input_file(source_segmentation)
        ])
    if lh_white_surf is not None:
        cargs.extend([
            "--lh-white",
            execution.input_file(lh_white_surf)
        ])
    if lh_pial_surf is not None:
        cargs.extend([
            "--lh-pial",
            execution.input_file(lh_pial_surf)
        ])
    if rh_white_surf is not None:
        cargs.extend([
            "--rh-white",
            execution.input_file(rh_white_surf)
        ])
    if rh_pial_surf is not None:
        cargs.extend([
            "--rh-pial",
            execution.input_file(rh_pial_surf)
        ])
    if lh_cortex_mask is not None:
        cargs.extend([
            "--lh-cortex-mask",
            execution.input_file(lh_cortex_mask)
        ])
    if rh_cortex_mask is not None:
        cargs.extend([
            "--rh-cortex-mask",
            execution.input_file(rh_cortex_mask)
        ])
    if fix_presurf_ribbon is not None:
        cargs.extend([
            "--fix-presurf-with-ribbon",
            execution.input_file(fix_presurf_ribbon)
        ])
    if label_cortex:
        cargs.append("--label-cortex")
    if label_wm:
        cargs.append("--label-wm")
    if label_wm_unknown is not None:
        cargs.extend([
            "--label-wm-unknown",
            *map(str, label_wm_unknown)
        ])
    if lh_annotation is not None:
        cargs.extend([
            "--lh-annot",
            execution.input_file(lh_annotation)
        ])
    if rh_annotation is not None:
        cargs.extend([
            "--rh-annot",
            execution.input_file(rh_annotation)
        ])
    if wmparc_dmax is not None:
        cargs.extend([
            "--wmparc-dmax",
            str(wmparc_dmax)
        ])
    if rip_unknown:
        cargs.append("--rip-unknown")
    if hypo_as_wm:
        cargs.append("--hypo-as-wm")
    if hashres is not None:
        cargs.extend([
            "--hashres",
            str(hashres)
        ])
    if nhops is not None:
        cargs.extend([
            "--nhops",
            str(nhops)
        ])
    if help_flag:
        cargs.append("--help")
    if version_flag:
        cargs.append("--version")
    if crs_test is not None:
        cargs.extend([
            "--crs-test",
            *map(str, crs_test)
        ])
    if ctab_file is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(ctab_file)
        ])
    if threads_number is not None:
        cargs.extend([
            "--threads",
            str(threads_number)
        ])
    ret = MriSurf2volsegOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_SURF2VOLSEG_METADATA",
    "MriSurf2volsegOutputs",
    "mri_surf2volseg",
]
