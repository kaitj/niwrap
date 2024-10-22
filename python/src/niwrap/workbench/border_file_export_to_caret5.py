# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BORDER_FILE_EXPORT_TO_CARET5_METADATA = Metadata(
    id="b3d3242dff6c74222d893494d40c2c367153290f.boutiques",
    name="border-file-export-to-caret5",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class BorderFileExportToCaret5Surface:
    """
    specify an input surface.
    """
    surface_in: InputPathType
    """a surface file for unprojection of borders"""
    
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
        cargs.append("-surface")
        cargs.append(execution.input_file(self.surface_in))
        return cargs


class BorderFileExportToCaret5Outputs(typing.NamedTuple):
    """
    Output object returned when calling `border_file_export_to_caret5(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def border_file_export_to_caret5(
    border_file: str,
    output_file_prefix: str,
    surface: list[BorderFileExportToCaret5Surface] | None = None,
    runner: Runner | None = None,
) -> BorderFileExportToCaret5Outputs:
    """
    Export border file to caret5 file format.
    
    A Workbench border file may contain borders for multiple structures and
    borders that are both projected and unprojected. It also contains a color
    table for the borders.
    
    Caret5 has both border (unprojected) and border projection (projected)
    files. In addition, each Caret5 border or border projection file typically
    contains data for a single structure. Caret5 also uses a border color file
    that associates colors with the names of the borders.
    
    This command will try to output both Caret5 border and border projection
    files. Each output border/border projection file will contains data for one
    structure so there may be many files created. The structure name is included
    in the name of each border or border projection file that is created.
    
    One Caret5 border color file will also be produced by this command.
    
    Providing surface(s) as input parameters is optional, but recommended.
    Surfaces may be needed to create both projected and/or unprojected
    coordinates of borders. If there is a failure to produce an output border or
    border projection due to a missing surface with the matching structure, an
    error message will be displayed and some output files will not be created.
    
    When writing new files, this command will overwrite a file with the same
    name. .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        border_file: workbench border file.
        output_file_prefix: prefix for name of output caret5\
            border/borderproj/bordercolor files.
        surface: specify an input surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BorderFileExportToCaret5Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BORDER_FILE_EXPORT_TO_CARET5_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-border-file-export-to-caret5")
    cargs.append(border_file)
    cargs.append(output_file_prefix)
    if surface is not None:
        cargs.extend([a for c in [s.run(execution) for s in surface] for a in c])
    ret = BorderFileExportToCaret5Outputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BORDER_FILE_EXPORT_TO_CARET5_METADATA",
    "BorderFileExportToCaret5Outputs",
    "BorderFileExportToCaret5Surface",
    "border_file_export_to_caret5",
]
