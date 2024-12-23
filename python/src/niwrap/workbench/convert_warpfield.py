# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_WARPFIELD_METADATA = Metadata(
    id="e0f48a3f4d002bf731b7f13e5d1964bc0562c643.boutiques",
    name="convert-warpfield",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class ConvertWarpfieldFromWorld:
    """
    input is a NIFTI 'world' warpfield.
    """
    input_: str
    """the input warpfield"""
    opt_absolute: bool = False
    """warpfield was written in absolute convention, rather than relative"""
    
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
        cargs.append("-from-world")
        cargs.append(self.input_)
        if self.opt_absolute:
            cargs.append("-absolute")
        return cargs


@dataclasses.dataclass
class ConvertWarpfieldFromFnirt:
    """
    input is a fnirt warpfield.
    """
    input_: str
    """the input warpfield"""
    source_volume: str
    """the source volume used when generating the input warpfield"""
    opt_absolute: bool = False
    """warpfield was written in absolute convention, rather than relative"""
    
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
        cargs.append("-from-fnirt")
        cargs.append(self.input_)
        cargs.append(self.source_volume)
        if self.opt_absolute:
            cargs.append("-absolute")
        return cargs


@dataclasses.dataclass
class ConvertWarpfieldToFnirt:
    """
    write output as a fnirt warpfield.
    """
    output: str
    """output - the output warpfield"""
    source_volume: str
    """the volume you want to apply the warpfield to"""
    
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
        cargs.append("-to-fnirt")
        cargs.append(self.output)
        cargs.append(self.source_volume)
        return cargs


class ConvertWarpfieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_warpfield(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def convert_warpfield(
    from_world: ConvertWarpfieldFromWorld | None = None,
    opt_from_itk_input: str | None = None,
    from_fnirt: ConvertWarpfieldFromFnirt | None = None,
    opt_to_world_output: str | None = None,
    opt_to_itk_output: str | None = None,
    to_fnirt: list[ConvertWarpfieldToFnirt] | None = None,
    runner: Runner | None = None,
) -> ConvertWarpfieldOutputs:
    """
    Convert a warpfield between conventions.
    
    NIFTI world warpfields can be used directly on mm coordinates via sampling
    the three subvolumes at the coordinate and adding the sampled values to the
    coordinate vector. They use the NIFTI coordinate system, that is, X is left
    to right, Y is posterior to anterior, and Z is inferior to superior.
    
    NOTE: this command does not invert the warpfield, and to warp a surface, you
    must use the inverse of the warpfield that warps the corresponding volume.
    
    The ITK format is used by ANTS.
    
    You must specify exactly one -from option, but you may specify multiple -to
    options, and -to-fnirt may be specified more than once.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        from_world: input is a NIFTI 'world' warpfield.
        opt_from_itk_input: input is an ITK warpfield: the input warpfield.
        from_fnirt: input is a fnirt warpfield.
        opt_to_world_output: write output as a NIFTI 'world' warpfield: output\
            - the output warpfield.
        opt_to_itk_output: write output as an ITK warpfield: output - the\
            output warpfield.
        to_fnirt: write output as a fnirt warpfield.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertWarpfieldOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_WARPFIELD_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-convert-warpfield")
    if from_world is not None:
        cargs.extend(from_world.run(execution))
    if opt_from_itk_input is not None:
        cargs.extend([
            "-from-itk",
            opt_from_itk_input
        ])
    if from_fnirt is not None:
        cargs.extend(from_fnirt.run(execution))
    if opt_to_world_output is not None:
        cargs.extend([
            "-to-world",
            opt_to_world_output
        ])
    if opt_to_itk_output is not None:
        cargs.extend([
            "-to-itk",
            opt_to_itk_output
        ])
    if to_fnirt is not None:
        cargs.extend([a for c in [s.run(execution) for s in to_fnirt] for a in c])
    ret = ConvertWarpfieldOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_WARPFIELD_METADATA",
    "ConvertWarpfieldFromFnirt",
    "ConvertWarpfieldFromWorld",
    "ConvertWarpfieldOutputs",
    "ConvertWarpfieldToFnirt",
    "convert_warpfield",
]
