import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def xor_test(xor):
    a = (0, 0, 1, 1)
    b = (0, 1, 0, 1)
    y = (0, 1, 1, 0)

    for i in range(4):
        xor.a.value = a[i]
        xor.b.value = b[i]
        await Timer(1, 'ns')
        assert xor.y.value == y[i], f"Error at iteration {i}"
