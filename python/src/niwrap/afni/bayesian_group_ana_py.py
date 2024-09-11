# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BAYESIAN_GROUP_ANA_PY_METADATA = Metadata(
    id="db94a9baf849869e651d770782b8c95df573de99.boutiques",
    name="BayesianGroupAna.py",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class BayesianGroupAnaPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bayesian_group_ana_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    summary: OutputPathType
    """Summary of the brmsfit object from R."""
    rhats: OutputPathType
    """Rhats for each effect and x variable combination."""
    intercept_table: OutputPathType
    """Table with the MedianEst, StdDev, 2.50%, 5%, 50%, 95%, and 97.50% of each
    ROI for the Intercept term."""
    x_var_table: OutputPathType
    """The same table as the Intercept but for the specified x variable."""


def bayesian_group_ana_py(
    data_table: InputPathType,
    y_variable: str,
    runner: Runner | None = None,
) -> BayesianGroupAnaPyOutputs:
    """
    This program conducts Bayesian Group Analysis (BGA) on a list of regions of
    interest (ROIs). Compared to the conventional univariate GLM, BGA pools and
    shares the information across the ROIs in a multilevel system.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/BayesianGroupAna.py.html
    
    Args:
        data_table: Input text file containing the data table.
        y_variable: Column name for the y variable.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BayesianGroupAnaPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BAYESIAN_GROUP_ANA_PY_METADATA)
    cargs = []
    cargs.append("/opt/afni/src/../install/BayesianGroupAna.py")
    cargs.append("-dataTable")
    cargs.append(execution.input_file(data_table))
    cargs.append("-y")
    cargs.append(y_variable)
    cargs.append("[OPTIONS]")
    ret = BayesianGroupAnaPyOutputs(
        root=execution.output_file("."),
        summary=execution.output_file("[PREFIX]_summary.txt"),
        rhats=execution.output_file("[PREFIX]_rhats.csv"),
        intercept_table=execution.output_file("[PREFIX]_Intercept_table.csv"),
        x_var_table=execution.output_file("[PREFIX]_table.csv"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BAYESIAN_GROUP_ANA_PY_METADATA",
    "BayesianGroupAnaPyOutputs",
    "bayesian_group_ana_py",
]