# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_NET_CORR_METADATA = Metadata(
    id="5990317130f7d840690ce681e6279ce513c9b810.boutiques",
    name="3dNetCorr",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dNetCorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_net_corr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_netcc: OutputPathType
    """Output correlation matrix file for network 000"""
    output_netts: OutputPathType
    """Output mean time series per ROI for network 000"""
    output_niml: OutputPathType
    """NIML/SUMA-esque file for visualizing connectivity info in a 3D brain for
    network 000"""
    output_roidat: OutputPathType
    """Columns contain information for each ROI in the used mask."""
    output_mask_nnull: OutputPathType
    """Mask of non-null time series"""
    output_indiv: OutputPathType
    """Directory containing individual time series files for network 000"""
    output_binary_mask_nnull: OutputPathType
    """Binary mask of the non-null time series"""


def v_3d_net_corr(
    prefix: str,
    inset: InputPathType,
    in_rois: InputPathType,
    mask: InputPathType | None = None,
    fish_z: bool = False,
    part_corr: bool = False,
    ts_out: bool = False,
    ts_label: bool = False,
    ts_indiv: bool = False,
    ts_wb_corr: bool = False,
    ts_wb_z: bool = False,
    weight_ts: InputPathType | None = None,
    weight_corr: InputPathType | None = None,
    ts_wb_strlabel: bool = False,
    nifti: bool = False,
    output_mask_nonnull: bool = False,
    push_thru_many_zeros: bool = False,
    allow_roi_zeros: bool = False,
    automask_off: bool = False,
    ignore_lt: bool = False,
    runner: Runner | None = None,
) -> V3dNetCorrOutputs:
    """
    Compute correlation matrix of a set of ROIs based on mean time series.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dNetCorr.html
    
    Args:
        prefix: Output file name prefix.
        inset: Time series file (4D data set).
        in_rois: Input a set of ROIs each labelled with distinct integers.\
            Multiple subbricks can be input, each will be treated as a separate\
            network.
        mask: Whole brain mask within which to calculate correlation.
        fish_z: Output Fisher Z-transform matrix along with correlation matrix.
        part_corr: Output the partial correlation matrix.
        ts_out: Output the mean time series of the ROIs.
        ts_label: Insert the integer ROI label at the start of each line of the\
            *.netts file created.
        ts_indiv: Create a directory for each network that contains the average\
            time series for each ROI in individual files.
        ts_wb_corr: Perform whole brain correlation for each ROI's average time\
            series and output as Pearson 'r' values.
        ts_wb_z: Perform whole brain correlation for each ROI's average time\
            series and output as Fisher transformed Z-scores.
        weight_ts: Input a 1D file of weights to be applied multiplicatively to\
            each ROI's average time series.
        weight_corr: Input a 1D file of weights to estimate a weighted Pearson\
            Correlation.
        ts_wb_strlabel: Apply string labels to the WB correlation/Z-score\
            output files.
        nifti: Output any correlation map files as NIFTI files.
        output_mask_nonnull: Output mask of non-null time series.
        push_thru_many_zeros: Push through the calculation even if any ROI\
            contains more than 10 percent of voxels with null time series.
        allow_roi_zeros: Allow ROIs to have all-zero time series.
        automask_off: Disable internal automasking of where time series are not\
            uniformly zero.
        ignore_lt: Ignore any label table labels in the '-in_rois' file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dNetCorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_NET_CORR_METADATA)
    cargs = []
    cargs.append("3dNetCorr")
    cargs.append(prefix)
    cargs.append(execution.input_file(inset))
    cargs.append(execution.input_file(in_rois))
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if fish_z:
        cargs.append("-fish_z")
    if part_corr:
        cargs.append("-part_corr")
    if ts_out:
        cargs.append("-ts_out")
    if ts_label:
        cargs.append("-ts_label")
    if ts_indiv:
        cargs.append("-ts_indiv")
    if ts_wb_corr:
        cargs.append("-ts_wb_corr")
    if ts_wb_z:
        cargs.append("-ts_wb_Z")
    if weight_ts is not None:
        cargs.extend([
            "-weight_ts",
            execution.input_file(weight_ts)
        ])
    if weight_corr is not None:
        cargs.extend([
            "-weight_corr",
            execution.input_file(weight_corr)
        ])
    if ts_wb_strlabel:
        cargs.append("-ts_wb_strlabel")
    if nifti:
        cargs.append("-nifti")
    if output_mask_nonnull:
        cargs.append("-output_mask_nonnull")
    if push_thru_many_zeros:
        cargs.append("-push_thru_many_zeros")
    if allow_roi_zeros:
        cargs.append("-allow_roi_zeros")
    if automask_off:
        cargs.append("-automask_off")
    if ignore_lt:
        cargs.append("-ignore_LT")
    ret = V3dNetCorrOutputs(
        root=execution.output_file("."),
        output_netcc=execution.output_file(prefix + "_000.netcc"),
        output_netts=execution.output_file(prefix + "_000.netts"),
        output_niml=execution.output_file(prefix + "_000.niml.dset"),
        output_roidat=execution.output_file(prefix + ".roidat"),
        output_mask_nnull=execution.output_file(prefix + "_mask_nnull"),
        output_indiv=execution.output_file(prefix + "_000_INDIV"),
        output_binary_mask_nnull=execution.output_file("PREFIX_mask_nnull"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dNetCorrOutputs",
    "V_3D_NET_CORR_METADATA",
    "v_3d_net_corr",
]
