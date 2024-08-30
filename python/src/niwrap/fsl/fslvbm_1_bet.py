# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLVBM_1_BET_METADATA = Metadata(
    id="ff01cd0bf1ddb86e2118893dad969cdff93f5a82",
    name="fslvbm_1_bet",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class Fslvbm1BetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslvbm_1_bet(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslvbm_1_bet(
    default_bet: bool = False,
    increased_robustness: bool = False,
    bet_parameters: str | None = None,
    runner: Runner | None = None,
) -> Fslvbm1BetOutputs:
    """
    fslvbm_1_bet by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Brain extraction for VBM using FSL BET.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSLVBM
    
    Args:
        default_bet: Default BET brain extraction with -f 0.4.
        increased_robustness: Increased robustness in the brain extraction when\
            a lot of neck is present.
        bet_parameters: Additional options to be passed on to BET.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Fslvbm1BetOutputs`).
    """
    runner = runner or get_global_runner()
    if (
        default_bet +
        increased_robustness
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "default_bet,\n"
            "increased_robustness"
        )
    execution = runner.start_execution(FSLVBM_1_BET_METADATA)
    cargs = []
    cargs.append("fslvbm_1_bet")
    if increased_robustness:
        cargs.append("-N")
    if bet_parameters is not None:
        cargs.append(bet_parameters)
    ret = Fslvbm1BetOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLVBM_1_BET_METADATA",
    "Fslvbm1BetOutputs",
    "fslvbm_1_bet",
]