# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LABEL_RESAMPLE_METADATA = Metadata(
    id="c0e9d5a876a0eec10684433606b4697acea320b1.boutiques",
    name="label-resample",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class LabelResampleAreaSurfs:
    """
    specify surfaces to do vertex area correction based on.
    """
    current_area: InputPathType
    """a relevant anatomical surface with <current-sphere> mesh"""
    new_area: InputPathType
    """a relevant anatomical surface with <new-sphere> mesh"""
    
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
        cargs.append("-area-surfs")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class LabelResampleAreaMetrics:
    """
    specify vertex area metrics to do area correction based on.
    """
    current_area: InputPathType
    """a metric file with vertex areas for <current-sphere> mesh"""
    new_area: InputPathType
    """a metric file with vertex areas for <new-sphere> mesh"""
    
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
        cargs.append("-area-metrics")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


class LabelResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label file"""
    opt_valid_roi_out_roi_out: OutputPathType | None
    """output the ROI of vertices that got data from valid source vertices: the
    output roi as a metric"""


def label_resample(
    label_in: InputPathType,
    current_sphere: InputPathType,
    new_sphere: InputPathType,
    method: str,
    label_out: str,
    area_surfs: LabelResampleAreaSurfs | None = None,
    area_metrics: LabelResampleAreaMetrics | None = None,
    opt_current_roi_roi_metric: InputPathType | None = None,
    opt_valid_roi_out_roi_out: str | None = None,
    opt_largest: bool = False,
    opt_bypass_sphere_check: bool = False,
    runner: Runner | None = None,
) -> LabelResampleOutputs:
    """
    Resample a label file to a different mesh.
    
    Resamples a label file, given two spherical surfaces that are in register.
    If ADAP_BARY_AREA is used, exactly one of -area-surfs or -area-metrics must
    be specified.
    
    The ADAP_BARY_AREA method is recommended for label data, because it should
    be better at resolving vertices that are near multiple labels, or in case of
    downsampling. Midthickness surfaces are recommended for the vertex areas for
    most data.
    
    The -largest option results in nearest vertex behavior when used with
    BARYCENTRIC, as it uses the value of the source vertex that has the largest
    weight.
    
    When -largest is not specified, the vertex weights are summed according to
    which label they correspond to, and the label with the largest sum is used.
    
    The <method> argument must be one of the following:
    
    ADAP_BARY_AREA
    BARYCENTRIC
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_in: the label file to resample.
        current_sphere: a sphere surface with the mesh that the label file is\
            currently on.
        new_sphere: a sphere surface that is in register with <current-sphere>\
            and has the desired output mesh.
        method: the method name.
        label_out: the output label file.
        area_surfs: specify surfaces to do vertex area correction based on.
        area_metrics: specify vertex area metrics to do area correction based\
            on.
        opt_current_roi_roi_metric: use an input roi on the current mesh to\
            exclude non-data vertices: the roi, as a metric file.
        opt_valid_roi_out_roi_out: output the ROI of vertices that got data\
            from valid source vertices: the output roi as a metric.
        opt_largest: use only the label of the vertex with the largest weight.
        opt_bypass_sphere_check: ADVANCED: allow the current and new 'spheres'\
            to have arbitrary shape as long as they follow the same contour.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_RESAMPLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-resample")
    cargs.append(execution.input_file(label_in))
    cargs.append(execution.input_file(current_sphere))
    cargs.append(execution.input_file(new_sphere))
    cargs.append(method)
    cargs.append(label_out)
    if area_surfs is not None:
        cargs.extend(area_surfs.run(execution))
    if area_metrics is not None:
        cargs.extend(area_metrics.run(execution))
    if opt_current_roi_roi_metric is not None:
        cargs.extend([
            "-current-roi",
            execution.input_file(opt_current_roi_roi_metric)
        ])
    if opt_valid_roi_out_roi_out is not None:
        cargs.extend([
            "-valid-roi-out",
            opt_valid_roi_out_roi_out
        ])
    if opt_largest:
        cargs.append("-largest")
    if opt_bypass_sphere_check:
        cargs.append("-bypass-sphere-check")
    ret = LabelResampleOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(label_out),
        opt_valid_roi_out_roi_out=execution.output_file(opt_valid_roi_out_roi_out) if (opt_valid_roi_out_roi_out is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL_RESAMPLE_METADATA",
    "LabelResampleAreaMetrics",
    "LabelResampleAreaSurfs",
    "LabelResampleOutputs",
    "label_resample",
]
