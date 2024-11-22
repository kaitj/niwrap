# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_FIBER_ORIENTATIONS_METADATA = Metadata(
    id="83932f9e32b874b47a5a87d2605029dbebc92a5c.boutiques",
    name="convert-fiber-orientations",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class ConvertFiberOrientationsFiber:
    """
    specify the parameter volumes for a fiber.
    """
    mean_f: InputPathType
    """mean fiber strength"""
    stdev_f: InputPathType
    """standard deviation of fiber strength"""
    theta: InputPathType
    """theta angle"""
    phi: InputPathType
    """phi angle"""
    psi: InputPathType
    """psi angle"""
    ka: InputPathType
    """ka bingham parameter"""
    kb: InputPathType
    """kb bingham parameter"""
    
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
        cargs.append("-fiber")
        cargs.append(execution.input_file(self.mean_f))
        cargs.append(execution.input_file(self.stdev_f))
        cargs.append(execution.input_file(self.theta))
        cargs.append(execution.input_file(self.phi))
        cargs.append(execution.input_file(self.psi))
        cargs.append(execution.input_file(self.ka))
        cargs.append(execution.input_file(self.kb))
        return cargs


class ConvertFiberOrientationsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_fiber_orientations(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fiber_out: OutputPathType
    """the output fiber orientation file"""


def convert_fiber_orientations(
    label_volume: InputPathType,
    fiber_out: str,
    fiber: list[ConvertFiberOrientationsFiber] | None = None,
    runner: Runner | None = None,
) -> ConvertFiberOrientationsOutputs:
    """
    Convert bingham parameter volumes to fiber orientation file.
    
    Takes precomputed bingham parameters from volume files and converts them to
    the format workbench uses for display. The <label-volume> argument must be a
    label volume, where the labels use these strings:
    
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_volume: volume of cifti structure labels.
        fiber_out: the output fiber orientation file.
        fiber: specify the parameter volumes for a fiber.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertFiberOrientationsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_FIBER_ORIENTATIONS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-convert-fiber-orientations")
    cargs.append(execution.input_file(label_volume))
    cargs.append(fiber_out)
    if fiber is not None:
        cargs.extend([a for c in [s.run(execution) for s in fiber] for a in c])
    ret = ConvertFiberOrientationsOutputs(
        root=execution.output_file("."),
        fiber_out=execution.output_file(fiber_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_FIBER_ORIENTATIONS_METADATA",
    "ConvertFiberOrientationsFiber",
    "ConvertFiberOrientationsOutputs",
    "convert_fiber_orientations",
]
