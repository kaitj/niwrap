# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


MREDIT_METADATA = Metadata(
    id="9a3820ed5ab2b1ccd72bf894c0ed8e03e87c182e",
    name="mredit",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MreditPlane:
    """
    fill one or more planes on a particular image axis
    """
    axis: int
    """fill one or more planes on a particular image axis"""
    coord: list[int]
    """fill one or more planes on a particular image axis"""
    value: float | int
    """fill one or more planes on a particular image axis"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-plane")
        cargs.extend(["", str(self.axis)])
        cargs.extend(["", *map(str, self.coord)])
        cargs.extend(["", str(self.value)])
        return cargs


@dataclasses.dataclass
class MreditSphere:
    """
    draw a sphere with radius in mm
    """
    position: list[float | int]
    """draw a sphere with radius in mm"""
    radius: float | int
    """draw a sphere with radius in mm"""
    value: float | int
    """draw a sphere with radius in mm"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-sphere")
        cargs.extend(["", *map(str, self.position)])
        cargs.extend(["", str(self.radius)])
        cargs.extend(["", str(self.value)])
        return cargs


@dataclasses.dataclass
class MreditVoxel:
    """
    change the image value within a single voxel
    """
    position: list[float | int]
    """change the image value within a single voxel"""
    value: float | int
    """change the image value within a single voxel"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-voxel")
        cargs.extend(["", *map(str, self.position)])
        cargs.extend(["", str(self.value)])
        return cargs


@dataclasses.dataclass
class MreditConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-config")
        cargs.extend(["", self.key])
        cargs.extend(["", self.value])
        return cargs


class MreditOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mredit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType | None
    """the (optional) output image"""


def mredit(
    input_: InputPathType,
    output: InputPathType | None = None,
    plane: list[MreditPlane] = None,
    sphere: list[MreditSphere] = None,
    voxel: list[MreditVoxel] = None,
    scanner: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MreditConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> MreditOutputs:
    """
    mredit by Robert E. Smith (robert.smith@florey.edu.au).
    
    Directly edit the intensities within an image from the command-line.
    
    A range of options are provided to enable direct editing of voxel
    intensities based on voxel / real-space coordinates. If only one image path
    is provided, the image will be edited in-place (use at own risk); if input
    and output image paths are provided, the output will contain the edited
    image, and the original image will not be modified in any way.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/mredit.html
    
    Args:
        input_: the input image
        output: the (optional) output image
        plane: fill one or more planes on a particular image axis
        sphere: draw a sphere with radius in mm
        voxel: change the image value within a single voxel
        scanner: indicate that coordinates are specified in scanner space,
            rather than as voxel coordinates
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MreditOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MREDIT_METADATA)
    cargs = []
    cargs.append("mredit")
    if plane is not None:
        cargs.extend(["-plane", *[a for c in [s.run(execution) for s in plane] for a in c]])
    if sphere is not None:
        cargs.extend(["-sphere", *[a for c in [s.run(execution) for s in sphere] for a in c]])
    if voxel is not None:
        cargs.extend(["-voxel", *[a for c in [s.run(execution) for s in voxel] for a in c]])
    if scanner:
        cargs.append("-scanner")
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend(["-config", *[a for c in [s.run(execution) for s in config] for a in c]])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.extend(["", execution.input_file(input_)])
    if output is not None:
        cargs.extend(["", execution.input_file(output)])
    ret = MreditOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}") if output is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MREDIT_METADATA",
    "MreditConfig",
    "MreditOutputs",
    "MreditPlane",
    "MreditSphere",
    "MreditVoxel",
    "mredit",
]
