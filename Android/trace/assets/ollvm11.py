import hashlib
import base64

dword_5C008 = [
    0x16A, 0x151, 0xD7, 0x134, 0x196, 0x229, 0x67, 0xFA,
    0x269, 0x272, 0x226, 0x122, 0xEC, 0x2B5, 0x216, 0x214,
    0x179, 0x9F, 0x277, 0x194, 0xF4, 0x2AD, 0xA0, 0x210,
    0x26D, 0x1B9, 0x257, 0x2C9, 0xE9, 0xA1, 0x16C, 0x15F,
    0x99, 0x2E1, 0xBF, 0x1C6, 0xB4, 0x21D, 0xDE, 0x16D,
    0xC4, 0x8B, 0x25D, 0x108, 0x11B, 0x12C, 0x14A, 0xC3,
    0x195, 0x2C7, 0xCA, 0x207, 0x206, 0x1B8, 0x1A0, 0x12D,
    0xCE, 0x93, 0x2DF, 0x205, 0xAA, 0x28B, 0x9B, 0x1DF,
    0x288, 0x200, 0x86, 0x169, 0x211, 0x297, 0x2D6, 0x135,
    0x223, 0xA9, 0x208, 0x1A2, 0x23A, 0x294, 0x1AD, 0x1CA,
    0x1E2, 0x102, 0xA7, 0x19C, 0x2B1, 0x1D1, 0x249, 0x72,
    0xD4, 0x1DD, 0x173, 0xB5, 0x17A, 0xE1, 0xA5, 0x10B,
    0x2D9, 0x281, 0x12B, 0xBD, 0x111, 0xBE, 0x1A9, 0x105,
    0x147, 0x82, 0x1E0, 0x1A3, 0x156, 0x23E, 0x22A, 0x190,
    0x71, 0x9E, 0x16B, 0x1C1, 0x11C, 0x204, 0x2E2, 0x2A2,
    0xA8, 0x14B, 0x2B6, 0xC9, 0x239, 0x116, 0x2A7, 0xD1,
    0x273, 0x6C, 0x21C, 0xE2, 0xEB, 0x2D0, 0x1DB, 0x6B,
    0x232, 0xEF, 0x85, 0x13F, 0xF5, 0x9D, 0xF8, 0x267,
    0x1F2, 0x75, 0x246, 0x1D8, 0x13B, 0x2D7, 0x2AC, 0xD5,
    0x187, 0x29C, 0x176, 0x131, 0x28D, 0x91, 0xB6, 0x114,
    0x2D8, 0x275, 0x11A, 0x26C, 0x110, 0x2AA, 0x1C3, 0x19F,
    0x1A8, 0x279, 0x2DE, 0x15D, 0x2DB, 0x6A, 0x230, 0x68,
    0x178, 0x2BD, 0x217, 0x146, 0x186, 0x1E6, 0x1B1, 0x143,
    0x2E3, 0x2AF, 0x8E, 0x1D0, 0xAC, 0x1DE, 0x260, 0x81,
    0x193, 0x266, 0x231, 0x1D2, 0xBA, 0x240, 0x18E, 0x7E,
    0xC1, 0x1F1, 0x1FE, 0x2A3, 0x250, 0x13A, 0x24A, 0x64,
    0x29A, 0x24B, 0x2CA, 0x188, 0xFD, 0x103, 0x100, 0x1D9,
    0x9A, 0x1F3, 0x182, 0x7D, 0xDA, 0xDF, 0x11F, 0x27E,
    0x1B4, 0x215, 0x8F, 0x263, 0x192, 0x150, 0x17D, 0x2A4,
    0x154, 0x23B, 0x14F, 0x12F, 0x29F, 0x2BA, 0x237, 0x2BC,
    0x126, 0x1FD, 0x168, 0x2C5, 0x254, 0x2E0, 0x1C9, 0x201,
    0x172, 0x140, 0x138, 0xE0, 0xB1, 0xBB, 0x2DD, 0x19E,
    0x1E7, 0x160, 0x13E, 0x7A, 0x1CB, 0x28C, 0x7F, 0xF9,
    0x14E, 0x2B8, 0x101, 0x1EA, 0x1D7, 0x1F7, 0x276, 0x1C2,
    0x8A, 0x2CF, 0x238, 0xDC, 0x2AE, 0x94, 0x157, 0x175,
    0x21F, 0x2C2, 0xAB, 0x130, 0x104, 0xFB, 0x24D, 0x222,
    0x221, 0x18C, 0x1FA, 0x1FC, 0x1B5, 0x87, 0x2BE, 0x1AF,
    0x1B7, 0xC2, 0x22B, 0x10A, 0x19B, 0x121, 0x198, 0x148,
    0x1F6, 0x280, 0x132, 0x17B, 0x1BB, 0xCD, 0x20E, 0x2BB,
    0xB7, 0x1CC, 0x244, 0x2A6, 0x264, 0x1EF, 0x251, 0x76,
    0x171, 0x2DC, 0x236, 0x25F, 0x159, 0x1A4, 0x1F4, 0x118,
    0x17E, 0x106, 0x115, 0x262, 0x1A6, 0x185, 0x1F5, 0x29B,
    0x29E, 0x13D, 0x9C, 0x224, 0xC5, 0x219, 0x25C, 0x149,
    0x88, 0x137, 0x2A9, 0xB2, 0x139, 0x24E, 0x183, 0x235,
    0x1FB, 0x15B, 0xC7, 0x1C5, 0xD9, 0x26B, 0x7B, 0x1E4,
    0xF7, 0x2C6, 0x22F, 0x16F, 0x2D2, 0xFC, 0x177, 0x1CD,
    0x241, 0x2CE, 0x1BE, 0x1BC, 0x7C, 0x1E3, 0x258, 0x2B0,
    0xAE, 0x125, 0xA6, 0x2D1, 0x1B6, 0xCF, 0x278, 0x18D,
    0x155, 0x1AB, 0x1F8, 0x270, 0x1D5, 0x2C1, 0x1B0, 0x27F,
    0x74, 0x1AE, 0xE7, 0x2A5, 0xD0, 0x98, 0x141, 0x289,
    0x1F0, 0x1AA, 0x1BF, 0x2CD, 0x1C8, 0x2B7, 0x296, 0x299,
    0x6F, 0x17C, 0xD8, 0x77, 0x124, 0xE8, 0x18F, 0x26E,
    0x2BF, 0x1DC, 0x21A, 0x209, 0x20A, 0x18A, 0x274, 0x1AC,
    0x28A, 0x109, 0x1EE, 0x73, 0x2B3, 0x136, 0x234, 0x1DA,
    0x10D, 0x27A, 0x2D4, 0x22E, 0x2C4, 0x83, 0x261, 0x18B,
    0x20F, 0x167, 0x1E5, 0x1F9, 0x252, 0x1E8, 0x89, 0x25E,
    0x23C, 0x129, 0xB3, 0xBC, 0x284, 0x112, 0x11D, 0x22D,
    0x2D3, 0x15C, 0x10F, 0xD2, 0xF2, 0x15E, 0x298, 0x28E,
    0x2CC, 0xEA, 0x120, 0x145, 0xF3, 0x202, 0x197, 0x181,
    0x2C3, 0x170, 0x1A7, 0x78, 0xE6, 0xC0, 0xF1, 0x1FF,
    0x295, 0x213, 0xC8, 0x164, 0x22C, 0x10C, 0x1D4, 0xCB,
    0x165, 0x1EC, 0xCC, 0x282, 0x1BD, 0xB0, 0x24F, 0x80,
    0xA2, 0x29D, 0x2D5, 0x14D, 0xE4, 0x16E, 0x158, 0x152,
    0xC6, 0x6D, 0xD3, 0x212, 0x184, 0x153, 0x180, 0x66,
    0x228, 0x220, 0x259, 0x2AB, 0x70, 0x27D, 0x2B9, 0x291,
    0xED, 0xAF, 0x127, 0x255, 0x123, 0x90, 0x293, 0xF0,
    0x271, 0x247, 0x162, 0x27C, 0x203, 0x119, 0x218, 0xFE,
    0x1C0, 0x1C4, 0x163, 0x243, 0x14C, 0x1D6, 0x1E1, 0x65,
    0x12A, 0x2DA, 0x292, 0xF6, 0x11E, 0x20D, 0x25B, 0x144,
    0xE5, 0xA3, 0x8C, 0x283, 0x1CF, 0x96, 0x191, 0x2A0,
    0x225, 0x199, 0x242, 0x92, 0x107, 0x21E, 0x166, 0x8D,
    0x290, 0x24C, 0x285, 0x287, 0x113, 0x133, 0x13C, 0x10E,
    0x17F, 0x1EB, 0xE3, 0x233, 0x26F, 0x265, 0x26A, 0xD6,
    0x19D, 0x15A, 0xAD, 0x256, 0x1A1, 0x23F, 0x6E, 0x1A5,
    0x245, 0x2C8, 0x1ED, 0x20C, 0xDD, 0x2B4, 0x21B, 0x1C7,
    0xA4, 0x97, 0x1B3, 0x2CB, 0x174, 0x1B2, 0x27B, 0x189,
    0x20B, 0x23D, 0x142, 0x28F, 0xDB, 0x69, 0x79, 0x2B2,
    0x1CE, 0x12E, 0x2A8, 0x268, 0x95, 0x25A, 0x227, 0xB8,
    0x253, 0xEE, 0xB9, 0x19A, 0x1BA, 0x161, 0x1D3, 0x2C0,
    0x128, 0x2A1, 0xFF, 0x117, 0x1E9, 0x84, 0x286, 0x248,
    0, 0
]


