def count_logical_blocks(freq_dict, pct_overprov):
    '''(dict of int:int, int) -> int

    Calculates the number of logical blocks required to accommodate the data from one trace.
    Adds the number of unique blocks affected by the trace to a percentage of over-provisioning blocks. Rounds up.

    e.g. 
    >>>count_logical_blocks({34:1, 35:2, 36:3}, 28)
    4

    e.g. 
    >>>count_logical_blocks(freq_dict, 28)
    300 000
    '''
    # write this, remember to round up


def count_erase_blocks(num_logical_blks, erase_blk_size, logical_blk_size):
    '''(int, float, float) -> int

    Calculates the number of erase blocks required to accommodate the data stored in a number of logical blocks. Rounds up. 
    Divides the total size of all logical blocks in KB by size of a physical erase block in KB.

    e.g.
    >>>count_erase_blocks(300 000, 4096.0, 4.096)
    300

    >>>count_erase_blocks((count_logical_blocks(freq_dict, 28)), 4096.0, (sector_size * 0.512))
    300
    '''
    # test this
    return (num_logical_blks * logical_blk_size) / erase_blk_size 
    # round up


def blocks_per_partition(num_erase_blks, num_partitions):
    '''(int, int) -> int

    Calculates the number of erase blocks to allocate to each SSD partition. Rounds up

    e.g.
    >>>blocks_per_partition(300, 3)
    100
    '''
    # test this
    return num_erase_blks/num_partitions
    # round up

# Also compute max number of logical blocks per erase block and number of overprovisioned erase blocks per partition (see notes in MakeSSD)