# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_FIND_CLUSTERS_METADATA = Metadata(
    id="f07ba30ac3261f3371abc68ab86581c6b5a293f4.boutiques",
    name="cifti-find-clusters",
    package="workbench",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiFindClustersLeftSurface:
    """
    specify the left surface to use.
    """
    surface: InputPathType
    """the left surface file"""
    opt_corrected_areas_area_metric: InputPathType | None = None
    """vertex areas to use instead of computing them from the surface: the
    corrected vertex areas, as a metric"""
    
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
        cargs.append("-left-surface")
        cargs.append(execution.input_file(self.surface))
        if self.opt_corrected_areas_area_metric is not None:
            cargs.extend([
                "-corrected-areas",
                execution.input_file(self.opt_corrected_areas_area_metric)
            ])
        return cargs


@dataclasses.dataclass
class CiftiFindClustersRightSurface:
    """
    specify the right surface to use.
    """
    surface: InputPathType
    """the right surface file"""
    opt_corrected_areas_area_metric: InputPathType | None = None
    """vertex areas to use instead of computing them from the surface: the
    corrected vertex areas, as a metric"""
    
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
        cargs.append("-right-surface")
        cargs.append(execution.input_file(self.surface))
        if self.opt_corrected_areas_area_metric is not None:
            cargs.extend([
                "-corrected-areas",
                execution.input_file(self.opt_corrected_areas_area_metric)
            ])
        return cargs


@dataclasses.dataclass
class CiftiFindClustersCerebellumSurface:
    """
    specify the cerebellum surface to use.
    """
    surface: InputPathType
    """the cerebellum surface file"""
    opt_corrected_areas_area_metric: InputPathType | None = None
    """vertex areas to use instead of computing them from the surface: the
    corrected vertex areas, as a metric"""
    
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
        cargs.append("-cerebellum-surface")
        cargs.append(execution.input_file(self.surface))
        if self.opt_corrected_areas_area_metric is not None:
            cargs.extend([
                "-corrected-areas",
                execution.input_file(self.opt_corrected_areas_area_metric)
            ])
        return cargs


@dataclasses.dataclass
class CiftiFindClustersSizeRatio:
    """
    ignore clusters smaller than a given fraction of the largest cluster in the
    structure.
    """
    surface_ratio: float
    """fraction of the structure's largest cluster area"""
    volume_ratio: float
    """fraction of the structure's largest cluster volume"""
    
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
        cargs.append("-size-ratio")
        cargs.append(str(self.surface_ratio))
        cargs.append(str(self.volume_ratio))
        return cargs


@dataclasses.dataclass
class CiftiFindClustersDistance:
    """
    ignore clusters further than a given distance from the largest cluster in
    the structure.
    """
    surface_distance: float
    """how far from the largest cluster a cluster can be, edge to edge, in mm"""
    volume_distance: float
    """how far from the largest cluster a cluster can be, edge to edge, in mm"""
    
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
        cargs.append("-distance")
        cargs.append(str(self.surface_distance))
        cargs.append(str(self.volume_distance))
        return cargs


class CiftiFindClustersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_find_clusters(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti"""


def cifti_find_clusters(
    cifti: InputPathType,
    surface_value_threshold: float,
    surface_minimum_area: float,
    volume_value_threshold: float,
    volume_minimum_size: float,
    direction: str,
    cifti_out: str,
    opt_less_than: bool = False,
    left_surface: CiftiFindClustersLeftSurface | None = None,
    right_surface: CiftiFindClustersRightSurface | None = None,
    cerebellum_surface: CiftiFindClustersCerebellumSurface | None = None,
    opt_cifti_roi_roi_cifti: InputPathType | None = None,
    opt_merged_volume: bool = False,
    size_ratio: CiftiFindClustersSizeRatio | None = None,
    distance: CiftiFindClustersDistance | None = None,
    opt_start_startval: int | None = None,
    runner: Runner | None = None,
) -> CiftiFindClustersOutputs:
    """
    Filter clusters by area/volume.
    
    Outputs a cifti file with nonzero integers for all brainordinates within a
    large enough cluster, and zeros elsewhere. The integers denote cluster
    membership (by default, first cluster found will use value 1, second cluster
    2, etc). Cluster values are not reused across maps of the output, but
    instead keep counting up. The input cifti file must have a brain models
    mapping on the chosen dimension, columns for .dtseries, and either for
    .dconn. The ROI should have a brain models mapping along columns, exactly
    matching the mapping of the chosen direction in the input file. Data outside
    the ROI is ignored.
    
    Author: Washington University School of Medicin
    
    Args:
        cifti: the input cifti.
        surface_value_threshold: threshold for surface data values.
        surface_minimum_area: threshold for surface cluster area, in mm^2.
        volume_value_threshold: threshold for volume data values.
        volume_minimum_size: threshold for volume cluster size, in mm^3.
        direction: which dimension to use for spatial information, ROW or\
            COLUMN.
        cifti_out: the output cifti.
        opt_less_than: find values less than <value-threshold>, rather than\
            greater.
        left_surface: specify the left surface to use.
        right_surface: specify the right surface to use.
        cerebellum_surface: specify the cerebellum surface to use.
        opt_cifti_roi_roi_cifti: search only within regions of interest: the\
            regions to search within, as a cifti file.
        opt_merged_volume: treat volume components as if they were a single\
            component.
        size_ratio: ignore clusters smaller than a given fraction of the\
            largest cluster in the structure.
        distance: ignore clusters further than a given distance from the\
            largest cluster in the structure.
        opt_start_startval: start labeling clusters from a value other than 1:\
            the value to give the first cluster found.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiFindClustersOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_FIND_CLUSTERS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-find-clusters")
    cargs.append(execution.input_file(cifti))
    cargs.append(str(surface_value_threshold))
    cargs.append(str(surface_minimum_area))
    cargs.append(str(volume_value_threshold))
    cargs.append(str(volume_minimum_size))
    cargs.append(direction)
    cargs.append(cifti_out)
    if opt_less_than:
        cargs.append("-less-than")
    if left_surface is not None:
        cargs.extend(left_surface.run(execution))
    if right_surface is not None:
        cargs.extend(right_surface.run(execution))
    if cerebellum_surface is not None:
        cargs.extend(cerebellum_surface.run(execution))
    if opt_cifti_roi_roi_cifti is not None:
        cargs.extend([
            "-cifti-roi",
            execution.input_file(opt_cifti_roi_roi_cifti)
        ])
    if opt_merged_volume:
        cargs.append("-merged-volume")
    if size_ratio is not None:
        cargs.extend(size_ratio.run(execution))
    if distance is not None:
        cargs.extend(distance.run(execution))
    if opt_start_startval is not None:
        cargs.extend([
            "-start",
            str(opt_start_startval)
        ])
    ret = CiftiFindClustersOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(cifti_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_FIND_CLUSTERS_METADATA",
    "CiftiFindClustersCerebellumSurface",
    "CiftiFindClustersDistance",
    "CiftiFindClustersLeftSurface",
    "CiftiFindClustersOutputs",
    "CiftiFindClustersRightSurface",
    "CiftiFindClustersSizeRatio",
    "cifti_find_clusters",
]
