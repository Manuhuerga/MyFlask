# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)


@app.route("/")  # Fill this in!
def index():
    return "<h1>Welcome to the home page</h1>"


@app.route("/puppy_latin/<name>")  # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    pupname = name[:-1] + "iful" if name[-1] == "y" else name + "y"

    return f"<h1>Your name is {pupname.capitalize()}</h1>"


if __name__ == "__main__":
    # Fill me in!
    app.run(debug=True)

from __future__ import absolute_import, division, print_function
import logging
from random import choice
from regression_common.base_classes.queries.link_status_query import LinkStatusQuery
from regression_common.test_utils import StressIterator, ASSERT
from tabulate import tabulate
from regression_common.utils.parametrization_utils import Parametrizer
from regression_common.utils.constants import INPHI_OK, INPHI_ERROR
import pytest

logger = logging.getLogger("regressionLog")


@pytest.mark.application("lynx_to_por", "lynx_400")
class TestDevice:

    dsp_filter = lambda combination: combination["dsp_mode"] == "SLC1"
    baud_rate = lambda combination: combination["baud_rate"] == "28p125G"
    op_modes = lambda combination: combination["op_mode"] == "DUAL_PRBS"

    combinations = Parametrizer.combinations(
        combinations_type="one_per_signalling",
        filters=[dsp_filter, baud_rate, op_modes],
    )

    def test_swizzle(self, universal_prbs_fixture, connect_fixture):
        """
        Checking the swizzle status
        """
        errors = []
        status = INPHI_OK
        bench = connect_fixture
        dut = bench.dut[0]

        for dev in bench.devices:
            logger.info("Connected to target: {}".format(dev.target_name))

        assert (
            dut.api.hsc_dev_swizzle_is_enabled(dut.dev_handle) == True
        ), "Error, the swizzle must be True in the first instance"

        for enable in False, True:
            dut.api.hsc_dev_swizzle_enable(dut.dev_handle, enable)
            enabled_swizzle = dut.api.hsc_dev_swizzle_is_enabled(dut.dev_handle)
            status |= ASSERT(
                enabled_swizzle == enable,
                f"I sent {enable} but received {enabled_swizzle}",
                errors,
            )

        assert INPHI_OK == status, str(errors)

    def test_fll(self, universal_prbs_fixture):
        """
        Checking the fll status
        """
        bench, test_config = universal_prbs_fixture
        errors = []
        status = INPHI_OK
        dut = bench.dut[0]

        active_devices = {bench.device_get(dev_name) for dev_name, cfg in test_config.items() if cfg}
        link_status_queries = [LinkStatusQuery(device=dev) for dev in active_devices]

        initial_stress_iterator = StressIterator(queries=link_status_queries)
        initial_stress_iterator.full_stress()
        errors.extend(initial_stress_iterator.errors)
        assert initial_stress_iterator.status == INPHI_OK, str(errors)

        for intf, channels in dut.active_channels.items():
            for channel in channels:
                if "TX" in dut.tr.intf(intf):
                    enable = choice((True, False))
                    dut.api.hsc_chn_fll_enable(dut._chn_struct_get(intf, channel), enable)
                    fll_status = dut.api.hsc_chn_fll_is_enabled(dut._chn_struct_get(intf, channel))
                    status |= ASSERT(
                        fll_status == enable,
                        f"I received {enable} in channel {channel} but the status is {fll_status}",
                        errors,
                    )
        assert INPHI_OK == status, str(errors)

    def test_dev_info(self, connect_fixture):
        """
        Check the device supports this features or not
        """
        errors = []
        status = INPHI_OK
        bench = connect_fixture
        dut = bench.dut[0]

        for dev in bench.devices:
            logger.info("Connected to target: {}".format(dev.target_name))

        dev_handle = dut.dev_handle
        has_dict = {
            "has_anlt": [dut.api.hsc_dev_has_anlt(dev_handle)],
            "has_xbar": [dut.api.hsc_dev_has_xbar(dev_handle)],
            "has_hmux": [dut.api.hsc_dev_has_hmux(dev_handle)],
            "has_fec": [dut.api.hsc_dev_has_fec(dev_handle)],
            "gpio pins": [dut.api.hsc_dev_num_gpio_pins(dev_handle)],
        }
        logger.info("\n")
        logger.info(
            tabulate(
                has_dict,
                headers=has_dict.keys(),
                tablefmt="github",
                floatfmt=".3f",
                numalign="right",
                stralign="right",
                colalign=("left",),
            )
        )
        logger.info("\n")

        assert INPHI_OK == status, str(errors)
