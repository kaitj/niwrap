# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BEDPOSTX_DATACHECK_METADATA = Metadata(
    id="f845cf6122ea726e2a835e5800129c5170746b41.boutiques",
    name="bedpostx_datacheck",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class BedpostxDatacheckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bedpostx_datacheck(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def bedpostx_datacheck(
    data_dir: str,
    runner: Runner | None = None,
) -> BedpostxDatacheckOutputs:
    """
    Check the data directory for BEDPOSTX compatibility.
    
    Author: Oxford Centre for Functional MRI of the Brain (FMRIB)
    
    Args:
        data_dir: Data directory to check for BEDPOSTX compatibility.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BedpostxDatacheckOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BEDPOSTX_DATACHECK_METADATA)
    cargs = []
    cargs.append("/usr/local/fsl/bin/bedpostx_datacheck")
    cargs.append(data_dir)
    ret = BedpostxDatacheckOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BEDPOSTX_DATACHECK_METADATA",
    "BedpostxDatacheckOutputs",
    "bedpostx_datacheck",
]
