# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_RESAMPLE_DCONN_MEMORY_METADATA = Metadata(
    id="6897a244659820e737362b7b9d26217d4c4a2122.boutiques",
    name="cifti-resample-dconn-memory",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class CiftiResampleDconnMemoryWeighted:
    """
    use weighted dilation (default).
    """
    opt_exponent_exponent: float | None = None
    """specify exponent in weighting function: exponent 'n' to use in (1 /
    (distance ^ n)) as the weighting function (default 7)"""
    opt_legacy_cutoff: bool = False
    """use v1.3.2 logic for the kernel cutoff"""
    
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
        cargs.append("-weighted")
        if self.opt_exponent_exponent is not None:
            cargs.extend([
                "-exponent",
                str(self.opt_exponent_exponent)
            ])
        if self.opt_legacy_cutoff:
            cargs.append("-legacy-cutoff")
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryVolumePredilate:
    """
    dilate the volume components before resampling.
    """
    dilate_mm: float
    """distance, in mm, to dilate"""
    opt_nearest: bool = False
    """use nearest value dilation"""
    weighted: CiftiResampleDconnMemoryWeighted | None = None
    """use weighted dilation (default)"""
    
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
        cargs.append("-volume-predilate")
        cargs.append(str(self.dilate_mm))
        if self.opt_nearest:
            cargs.append("-nearest")
        if self.weighted is not None:
            cargs.extend(self.weighted.run(execution))
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryWeighted_:
    """
    use weighted dilation (default).
    """
    opt_exponent_exponent: float | None = None
    """specify exponent in weighting function: exponent 'n' to use in (area /
    (distance ^ n)) as the weighting function (default 6)"""
    opt_legacy_cutoff: bool = False
    """use v1.3.2 logic for the kernel cutoff"""
    
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
        cargs.append("-weighted")
        if self.opt_exponent_exponent is not None:
            cargs.extend([
                "-exponent",
                str(self.opt_exponent_exponent)
            ])
        if self.opt_legacy_cutoff:
            cargs.append("-legacy-cutoff")
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemorySurfacePostdilate:
    """
    dilate the surface components after resampling.
    """
    dilate_mm: float
    """distance, in mm, to dilate"""
    opt_nearest: bool = False
    """use nearest value dilation"""
    opt_linear: bool = False
    """use linear dilation"""
    weighted: CiftiResampleDconnMemoryWeighted_ | None = None
    """use weighted dilation (default)"""
    
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
        cargs.append("-surface-postdilate")
        cargs.append(str(self.dilate_mm))
        if self.opt_nearest:
            cargs.append("-nearest")
        if self.opt_linear:
            cargs.append("-linear")
        if self.weighted is not None:
            cargs.extend(self.weighted.run(execution))
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryFlirt:
    """
    MUST be used if affine is a flirt affine.
    """
    source_volume: str
    """the source volume used when generating the affine"""
    target_volume: str
    """the target volume used when generating the affine"""
    
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
        cargs.append("-flirt")
        cargs.append(self.source_volume)
        cargs.append(self.target_volume)
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryAffine:
    """
    use an affine transformation on the volume components.
    """
    affine_file: str
    """the affine file to use"""
    flirt: CiftiResampleDconnMemoryFlirt | None = None
    """MUST be used if affine is a flirt affine"""
    
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
        cargs.append("-affine")
        cargs.append(self.affine_file)
        if self.flirt is not None:
            cargs.extend(self.flirt.run(execution))
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryWarpfield:
    """
    use a warpfield on the volume components.
    """
    warpfield: str
    """the warpfield to use"""
    opt_fnirt_source_volume: str | None = None
    """MUST be used if using a fnirt warpfield: the source volume used when
    generating the warpfield"""
    
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
        cargs.append("-warpfield")
        cargs.append(self.warpfield)
        if self.opt_fnirt_source_volume is not None:
            cargs.extend([
                "-fnirt",
                self.opt_fnirt_source_volume
            ])
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryLeftAreaSurfs:
    """
    specify left surfaces to do vertex area correction based on.
    """
    current_area: InputPathType
    """a relevant left anatomical surface with current mesh"""
    new_area: InputPathType
    """a relevant left anatomical surface with new mesh"""
    
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
        cargs.append("-left-area-surfs")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryLeftAreaMetrics:
    """
    specify left vertex area metrics to do area correction based on.
    """
    current_area: InputPathType
    """a metric file with vertex areas for the current mesh"""
    new_area: InputPathType
    """a metric file with vertex areas for the new mesh"""
    
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
        cargs.append("-left-area-metrics")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryLeftSpheres:
    """
    specify spheres for left surface resampling.
    """
    current_sphere: InputPathType
    """a sphere with the same mesh as the current left surface"""
    new_sphere: InputPathType
    """a sphere with the new left mesh that is in register with the current
    sphere"""
    left_area_surfs: CiftiResampleDconnMemoryLeftAreaSurfs | None = None
    """specify left surfaces to do vertex area correction based on"""
    left_area_metrics: CiftiResampleDconnMemoryLeftAreaMetrics | None = None
    """specify left vertex area metrics to do area correction based on"""
    
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
        cargs.append("-left-spheres")
        cargs.append(execution.input_file(self.current_sphere))
        cargs.append(execution.input_file(self.new_sphere))
        if self.left_area_surfs is not None:
            cargs.extend(self.left_area_surfs.run(execution))
        if self.left_area_metrics is not None:
            cargs.extend(self.left_area_metrics.run(execution))
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryRightAreaSurfs:
    """
    specify right surfaces to do vertex area correction based on.
    """
    current_area: InputPathType
    """a relevant right anatomical surface with current mesh"""
    new_area: InputPathType
    """a relevant right anatomical surface with new mesh"""
    
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
        cargs.append("-right-area-surfs")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryRightAreaMetrics:
    """
    specify right vertex area metrics to do area correction based on.
    """
    current_area: InputPathType
    """a metric file with vertex areas for the current mesh"""
    new_area: InputPathType
    """a metric file with vertex areas for the new mesh"""
    
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
        cargs.append("-right-area-metrics")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryRightSpheres:
    """
    specify spheres for right surface resampling.
    """
    current_sphere: InputPathType
    """a sphere with the same mesh as the current right surface"""
    new_sphere: InputPathType
    """a sphere with the new right mesh that is in register with the current
    sphere"""
    right_area_surfs: CiftiResampleDconnMemoryRightAreaSurfs | None = None
    """specify right surfaces to do vertex area correction based on"""
    right_area_metrics: CiftiResampleDconnMemoryRightAreaMetrics | None = None
    """specify right vertex area metrics to do area correction based on"""
    
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
        cargs.append("-right-spheres")
        cargs.append(execution.input_file(self.current_sphere))
        cargs.append(execution.input_file(self.new_sphere))
        if self.right_area_surfs is not None:
            cargs.extend(self.right_area_surfs.run(execution))
        if self.right_area_metrics is not None:
            cargs.extend(self.right_area_metrics.run(execution))
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryCerebellumAreaSurfs:
    """
    specify cerebellum surfaces to do vertex area correction based on.
    """
    current_area: InputPathType
    """a relevant cerebellum anatomical surface with current mesh"""
    new_area: InputPathType
    """a relevant cerebellum anatomical surface with new mesh"""
    
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
        cargs.append("-cerebellum-area-surfs")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryCerebellumAreaMetrics:
    """
    specify cerebellum vertex area metrics to do area correction based on.
    """
    current_area: InputPathType
    """a metric file with vertex areas for the current mesh"""
    new_area: InputPathType
    """a metric file with vertex areas for the new mesh"""
    
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
        cargs.append("-cerebellum-area-metrics")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class CiftiResampleDconnMemoryCerebellumSpheres:
    """
    specify spheres for cerebellum surface resampling.
    """
    current_sphere: InputPathType
    """a sphere with the same mesh as the current cerebellum surface"""
    new_sphere: InputPathType
    """a sphere with the new cerebellum mesh that is in register with the
    current sphere"""
    cerebellum_area_surfs: CiftiResampleDconnMemoryCerebellumAreaSurfs | None = None
    """specify cerebellum surfaces to do vertex area correction based on"""
    cerebellum_area_metrics: CiftiResampleDconnMemoryCerebellumAreaMetrics | None = None
    """specify cerebellum vertex area metrics to do area correction based on"""
    
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
        cargs.append("-cerebellum-spheres")
        cargs.append(execution.input_file(self.current_sphere))
        cargs.append(execution.input_file(self.new_sphere))
        if self.cerebellum_area_surfs is not None:
            cargs.extend(self.cerebellum_area_surfs.run(execution))
        if self.cerebellum_area_metrics is not None:
            cargs.extend(self.cerebellum_area_metrics.run(execution))
        return cargs


class CiftiResampleDconnMemoryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_resample_dconn_memory(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_resample_dconn_memory(
    cifti_in: InputPathType,
    cifti_template: InputPathType,
    template_direction: str,
    surface_method: str,
    volume_method: str,
    cifti_out: str,
    opt_surface_largest: bool = False,
    volume_predilate: CiftiResampleDconnMemoryVolumePredilate | None = None,
    surface_postdilate: CiftiResampleDconnMemorySurfacePostdilate | None = None,
    affine: CiftiResampleDconnMemoryAffine | None = None,
    warpfield: CiftiResampleDconnMemoryWarpfield | None = None,
    left_spheres: CiftiResampleDconnMemoryLeftSpheres | None = None,
    right_spheres: CiftiResampleDconnMemoryRightSpheres | None = None,
    cerebellum_spheres: CiftiResampleDconnMemoryCerebellumSpheres | None = None,
    runner: Runner | None = None,
) -> CiftiResampleDconnMemoryOutputs:
    """
    Use lots of memory to resample dconn.
    
    This command does the same thing as running -cifti-resample twice, but uses
    memory up to approximately 2x the size that the intermediate file would be.
    This is because the intermediate dconn is kept in memory, rather than
    written to disk, and the components before and after resampling/dilation
    have to be in memory at the same time during the relevant computation. The
    <template-direction> argument should usually be COLUMN, as dtseries,
    dscalar, and dlabel all have brainordinates on that direction. If spheres
    are not specified for a surface structure which exists in the cifti files,
    its data is copied without resampling or dilation. Dilation is done with the
    'nearest' method, and is done on <new-sphere> for surface data. Volume
    components are padded before dilation so that dilation doesn't run into the
    edge of the component bounding box.
    
    To get the v1.3.2 and earlier behavior of weighted dilation, specify
    exponent of 2 for surface and volume, and -legacy-cutoff for both surface
    and volume.
    
    The <volume-method> argument must be one of the following:
    
    CUBIC
    ENCLOSING_VOXEL
    TRILINEAR
    
    The <surface-method> argument must be one of the following:
    
    ADAP_BARY_AREA
    BARYCENTRIC
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_in: the cifti file to resample.
        cifti_template: a cifti file containing the cifti space to resample to.
        template_direction: the direction of the template to use as the\
            resampling space, ROW or COLUMN.
        surface_method: specify a surface resampling method.
        volume_method: specify a volume interpolation method.
        cifti_out: the output cifti file.
        opt_surface_largest: use largest weight instead of weighted average\
            when doing surface resampling.
        volume_predilate: dilate the volume components before resampling.
        surface_postdilate: dilate the surface components after resampling.
        affine: use an affine transformation on the volume components.
        warpfield: use a warpfield on the volume components.
        left_spheres: specify spheres for left surface resampling.
        right_spheres: specify spheres for right surface resampling.
        cerebellum_spheres: specify spheres for cerebellum surface resampling.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiResampleDconnMemoryOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_RESAMPLE_DCONN_MEMORY_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-resample-dconn-memory")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(execution.input_file(cifti_template))
    cargs.append(template_direction)
    cargs.append(surface_method)
    cargs.append(volume_method)
    cargs.append(cifti_out)
    if opt_surface_largest:
        cargs.append("-surface-largest")
    if volume_predilate is not None:
        cargs.extend(volume_predilate.run(execution))
    if surface_postdilate is not None:
        cargs.extend(surface_postdilate.run(execution))
    if affine is not None:
        cargs.extend(affine.run(execution))
    if warpfield is not None:
        cargs.extend(warpfield.run(execution))
    if left_spheres is not None:
        cargs.extend(left_spheres.run(execution))
    if right_spheres is not None:
        cargs.extend(right_spheres.run(execution))
    if cerebellum_spheres is not None:
        cargs.extend(cerebellum_spheres.run(execution))
    ret = CiftiResampleDconnMemoryOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(cifti_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_RESAMPLE_DCONN_MEMORY_METADATA",
    "CiftiResampleDconnMemoryAffine",
    "CiftiResampleDconnMemoryCerebellumAreaMetrics",
    "CiftiResampleDconnMemoryCerebellumAreaSurfs",
    "CiftiResampleDconnMemoryCerebellumSpheres",
    "CiftiResampleDconnMemoryFlirt",
    "CiftiResampleDconnMemoryLeftAreaMetrics",
    "CiftiResampleDconnMemoryLeftAreaSurfs",
    "CiftiResampleDconnMemoryLeftSpheres",
    "CiftiResampleDconnMemoryOutputs",
    "CiftiResampleDconnMemoryRightAreaMetrics",
    "CiftiResampleDconnMemoryRightAreaSurfs",
    "CiftiResampleDconnMemoryRightSpheres",
    "CiftiResampleDconnMemorySurfacePostdilate",
    "CiftiResampleDconnMemoryVolumePredilate",
    "CiftiResampleDconnMemoryWarpfield",
    "CiftiResampleDconnMemoryWeighted",
    "CiftiResampleDconnMemoryWeighted_",
    "cifti_resample_dconn_memory",
]
