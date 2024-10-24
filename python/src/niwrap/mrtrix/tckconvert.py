# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TCKCONVERT_METADATA = Metadata(
    id="e099f163628c4f4e1f744a964fec71d2c4cd255c.boutiques",
    name="tckconvert",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TckconvertConfig:
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
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


@dataclasses.dataclass
class TckconvertVariousString:
    obj: str
    """String object."""
    
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
        cargs.append(self.obj)
        return cargs


@dataclasses.dataclass
class TckconvertVariousFile:
    obj: InputPathType
    """File object."""
    
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
        cargs.append(execution.input_file(self.obj))
        return cargs


class TckconvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tckconvert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output track file."""


def tckconvert(
    input_: typing.Union[TckconvertVariousString, TckconvertVariousFile],
    output: str,
    scanner2voxel: InputPathType | None = None,
    scanner2image: InputPathType | None = None,
    voxel2scanner: InputPathType | None = None,
    image2scanner: InputPathType | None = None,
    sides: int | None = None,
    increment: int | None = None,
    dec: bool = False,
    radius: float | None = None,
    ascii_: bool = False,
    binary: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckconvertConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TckconvertOutputs:
    """
    Convert between different track file formats.
    
    The program currently supports MRtrix .tck files (input/output), ascii text
    files (input/output), VTK polydata files (input/output), and RenderMan RIB
    (export only).
    
    Note that ascii files will be stored with one streamline per numbered file.
    To support this, the command will use the multi-file numbering syntax, where
    square brackets denote the position of the numbering for the files, for
    example:
    
    $ tckconvert input.tck output-'[]'.txt
    
    will produce files named output-0000.txt, output-0001.txt, output-0002.txt,
    ...
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input track file.
        output: the output track file.
        scanner2voxel: if specified, the properties of this image will be used\
            to convert track point positions from real (scanner) coordinates into\
            voxel coordinates.
        scanner2image: if specified, the properties of this image will be used\
            to convert track point positions from real (scanner) coordinates into\
            image coordinates (in mm).
        voxel2scanner: if specified, the properties of this image will be used\
            to convert track point positions from voxel coordinates into real\
            (scanner) coordinates.
        image2scanner: if specified, the properties of this image will be used\
            to convert track point positions from image coordinates (in mm) into\
            real (scanner) coordinates.
        sides: number of sides for streamlines.
        increment: generate streamline points at every (increment) points.
        dec: add DEC as a primvar.
        radius: radius of the streamlines.
        ascii_: write an ASCII VTK file (this is the default).
        binary: write a binary VTK file.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TckconvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKCONVERT_METADATA)
    cargs = []
    cargs.append("tckconvert")
    if scanner2voxel is not None:
        cargs.extend([
            "-scanner2voxel",
            execution.input_file(scanner2voxel)
        ])
    if scanner2image is not None:
        cargs.extend([
            "-scanner2image",
            execution.input_file(scanner2image)
        ])
    if voxel2scanner is not None:
        cargs.extend([
            "-voxel2scanner",
            execution.input_file(voxel2scanner)
        ])
    if image2scanner is not None:
        cargs.extend([
            "-image2scanner",
            execution.input_file(image2scanner)
        ])
    if sides is not None:
        cargs.extend([
            "-sides",
            str(sides)
        ])
    if increment is not None:
        cargs.extend([
            "-increment",
            str(increment)
        ])
    if dec:
        cargs.append("-dec")
    if radius is not None:
        cargs.extend([
            "-radius",
            str(radius)
        ])
    if ascii_:
        cargs.append("-ascii")
    if binary:
        cargs.append("-binary")
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend([
            "-nthreads",
            str(nthreads)
        ])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.extend(input_.run(execution))
    cargs.append(output)
    ret = TckconvertOutputs(
        root=execution.output_file("."),
        output=execution.output_file(output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TCKCONVERT_METADATA",
    "TckconvertConfig",
    "TckconvertOutputs",
    "TckconvertVariousFile",
    "TckconvertVariousString",
    "tckconvert",
]
