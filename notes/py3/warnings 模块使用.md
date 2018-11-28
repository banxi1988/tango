## warnings 模块的简要说明

1. 通过 `warnings.warn` 抛出警告。
2. 警告的基类是 `Warning` 其是 `Exception` 的子类，所以上面说 **抛出** 警告。
3. 警告的默认处理方式是输出到 `sys.stderr`.
4. 可以控制警告的处理方式。

### 警告类型

警告有如下几种类型:

-   `Warning` 基类
-   `UserWarning` 默认类别
-   `DeprecationWarning` 默认是忽略的
-   `SyntaxWarning`
-   `RuntimeWarning`
-   `FutureWarning`
-   `PendingDeprecationWarning` 默认是忽略的。
-   `ImportWarning` 默认是忽略的。
-   `UnicodeWarning`
-   `BytesWarning`
-   `ResourceWarning`

### 警告过滤器

过滤器可以控制某一类，或者符合某些条件的警告的处理方式。
可选的处理方式(action)有:

-   `"default"` 默认处理方式， 而且警告在行级别去重
-   `"error"` 将警告转成错误抛出。
-   `"ignore"` 忽略警告
-   `"always"` 总是输出警告
-   `"module"` 警告在模块级别去重
-   `"once"` 匹配的警告是输出一次。

1. `warnings.filterwarnings(action, message='', category=Warning, module='', lineno=0, append=False)`
   添加警告过滤器的全参数调用接口。

2. `warnings.simplefilter(action, category=Warning, lineno=0, append=False)`
   只添加过滤指定警告类型的过滤器

## Django 中警告模块的使用

### 测试模块中的使用

见 `tests/runtests.py` 中的注释说明.

### 代码中的使用

1. 在 `django.utils.deprecation` 模块中定义的几个警告。主要是在 3.0 中准备删除的特性的警告。
2. 在上述模块中还定义了 `RenameMethodsBase` 用于方便处理自定义类中的重命名方法之后，调用老方法时输出警告。

3. 其他使用数据，通过搜索 `warnings.warn` 发现有在 32 个文件中有 45 处使用记录。
   这些使用中其中有一个参数 `stacklevel=2` 是比较常见的。因为 Django 作为一个库，一般需要用来警告调用者的使用。所以使用 `stacklevel` 设置为 2，意思就是针对调用对应函数的调用者抛出警告，而不是函数本身.
