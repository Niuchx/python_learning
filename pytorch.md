Calculate the number of parameters
```python
def get_n_params(model):
    total_num = 0
    for p in model.parameters():
        total_num += p.numel()
    return total_num
```