def KuanxueSign(start_time: int, first_install_time: int, random_long: int, package_code_path: str):
    # part 1
    s0 = "{:08x}{:08x}".format(start_time, first_install_time)
    s0 = (s0 + (64 - len(s0)) * chr(0)).encode()

    sha_a = hashlib.sha256()
    s1 = bytes([c ^ 0x5c for c in s0])
    sha_a.update(s1)

    sha_b = hashlib.sha256()
    s2 = bytes([c ^ 0x6a for c in s1])
    sha_b.update(s2)
    sha_b.update(package_code_path.encode())

    sha_a.update(sha_b.digest())
    part1 = sha_a.hexdigest()

    # part 2
    part2 = ''
    for c in package_code_path:
        part2 += '{:04x}'.format(dword_5C008[random_long % 5 + ord(c)])

    # part 3
    s0 = "{:08x}{:08x}".format(start_time, first_install_time)
    part3 = base64.b64encode(s0.encode())
    std_base64_chars = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    ollvm11_base64_chars = b'0123456789_-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    part3 = part3.translate(bytes.maketrans(std_base64_chars, ollvm11_base64_chars))
    part3 = part3.decode()
    return part1 + part2 + part3


start_time = 0x000001810ab738de
first_install_time = 0x000001810a9cf720
random_long = 0x323dc9aaad544800
package_code_path = "/data/app/com.kanxue.ollvm_ndk_11-dCqD-Kzs9cAqsSQx_9WYTg==/base.apk"

result = KuanxueSign(start_time, first_install_time, random_long, package_code_path)

print(result)
