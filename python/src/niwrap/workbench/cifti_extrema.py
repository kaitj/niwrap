# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_EXTREMA_METADATA = Metadata(
    id="e2347f8f12544ea1ca555953aad610c37be719f5.boutiques",
    name="cifti-extrema",
    package="workbench",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiExtremaThreshold:
    """
    ignore small extrema.
    """
    low: float
    """the largest value to consider for being a minimum"""
    high: float
    """the smallest value to consider for being a maximum"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-threshold")
        cargs.append(str(self.low))
        cargs.append(str(self.high))
        return cargs


class CiftiExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_extrema(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti"""


def cifti_extrema(
    cifti: InputPathType,
    surface_distance: float,
    volume_distance: float,
    direction: str,
    cifti_out: str,
    opt_left_surface_surface: InputPathType | None = None,
    opt_right_surface_surface: InputPathType | None = None,
    opt_cerebellum_surface_surface: InputPathType | None = None,
    opt_surface_presmooth_surface_kernel: float | None = None,
    opt_volume_presmooth_volume_kernel: float | None = None,
    opt_presmooth_fwhm: bool = False,
    threshold: CiftiExtremaThreshold | None = None,
    opt_merged_volume: bool = False,
    opt_sum_maps: bool = False,
    opt_consolidate_mode: bool = False,
    opt_only_maxima: bool = False,
    opt_only_minima: bool = False,
    runner: Runner | None = None,
) -> CiftiExtremaOutputs:
    """
    Find extrema in a cifti file.
    
    Finds spatial locations in a cifti file that have more extreme values than
    all nearby locations in the same component (surface or volume structure).
    The input cifti file must have a brain models mapping along the specified
    direction. COLUMN is the direction that works on dtseries and dscalar. For
    dconn, if it is symmetric use COLUMN, otherwise use ROW.
    
    Author: Washington University School of Medicin
    
    Args:
        cifti: the input cifti.
        surface_distance: the minimum distance between extrema of the same\
            type, for surface components.
        volume_distance: the minimum distance between extrema of the same type,\
            for volume components.
        direction: which dimension to find extrema along, ROW or COLUMN.
        cifti_out: the output cifti.
        opt_left_surface_surface: specify the left surface to use: the left\
            surface file.
        opt_right_surface_surface: specify the right surface to use: the right\
            surface file.
        opt_cerebellum_surface_surface: specify the cerebellum surface to use:\
            the cerebellum surface file.
        opt_surface_presmooth_surface_kernel: smooth on the surface before\
            finding extrema: the size of the gaussian surface smoothing kernel in\
            mm, as sigma by default.
        opt_volume_presmooth_volume_kernel: smooth volume components before\
            finding extrema: the size of the gaussian volume smoothing kernel in\
            mm, as sigma by default.
        opt_presmooth_fwhm: smoothing kernel distances are FWHM, not sigma.
        threshold: ignore small extrema.
        opt_merged_volume: treat volume components as if they were a single\
            component.
        opt_sum_maps: output the sum of the extrema maps instead of each map\
            separately.
        opt_consolidate_mode: use consolidation of local minima instead of a\
            large neighborhood.
        opt_only_maxima: only find the maxima.
        opt_only_minima: only find the minima.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiExtremaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_EXTREMA_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-extrema")
    cargs.append(execution.input_file(cifti))
    cargs.append(str(surface_distance))
    cargs.append(str(volume_distance))
    cargs.append(direction)
    cargs.append(cifti_out)
    if opt_left_surface_surface is not None:
        cargs.extend([
            "-left-surface",
            execution.input_file(opt_left_surface_surface)
        ])
    if opt_right_surface_surface is not None:
        cargs.extend([
            "-right-surface",
            execution.input_file(opt_right_surface_surface)
        ])
    if opt_cerebellum_surface_surface is not None:
        cargs.extend([
            "-cerebellum-surface",
            execution.input_file(opt_cerebellum_surface_surface)
        ])
    if opt_surface_presmooth_surface_kernel is not None:
        cargs.extend([
            "-surface-presmooth",
            str(opt_surface_presmooth_surface_kernel)
        ])
    if opt_volume_presmooth_volume_kernel is not None:
        cargs.extend([
            "-volume-presmooth",
            str(opt_volume_presmooth_volume_kernel)
        ])
    if opt_presmooth_fwhm:
        cargs.append("-presmooth-fwhm")
    if threshold is not None:
        cargs.extend(threshold.run(execution))
    if opt_merged_volume:
        cargs.append("-merged-volume")
    if opt_sum_maps:
        cargs.append("-sum-maps")
    if opt_consolidate_mode:
        cargs.append("-consolidate-mode")
    if opt_only_maxima:
        cargs.append("-only-maxima")
    if opt_only_minima:
        cargs.append("-only-minima")
    ret = CiftiExtremaOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(cifti_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_EXTREMA_METADATA",
    "CiftiExtremaOutputs",
    "CiftiExtremaThreshold",
    "cifti_extrema",
]
