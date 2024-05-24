# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


MESHCONVERT_METADATA = Metadata(
    id="f2a617306afe557a6724c61cbcc4056bbc346da5",
    name="meshconvert",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MeshconvertTransform:
    """
    transform vertices from one coordinate space to another, based on a template image; options are: first2real, real2first, voxel2real, real2voxel, fs2real
    """
    mode: typing.Literal["mode"]
    """transform vertices from one coordinate space to another, based on a
    template image; options are: first2real, real2first, voxel2real, real2voxel,
    fs2real"""
    image: InputPathType
    """transform vertices from one coordinate space to another, based on a
    template image; options are: first2real, real2first, voxel2real, real2voxel,
    fs2real"""
    
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
        cargs.append("-transform")
        cargs.extend(["", self.mode])
        cargs.extend(["", execution.input_file(self.image)])
        return cargs


@dataclasses.dataclass
class MeshconvertConfig:
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


class MeshconvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `meshconvert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output mesh file"""


def meshconvert(
    input_: InputPathType,
    output: InputPathType,
    binary: bool = False,
    transform: MeshconvertTransform | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MeshconvertConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> MeshconvertOutputs:
    """
    meshconvert by Robert E. Smith (robert.smith@florey.edu.au).
    
    Convert meshes between different formats, and apply transformations.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/meshconvert.html
    
    Args:
        input_: the input mesh file
        output: the output mesh file
        binary: write the output mesh file in binary format (if supported)
        transform: transform vertices from one coordinate space to another,
            based on a template image; options are: first2real, real2first,
            voxel2real, real2voxel, fs2real
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
        NamedTuple of outputs (described in `MeshconvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MESHCONVERT_METADATA)
    cargs = []
    cargs.append("meshconvert")
    if binary:
        cargs.append("-binary")
    if transform is not None:
        cargs.extend(["-transform", *transform.run(execution)])
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
    cargs.extend(["", execution.input_file(output)])
    ret = MeshconvertOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MESHCONVERT_METADATA",
    "MeshconvertConfig",
    "MeshconvertOutputs",
    "MeshconvertTransform",
    "meshconvert",
]
