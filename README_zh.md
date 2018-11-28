# Django with type hints -> tango

## 项目笔记

1. 克隆 Django 之后，将项目名称改为 tango (2018-11-28)
2. `git clone https://github.com/banxi1988/tango.git`
3. 基于 3.7.1 创建虚拟环境 `pyenv virtualenv 3.7.1 tango`
4. 在项目根目录执行 `echo tango > .python-version`
5. 重新进入目录，确认已经激活对应虚拟环境

```
➜  tango (master) ✗ pyenv which pip
/Users/banxi/.pyenv/versions/tango/bin/pip
```

## 项目测试

参考： https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests

1. `cd tests`
2. `pip install -e ..` 也就是将父目录中的 Django 项目作为此测试依赖包。参见 pip 帮助
    > Install a project in editable mode (i.e. setuptools "develop mode") from a local project path or a VCS url.

3.`pip install -r requirements/py3.txt`

4. `./runtests.py`

### 安装测试依赖问题

问题 1：

```
 In file included from src/_pylibmcmodule.c:34:
    src/_pylibmcmodule.h:42:10: fatal error: 'libmemcached/memcached.h' file not found
    #include <libmemcached/memcached.h>
```

解决方法： 通过 brew 安装对应库.
`brew install libmemcached`

### 执行测试中的错误信息:

1. > objc[13187]: +[__NSPlaceholderDate initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead. Set a breakpoint on objc_initializeAfterForkError to debug.

2. > Execution of msgfmt failed: pyenv: msgfmt: command not found

3. > django.core.management.base.CommandError: Unable to get gettext version. Is it installed?
   > 可能是因为找不到 `gettext`. 确认有安装，然后重新安装 `brew reinstall gettext`
   > 其说明如下：

```
==> Caveats
gettext is keg-only, which means it was not symlinked into /usr/local,
because macOS provides the BSD gettext library & some software gets confused if both are in the library path.

If you need to have gettext first in your PATH run:
  echo 'export PATH="/usr/local/opt/gettext/bin:$PATH"' >> ~/.zshrc

For compilers to find gettext you may need to set:
  export LDFLAGS="-L/usr/local/opt/gettext/lib"
  export CPPFLAGS="-I/usr/local/opt/gettext/include"

```

所以执行 `echo 'export PATH="/usr/local/opt/gettext/bin:$PATH"' >> ~/.zshrc` 然后重新
`source ~/.zshrc`

## 一些安装记录

1. `pip install -e ..` 执行记录

```
➜  tests (master) ✔ pip install -e ..
Obtaining file:///Users/banxi/Workspace/tango
Collecting pytz (from Django==2.2.dev20181128031119)
  Using cached https://files.pythonhosted.org/packages/f8/0e/2365ddc010afb3d79147f1dd544e5ee24bf4ece58ab99b16fbb465ce6dc0/pytz-2018.7-py2.py3-none-any.whl
Collecting sqlparse (from Django==2.2.dev20181128031119)
  Using cached https://files.pythonhosted.org/packages/65/85/20bdd72f4537cf2c4d5d005368d502b2f464ede22982e724a82c86268eda/sqlparse-0.2.4-py2.py3-none-any.whl
Installing collected packages: pytz, sqlparse, Django
  Running setup.py develop for Django
Successfully installed Django pytz-2018.7 sqlparse-0.2.4
```

2. `libmemcached` 安装记录

```

==> Installing dependencies for libmemcached: openssl, libevent and memcached
==> Installing libmemcached dependency: openssl
==> Downloading https://homebrew.bintray.com/bottles/openssl-1.0.2q.mojave.bottle.tar.gz
######################################################################## 100.0%
==> Pouring openssl-1.0.2q.mojave.bottle.tar.gz
==> Caveats
A CA file has been bootstrapped using certificates from the SystemRoots
keychain. To add additional certificates (e.g. the certificates added in
the System keychain), place .pem files in
  /usr/local/etc/openssl/certs

and run
  /usr/local/opt/openssl/bin/c_rehash

openssl is keg-only, which means it was not symlinked into /usr/local,
because Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries.

If you need to have openssl first in your PATH run:
  echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.zshrc

For compilers to find openssl you may need to set:
  export LDFLAGS="-L/usr/local/opt/openssl/lib"
  export CPPFLAGS="-I/usr/local/opt/openssl/include"

For pkg-config to find openssl you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"

==> Summary
🍺  /usr/local/Cellar/openssl/1.0.2q: 1,794 files, 12.1MB
==> Installing libmemcached dependency: libevent
==> Downloading https://homebrew.bintray.com/bottles/libevent-2.1.8.mojave.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libevent-2.1.8.mojave.bottle.tar.gz
🍺  /usr/local/Cellar/libevent/2.1.8: 846 files, 2.2MB
==> Installing libmemcached dependency: memcached
==> Downloading https://homebrew.bintray.com/bottles/memcached-1.5.12.mojave.bottle.tar.gz
######################################################################## 100.0%
==> Pouring memcached-1.5.12.mojave.bottle.tar.gz
==> Caveats
To have launchd start memcached now and restart at login:
  brew services start memcached
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/memcached/bin/memcached
==> Summary
🍺  /usr/local/Cellar/memcached/1.5.12: 11 files, 198.9KB
==> Installing libmemcached
==> Downloading https://homebrew.bintray.com/bottles/libmemcached-1.0.18_2.mojave.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libmemcached-1.0.18_2.mojave.bottle.tar.gz
🍺  /usr/local/Cellar/libmemcached/1.0.18_2: 231 files, 1.7MB
==> Caveats
==> openssl
A CA file has been bootstrapped using certificates from the SystemRoots
keychain. To add additional certificates (e.g. the certificates added in
the System keychain), place .pem files in
  /usr/local/etc/openssl/certs

and run
  /usr/local/opt/openssl/bin/c_rehash

openssl is keg-only, which means it was not symlinked into /usr/local,
because Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries.

If you need to have openssl first in your PATH run:
  echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.zshrc

For compilers to find openssl you may need to set:
  export LDFLAGS="-L/usr/local/opt/openssl/lib"
  export CPPFLAGS="-I/usr/local/opt/openssl/include"

For pkg-config to find openssl you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"

==> memcached
To have launchd start memcached now and restart at login:
  brew services start memcached
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/memcached/bin/memcached
```
