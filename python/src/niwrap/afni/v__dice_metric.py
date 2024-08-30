# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__DICE_METRIC_METADATA = Metadata(
    id="02454d6067b4a4327f43f73c720bc9635a3e4821",
    name="@DiceMetric",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VDiceMetricOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__dice_metric(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__dice_metric(
    base: InputPathType,
    dsets: list[InputPathType],
    max_roi: float | int | None = None,
    labeltable: InputPathType | None = None,
    forceoutput: InputPathType | None = None,
    echo: bool = False,
    save_match: bool = False,
    save_diff: bool = False,
    do_not_mask_by_base: bool = False,
    mask_by_base: bool = False,
    prefix: str | None = None,
    ignore_bad: bool = False,
    keep_tmp: bool = False,
    runner: Runner | None = None,
) -> VDiceMetricOutputs:
    """
    @DiceMetric by AFNI Team.
    
    Computes Dice Metric between BASE and each of the DSET volumes.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@DiceMetric.html
    
    Args:
        base: Name of base (reference) segmentation.
        dsets: Data sets for which the Dice Metric with BASE is computed. This\
            should be the last option on the command line.
        max_roi: The maximum possible ROI index. Default is 12 or based on\
            LTFILE if specified.
        labeltable: If given, the labeltable is used to set the default MAX_ROI\
            parameter. Also, this option forces an output for each key in the\
            LTFILE.
        forceoutput: If given, force output for each class in LTFILE.
        echo: Set echo.
        save_match: Save volume showing BASE*equals(BASE,DSET).
        save_diff: Save volume showing BASE*(1-equals(BASE,DSET)).
        do_not_mask_by_base: Do not mask dset by step(base) before computing\
            Dice coefficient.
        mask_by_base: Mask dset by the step(base) before computing Dice\
            coefficient.
        prefix: Use PREFIX for the output table. Default is separate results\
            for each dset to stdout.
        ignore_bad: Warn if encountering bad scenarios, but do not create a\
            zero entry.
        keep_tmp: Keep temporary files for debugging. Note that you should\
            delete temporary files before rerunning the script.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDiceMetricOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DICE_METRIC_METADATA)
    cargs = []
    cargs.append("@DiceMetric")
    cargs.append("<-base")
    cargs.append("BASE>")
    cargs.append("<-dsets")
    cargs.append("DSET1")
    cargs.append("[DSET2")
    cargs.append("...]>")
    cargs.append("[max_N_roi")
    cargs.append("MAX_ROI]")
    if keep_tmp:
        cargs.append("-keep_tmp")
    cargs.append("[OPTIONS...]")
    ret = VDiceMetricOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VDiceMetricOutputs",
    "V__DICE_METRIC_METADATA",
    "v__dice_metric",
]