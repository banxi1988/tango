import inspect
import warnings
from typing import ClassVar, Tuple


class RemovedInDjango31Warning(DeprecationWarning):
    pass


class RemovedInDjango40Warning(PendingDeprecationWarning):
    pass


RemovedInNextVersionWarning = RemovedInDjango31Warning


class warn_about_renamed_method:
    """对使用已重命名方法的警告的装饰器类"""

    def __init__(
        self, class_name, old_method_name, new_method_name, deprecation_warning
    ):
        self.class_name = class_name
        self.old_method_name = old_method_name
        self.new_method_name = new_method_name
        self.deprecation_warning = deprecation_warning

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            warnings.warn(
                "`%s.%s` is deprecated, use `%s` instead."
                % (self.class_name, self.old_method_name, self.new_method_name),
                self.deprecation_warning,
                2,
            )
            return f(*args, **kwargs)

        return wrapped


class RenameMethodsBase(type):
    """
    支持有重命名方法的元类。
    当重命名一个方法时，按如下处理流程处理：
        1) 如果没有的话，定义新方法，并且抛出警告。
        2) 如果没有老方法的话，定义之。
        3）当调用老方法时，抛出警告.

    Handles the deprecation paths when renaming a method.

    It does the following:
        1) Define the new method if missing and complain about it.
        2) Define the old method if missing.
        3) Complain whenever an old method is called.

    See #15363 for more details.
    """

    renamed_methods: ClassVar[Tuple[Tuple[str, str, Warning]]] = ()

    def __new__(cls, name, bases, attrs):
        # __new__ 是 元类对新定义的子类进行修改时常用实现的方法
        # 相当于调用 type(name,bases,attrs) 来创建新的类
        new_class = super().__new__(cls, name, bases, attrs)

        # 遍历父类
        for base in inspect.getmro(new_class):
            class_name = base.__name__
            # 遍历父类中定义的重命名方法
            for renamed_method in cls.renamed_methods:
                old_method_name = renamed_method[0]
                old_method = base.__dict__.get(old_method_name)
                new_method_name = renamed_method[1]
                new_method = base.__dict__.get(new_method_name)
                deprecation_warning = renamed_method[2]
                wrapper = warn_about_renamed_method(class_name, *renamed_method)

                # 如果声明了定义重命名后的方法但是没有定义，抛出警告,并继续使用定义的老的方法
                # 将老的方法使用 wrapper 包装成调用新方法前输出警告的方法。
                # Define the new method if missing and complain about it
                if not new_method and old_method:
                    warnings.warn(
                        "`%s.%s` method should be renamed `%s`."
                        % (class_name, old_method_name, new_method_name),
                        deprecation_warning,
                        2,
                    )
                    setattr(base, new_method_name, old_method)
                    setattr(base, old_method_name, wrapper(old_method))

                # Define the old method as a wrapped call to the new method.
                if not old_method and new_method:
                    setattr(base, old_method_name, wrapper(new_method))

        return new_class


class DeprecationInstanceCheck(type):
    def __instancecheck__(self, instance):
        warnings.warn(
            "`%s` is deprecated, use `%s` instead." % (self.__name__, self.alternative),
            self.deprecation_warning,
            2,
        )
        return super().__instancecheck__(instance)


class MiddlewareMixin:
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, "process_request"):
            response = self.process_request(request)
        response = response or self.get_response(request)
        if hasattr(self, "process_response"):
            response = self.process_response(request, response)
        return response
