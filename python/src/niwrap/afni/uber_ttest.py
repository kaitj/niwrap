# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

UBER_TTEST_METADATA = Metadata(
    id="a73e093f5a37572dc0088aa515c27b84ef10f305.boutiques",
    name="uber_ttest",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class UberTtestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `uber_ttest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_script: OutputPathType | None
    """Script file generated by the non-GUI option"""


def uber_ttest(
    qt_opts: str | None = None,
    help_: bool = False,
    help_gui: bool = False,
    hist: bool = False,
    show_valid_opts: bool = False,
    ver: bool = False,
    no_gui: bool = False,
    program: str | None = None,
    print_script: bool = False,
    save_script: str | None = None,
    mask: InputPathType | None = None,
    set_name_a: str | None = None,
    set_name_b: str | None = None,
    dsets_a: str | None = None,
    dsets_b: str | None = None,
    beta_a: float | None = None,
    beta_b: float | None = None,
    tstat_a: float | None = None,
    tstat_b: float | None = None,
    results_dir: str | None = None,
    runner: Runner | None = None,
) -> UberTtestOutputs:
    """
    GUI for group t-test analysis.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        qt_opts: Pass PyQt4 options directly to the GUI.
        help_: Display help information.
        help_gui: Display help information for the GUI.
        hist: Display the history.
        show_valid_opts: Show valid options.
        ver: Display the version information.
        no_gui: Run without the GUI.
        program: Specify the program to use.
        print_script: Print the script.
        save_script: Save the script to a file.
        mask: Specify the mask file.
        set_name_a: Set name for group A.
        set_name_b: Set name for group B.
        dsets_a: Datasets for group A.
        dsets_b: Datasets for group B.
        beta_a: Beta values for group A.
        beta_b: Beta values for group B.
        tstat_a: T-statistic values for group A.
        tstat_b: T-statistic values for group B.
        results_dir: Directory for saving results.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UberTtestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UBER_TTEST_METADATA)
    cargs = []
    cargs.append("uber_ttest.py")
    if qt_opts is not None:
        cargs.append(qt_opts)
    if help_:
        cargs.append("-help")
    if help_gui:
        cargs.append("-help_gui")
    if hist:
        cargs.append("-hist")
    if show_valid_opts:
        cargs.append("-show_valid_opts")
    if ver:
        cargs.append("-ver")
    if no_gui:
        cargs.append("-no_gui")
    if program is not None:
        cargs.extend([
            "-program",
            program
        ])
    if print_script:
        cargs.append("-print_script")
    if save_script is not None:
        cargs.extend([
            "-save_script",
            save_script
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if set_name_a is not None:
        cargs.extend([
            "-set_name_A",
            set_name_a
        ])
    if set_name_b is not None:
        cargs.extend([
            "-set_name_B",
            set_name_b
        ])
    if dsets_a is not None:
        cargs.extend([
            "-dsets_A",
            dsets_a
        ])
    if dsets_b is not None:
        cargs.extend([
            "-dsets_B",
            dsets_b
        ])
    if beta_a is not None:
        cargs.extend([
            "-beta_A",
            str(beta_a)
        ])
    if beta_b is not None:
        cargs.extend([
            "-beta_B",
            str(beta_b)
        ])
    if tstat_a is not None:
        cargs.extend([
            "-tstat_A",
            str(tstat_a)
        ])
    if tstat_b is not None:
        cargs.extend([
            "-tstat_B",
            str(tstat_b)
        ])
    if results_dir is not None:
        cargs.extend([
            "-results_dir",
            results_dir
        ])
    ret = UberTtestOutputs(
        root=execution.output_file("."),
        output_script=execution.output_file(save_script) if (save_script is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "UBER_TTEST_METADATA",
    "UberTtestOutputs",
    "uber_ttest",
]
