import DictBuilder

trace_file = 'sample_trace.txt'
# trace_file = 'blkparseout_ext4.txt'
# trace_file = 'blkparseout_btrfs.txt'
# trace_file = 'blkparseout_f2fs.txt'
sectors_per_block = 8

test_dict = DictBuilder.build_dict(trace_file, sectors_per_block)
print(test_dict)
# values = test_dict.values()
# print(values)