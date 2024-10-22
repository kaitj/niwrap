# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_APPLY_AFFINE_METADATA = Metadata(
    id="bc7bedf2247f5ce1c3534b41ffc51edcdb4ffba5.boutiques",
    name="surface-apply-affine",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class SurfaceApplyAffineFlirt:
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


class SurfaceApplyAffineOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_apply_affine(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_surf: OutputPathType
    """the output transformed surface"""


def surface_apply_affine(
    in_surf: InputPathType,
    affine: str,
    out_surf: str,
    flirt: SurfaceApplyAffineFlirt | None = None,
    runner: Runner | None = None,
) -> SurfaceApplyAffineOutputs:
    """
    Apply affine transform to surface file.
    
    For flirt matrices, you must use the -flirt option, because flirt matrices
    are not a complete description of the coordinate transform they represent.
    If the -flirt option is not present, the affine must be a nifti 'world'
    affine, which can be obtained with the -convert-affine command, or aff_conv
    from the 4dfp suite.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        in_surf: the surface to transform.
        affine: the affine file.
        out_surf: the output transformed surface.
        flirt: MUST be used if affine is a flirt affine.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceApplyAffineOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_APPLY_AFFINE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-apply-affine")
    cargs.append(execution.input_file(in_surf))
    cargs.append(affine)
    cargs.append(out_surf)
    if flirt is not None:
        cargs.extend(flirt.run(execution))
    ret = SurfaceApplyAffineOutputs(
        root=execution.output_file("."),
        out_surf=execution.output_file(out_surf),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_APPLY_AFFINE_METADATA",
    "SurfaceApplyAffineFlirt",
    "SurfaceApplyAffineOutputs",
    "surface_apply_affine",
]
