# ffplay 简单使用(播放)

```bash
ffplay [:filename:]  # 播放
```

w  切换显示模式
p/Space 暂停
q/Esc 退出
F  全屏

# ffprobe 简单使用 (查看文件信息)

```bash
ffprobe [:filename:]  # 查看文件信息
```

# ffmpeg 简单使用

## 3.0 其他

```bash
ffmpeg -codes  # 输出所有 编解码器
ffmpeg -pix_fmts # 输出所有 颜色空间
```



## 3.1 转换文件格式

### 3.1.1 转换视频格式

``` bash
ffmpeg -i input.mov output.mp4  # 转换视频格式
ffmpeg 
	-i [:inputName:] 
	-s [::wight_height::] # 1920x1080
	-pix_fmt [:pixel_format:] # 颜色空间. 例: yuv420p
	-vcodec [:codecName:] # 视频编解码器.例: libx264
	-preset [::]  # 编码器预设. 例: veryfast(录制时). veryslow(压缩视频) . normal = medium
	-profile:v [::]  # 压缩比. 例: baseline(实时通信). main(流媒体). high(超清)
    -level:v [::] # 编码器的具体规范和限制. 例: 4.1(1080p)
    
    # 码率控制模式(单遍编码)
    -crf [::]  # 恒定速率因子模式(压制视频). 要求画质. 体积较大. 0~51. normal = 23. 越小，质量越高
    -qp [::] # 恒定量化器模式. 画质高, 体积超大.0~51. normal = 23. 越小，质量越高
    -b [::] # 固定目标码率. 体积, 码率一定
    
    -r [::]  # 视频帧率
    -acodec [::]  # 音频编码器
    -ar [:音频采样率:]  # @音频采样率: 例如 44100 或 48000. 不指定则默认与 输入相同
	-ab [:音频比特率:] # @音频比特率: 如: 320K. 默认: 128K
	-ac [:声道数:] # @声道数: 1 或 2. 默认: 输入
	-b:a [::]  # 比特率: 例: 128k
	[:outputName:]
```

### 3.1.2 转换音频格式

```bash
ffmpeg 
	-i [:inputName:] 
	-acodec [:codecName:] # @编码器. 默认: 自动匹配 
	-ar [:音频采样率:]  # @音频采样率: 例如 44100 或 48000. 不指定则默认与 输入相同
	-ab [:音频比特率:] # @音频比特率: 如: 320K. 默认: 128K
	-ac [:声道数:] # @声道数: 1 或 2. 默认: 输入
    -aframes [:音频帧数:] 
    -aq [:quality:]  # 设置音频质量
    -an # 静音
    -vol [:volume:]  # 音量. normal = 256
    -af [:filter_graph:]  # 过滤器
	[:outputName:] # 转换音频格式
```

### 3.1.3 提取纯 视频/音频

```bash
ffmpeg -i [:inputName:] -vcodec copy -an [:outputName:]  # 提取纯视频
ffmpeg -i [:inputName:] -vn -acodec copy [:outputName:]  # 提取纯音频

# 音频格式对应
ACC编码 -> .m4a

# 提取音频时可能会有多个音频轨道
添加 
-map 0:2
-map 0:3
```

### 3.1.4 合并 视频、音频

```bash
ffmpeg -i [:audioName:] -i [:videoName:] -c copy [:outputName:]  # 合并 视频、音频
```

### 3.1.5 截取 音频

```bash
ffmpeg 
	-i [:inputName:]
    -ss [:startTime: [hour:min:sec] 或 [min:sec] 或 [sec] ]  # 开始时间
    -to [:endTime:  [hour:min:sec] 或 [min:sec] 或 [sec] ]  # 结束时间
    -acodec copy
    [:outputName:]  # 从 -ss 截取到 -to 
ffmpeg 
	-i [:inputName:]
    -ss [:startTime: [hour:min:sec] 或 [min:sec] 或 [sec] ]  # 开始时间 
    -t [:secTime:] # 截取时间
    -sseof # 从视频末尾开始
    -acodec copy
    [:outputName:]  # 从 -ss 截取 -t 秒 
```

### 3.1.6 截取 视频

```bash
ffmpeg 
	-i [:inputName:]
    -ss [:startTime: [hour:min:sec] 或 [min:sec] 或 [sec] ]  # 开始时间
    -to [:endTime:  [hour:min:sec] 或 [min:sec] 或 [sec] ]  # 结束时间
    -c copy
    [:outputName:]  # 从 -ss 截取到 -to 
ffmpeg 
	-i [:inputName:]
    -ss [:startTime: [hour:min:sec] 或 [min:sec] 或 [sec] ]  # 开始时间 
    -t [:secTime:] # 截取时间
    -sseof # 从视频末尾开始
    -c copy
    [:outputName:]  # 从 -ss 截取 -t 秒 
    
ffmpeg 
    -ss [:startTime: [hour:min:sec] 或 [min:sec] 或 [sec] ]  # 开始时间 
  	-i [:inputName:]
  	-t [:secTime:] # 截取时间
    -sseof # 从视频末尾开始
    -c copy
    -copyts # 保留时间戳
    [:outputName:]  # 从 -ss 截取 -t 秒    ->  -ss -i 调换位置会启用关键帧技术
```

### 3.1.7 合并多个视频

```bash
ffmpeg -i "concat:fileName1.mp4|fileName2.mp4|fileName3.mp4" -c copy [:outputName:]
```

### 3.1.8 截取 视频中的图片

```bash
ffmpeg 
	-i [:inputName:] 
	-ss [:sec:]  # 第几秒
    -vframes [:frame:]  # 这一秒的第几帧
    [:outputName.jpg:]
```

### 3.1.9 添加水印

```bash
ffmpeg 
	-i [:inputVideo:]
	-i [:inputLog:]
	-filter_complex  "overlay=20:20" # 添加滤镜. overlay=20:20 -> 距左边、顶部20像素
    [:outputName]
```

### 3.1.10 简单制作GIF

```bash
ffmpeg
	-i [:inputName:] 
	-ss 7  # 开始时间
	-to 8 # 结束时间
	-s 640x320 # 缩放
	-r 15  # 降低(设置)帧率
	[:outputName:]
```

### 3.1.11 录屏

```bash
ffmpeg 
	-f gdigrab  # 各个平台不同. 这个仅仅捕捉屏幕
    -i desktop out.mp4  # Q 退出 
```

### 3.1.12 直播推流

```bash
ffmpeg -re -i rec.mp4 网站要求编码 -f flv "rtmp地址 或 直播码"
```



# 编码格式简单介绍

1080P及以下

MP4: H264视频编码 + AAC音频编码
WebM: VP8 视频编码 + Vorbis音频编码
OGG: Theora视频编码 + Vorbis音频编码 ( 开源 -- HTML5默认支持 )

# 推荐软件

Avidemux  快速 操作? 视频
