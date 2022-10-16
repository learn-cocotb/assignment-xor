import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def dut(dut):
    a = (0, 0, 1, 1)
    b = (0, 1, 0, 1)
    y = (0, 1, 1, 0)

    for i in range(4):
        dut.a.value = a[i]
        dut.b.value = b[i]
        await Timer(1, 'ns')
        assert dut.y.value == y[i], f"Error at iteration {i}"
