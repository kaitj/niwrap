# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_SETUP_GROUP_IN_CORR_METADATA = Metadata(
    id="de29e68b50548580e79210d656042b141dbd77c7.boutiques",
    name="3dSetupGroupInCorr",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dSetupGroupInCorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_setup_group_in_corr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    niml_file: OutputPathType
    """Text file containing the header information describing the data file."""
    data_file: OutputPathType
    """Data file containing all the time series from all the datasets."""


def v_3d_setup_group_in_corr(
    datasets: list[InputPathType],
    prefix: str,
    mask_dataset: InputPathType | None = None,
    short_flag: bool = False,
    byte_flag: bool = False,
    labels_file: InputPathType | None = None,
    delete_flag: bool = False,
    prep_method: str | None = None,
    lr_pairs: list[str] | None = None,
    runner: Runner | None = None,
) -> V3dSetupGroupInCorrOutputs:
    """
    Pre-process a collection of AFNI 3D+time datasets for use with Group InstaCorr.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        datasets: AFNI 3D+time datasets to be processed.
        prefix: Prefix for output dataset names.
        mask_dataset: Mask dataset for voxel selection.
        short_flag: Store data as 16-bit shorts.
        byte_flag: Store data as 8-bit bytes.
        labels_file: File containing a list of labels for each dataset.
        delete_flag: Delete input datasets from disk after processing.
        prep_method: Preprocess each data time series with the specified\
            method.
        lr_pairs: Set the domains for left and right hemisphere surfaces and\
            indicate that the datasets are arranged in (Left, Right) pairs.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSetupGroupInCorrOutputs`).
    """
    if lr_pairs is not None and not (len(lr_pairs) <= 2): 
        raise ValueError(f"Length of 'lr_pairs' must be less than 2 but was {len(lr_pairs)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SETUP_GROUP_IN_CORR_METADATA)
    cargs = []
    cargs.append("3dSetupGroupInCorr")
    cargs.extend([execution.input_file(f) for f in datasets])
    if mask_dataset is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask_dataset)
        ])
    cargs.extend([
        "-prefix",
        prefix
    ])
    if short_flag:
        cargs.append("-short")
    if byte_flag:
        cargs.append("-byte")
    if labels_file is not None:
        cargs.extend([
            "-labels",
            execution.input_file(labels_file)
        ])
    if delete_flag:
        cargs.append("-DELETE")
    if prep_method is not None:
        cargs.extend([
            "-prep",
            prep_method
        ])
    if lr_pairs is not None:
        cargs.extend([
            "-LRpairs",
            *lr_pairs
        ])
    ret = V3dSetupGroupInCorrOutputs(
        root=execution.output_file("."),
        niml_file=execution.output_file(prefix + ".grpincorr.niml"),
        data_file=execution.output_file(prefix + ".grpincorr.data"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dSetupGroupInCorrOutputs",
    "V_3D_SETUP_GROUP_IN_CORR_METADATA",
    "v_3d_setup_group_in_corr",
]
