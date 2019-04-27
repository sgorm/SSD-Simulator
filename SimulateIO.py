# Inputs:
    # trace_file
    # partition_dict
    # SSD
    # main_blocks_per_partition
    # pages_per_erase_block
    # also use logical_block_size_in_KB and physical_page_size_in_KB?

# Outputs:
    # write_amplification

# What we need to do: 
    # initialize total_user_writes = 0
    # initialize total_GC_writes = 0
    # Re-read trace_file line-by-line, use get_blocks on each line. Then, for each logical block in list:
        # Check assigned partition in partition_dict
        # Go to assigned partition in SSD and check all sublists of partition for block number.
        # If it's there, change it to a negative number. If not, just continue on. 
        # Then check same partition, from beginning, sublist-by-sublist until one sublist is not full 
            # (A sublist is full if length of sublist >= pages_per_erase_block)
        # If index of empty sublist <= main_blocks_per_partition, write the block number to the sublist 
            # (do we have to write 8 times if 1 erase block = 8 pages? I think so)
        # If index of empty sublist > main_blocks_per_partition, garbage collect -- you have reached the overprovisioned blocks
            # Once garbage collection is complete, have it return GC_writes and add that to total_GC_writes
            # then check sublists again to find the first empty one, and write block number there
        # increment total_user_writes += 1
    # write_amplification = total_user_writes / (total_user_writes + total_GC_writes)
    # return write_amplification

    # garbage collection
    # define as a separate function - takes a partition, returns a new partition and returns GC_writes
        # For each sublist (i.e. erase block) in the partition:
            # rewrite all positive block numbers to new erase blocks, counting every write, then empty the old blocks
            # At some point, have to sort so empty lists are at the end of the partition

# How do we statically vs. dynamically allocate erase blocks?
