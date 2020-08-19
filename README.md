# run-anything-async

## Usage:

```python
    @async_no_await
    def greeting():
        # Do some long, complicated task
        print("Hello World")

    my_task: Future = greeting()
```
