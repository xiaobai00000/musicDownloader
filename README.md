# musicDownloader
一个可以下载网易云免费听但不能免费下载音乐的脚本。注意，仅能下载网易云的，而且免费试听的，只是下载要会员的。为mp3下载。

＃ 使用方法
直接在终端运行以下命令
＃＃sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list && apt update && apt upgrade && pkg install python && pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install bs4 -i https://pypi.tuna.tsinghua.edu.cn/simple
