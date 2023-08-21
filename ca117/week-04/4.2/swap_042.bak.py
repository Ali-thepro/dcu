#!/usr/vin/env python3

def swap_keys_values(d):
    return dict(zip(d.values(), d.keys()))


#!/usr/bin/env python3

# def swap_keys_values(d):
#     return {v : k for k, v in d.items()}        can use sorted(d.items) but he does it when he runs the code