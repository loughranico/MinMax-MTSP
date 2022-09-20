import torch

filename = 'ortools/TL2/test/agent5/city50/minmax_ortools_test_agent5_city50_num1.pt'

t = torch.load(filename)
print(t.keys())

print(t['time'])
