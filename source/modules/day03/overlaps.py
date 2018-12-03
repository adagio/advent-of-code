from collections import Counter

from modules.day03.claim import DataClassClaim
from modules.day03.parse import parse


def __get_claims(lines):
    claims = []
    for line in lines:
        claim_obj = parse(line)
        claim = DataClassClaim(**claim_obj)
        claims.append(claim)
    return claims


def __get_coord_freqs(claims):

    coords = []

    for claim in claims:
        claim_coords = Counter(claim.get_coords())
        coords.extend(claim_coords)

    freqs = Counter(coords)

    return freqs


def how_many_overlaps(lines):

    claims = __get_claims(lines)
    freqs = __get_coord_freqs(claims)

    total = sum(1 for key,value in freqs.items() if freqs[key] >= 2)

    return total


def get_non_overlapped_coords(lines):

    claims = __get_claims(lines)
    freqs = __get_coord_freqs(claims)

    non_overlapped_coords = []
    for key,value in freqs.items():
        if freqs[key] == 1:
            non_overlapped_coords.append(key)

    return non_overlapped_coords


def __are_coords_in_group(coords, group):
    for i in range(0, len(coords)):
        if coords[i] in group:
            if i == len(coords)-1:
                return True
            else:
                continue
        else:
            return False




def get_non_overlapped_claim(lines):

    claims = __get_claims(lines)
    freqs = __get_coord_freqs(claims)

    non_overlapped_coords = []
    for key,value in freqs.items():
        if freqs[key] == 1:
            non_overlapped_coords.append(key)

    for claim in claims:
        claim_coords = claim.get_coords()
        if __are_coords_in_group(claim_coords, non_overlapped_coords):
            return claim
