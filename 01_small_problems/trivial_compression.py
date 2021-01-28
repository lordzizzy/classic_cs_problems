
from typing import Generator
from termcolor import colored


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def bit_string(self) -> int:
        return self._bit_str

    def _compress(self, gene: str) -> None:
        bit_str: int = 1
        for n in gene.upper():
            bit_str <<= 2
            if n == "A":
                bit_str |= 0b00
            elif n == "C":
                bit_str |= 0b01
            elif n == "G":
                bit_str |= 0b10
            elif n == "T":
                bit_str |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide:{n}")
        self._bit_str: int = bit_str

    def decompress(self) -> str:
        def gen_genes(bit_str: int) -> Generator[str, None, None]:
            end = bit_str.bit_length() - 1  # -1 because of sentinel
            for i in range(0, end, 2):
                bits: int = bit_str >> i & 0b11
                if bits == 0b00:
                    yield "A"
                elif bits == 0b01:
                    yield "C"
                elif bits == 0b10:
                    yield "G"
                elif bits == 0b11:
                    yield "T"
                else:
                    raise ValueError(f"Invalid bits: {bits}")

        gene: str = "".join(gen_genes(self._bit_str))
        # return gene as reversed sequence slice to correct the reverse reading of genes above
        return gene[::-1]


def test_gene_compress(gene: str, expected: int):
    cg = CompressedGene(gene)
    r = cg.bit_string()
    if r == expected:
        print(
            colored(f"PASSED compress => gene {gene}'s bitstring is {cg.bit_string()}", "green"))
    else:
        print(
            colored(f"FAILED compress => gene {gene}'s bitstring is {cg.bit_string()}, but expected is {expected}", "red"))


def test_gene_decompress(bit_str: int, expected: str):
    cg = CompressedGene(expected)
    r = cg.decompress()
    if r == expected:
        print(
            colored(f"PASSED decompress => {bit_str} is decompressed into {r}", "green"))
    else:
        print(colored(
            f"FAILED decompress => {bit_str} is decompressed into {r}, but expected: {expected}", "red"))


if __name__ == "__main__":
    test_gene_compress(gene="ACGTAAA", expected=0b100011011000000)
    test_gene_decompress(bit_str=0b100011011000000, expected='ACGTAAA')
